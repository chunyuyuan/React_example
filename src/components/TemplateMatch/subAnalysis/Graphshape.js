import React, { Component } from 'react';
import { Rnd } from 'react-rnd';
import axios from 'axios';
import Select from 'react-select';
import Switch from "react-switch";
import Checkbox from '../CheckBox';
import {VictoryZoomContainer,VictoryVoronoiContainer,VictoryTooltip,VictoryScatter,VictoryLine,VictoryTheme, VictoryChart,VictoryAxis,VictoryContainer,VictoryBar,VictoryLabel} from 'victory';
import '../../../App.css';
import returncon from '../img/img_reset.png';
import arrowicon from '../img/images.png';
import legendicon from '../img/legend.PNG';
import Graphattr from './Graphattr'
export default class Graphshape extends Component {
    constructor(props) {
        super(props);
      
       this. state ={
        x: 713 ,y:334,width:412,height:180,
          g1:false,
          demog:false,
          travel:false,
          item: false,
          book:false,
          valuemin:0,
          valuemax:365,
        
          zoomDomain: { y: [0, 1] }     
            
    
      }
      
    }
    handleZoom(domain) {
        this.setState({ zoomDomain: domain });
      }
      activateLasers=()=>{
        this.setState({ x: 713 ,y:334,width:412,height:180});
      }
    render() {

        const arr=["Degree Centrality","Closeness Centrality","Betweenness Centrality","Katz Centrality","Harmonic Centrality","Pagerank","Number of Nodes","Number of Edges","Degree","Average Neighbor Degree"];
        let  part3;
        
        part3=<Graphattr  timemin={this.props.timemin} timemax={this.props.timemax}/>

        const rendercancel = ()=> {
          
       
            return ".box2";
        
      
      }
        const style = {
            display:  "inline-block",
            alignItems: "center",
            justifyContent: "center",
            border: "solid 1px #ddd",
            background: 'rgba(255,255,255,1)',
            
          };
          console.log(this.props.data)
        return (
          <div>
            <Rnd
    style={style}
   size={{ width: this.state.width,  height: this.state.height  }}
   position={{  x: this.state.x, y: this.state.y}}
   onDragStop={(e, d) => { this.setState({ x: d.x, y: d.y },()=>{console.log(this.state.x,this.state.y)}) }}
   onResize={(e, direction, ref, delta, position) => {
     this.setState({
       width: ref.offsetWidth,
       height: ref.offsetHeight,
       ...position,
     },()=>{console.log(this.state.width,this.state.height)});
   }}
   minWidth={'2%'}
   minHeight={'5%'}
   bounds="window"
   cancel ={ rendercancel()}
 >
       <div  style={{backgroundColor: "lightblue",fontSize:"10px" }}>  {"Graph Shape Difference Normalization Analysis"} <button style={{position: 'absolute',
  right: 0,top:0,height:'15px',width:'30px',backgroundColor: "white",}} onClick={this.activateLasers}>
 <img src={returncon} style={{position: 'absolute',top:1,right:0,left:8,bottom:0,height:'8px',width:'8px'}}/>
</button></div>
         
     <div   className='box2' style={{display:'block'}}>
  <svg

        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20) }
        viewBox="0 0 800 500"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
        <VictoryChart 
          

        width={700}
        height={500}standalone={false} domainPadding={10} padding={{ left: 105,right:0, bottom: 130,top:60 }}
       
 >
    <VictoryLine data={this.props.data}  y="Graph1" x="index" style={{
      data: { stroke: "red" }   
      
     
    }}/>
   <VictoryScatter data={this.props.data}
    y="Graph1" x="index"
         
            style={{
                data: {fill: "red"}, labels: {fill: "black",fontSize:'20px'}
              }}
              size={5 }
       
              
          /> 
     <VictoryLine data={this.props.data}  y="Graph2" x="index" style={{
      data: { stroke: "lightblue" }   
      
     
    }}/>
    <VictoryScatter data={this.props.data}
    y="Graph2" x="index"
         
            style={{
                data: {fill: "lightblue"}, labels: {fill: "black",fontSize:'20px'}
              }}
              size={5 }
        
              
          /> 
     <VictoryLine data={this.props.data}  y="Graph3" x="index" style={{
      data: { stroke: "green" }   
      
     
    }}/>
     <VictoryScatter data={this.props.data}
    y="Graph3" x="index"
         
            style={{
                data: {fill: "green"}, labels: {fill: "black",fontSize:'20px'}
              }}
              size={5 }
          
              
          /> 
     <VictoryLine data={this.props.data}  y="Graph4" x="index" style={{
      data: { stroke: "brown" }   
      
     
    }}/>
   <VictoryScatter data={this.props.data}
    y="Graph4" x="index"
         
            style={{
                data: {fill: "brown"}, labels: {fill: "black",fontSize:'20px'}
              }}
              size={5 }
            

              
          /> 
         <VictoryLine data={this.props.data}  y="Graph5" x="index" style={{
      data: { stroke: "gold" }   
      
     
    }}/> 
     <VictoryScatter data={this.props.data}
    y="Graph5" x="index"
         
            style={{
                data: {fill: "gold"}, labels: {fill: "black",fontSize:'20px'}
              }}
              size={5 }
             

              
          />       
   <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: "18px"} ,axisLabel: {fontSize:  20, padding: 60}}} domain={{y:[0,]}}    label="difference normalization "/>
                   <VictoryAxis  tickValues={arr}    style={{ tickLabels: { fontSize: '12px' , padding:  0} ,axisLabel: {fontSize: 30, padding: 20}}} tickLabelComponent={<VictoryLabel  angle={90} verticalAnchor="middle" textAnchor="start"/>} />
       
             
</VictoryChart>

        </g>
      
               </svg>

               <img src={arrowicon} style={{position:'absolute', bottom:'30%',right:10,width:'8%', height:'50%'}}/>
               <img src={legendicon} style={{position:'absolute', top:14.5,right:'40%',width:'50%', height:'7%'}}/>
             
               </div>


 </Rnd>
 {part3}
 </div>
        )
    }
}
