// Service and Module Imports
import React, {useState, useEffect} from 'react'
import { Route, Routes } from 'react-router-dom'
import { CheckSession } from "./services/Auth";
import Client from './services/api';
import {LoginContext} from './services/LoginContext.jsx'
// Page and Component Imports
import Bar from './components/Nav'
import LoginPage from './components/Login';
import Register from './components/Register';
import Home from './pages/Home'
import Welcome from './pages/Welcome'
import Dash from './pages/mere/Dash';
import Blog from './pages/mere/Blog';
import BlogManagement from './pages/mere/BlogManagement';
import Profile from './pages/Profile';
import Portfolio from './pages/Portfolio';
// Style Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import './styles/App.css'

const App = () => {
  const [loginStatus, setLoginStatus] = useState(false)
  const [user, setUser] = useState({})

  useEffect(() => {
    const user_id = localStorage.getItem('user_id')
    const username = localStorage.getItem('username')
    setUser(user_id, username)
    if(user_id && username){
      if(loginTest(username)) setLoginStatus(true)
    }else setLoginStatus(false)
  }, [loginStatus])

  const loginTest = async (username) => {
    await Client.get(`users/${username}`)
    .then(res => {
      if (res.status === 200){
        setLoginStatus(true)
        return true
      }else{
        setLoginStatus(false)
        return false
      }
    })
    .catch(err => {
      setLoginStatus(false)
      console.log(err, "ERROR HERE")
    })
  }

  return (
    <div className="App">
      <LoginContext.Provider value={{loginStatus, setLoginStatus, user, setUser}}>
      <header className="App-header">
        
        <Bar loginStatus={loginStatus} user={user}/>
      </header>
      <main role="main" className="container">
        {/* <div className="col-md-4 position-absolute top-20 end-0">
          <div className="content-section">
            <h3>Latest Activity</h3>
            <p className='text-muted'>You can put any information here you'd like.
              <ul className="list-group">
                <li className="list-group-item list-group-item-light">Latest Posts</li>
                <li className="list-group-item list-group-item-light">Announcements</li>
                <li className="list-group-item list-group-item-light">Calendars</li>
                <li className="list-group-item list-group-item-light">etc</li>
              </ul>
            </p>
          </div>
        </div> */}
        <div style={{marginTop: "2em"}}>
          
          <Routes>
            <Route path='/' element={<Home/>}/>
            <Route path='/welcome' element={<Welcome loginStatus={loginStatus} user={user}/>}/>
            <Route path='/blog' element={<Blog loginStatus={loginStatus} user={user}/>}/>
            <Route path='/blogmanage' element={<BlogManagement loginStatus={loginStatus} user={user}/>}/>
            <Route path='/mdash' element={<Dash loginStatus={loginStatus} user={user}/>}/>
            <Route path='/port' element={<Portfolio loginStatus={loginStatus} user={user}/>}/>
            <Route path='/profile' element={<Profile loginStatus={loginStatus} user={user}/>}/>
            <Route path='/login' element={<LoginPage/>}/>
            <Route path='/register' element={<Register/>}/>
          </Routes>
          
        </div>
      </main>
      </LoginContext.Provider>
    </div>
  )
}

export default App
