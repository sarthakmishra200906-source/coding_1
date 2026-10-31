import React, { Component } from "react";

export default class NewsItem extends Component {
  render() {
    let { title, description, imageUrl, image_url, newsUrl, link, sourceName, date } = this.props;

    const defaultImg =
      "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=600&auto=format&fit=crop&q=60";

    const finalImg = imageUrl || image_url || defaultImg;
    const finalUrl = newsUrl || link || "#";

    return (
      <div className="h-100">
        <div className="card h-100 shadow-sm">
          <img
            src={finalImg}
            onError={(e) => {
              e.target.onerror = null;
              e.target.src = defaultImg;
            }}
            className="card-img-top"
            alt={title || "News thumbnail"}
            style={{ height: "200px", objectFit: "cover" }}
          />
          <div className="card-body d-flex flex-column">
            {sourceName && (
              <div className="mb-2">
                <span className="badge bg-danger">{sourceName}</span>
              </div>
            )}
            <h5 className="card-title">{title ? `${title.slice(0, 50)}...` : "Latest News"}</h5>
            <p className="card-text text-secondary">
              {description ? `${description.slice(0, 95)}...` : "Click below to read the complete article and full story."}
            </p>
            {date && (
              <p className="card-text">
                <small className="text-muted">
                  {new Date(date).toLocaleDateString("en-IN", {
                    month: "short",
                    day: "numeric",
                    year: "numeric"
                  })}
                </small>
              </p>
            )}
            <a
              href={finalUrl}
              target="_blank"
              rel="noreferrer"
              className="btn btn-sm btn-dark mt-auto"
            >
              Read More &rarr;
            </a>
          </div>
        </div>
      </div>
    );
  }
}
