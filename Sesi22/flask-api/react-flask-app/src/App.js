import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [placeholder, setPlaceholder] = useState('Hi')
  const [currentTime, setCurrentTime] = useState(0)

  useEffect(() => {
    fetch('/hello').then(res => res.json()).then(data => {
      console.log(data);
      setPlaceholder(data.message)

      const timeInterval = setInterval(() => {
        fetch('/time')
        .then((res)=> res.json())
        .then((data) => setCurrentTime(data.time))
      }, 1000)

      return() => {
        clearInterval(timeInterval)
      }
    })
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>Flask says {placeholder}</p>
        <p>The current time is <code>{currentTime && new Date(currentTime * 1000).toString()}</code></p>
      </header>
    </div>
  );
}

export default App;
