import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import {CreatePost} from '../../services/BlogServices'
// import BlogManagement from './BlogManagement'
const Blog = () => {
    const nav = useNavigate()
    
    const [pst, setPst] = useState({
        title: '',
        text: ''
    })
    const handleChange = (e) => {
        setPst({...pst, [e.target.name]: e.target.value})
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        await CreatePost(pst)
        // alert(`Title: ${pst.title}\nText: ${pst.text}`)
        setPst({title: '', text: ''})
    }
    const Nav1 = (e) => {
        nav("/blogmanage")
    }
    
    return(
        <div className="container">
            <form>
                <div className="row mb-3">
                    <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Title</label>
                    <div className="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='title'
                            placeholder='Enter Title'
                            value={pst.title}
                            maxLength='250'
                            required
                            className="form-control" 
                            id="inputEmail3"/>
                    </div>
                    </div>
                    <div className="row mb-3">
                    <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Text</label>
                    <div className="col-sm-10">
                        <input 
                            type="text"
                            onChange={handleChange} 
                            name='text'
                            placeholder='Enter Text Here'
                            value={pst.text}
                            maxLength='250'
                            required
                            className="form-control" 
                            id="inputEmail3"/>
                    </div>
                </div>
                <button className='btn btn-outline-dark' type='submit' onClick={handleSubmit}>Submit</button>
            </form>
            <button className='btn btn-outline-dark' onClick={Nav1}>Manage Personal Blog</button>
        </div>
    )
}
export default Blog