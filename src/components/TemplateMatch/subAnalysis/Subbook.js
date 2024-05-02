import React, { Component } from 'react';
import '../../../App.css';
import { Rnd } from 'react-rnd';
import axios from 'axios';

import {VictoryBar,VictoryLine, VictoryChart,VictoryAxis,VictoryContainer,VictoryLabel} from 'victory';



export default class Subbook extends Component {
    constructor(props) {
        super(props);
       
      }
      state ={
        template:[],
        graph1:[],
        graph2:[],
        graph3:[],
        graph4:[],
        graph5:[],
        template1:[],
        graph11:[],
        graph21:[],
        graph31:[],
        graph41:[],
        graph51:[],
        results:[],
        x: 100,
        y: 180,
        width: 150,
        height: 100,
      }
      componentDidMount(){
          
    
        }



    render() {
        const style = {
            display:  "inline-block",
            alignItems: "center",
            justifyContent: "center",
            border: "solid 1px #ddd",
            background: "#f0f0f0"
          };
          const rendercancel = ()=> {
          
       
            return ".box";
        
      
      }
      const results=this.state.results;
        return (
         
              
             
             <Rnd
              style={style}
             size={{ width: this.state.width,  height: this.state.height }}
             position={{ x: this.state.x, y: this.state.y }}
             onDragStop={(e, d) => { this.setState({ x: d.x, y: d.y }) }}
             onResize={(e, direction, ref, delta, position) => {
               this.setState({
                 width: ref.offsetWidth,
                 height: ref.offsetHeight,
                 ...position,
               });
             }}
             minWidth={140}
             minHeight={100}
             bounds="window"
             cancel ={ rendercancel()}
           >  
             <div  style={{backgroundColor: "lightblue",fontSize:"10px",width: '100%',height:'10%',}}>  {"Demographics analysis"}</div>
           <div  className='box'style={{ overflow:'auto', width: '100%',height:'90%',display:  "inline-block" } }>
           
           <div  style={{overflow:'auto',display:'inline-block', 
width:'100%', position:'relative',top:'10px',fontSize:'10px',
 textAlign:'center'}}>
      
            <div >{"template"}</div>  
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
             
                <div>{'Source->0 Target->-99 Time->-99 Weight->-99'}</div>
         
                </div> 
            <div>{"graph1 : "}</div> 
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
             
                <div>{'Source->616050 Target->590502 Time->01/09/2004 Weight->0.166667'}</div>
         
                </div> 

            <div>{"graph2 : "}</div> 
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
                
                <div>{'Source->563211 Target->564798 Time->10/13/2001 Weight->0.018868'}</div>
                <div>{'Source->563211 Target->627390 Time->04/07/2009 Weight->0.200000'}</div>
                <div>{'Source->563211 Target->561114 Time->03/14/2016 Weight->0.250000'}</div>
                <div>{'Source->541017 Target->601492 Time->12/17/2022 Weight->0.142857'}</div>
                
                
                </div> 




            <div>{"graph3 : "}</div>  
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
                <div>{'Source->614761 Target->514306 Time->05/10/2018 Weight->0.1'}</div>
         
                </div> 
            <div>{"graph4 : "}</div> 
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
                <div>{'NAN'}</div>
         
                </div>  
            <div>{"graph5 : "}</div>  
            <div style={{ 
width:'100%', position:'relative',left:'0%',fontSize:'8px',
            textAlign:'center'}}>
            
                <div>{'NAN'}</div>
         
                </div> 
          

            </div>
                  

        
           
            
                
               </div>  
               </Rnd>  
         
        )
    }
}
