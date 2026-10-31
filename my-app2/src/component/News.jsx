import React, { Component } from 'react'
import NewsItem from './NewsItem'

export default class News extends Component {
  apiKey = import.meta.env.VITE_NEWS_API_KEY;

  static defaultProps = {
    category: 'all',
  };

  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      loading: true,
      loadingMore: false,
      nextPageToken: null,
      hasMore: true,
      underMaintenance: false,
    };
    this.observer = null;
  }

  getCategoryHeading = () => {
    const { category } = this.props;
    switch (category) {
      case 'entertainment':
        return 'Entertainment News';
      case 'sports':
        return 'Sports News';
      case 'stock':
        return 'Stock & Market News';
      case 'politics':
        return 'Politics News';
      case 'business':
        return 'Business News';
      default:
        return 'Top India Headlines (All News)';
    }
  };

  getCategoryFilter = () => {
    const category = this.props.category || 'all';
    if (category === 'stock') {
      return '&q=stock';
    } else if (category !== 'all') {
      return `&category=${category}`;
    }
    return '';
  };

  // Triggered on navigation / category switch
  fetchInitialNews = async () => {
    if (this.props.setProgress) this.props.setProgress(20);
    this.setState({ loading: true, underMaintenance: false, hasMore: true });

    try {
      const categoryFilter = this.getCategoryFilter();
      const url = `https://newsdata.io/api/1/news?apikey=${this.apiKey}&country=in&language=en&size=6${categoryFilter}`;

      if (this.props.setProgress) this.props.setProgress(45);
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }

      if (this.props.setProgress) this.props.setProgress(70);
      const data = await response.json();

      if (data.status === "success" && data.results && data.results.length > 0) {
        if (this.props.setProgress) this.props.setProgress(90);
        this.setState({
          articles: data.results,
          nextPageToken: data.nextPage || null,
          hasMore: Boolean(data.nextPage),
          loading: false,
          underMaintenance: false,
        }, () => {
          if (this.props.setProgress) {
            this.props.setProgress(100);
            setTimeout(() => {
              if (this.props.setProgress) this.props.setProgress(0);
            }, 350);
          }
        });
      } else {
        throw new Error(data.results?.message || "Failed to retrieve news from API");
      }
    } catch (error) {
      console.error("NewsData API Error:", error);
      if (this.props.setProgress) {
        this.props.setProgress(100);
        setTimeout(() => {
          if (this.props.setProgress) this.props.setProgress(0);
        }, 350);
      }
      this.setState({
        underMaintenance: true,
        loading: false,
      });
    }
  };

  // Triggered on infinite scrolling: DOES NOT touch the top red loading bar
  fetchMoreNews = async () => {
    if (this.state.loadingMore || !this.state.hasMore || !this.state.nextPageToken) {
      return;
    }

    this.setState({ loadingMore: true });

    try {
      const categoryFilter = this.getCategoryFilter();
      const url = `https://newsdata.io/api/1/news?apikey=${this.apiKey}&country=in&language=en&size=6${categoryFilter}&page=${this.state.nextPageToken}`;

      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }

      const data = await response.json();

      if (data.status === "success" && data.results && data.results.length > 0) {
        // Prevent duplicate articles
        const existingIds = new Set(this.state.articles.map((a) => a.article_id || a.link));
        const uniqueNew = data.results.filter((a) => !existingIds.has(a.article_id || a.link));

        this.setState((prevState) => ({
          articles: [...prevState.articles, ...uniqueNew],
          nextPageToken: data.nextPage || null,
          hasMore: Boolean(data.nextPage),
          loadingMore: false,
        }));
      } else {
        this.setState({ hasMore: false, loadingMore: false });
      }
    } catch (error) {
      console.error("Error loading more news:", error);
      this.setState({ loadingMore: false });
    }
  };

  componentDidMount() {
    this.fetchInitialNews();
  }

  componentWillUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  }

  sentinelRef = (element) => {
    if (this.observer) {
      this.observer.disconnect();
    }
    if (element) {
      this.observer = new IntersectionObserver(
        (entries) => {
          if (entries[0].isIntersecting) {
            this.fetchMoreNews();
          }
        },
        { rootMargin: '250px' }
      );
      this.observer.observe(element);
    }
  };

  render() {
    return (
      <div className="container my-4">
        <div className="text-center mb-4">
          <h2 className="fw-bold">NewsMonkey - {this.getCategoryHeading()}</h2>
          <p className="text-muted">
            Continuous live feed &bull; {this.state.articles.length} stories loaded
          </p>
        </div>

        {/* 1. Maintenance Screen when initial fetch fails */}
        {this.state.underMaintenance && (
          <div className="row justify-content-center my-5">
            <div className="col-md-8">
              <div className="card text-center shadow border-warning">
                <div className="card-body p-5">
                  <div style={{ fontSize: "3.5rem" }}>🛠️</div>
                  <h3 className="card-title text-danger mt-3">News App Under Maintenance</h3>
                  <p className="card-text text-muted mt-2">
                    We are currently unable to connect to the news server. Please try again in a few moments.
                  </p>
                  <button
                    className="btn btn-dark mt-3"
                    onClick={this.fetchInitialNews}
                  >
                    🔄 Retry Connection
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* News Grid */}
        {!this.state.loading && !this.state.underMaintenance && (
          <>
            <div className="row g-4">
              {this.state.articles.map((article, index) => (
                <div className="col-md-4" key={article.article_id || article.link || index}>
                  <NewsItem
                    title={article.title}
                    description={article.description}
                    imageUrl={article.image_url}
                    newsUrl={article.link}
                    sourceName={article.source_name || article.source_id}
                    date={article.pubDate}
                  />
                </div>
              ))}
            </div>

            {/* Sentinel element to trigger next page when scrolled into view */}
            {this.state.hasMore && (
              <div ref={this.sentinelRef} className="text-center my-4 py-3">
                {this.state.loadingMore && (
                  <div>
                    <div className="spinner-border text-primary" role="status">
                      <span className="visually-hidden">Loading more...</span>
                    </div>
                    <p className="text-muted mt-2 small">Loading more news...</p>
                  </div>
                )}
              </div>
            )}

            {/* End of results message */}
            {!this.state.hasMore && this.state.articles.length > 0 && (
              <div className="text-center my-5 py-3">
                <hr className="w-25 mx-auto mb-3" />
                <p className="text-muted fw-semibold">
                  🎉 You have reached the end of the news for this category.
                </p>
              </div>
            )}
          </>
        )}
      </div>
    );
  }
}
