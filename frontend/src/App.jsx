import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import Todo from './components/Todo'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <div>
        {/* <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a> */}
        {/* <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a> */}
      </div>
      <h1>While Mom Is Away App</h1>
      <div className="card">
        <Todo />
        {/* <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button> */}
      </div>
    </>
  )
}

export default App