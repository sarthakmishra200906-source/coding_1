# 📚 NewsMonkey Refactor Guide
## Class-based Components → Functional Components + Hooks

> **Reference:** CodeWithHarry React Course — Video #39  
> **Project:** NewsMonkey — A live news app built with React + NewsData.io API  
> **Goal:** Convert every class-based component to a modern functional component using `useState` and `useEffect` hooks.

---

## 🧠 Why Refactor? (Concept Notes)

| Old Way (Class Component) | New Way (Functional Component) |
|:---|:---|
| `class News extends Component` | `function News(props)` or `const News = () =>` |
| `this.state = { ... }` | `const [value, setValue] = useState(...)` |
| `this.setState({ key: val })` | `setValue(val)` |
| `componentDidMount()` | `useEffect(() => { ... }, [])` |
| `this.props.something` | `props.something` or destructured `{ something }` |
| `componentWillUnmount()` | `return () => cleanup` inside `useEffect` |
| `this.myMethod = () => ...` | just `const myMethod = () => ...` |

> **Key Rule:** In functional components, there is NO `this`. Everything is just a plain variable or function.

---

## 📁 Project File Map

```
my-app2/
├── src/
│   ├── App.jsx               ← Root component (manages category + progress state)
│   ├── nav.jsx               ← Navbar (receives props, renders category buttons)
│   ├── main.jsx              ← Entry point (never needs to change)
│   └── component/
│       ├── News.jsx          ← Main news feed (infinite scroll, API fetch)
│       ├── NewsItem.jsx      ← Single news card (pure display component)
│       └── TopLoadingBar.jsx ← Red progress bar below navbar
├── .env                      ← Secret API key (gitignored)
├── .env.example              ← Template for API key (safe to commit)
└── .gitignore
```

---

## 🔧 Step-by-Step Refactor

---

### Step 1 — `TopLoadingBar.jsx`

**Why start here?** It's the simplest component — no state, no effects. Just receives a prop and renders a styled div. Perfect for learning the pattern.

#### ❌ BEFORE (Class Component)

```jsx
import React, { Component } from 'react';

// Class components always need to extend Component from React
export default class TopLoadingBar extends Component {
  render() {
    // Props are accessed via this.props
    const progress = this.props.progress || 0;
    const isVisible = progress > 0;

    return (
      <div style={{ width: `${progress}%`, ... }} />
    );
  }
}
```

#### ✅ AFTER (Functional Component)

```jsx
// Step 1: Remove the Component import — functional components don't need it
import React from 'react';

// Step 2: Convert class to a plain function
// Props are received directly as a parameter — no `this` needed
const TopLoadingBar = ({ progress = 0 }) => {
  // Step 3: Just write logic directly in the function body (no render() method)
  const isVisible = progress > 0;

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        width: `${progress}%`,
        height: '3.5px',
        backgroundColor: '#ff0033',
        boxShadow: isVisible ? '0 0 10px #ff0033, 0 0 6px #ff0033' : 'none',
        transition: progress === 0 ? 'opacity 0.3s ease' : 'width 0.35s ease, opacity 0.35s ease',
        opacity: isVisible ? 1 : 0,
        zIndex: 1055,
        pointerEvents: 'none',
      }}
    />
  );
};

export default TopLoadingBar;
```

**What changed:**
- ❌ `class TopLoadingBar extends Component` → ✅ `const TopLoadingBar = ({ progress = 0 }) =>`
- ❌ `this.props.progress` → ✅ `progress` (destructured from props directly)
- ❌ `render() { return ... }` → ✅ `return ...` (no render wrapper needed)

---

### Step 2 — `NewsItem.jsx`

**Why?** Another pure display component — no state. Just receives props and returns JSX.

#### ❌ BEFORE (Class Component)

```jsx
import React, { Component } from "react";

export default class NewsItem extends Component {
  render() {
    // Must use this.props to access everything
    let { title, description, imageUrl, image_url, newsUrl, link, sourceName, date } = this.props;

    const defaultImg = "https://images.unsplash.com/...";
    const finalImg = imageUrl || image_url || defaultImg;
    const finalUrl = newsUrl || link || "#";

    return (
      <div className="h-100">
        ...card JSX...
      </div>
    );
  }
}
```

#### ✅ AFTER (Functional Component)

```jsx
// Step 1: Remove Component from imports
import React from "react";

// Step 2: Convert to arrow function — destructure all props directly in the parameter
const NewsItem = ({ title, description, imageUrl, image_url, newsUrl, link, sourceName, date }) => {
  // Step 3: All logic goes directly here — no render() wrapper
  const defaultImg = "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=600&auto=format&fit=crop&q=60";
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
            {description ? `${description.slice(0, 95)}...` : "Click below to read the complete article."}
          </p>
          {date && (
            <p className="card-text">
              <small className="text-muted">
                {new Date(date).toLocaleDateString("en-IN", {
                  month: "short",
                  day: "numeric",
                  year: "numeric",
                })}
              </small>
            </p>
          )}
          <a href={finalUrl} target="_blank" rel="noreferrer" className="btn btn-sm btn-dark mt-auto">
            Read More &rarr;
          </a>
        </div>
      </div>
    </div>
  );
};

export default NewsItem;
```

**What changed:**
- ❌ `class NewsItem extends Component` → ✅ `const NewsItem = ({ ...props }) =>`
- ❌ `let { ... } = this.props;` → ✅ Props destructured in function parameters
- ❌ `render() { return ... }` → ✅ Direct `return`

---

### Step 3 — `nav.jsx`

**Why?** Receives `category`, `setCategory`, and `progress` as props. Has a hardcoded array. No state inside — pure rendering.

#### ❌ BEFORE (Class Component)

```jsx
import React, { Component } from 'react';
import TopLoadingBar from './component/TopLoadingBar';

export default class Nav extends Component {
  // Class-level array (this is fine but not idiomatic React)
  categories = [
    { id: 'all', label: 'Home' },
    { id: 'entertainment', label: 'Entertainment' },
    { id: 'sports', label: 'Sport' },
    { id: 'stock', label: 'Stock' },
    { id: 'politics', label: 'Politics' },
    { id: 'business', label: 'Business' },
  ];

  render() {
    // Props accessed via this.props
    const { category, setCategory, progress } = this.props;
    ...
  }
}
```

#### ✅ AFTER (Functional Component)

```jsx
import React from 'react';
import TopLoadingBar from './component/TopLoadingBar';

// Step 1: Move the constant array OUTSIDE the component
// Why? It never changes, so it doesn't need to be recreated on every render
const CATEGORIES = [
  { id: 'all', label: 'Home' },
  { id: 'entertainment', label: 'Entertainment' },
  { id: 'sports', label: 'Sport' },
  { id: 'stock', label: 'Stock' },
  { id: 'politics', label: 'Politics' },
  { id: 'business', label: 'Business' },
];

// Step 2: Destructure props directly in the function signature — no `this` needed
const Nav = ({ category, setCategory, progress }) => {
  // Step 3: No render() — JSX is returned directly
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm position-relative">
      <div className="container-fluid">
        <a
          className="navbar-brand fw-bold text-warning"
          href="#"
          onClick={(e) => {
            e.preventDefault();
            setCategory('all'); // No `this.` needed — setCategory is just a variable
          }}
        >
          🐒 NewsMonkey
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {/* Step 4: Use the constant array — no `this.categories` */}
            {CATEGORIES.map((cat) => {
              const isActive = category === cat.id;
              return (
                <li className="nav-item" key={cat.id}>
                  <button
                    type="button"
                    className={`nav-link btn btn-link text-decoration-none ${
                      isActive ? 'active text-warning fw-bold' : 'text-light'
                    }`}
                    style={{ border: 'none', background: 'none' }}
                    onClick={() => setCategory(cat.id)}
                  >
                    {cat.label}
                  </button>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
      <TopLoadingBar progress={progress} />
    </nav>
  );
};

export default Nav;
```

**What changed:**
- ❌ `categories = [...]` inside class → ✅ `const CATEGORIES = [...]` outside function
- ❌ `this.props` → ✅ Destructured directly in function signature
- ❌ `this.categories.map(...)` → ✅ `CATEGORIES.map(...)`

---

### Step 4 — `News.jsx` (Most Important)

**Why is this the hardest?** Because it has:
- Multiple pieces of state
- A lifecycle method (`componentDidMount`)
- A cleanup method (`componentWillUnmount`)
- An `IntersectionObserver` stored as an instance variable (`this.observer`)
- Async data fetching

Each of these maps to a specific hook.

#### 🗺️ Concept Map: Class → Hooks

```
this.state = { articles: [] }              →  const [articles, setArticles] = useState([])
this.state = { loading: true }             →  const [loading, setLoading] = useState(true)
this.state = { loadingMore: false }        →  const [loadingMore, setLoadingMore] = useState(false)
this.state = { nextPageToken: null }       →  const [nextPageToken, setNextPageToken] = useState(null)
this.state = { hasMore: true }             →  const [hasMore, setHasMore] = useState(true)
this.state = { underMaintenance: false }   →  const [underMaintenance, setUnderMaintenance] = useState(false)

this.observer = null                       →  const observerRef = useRef(null)
  (instance variable, not state —          →  (useRef stores a value that persists across
   doesn't trigger re-render)                  renders without causing a re-render)

componentDidMount()                        →  useEffect(() => { ... }, [category])
  (runs after first render)                   ([] = run once on mount,
                                               [category] = re-run when category changes)

componentWillUnmount()                     →  return () => { cleanup } inside useEffect
  (cleanup when component is removed)         (the "cleanup return" of useEffect)
```

#### ❌ BEFORE (Class Component) — Key Sections

```jsx
import React, { Component } from 'react'
import NewsItem from './NewsItem'

export default class News extends Component {
  apiKey = import.meta.env.VITE_NEWS_API_KEY;

  static defaultProps = {
    category: 'all',
  };

  constructor(props) {
    super(props); // Always required in class components
    this.state = {
      articles: [],
      loading: true,
      loadingMore: false,
      nextPageToken: null,
      hasMore: true,
      underMaintenance: false,
    };
    this.observer = null; // Instance variable for IntersectionObserver
  }

  getCategoryFilter = () => {
    const category = this.props.category || 'all'; // this.props
    ...
  };

  fetchInitialNews = async () => {
    if (this.props.setProgress) this.props.setProgress(20); // this.props
    this.setState({ loading: true }); // this.setState
    ...
    this.setState({ articles: data.results }); // this.setState
  };

  fetchMoreNews = async () => {
    if (this.state.loadingMore) return; // this.state
    this.setState({ loadingMore: true }); // this.setState
    ...
  };

  componentDidMount() {
    this.fetchInitialNews(); // Lifecycle method
  }

  componentWillUnmount() {
    if (this.observer) {     // Instance variable
      this.observer.disconnect();
    }
  }

  sentinelRef = (element) => {
    if (this.observer) this.observer.disconnect(); // Instance variable
    if (element) {
      this.observer = new IntersectionObserver(...); // Instance variable
      this.observer.observe(element);
    }
  };

  render() {
    return (
      <div>
        ...{this.state.articles.map(...)} ...  // this.state everywhere
      </div>
    );
  }
}
```

#### ✅ AFTER (Functional Component)

```jsx
// Step 1: Import the hooks you need from React
import React, { useState, useEffect, useRef, useCallback } from 'react';
import NewsItem from './NewsItem';

// Step 2: API key stays the same — just a module-level constant
const API_KEY = import.meta.env.VITE_NEWS_API_KEY;

// Step 3: Convert to functional component
// Props are destructured directly — no `this`, no constructor
const News = ({ category = 'all', setProgress }) => {

  // ─── Step 4: useState — Replace ALL this.state properties ─────────────────
  // Each piece of state becomes its own useState call
  // Syntax: const [value, setterFunction] = useState(initialValue)
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);
  const [nextPageToken, setNextPageToken] = useState(null);
  const [hasMore, setHasMore] = useState(true);
  const [underMaintenance, setUnderMaintenance] = useState(false);

  // ─── Step 5: useRef — Replace instance variables (this.observer) ──────────
  // useRef stores a mutable value that persists across renders
  // but does NOT trigger a re-render when changed (unlike useState)
  // This is perfect for the IntersectionObserver which is not displayed in the UI
  const observerRef = useRef(null);

  // ─── Step 6: Helper function (no this needed) ─────────────────────────────
  const getCategoryFilter = () => {
    if (category === 'stock') return '&q=stock';
    if (category !== 'all') return `&category=${category}`;
    return '';
  };

  const getCategoryHeading = () => {
    switch (category) {
      case 'entertainment': return 'Entertainment News';
      case 'sports':        return 'Sports News';
      case 'stock':         return 'Stock & Market News';
      case 'politics':      return 'Politics News';
      case 'business':      return 'Business News';
      default:              return 'Top India Headlines (All News)';
    }
  };

  // ─── Step 7: Fetch functions (no this, use state setters directly) ─────────
  const fetchInitialNews = useCallback(async () => {
    // Call setProgress directly — no this.props.setProgress
    if (setProgress) setProgress(20);
    setLoading(true);
    setUnderMaintenance(false);
    setHasMore(true);

    try {
      const categoryFilter = getCategoryFilter();
      const url = `https://newsdata.io/api/1/news?apikey=${API_KEY}&country=in&language=en&size=6${categoryFilter}`;

      if (setProgress) setProgress(45);
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);

      if (setProgress) setProgress(70);
      const data = await response.json();

      if (data.status === 'success' && data.results?.length > 0) {
        if (setProgress) setProgress(90);

        // Use state setters directly — no this.setState
        setArticles(data.results);
        setNextPageToken(data.nextPage || null);
        setHasMore(Boolean(data.nextPage));
        setLoading(false);
        setUnderMaintenance(false);

        if (setProgress) {
          setProgress(100);
          setTimeout(() => setProgress(0), 350);
        }
      } else {
        throw new Error('No articles returned');
      }
    } catch (error) {
      console.error('NewsData API Error:', error);
      if (setProgress) {
        setProgress(100);
        setTimeout(() => setProgress(0), 350);
      }
      setUnderMaintenance(true);
      setLoading(false);
    }
  // useCallback dependency array — re-create this function only when category or setProgress changes
  }, [category, setProgress]);

  // fetchMoreNews reads loadingMore/hasMore/nextPageToken from state
  // useCallback prevents unnecessary re-creation of this function
  const fetchMoreNews = useCallback(async () => {
    // Access state values directly — no this.state
    if (loadingMore || !hasMore || !nextPageToken) return;

    setLoadingMore(true);

    try {
      const categoryFilter = getCategoryFilter();
      const url = `https://newsdata.io/api/1/news?apikey=${API_KEY}&country=in&language=en&size=6${categoryFilter}&page=${nextPageToken}`;

      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);

      const data = await response.json();

      if (data.status === 'success' && data.results?.length > 0) {
        // Deduplicate articles — use functional updater form of setState
        // prevArticles is the guaranteed up-to-date previous state
        setArticles((prevArticles) => {
          const existingIds = new Set(prevArticles.map((a) => a.article_id || a.link));
          const uniqueNew = data.results.filter((a) => !existingIds.has(a.article_id || a.link));
          return [...prevArticles, ...uniqueNew];
        });
        setNextPageToken(data.nextPage || null);
        setHasMore(Boolean(data.nextPage));
        setLoadingMore(false);
      } else {
        setHasMore(false);
        setLoadingMore(false);
      }
    } catch (error) {
      console.error('Error loading more news:', error);
      setLoadingMore(false);
    }
  }, [loadingMore, hasMore, nextPageToken, category]);

  // ─── Step 8: useEffect — Replace componentDidMount + componentWillUnmount ──
  //
  // useEffect(callback, dependencyArray)
  //
  //   [] empty array  = run once after first render (like componentDidMount)
  //   [category]      = re-run whenever `category` changes (category navigation)
  //   no array        = run after EVERY render (rarely needed)
  //   return fn       = the cleanup function (like componentWillUnmount)

  // Effect 1: Fetch fresh news whenever the category changes
  useEffect(() => {
    // Reset all state for the new category
    setArticles([]);
    setNextPageToken(null);
    setHasMore(true);
    setLoading(true);
    setUnderMaintenance(false);

    fetchInitialNews();
  }, [category]); // Re-runs when `category` prop changes

  // Effect 2: Manage the IntersectionObserver for infinite scroll
  // Depends on fetchMoreNews, which changes when scroll dependencies change
  useEffect(() => {
    // The sentinelRef callback equivalent:
    // Disconnect old observer before creating a new one
    if (observerRef.current) {
      observerRef.current.disconnect();
    }

    // Create a new IntersectionObserver that fires fetchMoreNews
    // rootMargin: '250px' means it fires 250px BEFORE the element is visible
    observerRef.current = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          fetchMoreNews();
        }
      },
      { rootMargin: '250px' }
    );

    // Observe the sentinel element (referenced via a separate ref below)
    if (sentinelElement.current) {
      observerRef.current.observe(sentinelElement.current);
    }

    // Cleanup: disconnect when component unmounts OR when fetchMoreNews changes
    // This replaces componentWillUnmount
    return () => {
      if (observerRef.current) {
        observerRef.current.disconnect();
      }
    };
  }, [fetchMoreNews]); // Re-run when fetchMoreNews reference changes

  // Ref for the sentinel div at the bottom of the list
  const sentinelElement = useRef(null);

  // ─── Step 9: Return JSX — no render() wrapper needed ──────────────────────
  return (
    <div className="container my-4">
      <div className="text-center mb-4">
        <h2 className="fw-bold">NewsMonkey - {getCategoryHeading()}</h2>
        {/* Access state variables directly — no this.state */}
        <p className="text-muted">
          Continuous live feed &bull; {articles.length} stories loaded
        </p>
      </div>

      {/* Maintenance screen — no this.state.underMaintenance */}
      {underMaintenance && (
        <div className="row justify-content-center my-5">
          <div className="col-md-8">
            <div className="card text-center shadow border-warning">
              <div className="card-body p-5">
                <div style={{ fontSize: '3.5rem' }}>🛠️</div>
                <h3 className="card-title text-danger mt-3">News App Under Maintenance</h3>
                <p className="card-text text-muted mt-2">
                  We are unable to connect to the news server. Please try again.
                </p>
                {/* Call fetchInitialNews directly — no this.fetchInitialNews */}
                <button className="btn btn-dark mt-3" onClick={fetchInitialNews}>
                  🔄 Retry Connection
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* News Grid — direct state access, no `this.` */}
      {!loading && !underMaintenance && (
        <>
          <div className="row g-4">
            {articles.map((article, index) => (
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

          {/* Sentinel element — use ref object instead of callback ref */}
          {hasMore && (
            <div ref={sentinelElement} className="text-center my-4 py-3">
              {loadingMore && (
                <div>
                  <div className="spinner-border text-primary" role="status">
                    <span className="visually-hidden">Loading more...</span>
                  </div>
                  <p className="text-muted mt-2 small">Loading more news...</p>
                </div>
              )}
            </div>
          )}

          {!hasMore && articles.length > 0 && (
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
};

export default News;
```

---

### Step 5 — `App.jsx`

**Why?** Root component — manages `category` and `progress` state, passes them down.

#### ❌ BEFORE (Class Component)

```jsx
import React, { Component } from 'react'
import Nav from './nav'
import News from './component/News'

export default class App extends Component {
  state = {
    category: 'all',
    progress: 0,
  }

  setProgress = (progress) => {
    this.setState({ progress });
  }

  setCategory = (category) => {
    this.setState({ category, progress: 15 }); // Kick off loading bar
  }

  render() {
    return (
      <div>
        <Nav
          category={this.state.category}
          setCategory={this.setCategory}
          progress={this.state.progress}
        />
        <News
          key={this.state.category}
          category={this.state.category}
          setProgress={this.setProgress}
        />
      </div>
    )
  }
}
```

#### ✅ AFTER (Functional Component)

```jsx
// Step 1: Import useState instead of Component
import React, { useState } from 'react';
import Nav from './nav';
import News from './component/News';

const App = () => {
  // Step 2: Replace this.state with individual useState hooks
  const [category, setCategory] = useState('all');
  const [progress, setProgress] = useState(0);

  // Step 3: Replace class methods with plain functions
  // This function is passed to Nav as a prop
  const handleCategoryChange = (newCategory) => {
    setCategory(newCategory);  // No this.setState — just call the setter directly
    setProgress(15);           // Kick off the top loading bar animation
  };

  // Step 4: Return JSX directly — no render() method
  return (
    <div>
      <Nav
        category={category}          // No this.state.category
        setCategory={handleCategoryChange}
        progress={progress}          // No this.state.progress
      />
      <News
        key={category}               // key prop forces full remount on category change
        category={category}
        setProgress={setProgress}    // Pass the setter directly as a prop
      />
    </div>
  );
};

export default App;
```

---

## 🧩 Quick Reference: The 4 Core Hooks Used

### `useState`
```jsx
// Declare a state variable and its setter
const [count, setCount] = useState(0);

// Reading: just use `count` directly
console.log(count);

// Writing: call the setter
setCount(5);

// Functional update (use when new state depends on old state)
setCount(prev => prev + 1);
```

### `useEffect`
```jsx
// Runs ONCE after mount (like componentDidMount)
useEffect(() => {
  fetchData();
}, []);

// Runs when `category` changes (like componentDidUpdate)
useEffect(() => {
  fetchData();
}, [category]);

// Cleanup on unmount (like componentWillUnmount)
useEffect(() => {
  const timer = setInterval(...);
  return () => clearInterval(timer); // ← cleanup function
}, []);
```

### `useRef`
```jsx
// Store a mutable value that does NOT trigger re-render
const observerRef = useRef(null);
observerRef.current = new IntersectionObserver(...);

// Attach to DOM element
const myDiv = useRef(null);
<div ref={myDiv}> ... </div>
// Access: myDiv.current.scrollTop
```

### `useCallback`
```jsx
// Memoize a function so it is only re-created when dependencies change
// Prevents unnecessary re-renders of child components that receive this function as a prop
const fetchMore = useCallback(async () => {
  ...
}, [dependency1, dependency2]);
```

---

## ⚠️ Common Mistakes to Avoid

| Mistake | Why It's Wrong | Fix |
|:---|:---|:---|
| `this.state.articles` in functional | `this` does not exist | Just use `articles` |
| `this.setState({ articles: [] })` | `this` does not exist | Use `setArticles([])` |
| `this.props.category` in functional | `this` does not exist | Destructure: `const News = ({ category })` |
| Calling `setState` inside `useEffect` without a dependency array | Infinite loop | Add proper dependency array `[]` or `[dep]` |
| Forgetting cleanup return in `useEffect` | Memory leak from observers/timers | Always return cleanup: `return () => observer.disconnect()` |
| Putting API calls outside `useEffect` | Runs on every render | Always wrap async fetches in `useEffect` |

---

## 🚀 Refactoring Order (Recommended)

```
1. TopLoadingBar.jsx   ← Easiest: no state, no effects, pure props → JSX
2. NewsItem.jsx        ← Easy: no state, no effects, just props + rendering  
3. nav.jsx             ← Easy: no state, just props and a constant array
4. App.jsx             ← Medium: two useState hooks, two handler functions
5. News.jsx            ← Hardest: multiple useState, useEffect, useRef, useCallback
```

> **Pro tip:** Always refactor the simplest components first. It builds your confidence and lets you spot the pattern before tackling the complex ones.

---

## 📝 Summary of All Changes

| What to remove (Class) | What to add (Functional) |
|:---|:---|
| `class X extends Component` | `const X = () =>` |
| `constructor(props)` | Nothing needed |
| `super(props)` | Nothing needed |
| `this.state = { ... }` | `const [x, setX] = useState(...)` |
| `this.setState({ x: val })` | `setX(val)` |
| `this.props.something` | `something` (from destructured params) |
| `render() { return ... }` | Just `return ...` |
| `componentDidMount()` | `useEffect(() => { ... }, [])` |
| `componentWillUnmount()` | `return () => cleanup` inside `useEffect` |
| `this.someVar = value` (instance var) | `const someRef = useRef(value)` → `someRef.current` |
| `static defaultProps = {...}` | Default values in function params `= defaultValue` |

---

*Generated as a personal study guide — CodeWithHarry React Course, Video #39*
