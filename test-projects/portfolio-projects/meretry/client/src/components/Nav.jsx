import React from 'react'
import {Link, useNavigate} from 'react-router-dom'
import { Nav, Navbar, NavDropdown, Card } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import '../styles/App.css'

const Bar = ({authenticated, user, handleLogout}) => {
    const nav = useNavigate()
    let authOptions
    if(user){
        authOptions = (
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" style={{justifyContent: 'space-evenly'}}>
                <Navbar.Brand onClick={() => nav('/home')}>Meredith Hanna</Navbar.Brand>
                <Card.Text style={{marginTop: '.5em'}}>Welcome {user.username}</Card.Text>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav" style={{justifyContent: 'space-between'}}>
                    <Nav className="mr-auto">
                        <Nav.Link href='/home'>Home</Nav.Link>
                        {/* <Nav.Link href="/collab">Collaborations</Nav.Link> */}
                        {/* <Nav.Link href={`/profile/${user.id}`}>Profile</Nav.Link> */}
                        {/* <Nav.Link href="/merch">Merch</Nav.Link> */}
                        {/* <NavDropdown title="Portfolio" id="collasible-nav-dropdown" >
                            <NavDropdown.Item id='d-item' href="/portfolio">~ Main Portfolio Page ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/glam">~ Boudoir ~ Glamour ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/swim">~ Swimwear ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/brand">~ Brands ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/public">~ Publications ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/port">~ Portrait ~ LifeStyle ~</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item id='d-item' href="/portfolio/misc">~ Other ~</NavDropdown.Item>
                        </NavDropdown> */}
                    </Nav>
                </Navbar.Collapse>
            </Navbar>  
        )
    }
    const publicOptions = (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" style={{justifyContent: 'space-evenly'}}>
            <Navbar.Brand onClick={() => nav('/home')}>Meredith Hanna</Navbar.Brand>
                <Card.Text style={{marginTop: '.5em'}}></Card.Text>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav" style={{justifyContent: 'space-between'}}>
                    <Nav className="mr-auto">
                        <Nav.Link href='/home'>Home</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
        </Navbar>
    )
    return(
        <header className='master-header'>
            <div className="Mere-header" onClick={() => {
          (authenticated && user ? nav('/home') : nav('/login'))}}>
        </div>
            {authenticated && user ? authOptions : publicOptions}
        </header>
    )
}

export default Bar