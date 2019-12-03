import React, { Component } from 'react';
import './App.css';
import { LOADIPHLPAPI } from 'dns';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      str: '',
      result: '',
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    this.setState({str: this.state.value});
    this.getPrediction();
    alert(this.state.value);
    event.preventDefault();
  }

  getPrediction = async() => {
    const response = await fetch('http://127.0.0.1:5000/string/?stringname=' + this.state.str)
    this.setState({result:response})
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
            What news do you want to fact check? {this.state.str}
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
