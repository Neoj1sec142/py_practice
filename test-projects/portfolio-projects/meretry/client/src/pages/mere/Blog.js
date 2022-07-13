import React, {useState, useEffect} from 'react'

const Blog = () => {
    const [pst, setPst] = useState({
        title: '',
        text: ''
    })
    const handleChange = (e) => {
        setPst({...pst, [e.target.name]: e.target.value})
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
            </form>
        </div>
    )
}
export default Blog