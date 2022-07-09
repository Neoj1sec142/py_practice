import React, {useState} from 'react'
import { useNavigate, Link } from 'react-router-dom'
import {SignInUser} from '../services/Auth'

const LoginPage = (props) => {
    let navigate = useNavigate()
    const [user, setUser] = useState({username: '', password: ''})

    const handleChange = (e) => {
        setUser({...user, [e.target.name]: e.target.value})
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        const payload = await SignInUser(user)
        props.setUser(payload)
        props.toggleAuthenticated(true)
        setUser({username: '', password: ''})
        navigate('/')
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <div class="row mb-3">
                    <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
                    <div class="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='username'
                            placeholder='Enter Username'
                            value={user.username}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
                    <div class="col-sm-10">
                        <input 
                            type="password" 
                            onChange={handleChange}
                            name='password'
                            value={user.password}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputPassword3"/>
                    </div>
                </div>
                <button type='submit' disabled={!user.username || !user.password}>Log In</button>
                <h4>Don't have an account?<Link to={'/register'}>Click Here</Link> to register.</h4>
            </form>
        </div>
    )
}

export default LoginPage