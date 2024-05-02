import React, { Component } from 'react';
import '../../../App.css';
import { Rnd } from 'react-rnd';
import axios from 'axios';

import {VictoryBar,VictoryLine, VictoryChart,VictoryAxis,VictoryContainer,VictoryLabel} from 'victory';



export default class Subdemo extends Component {
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
          
        axios.get('http://127.0.0.1:5000/demoanalysis').then (res=>{
           // console.log(res);
            var x=res.data.split("&&");
          // console.log(JSON.parse(x[0]) )
            this.setState({template:JSON.parse(x[0]),graph1:JSON.parse(x[1]),graph2:JSON.parse(x[2]),graph3:JSON.parse(x[3]),graph4:JSON.parse(x[4]),graph5:JSON.parse(x[5])});
            this.setState({template1:JSON.parse(x[6]),graph11:JSON.parse(x[7]),graph21:JSON.parse(x[8]),graph31:JSON.parse(x[9]),graph41:JSON.parse(x[10]),graph51:JSON.parse(x[11])});
            this.setState({results: JSON.parse(x[12])});       
          })
        }



    render() {
      const arr=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
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
            <div style={{overflow:'auto',}}>
              
             
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
             <div  style={{backgroundColor: "lightblue",fontSize:"10px"}}>  {"Demographics analysis"}</div>
           <div  style={{  width: '100%',height:'45%',display:  "flex" } }>
             <svg
        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20)/2 }
        viewBox="0 0 1000 400"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
        <VictoryChart width={1000}
        height={300}standalone={false} domainPadding={100} padding={{ left: 100,right:20, bottom: 60 }}
 >
    <VictoryLine data={this.state.template}  x="index" y="value" style={{
      data: { stroke: "black" }   
     
    }}/>
                
                 <VictoryLine data={this.state.graph1} x="index" y="value"  style={{
      data: { stroke: "red" }
     
    }}/>
                 <VictoryLine data={this.state.graph2} x="index" y="value"  style={{
      data: { stroke: "blue" }
     
    }}/>
                
                <VictoryLine data={this.state.graph3} x="index" y="value"  style={{
      data: { stroke: "green" }
     
    }}/>
                <VictoryLine data={this.state.graph4} x="index" y="value" style={{
      data: { stroke: "brown" }
     
    }} />
                
                <VictoryLine data={this.state.graph5} x="index" y="value" style={{
      data: { stroke: "gold" }
     
    }}/>
  <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: "14px"} ,axisLabel: {fontSize:  20, padding: 60}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="procurement average weight "/>
                   <VictoryAxis  tickValues={arr}  offsetY={50}  style={{ tickLabels: { fontSize: '12px' , padding:  0} ,axisLabel: {fontSize: 30, padding: 20}}} tickLabelComponent={<VictoryLabel  angle={90} verticalAnchor="middle" textAnchor="start"/>} />
               
</VictoryChart>
        </g>
               </svg>
               <div className="box" style={{ padding: '5px',display:"inline-block",width: '40%',height:'90%',border: '1px solid white',overflow:'auto', fontSize:      '8px',textAlign: 'justify'}}>
                   <div>{"wasserstein distance"}</div>  
      <div><span style={{color:"black"}}>{"template"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  0.00"}</div>
                   <div><span style={{color:"red"}}>{"graph1"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[0]}</div>
                   <div><span style={{color:"blue"}}>{"graph2"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[1]}</div>
                   <div><span style={{color:"green"}}>{"graph3"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[2]}</div>
                   <div><span style={{color:"brown"}}>{"graph4"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[3]}</div>
                   <div><span style={{color:"gold"}}>{"graph5"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[4]}</div>
                  
                
                  </div>
               </div>
               <div  style={{  width: '100%',height:'45%',display:  "flex" } }>
             <svg
        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20)/2 }
        viewBox="0 0 1000 400"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
        <VictoryChart width={1000}
        height={300}standalone={false} domainPadding={100} padding={{ left: 100,right:20, bottom: 60 }}
 >
    <VictoryLine data={this.state.template1}  x="index" y="value" style={{
      data: { stroke: "black" }   
     
    }}/>
                
                 <VictoryLine data={this.state.graph11} x="index" y="value"  style={{
      data: { stroke: "red" }
     
    }}/>
                 <VictoryLine data={this.state.graph21} x="index" y="value"  style={{
      data: { stroke: "blue" }
     
    }}/>
                
                <VictoryLine data={this.state.graph31} x="index" y="value"  style={{
      data: { stroke: "green" }
     
    }}/>
                <VictoryLine data={this.state.graph41} x="index" y="value" style={{
      data: { stroke: "brown" }
     
    }} />
                
                <VictoryLine data={this.state.graph51} x="index" y="value" style={{
      data: { stroke: "gold" }
     
    }}/>
   <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: "14px"} ,axisLabel: {fontSize:  20, padding: 60}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="procurement freq "/>
                 <VictoryAxis  tickValues={arr}  offsetY={50}  style={{ tickLabels: { fontSize: '12px' , padding:  0} ,axisLabel: {fontSize: 30, padding: 20}}} tickLabelComponent={<VictoryLabel  angle={90} verticalAnchor="middle" textAnchor="start"/>} />
               
</VictoryChart>
        </g>
               </svg>
               <div className="box" style={{ padding: '5px',display:"inline-block",width: '40%',height:'90%',border: '1px solid white',overflow:'auto', fontSize:      '8px',textAlign: 'justify'}}>
                   <div>{"wasserstein distance"}</div>  
      <div><span style={{color:"black"}}>{"template"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  0.00"}</div>
                   <div><span style={{color:"red"}}>{"graph1"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[5]}</div>
                   <div><span style={{color:"blue"}}>{"graph2"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[6]}</div>
                   <div><span style={{color:"green"}}>{"graph3"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[7]}</div>
                   <div><span style={{color:"brown"}}>{"graph4"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[8]}</div>
                   <div><span style={{color:"gold"}}>{"graph5"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[9]}</div>
                  
                
                  </div>
               </div>
               </Rnd>  
            </div>
        )
    }
}
