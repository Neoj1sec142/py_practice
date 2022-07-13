import React from 'react'
import { useNavigate } from 'react-router-dom'
const BlogManagement = (props) => {
    const nav = useNavigate()
    const nav1 = () => {
        nav('/mdash')
    }
    return(
        <div className='container'>
            <h1>Blog Posts To manage Here</h1>
            <button className='btn btn-outline-dark' onClick={nav1}>Back to Dash</button>
        </div>
    )
}
export default BlogManagement