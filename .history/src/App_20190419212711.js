import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className = "Header">
          <header className="App-header">
            <p>
              WhatsFake
            </p>
          </header>
          <p className ="text">
            What text do you want to fact check?
          </p>
          <form onSubmit={alert("yo")}>
            <label>
              Name:
              <input type="text" value={this.state.value} onChange={this.handleChange} />
            </label>
            <input type="submit" value="Submit" />
          </form>
        </div>
      </div>
    );
  }
}

export default App;
