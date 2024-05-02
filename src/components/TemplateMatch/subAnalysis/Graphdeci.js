import React, { Component } from 'react';
import { Rnd } from 'react-rnd';
import axios from 'axios';
import Select from 'react-select';
import Switch from "react-switch";
import Checkbox from '../CheckBox';
import {VictoryPie,VictoryZoomContainer,VictoryVoronoiContainer,VictoryTooltip,VictoryScatter,VictoryLine,VictoryTheme, VictoryChart,VictoryAxis,VictoryContainer,VictoryBar,VictoryLabel} from 'victory';
import '../../../App.css';
import returncon from '../img/img_reset.png';
import arrowicon from '../img/images.png';
import legendicon from '../img/legend.PNG';
export default class Graphdeci extends Component {
    constructor(props) {
        super(props);
      
       this. state ={
        x: 713 ,y:6,width:412,height:140,
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
        this.setState({x: 713 ,y:6,width:412,height:140});
      }
    render() {
     console.log(this.props.rate)
     
        const arr=["Degree Centrality","Closeness Centrality","Betweenness Centrality","Katz Centrality","Harmonic Centrality","Pagerank","Number of Nodes","Number of Edges","Degree","Average Neighbor Degree"];
  

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
        
        return (
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
       <div  style={{backgroundColor: "lightblue",fontSize:"10px" }}>  {"Graph match result Analysis"} <button style={{position: 'absolute',
  right: 0,top:0,height:'15px',width:'30px',backgroundColor: "white",}} onClick={this.activateLasers}>
 <img src={returncon} style={{position: 'absolute',top:1,right:0,left:8,bottom:0,height:'8px',width:'8px'}}/>
</button></div>
         
     <div   className='box2' style={{display:'block'}}>
  <svg

        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20) }
        viewBox="0 0 500 500"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
      
<VictoryPie
          standalone={false}
          width={400} height={400}
          data={this.props.rate}
          x="index"
          y="value"
          innerRadius={68} labelRadius={80}
          labels={({ datum }) => datum.index+": "+datum.value}
          style={{ labels: { fontSize: 15, fill: "white" } }}
          colorScale={["red", "blue", "green", "brown", "gold" ]}
          labelComponent={<VictoryLabel angle={45}/>}
        />
        </g>
      
               </svg>

              
               </div>


 </Rnd>
        )
    }
}
