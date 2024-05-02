import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import logo from '../graph_icon.svg';
import logo_temp from '../template_icon.svg';
import logo_seed from '../seed_icon.svg';
import logo_blind from '../blind_icon.svg';
import 'bootstrap/dist/css/bootstrap.min.css'
import '../App.css';
import styled from "styled-components";
import {ButtonContainer} from "./Button";

export default class Navbar extends Component {

render(){
    return (

<NavWrapper className="navbar navbar-expand-sm  navbar-dark px-sm-5">
   
<img src={logo} alt="store" className="graph_icon"/>
<div className="text-title">Mini Challenge 1</div> <Link to="/"></Link>

<Link to="/" className="ml-auto">
<ButtonContainer className="button1 " >
<span className="mr-2">
   <img src={logo_temp} alt="store" className="temp_icon"/>
   </span>
template match
</ButtonContainer >
    </Link>
    <Link to="/seedMatch" className="ml-auto">
<ButtonContainer className="button2 " >
<span className="mr-2">
   <img src={logo_seed} alt="store" className="seed_icon "/>
   </span>
seed match
</ButtonContainer >
    </Link>
    <Link to="/blindMatch" className="ml-auto">
<ButtonContainer className="button3 " >
<span className="mr-2">
   <img src={ logo_blind} alt="store" className="temp_icon"/>
   </span>
blind match
</ButtonContainer >
    </Link>



    </NavWrapper>

    );
}




}

const NavWrapper=styled.nav`

background: var(--mainGreen);

`