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
import Welcome from './pages/Welcome'
import Dash from './pages/mere/Dash';
import Blog from './pages/mere/Blog';
// Style Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import './styles/App.css'
import BlogManagement from './pages/mere/BlogManagement';



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
          <LoginContext.Provider value={{userInfo, setUserInfo}}>
          <Routes>
            <Route path='/' element={<Home/>}/>
            <Route path='/welcome' element={<Welcome authenticated={authenticated} user={user}/>}/>
            <Route path='/blog' element={<Blog authenticated={authenticated} userInfo={userInfo}/>}/>
            <Route path='/blogmanage' element={<BlogManagement authenticated={authenticated} userInfo={userInfo}/>}/>
            <Route path='/mdash' element={<Dash authenticated={authenticated} userInfo={userInfo}/>}/>
            <Route path='/login' element={<LoginPage/>}/>
            <Route path='/register' element={<Register/>}/>
          </Routes>
          </LoginContext.Provider>
        </div>
      </main>
    </div>
  )
}

export default App
