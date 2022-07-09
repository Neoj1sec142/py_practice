// Service and Module Imports
import React, {useState, useEffect} from 'react'
import { Route, Routes } from 'react-router-dom'
import { CheckSession } from "./services/Auth";
import {LoginContext} from './services/LoginContext.jsx'
// Page and Component Imports
import Bar from './components/Nav'
import LoginPage from './components/Login';
import Register from './components/Register';
import Home from './pages/Home'
// Style Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import './styles/App.css'

const App = () => {
  const [authenticated, toggleAuthenticated] = useState(false)
  const [user, setUser] = useState(null)
  const [userInfo, setUserInfo] = useState(null)

  const checkToken = async () => {
    const user = await CheckSession()
    setUser(user)
    setUserInfo(user)
    toggleAuthenticated(true)
  }

  const handleLogout = () => {
    setUser(null)
    setUserInfo(null)
    toggleAuthenticated(false)
    localStorage.clear()
  }

  useEffect(() => {
    const token = localStorage.getItem('token')
    if(token){
      checkToken()
    }
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <Bar authenticated={authenticated} user={user} handleLogout={handleLogout}/>
      </header>
      <LoginContext.Provider value={{userInfo, setUserInfo}}>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/register' element={<Register/>}/>
      </Routes>
      </LoginContext.Provider>
    </div>
  )
}

export default App
