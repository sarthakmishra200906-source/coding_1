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
    // When navigating to a new category, kick off the progress bar
    this.setState({ category, progress: 15 });
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
