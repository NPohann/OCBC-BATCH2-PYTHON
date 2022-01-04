import './App.css';
import Content from './components/content';
import Header from './components/header';

function Footer() {
  return (
    <div className="footer">
      <p>&copy; My self - 2021</p>
    </div>
  )
}

function App() {
  return (
    <div className="container">
      <Header />
      <hr />
      <Content />
      <hr />
      <Footer />
    </div>
  )
}

export default App