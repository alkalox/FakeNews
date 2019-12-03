import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }
  
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
            What news do you want to fact check?
          </p>
          <div className="Form">
            <form onSubmit={this.handleSubmit}>
              <label>
                <input 
                  type="text" 
                  value={this.state.value} 
                  onChange={this.handleChange} 
                  placeholder = "Paste the news you want to fact check.." 
                  className ="input" />
              </label>
              <input type="submit" value="Submit" className ="submit" />
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
