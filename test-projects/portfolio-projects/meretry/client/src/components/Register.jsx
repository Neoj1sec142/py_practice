import React, {useState} from 'react'
import {RegisterUser} from '../services/Auth'
import Client from '../services/api'
import { useNavigate } from 'react-router-dom'
import {Card} from 'react-bootstrap'

const Register = () => {
    let nav = useNavigate()
    const [newUser, setNewUser] = useState({
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
    })

    const handleChange = (e) => {
        setNewUser({...newUser, [e.target.name]: e.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        await RegisterUser({
            first_name: newUser.first_name,
            last_name: newUser.last_name,
            username: newUser.username, 
            email: newUser.email,
            password: newUser.password
        })
        .then((res) => {
            localStorage.setItem('username', newUser.username)
            localStorage.setItem('user_id', res.data.id)
            Client.post('token/obtain/', {
                username: newUser.username,
                password: newUser.password
            }, {mode: "CORS"})
            .then(res => {
                Client.defaults.headers['Authorization'] = `JWT ${res.data.access}`
                localStorage.setItem('access_token', res.data.access)
                localStorage.setItem('refresh_token', res.data.refresh)
                nav('/login')
                return res
            })
        })
        setNewUser({
            first_name: '',
            last_name: '',
            username: '',
            email: '',
            password: '',
            confirmPassword: ''
        })
    }
    return(
        <div className='container'>
            <div class="title">
                <h2>Register Your Account</h2>
            </div>
            <form className="col" onSubmit={handleSubmit}>
                <div class="row mb-3">
                    {/* <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='first_name'
                            placeholder='Enter Your First Name'
                            value={newUser.first_name}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    {/* <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='last_name'
                            placeholder='Enter Your Last Name'
                            value={newUser.last_name}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    {/* <label for="inputEmail3" class="col-sm-2 col-form-label">Username</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='username'
                            placeholder='Create Your Username'
                            value={newUser.username}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    {/* <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="email"
                            onChange={handleChange} 
                            name='email'
                            placeholder='Enter Your Email'
                            value={newUser.email}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    {/* <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="password" 
                            onChange={handleChange}
                            name='password'
                            placeholder='Choose Your Password'
                            value={newUser.password}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputPassword3"/>
                    </div>
                </div>
                <div class="row mb-3">
                    {/* <label for="inputPassword3" class="col-sm-2 col-form-label">Confirm Password</label> */}
                    <div class="col-sm-10">
                        <input 
                            type="password" 
                            onChange={handleChange}
                            name='confirmPassword'
                            placeholder='Confirm Your Password'
                            value={newUser.confirmPassword}
                            maxLength='250'
                            required
                            class="form-control" 
                            id="inputPassword3"/>
                    </div>
                </div>
                <button
                    disabled={
                    !newUser.email ||
                    (!newUser.password &&
                        newUser.confirmPassword === newUser.password)
                    }>Sign In</button>
            </form>
        </div>
    )
}

export default Register