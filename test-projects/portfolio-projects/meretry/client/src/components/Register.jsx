import React, {useState} from 'react'
import {RegisterUser} from '../services/Auth'
import { useNavigate } from 'react-router-dom'
import {Card} from 'react-bootstrap'

const Register = () => {
    let nav = useNavigate()
    const [newUser, setNewUser] = useState({
        fullname: '',
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
            fullname: newUser.fullname,
            username: newUser.username, 
            email: newUser.email,
            password: newUser.password
        })
        setNewUser({
            fullname: '',
            username: '',
            email: '',
            password: '',
            confirmPassword: ''
        })
        nav('/login')
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
                            name='fullname'
                            placeholder='Enter Your Full Name'
                            value={newUser.fullname}
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