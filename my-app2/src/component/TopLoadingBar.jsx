import React, { Component } from 'react';

export default class TopLoadingBar extends Component {
  render() {
    const progress = this.props.progress || 0;
    const isVisible = progress > 0;

    return (
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          width: `${progress}%`,
          height: '3.5px',
          backgroundColor: '#ff0033', // Vibrant red
          boxShadow: isVisible ? '0 0 10px #ff0033, 0 0 6px #ff0033' : 'none',
          transition: progress === 0 ? 'opacity 0.3s ease' : 'width 0.35s ease, opacity 0.35s ease',
          opacity: isVisible ? 1 : 0,
          zIndex: 1055,
          pointerEvents: 'none',
        }}
      />
    );
  }
}

