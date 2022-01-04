import React from 'react';
import './App.css';
import Times from './components/time';

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      date: new Date()
    }
  }

  tick() {
    this.setState({
      date: new Date()
    })
  }

  componentWillUnmount() {
    clearInterval(this.timerID)
  }

  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000)
  }

  render() {
    return (
      <div className='App'>
        <h1>Realtime Clock</h1>
        <hr />
        <h1>{this.state.date.toLocaleTimeString()}</h1>
        <Times />
      </div>
    )
  }
}

// function App() {
//   return (
//     <Times />
//   )
// }

export default App;
