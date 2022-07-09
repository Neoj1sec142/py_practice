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
        <div></div>
    )
}

export default LoginPage