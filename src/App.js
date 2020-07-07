import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { FileAttachment } from 'material-ui/svg-icons';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { apiResponse: "" };
  }

  callApi() {
    fetch("http://localhost:5000/")
      .then(res => res.text())
      .then(res => this.setState({ apiResponse: res }))
      .catch(err => err);
  }

  componentDidMount() {
    this.callApi();
  }

  render() {
    return (
      <h1>Test.</h1>
    );
  }
}

export default App;
