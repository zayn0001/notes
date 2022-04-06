import React from 'react';
import ReactDOM from 'react-dom';
import './Footer.css'
import wa from './whatsapp.jpg'
import fb from './facebook4.jpg'
import ig from './instagram1.jpg'



function Footer() {
    return (
        <div id="footer">
        <a href="" target="_blank"><span className="logo"><img src={fb}></img></span></a>
		<a href="" target="_blank"><span className="logo"><img src={ig}></img></span></a>
		<a href="" target="_blank"><span className="logo"><img src={wa}></img></span></a>
		<div style={{marginTop: "5px", fontSize: "14px"}}>&copy; 2022 by Mishal Faisal.</div>
	    </div>
    )
}

export default Footer;