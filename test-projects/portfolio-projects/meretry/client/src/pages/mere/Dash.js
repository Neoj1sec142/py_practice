import { useState } from "react"
import Blog from "./Blog"
const Dash = (props) => {
    const [btn, setBtn] = useState(0)
    // console.log(props, "Props")
    if(btn === 0){
        return(
            <div className="row-md-4">
            <div className="content-section">
                <h3 className="title">Meredith's Dashboard</h3>
                <div className='title text-muted'>These are links to tools only you have access too.
                <ul className="list-group">
                    <li className="list-group-item list-group-item-dark"><button onClick={() => setBtn(1)} className="btn btn-outline-secondary">Manage Posts</button></li>
                    <li className="list-group-item list-group-item-dark"><button onClick={() => setBtn(2)} className="btn btn-outline-secondary">Personal Blog</button></li>
                    <li className="list-group-item list-group-item-dark"><button onClick={() => setBtn(3)} className="btn btn-outline-secondary">Calendars</button></li>
                    <li className="list-group-item list-group-item-dark"><button onClick={() => setBtn(4)} className="btn btn-outline-secondary">Check Bookings</button></li>
                    <li className="list-group-item list-group-item-dark"><button onClick={() => setBtn(0)} className="btn btn-outline-secondary">Back to Dash</button></li>
                </ul>
                </div>
            </div>
            </div>
        )
    }else if(btn === 1){
        return(
            <div>
                <h1>Post Management Component Here</h1>
                <button className="btn btn-outline-secondary" onClick={() => setBtn(0)}>Back to Dash</button>
            </div>
        )
    }else if (btn === 2){
        return(
            <div>
                <h1>Personal Blog</h1>
                <Blog />
                <button className="btn btn-outline-secondary" onClick={() => setBtn(0)}>Back to Dash</button>
            </div>
        )
    }else if(btn === 3){
        return(
            <div>
                <h1>Post Management Component Here</h1>
                <button className="btn btn-outline-secondary" onClick={() => setBtn(0)}>Back to Dash</button>
            </div>
        )
    }else if(btn === 4){
        return(
            <div>
                <h1>Post Management Component Here</h1>
                <button className="btn btn-outline-secondary" onClick={() => setBtn(0)}>Back to Dash</button>
            </div>
        )
    }else{
        return(
        <div>Loading</div>
        )
    }
}

export default Dash