import Content from './components/content';
import Footer from './components/footer';
import Header from './components/header';
import logo from './logo.svg';
import React from 'react';
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div>
      <Header />
      <div className='container'>
        <Content />
      </div>
      <Footer />
    </div>
  );
}

export default App;
