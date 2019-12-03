import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './App.css';

class App extends Component {
  render () {
    return (    
    <Router>
      <div>
        <Route path="/" exact component={Home} />
        <Route path="/howitworks" exact component={How} />
      </div>
    </Router>)
  }
}

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      str: '',
      result: '',
      isResult: false,
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
    event.preventDefault();
  }

  getPrediction = async() => {
    const response = await fetch('http://127.0.0.1:5000/string?stringname=' + this.state.value)
    const convert = await response.json()
    this.setState({result:convert})
    this.setState({isResult:true})
  }

  
  render() {
    return (
      <div className="App">
        <div className = "Header">
          <header className="App-header">
            <Link to="/howitworks">How it works</Link>
            <p>
              WhatsFake
            </p>
            <Link to="/howitworks">How it works</Link>
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
          {this.state.isResult ? (<div className = "result">
            <p> The entered news {this.state.value} is {this.state.result}</p>
            </div>) : ( <p></p>)}
        </div>
      </div>
    );
  }
}

class How extends Component {
  render () {
    return ( 
      <h1>
        This is how it works
      </h1>   
    )
  }
}



export default App;
