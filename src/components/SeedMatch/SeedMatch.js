import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import '../../App.css';
import { Rnd } from 'react-rnd';
import axios from 'axios';

import {VictoryLabel,VictoryPie,VictoryLine, VictoryChart,VictoryGroup ,VictoryAxis,VictoryContainer} from 'victory';
import Chart from "react-apexcharts";

import  Barchart from './Barchart';



export default class SeedMatch extends Component {
  state ={
    width: 200,
    height: 100,
    x: 70,
    y: 180,
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
const links = [{
  target: "pusat",
  source: "dki",
  strength: 0.2,
  value: 1
}, {
  target: "pusat",
  source: "jabar",
  strength: 0.2,
  value: 3
}, {
  target: "pusat",
  source: "jatim",
  strength: 0.2,
  value: 6
}, {
  target: "pusat",
  source: "diy",
  strength: 0.2,
  value: 1
}, {
  target: "pusat",
  source: "bali",
  strength: 0.2,
  value: 1
}, {
  target: "pusat",
  source: "ntt",
  strength: 0.2,
  value: 1
},

//{ target: "pusat", source: "malang" , strength: 0.2, value:3 },
//{ target: "pusat", source: "lamongan" , strength: 0.2, value:6 },
{
  target: "jabar",
  source: "ntt",
  strength: 0.7,
  value: 2
},{
  target: "jabar",
  source: "diy",
  strength: 0.7,
  value: 2
},
{
  target: "dki",
  source: "jaksel",
  strength: 0.7,
  value: 2
}, {
  target: "dki",
  source: "jakpus",
  strength: 0.7,
  value: 3
}, {
  target: "jabar",
  source: "sumedang",
  strength: 0.7,
  value: 0.5
}, {
  target: "jabar",
  source: "bekasi",
  strength: 0.7,
  value: 2
}, {
  target: "jabar",
  source: "bandung",
  strength: 0.7,
  value: 2
}, {
  target: "jatim",
  source: "malang",
  strength: 0.7,
  value: 3
}, {
  target: "jatim",
  source: "lamongan",
  strength: 0.7,
  value: 1
},{
  target: "jatim",
  source: "jaksel",
  strength: 0.7,
  value: 1
}, {
  target: "diy",
  source: "sleman",
  strength: 0.7,
  value: 3
}, {
  target: "diy",
  source: "jogja",
  strength: 0.7,
  value: 1
}, {
  target: "bali",
  source: "bali1",
  strength: 0.7,
  value: 1
}, {
  target: "bali",
  source: "bali2",
  strength: 0.7,
  value: 1
}, {
  target: "ntt",
  source: "ntt1",
  strength: 0.7,
  value: 1
}, {
  target: "ntt",
  source: "ntt2",
  strength: 0.7,
  value: 1
}, {
  target: "jabar",
  source: "bali",
  strength: 0.7,
  value: 1
}
];
const nodes= [{
id: "pusat",
group: 0,
label: "pusat",
level: 0
}, {
id: "dki",
group: 1,
label: "dki",
level: 1
}, {
id: "jaksel",
group: 1,
label: "jaksel",
level: 3
}, {
id: "jakpus",
group: 1,
label: "jakpus",
level: 3
}, {
id: "jabar",
group: 2,
label: "jabar",
level: 1
}, {
id: "sumedang",
group: 2,
label: "sumedang",
level: 3
}, {
id: "bekasi",
group: 2,
label: "bekasi",
level: 3
}, {
id: "bandung",
group: 2,
label: "bandung",
level: 3
}, {
id: "jatim",
group: 3,
label: "jatim",
level: 1
}, {
id: "malang",
group: 3,
label: "malang",
level: 3
}, {
id: "lamongan",
group: 3,
label: "lamongan",
level: 3
}, {
id: "diy",
group: 4,
label: "diy",
level: 1
}, {
id: "sleman",
group: 4,
label: "sleman",
level: 3
}, {
id: "jogja",
group: 4,
label: "jogja",
level: 3
}, {
id: "bali",
group: 5,
label: "bali",
level: 1
}, {
id: "bali1",
group: 5,
label: "bali1",
level: 3
}, {
id: "bali2",
group: 5,
label: "bali2",
level: 3
}, {
id: "ntt",
group: 6,
label: "ntt",
level: 1
}, {
id: "ntt1",
group: 6,
label: "ntt1",
level: 3
}, {
id: "ntt2",
group: 6,
label: "ntt2",
level: 3
}] ;
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
        
       <div  style={{ width: '100%',height:'6%',backgroundColor: "lightblue",fontSize:"5px"}}>  {"Email analysis"}</div>
       
         <div style={{  width: '100%',height:'94%',display:  "inline-block" } }> 
        <div
            className="box"
            style={{  width: '100%',height:'50%' ,border: '1px solid white', display:  "flex" }}
          >
            
            <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello1
           
          </div>
          <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello2
           
          </div>
          <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello3
           
          </div>
         
            
          </div>
          <div
            className="box"
            style={{  width: '100%',height:'50%', border: '1px solid white',display:  "flex" }}
          >
          <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello4
            
          </div>
          <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello5
            
          </div>
          <div
            className="box"
            style={{  width: '33%',height:'100%' ,border: '1px solid white' }}
          >
         
            hello6
           
          </div>
            
          </div>
          </div>
     
      </Rnd>
    )
  }
}

