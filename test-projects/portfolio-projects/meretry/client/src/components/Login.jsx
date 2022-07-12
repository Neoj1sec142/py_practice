import React, {useState, useContext} from 'react'
import { useNavigate, Link } from 'react-router-dom'
import {LoginContext} from '../services/LoginContext'
// import {SignInUser} from '../services/Auth'
import Client from '../services/api'


const LoginPage = (props) => {
    let navigate = useNavigate()
    const [{setLoginStatus}] = useContext(LoginContext)
    const [login, setLogin] = useState({username: '', password: ''})

    const handleChange = (e) => {setLogin({...login, [e.target.name]: e.target.value})}
    
    const handleSubmit = async (e) => {
        e.preventDefault()
        await Client.post('token/obtain/', {
            username: login.username,
            password: login.password
        })
        .then(res => {
            if(res.status === 200){
                Client.defaults.headers['Authorization'] = `JWT ${res.data.access}`
                localStorage.setItem('access_token', res.data.access)
                localStorage.setItem('refresh_token', res.data.refresh)
            }else{return res}
        })
        .then(res => {
            Client.get(`users/${login.username}`)
            .then(res => {
                localStorage.setItem('user_id', res.data.id)
                localStorage.setItem('username', login.username)
                setLoginStatus(true)
            })
            navigate('/welcome')
        })
        .catch(err => console.log(err, "C-Login-35"))
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <div className="row mb-3">
                    <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Email</label>
                    <div className="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='username'
                            placeholder='Enter Username'
                            value={login.username}
                            maxLength='250'
                            required
                            className="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div className="row mb-3">
                    <label htmlFor="inputPassword3" className="col-sm-2 col-form-label">Password</label>
                    <div className="col-sm-10">
                        <input 
                            type="password" 
                            onChange={handleChange}
                            name='password'
                            value={login.password}
                            maxLength='250'
                            required
                            className="form-control" 
                            id="inputPassword3"/>
                    </div>
                </div>
                <button type='submit' disabled={!login.username || !login.password}>Log In</button>
                <h4>Don't have an account?<Link to={'/register'}>Click Here</Link> to register.</h4>
            </form>
        </div>
    )
}

export default LoginPage