import React from 'react';
import ReactDOM from 'react-dom';
import "./Navbar.css";
import logo from './logo192.png'
function Navbar(){
    return (
        <>
        <nav id='header-nav' className="navbar navbar-light navbar-expand-lg">
		<div className='container-fluid'>
			<img src={logo} className="navbar-logo"></img>
			<a href='' className='navbar-brand p-2'>Mishal Faisal</a>
			<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    			<span className="navbar-toggler-icon"></span>
  			</button>

			<div className='collapse navbar-collapse'  id = 'navbarSupportedContent'>
				<div className="navbar-nav" id="navlist">
					<a href="#about" className="nav-link">About</a>
					<a href="#portfolio" className="nav-link">Portfolio</a>
					<a href="#skills" className="nav-link">Skills</a>
					<a href="#contact" className="nav-link">Contact</a>
				</div>
			</div>
		</div>
	    </nav>
        </>
    )
}

export default Navbar;