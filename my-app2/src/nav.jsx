import React, { Component } from 'react'
import TopLoadingBar from './component/TopLoadingBar'

export default class Nav extends Component {
  categories = [
    { id: 'all', label: 'Home' },
    { id: 'entertainment', label: 'Entertainment' },
    { id: 'sports', label: 'Sport' },
    { id: 'stock', label: 'Stock' },
    { id: 'politics', label: 'Politics' },
    { id: 'business', label: 'Business' },
  ];

  render() {
    const { category, setCategory, progress } = this.props;

    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm position-relative">
        <div className="container-fluid">
          <a
            className="navbar-brand fw-bold text-warning"
            href="#"
            onClick={(e) => {
              e.preventDefault();
              setCategory('all');
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
              {this.categories.map((cat) => {
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

        {/* Red Top Loading Bar situated directly below the navbar */}
        <TopLoadingBar progress={progress} />
      </nav>
    );
  }
}
