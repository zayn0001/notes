import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import Navbar from './Navbar/Navbar.js';
import Footer from './Footer/Footer.js'

ReactDOM.render(
  <>
  <Navbar />
  <Footer />
  </>,
  document.getElementById('root')
);

//components can be inside components
















// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
