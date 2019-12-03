import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './App.css';

class App extends Component {
  render () {
    return (    
    <Router>
      <div>
        <Route path="/" exact component={Home} />
        <Route path="/howitworks" component={How} />
        <Route path="/addtodatabase" component={Add} />
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
          <header className="App-header">
            <p className = "left">
              <Link to="/addtodatabase" style={{color: 'white', textDecoration: 'underline'}}>Add to database</Link>
            </p>
            <p>
              WhatsFake
            </p>
            <p className = "right">
              <Link to="/howitworks" style={{color: 'white', textDecoration: 'underline'}}>How it works</Link>
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
          {this.state.isResult ? (<div className = "result">
            <p> The entered news {this.state.value} is {this.state.result}</p>
            </div>) : ( <p></p>)}
      </div>
    );
  }
}

class How extends Component {
  render () {
    return ( 
      <div className="App">
        <p className = "right">
          <Link to="/" style={{color: 'white', textDecoration: 'underline'}}>Back</Link>
        </p>
        <p className ="textbox">
        Scikit-learn (formerly scikits.learn) is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
        </p>
      </div>
    )
  }
}

class Add extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
    };

    this.handleChange2 = this.handleChange2.bind(this);
    this.handleSubmit2 = this.handleSubmit2.bind(this);
  }

  handleChange2(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit2(event) {
    alert("Your submission was added to the database.")
    this.setState({value: ''});
  }

  render () {
    return (
      <div className="App">
          <header className="App-header">
            <p>
              <Link to="/" style={{color: 'white', textDecoration: 'underline'}}>Back</Link>
            </p>
          </header>
          <p className ="text">
            Add to our database
          </p>
          <div className="Form">
            <form onSubmit={this.handleSubmit2}>
              <label>
                <input 
                  type="text" 
                  value={this.state.value} 
                  onChange={this.handleChange2}
                  placeholder = "Paste the news to grow our database" 
                  className ="input" />
              </label>
              <input type="submit" value="Submit" className ="submit" />
            </form>
            <p className = "text2"> 
              Submit a news article title, that will be added to our database, so that our algorithm keeps providing updated results.
            </p>
          </div>
      </div>
    )
  }
}

export default App;
