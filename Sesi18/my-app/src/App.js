import { useState, useEffect } from 'react'
import logo from './logo.svg';
import './App.css';
import Counter from './components/counter';
import Card from './components/card';
// import Header from './components/header';
// import Button from './components/button';

function App() {

  const [ todos, setTodos ] = useState([])
  const [ todo, setTodo ] = useState()
  const [ name, setName  ] = useState('Budi')
  const [ anotherName, setAnotherName ] = useState('Pohan')
  const [ url ] = useState('https://jsonplaceholder.typicode.com/todos')

  function changeName (e) {
    console.log(e)
    const oldName = name
    setName(anotherName)
    setAnotherName(oldName)
  }

  function getTodo(id){
    fetch(url + `/${id}`)
      .then(response => response.json())
      .then(result => setTodo(result))
  }

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos')
      .then(response => response.json())
      .then(result => setTodos(result))
  }, [])

  useEffect(()=> {
    console.log(todos)
  }, [todos])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {
          todo && (
            <div>
              {todo.title} - {todo.userId} - { todo.completed ? 'Completed' : 'Pending' }
              <button onClick={() => setTodo()}>Go back</button>
            </div>
          )
        }
        
        {
          !todo && todos.map(todo => (
            // <div key={todo.id}>
            //   <button onClick={() => getTodo(todo.id)}>
            //     {todo.title} by {todo.userId}
            //   </button>
            // </div>
            <Card key={todo.id} title={todo.title} userId={todo.userId} completed={todo.completed}/>
          ))
        }
        <p>
          Edit <code>{name}</code> and save to reload.
        </p>
        {/* <button onClick={changeName}>Ganti Nama</button> */}
        <Counter />
        {/* <Header batch="2" logo={logo}/>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

// class App extends Component {
//   render() {
//     return (
//       <div className="App">
//         <div className="App-header">
//           <img src={logo}className="App-logo"alt="logo"/>
//           <h2>Welcome to React</h2>
//         </div>
//         <p className="App-intro"> Saya belajar dengan tekun supaya bisa menjadi website developer yang hebat.</p>
//       </div>
//     )
//   }
// }

export default App;
