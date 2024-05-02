
import { slide as Menu } from "react-burger-menu";
import React, { Component } from 'react';
import phone from './img/phone.svg';
import email from './img/email.svg';
import deal from './img/deal.svg';
import writing from './img/writing.svg';
import information from './img/information.svg';
import travel from './img/travel.svg';
import csvicon from './img/csv_icon.svg';
import 'bootstrap/dist/css/bootstrap.min.css'
import '../../App.css';
import styled from "styled-components";
import Checkbox from './CheckBox';

const checkboxes2 = [
    {
      name: ' Phone ',
      key: 'checkphone',
      label: 'Check Box phone',
      data: phone,
    },
    {
      name: ' Email ',
      key: 'checkemail',
      label: 'Check Box email',
      data: email,
    },
    {
      name: ' Procurement ',
      key: 'checkdeal',
      label: 'Check Box deal',
      data: deal,
    },
    {
      name: ' Co-authorship ',
      key: 'checkwriting',
      label: 'Check Box writing',
      data: writing,
    },
    {
      name: ' Demographics ',
      key: 'checkinformation',
      label: 'Check Box information',
      data: information,
    },
    {
      name: ' Travel ',
      key: 'checktravel',
      label: 'Check Box travel',
      data: travel,
    },
  ];
 /* const checkboxes1 = [
    {
      name: ' CGCS-Template.csv ',
      key: 'checktemp',
      label: 'Check Box temp',
      data: csvicon,
    },
    {
      name: ' Q1-Graph1.csv ',
      key: 'checkeq1',
      label: 'Check Box q1',
      data: csvicon,
    },
    {
        name: ' Q1-Graph2.csv ',
        key: 'checkeq2',
        label: 'Check Box q2',
        data: csvicon,
      },
      {
        name: ' Q1-Graph3.csv ',
        key: 'checkeq3',
        label: 'Check Box q3',
        data: csvicon,
      },
      {
        name: ' Q1-Graph4.csv ',
        key: 'checkeq4',
        label: 'Check Box q4',
        data: csvicon,
      },
      {
        name: ' Q1-Graph5.csv ',
        key: 'checkeq5',
        label: 'Check Box q5',
        data: csvicon,
      },
  ];*/
  const checkboxes1 = [
    {
      name: ' Graphs ',
      key: 'checktemp',
      label: 'Check Box temp',
      data: csvicon,
    }
  ];

  export default class Sidebar extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          checkedItems1: new Map(),
          checkedItems2: new Map(),
          
        }
       
    
        this.handleChange1 = this.handleChange1.bind(this);
        this.handleChange2 = this.handleChange2.bind(this);
      }
      childFunction=(e)=>{
        e.preventDefault();
        this.props.functionCallFromParent("Hello From Child1");
    }
    
      handleChange1(e) {
        const item = e.target.name;
        const isChecked = e.target.checked;
        this.setState(() => ({ checkedItems1: this.state.checkedItems1.set(item, isChecked) }),()=>{this.props.functionCallFromParent(this.state);});
      
        
     
        
        
    }
      handleChange2(e) {
        const item = e.target.name;
        const isChecked = e.target.checked;
        
        this.setState(() => ({ checkedItems2: this.state.checkedItems2.set(item, isChecked) }),()=>{this.props.functionCallFromParent(this.state);});
        
    
    }




render() {
  return (
    // Pass on our props
    <Menu {...this.props}>
        <NavWrapper1 className="navbar ">
       <div className="text-title1">
 Graph Analysis</div>
 <div> 

<ul className="menu_custompozition4">
          <div>
            {
               
              checkboxes1.map(item => (
                <li  key={item.key}>
                <div   className="mr-2">
                <Checkbox  name={item.name} checked={this.state.checkedItems1.get(item.name)} onChange={this.handleChange1.bind(this)} />
               
    
                    <img  style={{ marginLeft: 12 }} src={item.data} alt="store" className="temp_icon"/>
                 {item.name}
                   </div >
                </li>
              ))
            }
          </div>
          </ul> 
          </div>
    </NavWrapper1>
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   <NavWrapper2 className="navbar ">
       <div className="text-title1">
 channel type</div>
 <div> 

<ul className="menu_custompozition5">
          <div>
            {
               
              checkboxes2.map(item => (
                <li key={item.key}>
                <div  className="mr-2">
                <Checkbox  name={item.name} checked={this.state.checkedItems2.get(item.name)} onChange={this.handleChange2} />
               
    
                    <img  style={{ marginLeft: 12 }} src={item.data} alt="store" className="temp_icon"/>
                  {item.name}
                   </div >
                </li>
              ))
            }
          </div>
          </ul> 
          </div>
    </NavWrapper2>
    
    
   
    </Menu>
  );
};
  };
const NavWrapper1=styled.nav`

background: white;


margin: 0.2em;
width: 90%;
height: 25%;
position: absolute;
left:0;
top:6%;
border: 4px solid black;
border-radius: 3px;

`
const NavWrapper2=styled.nav`

background: white;


margin: 0.2em;
width: 90%;
height: 50%;
position: absolute;
left:0;
top:35%;
border: 4px solid black;
border-radius: 3px;

`
