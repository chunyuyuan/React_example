import React, { Component } from 'react';
import '../../../App.css';
import { Rnd } from 'react-rnd';
import axios from 'axios';

import {VictoryLine, VictoryChart,VictoryAxis,VictoryContainer} from 'victory';



export default class Subemail extends Component {
    constructor(props) {
        super(props);
        this.selector = React.createRef();
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
            template2:[],
            graph12:[],
            graph22:[],
            graph32:[],
            graph42:[],
            graph52:[],
            results:[],
            x: 70,
            y: 180,
            width: 150,
            height: 100,
            valuemin:0,
            valuemax:365,
            
            };

            async componentDidUpdate(prevProps, prevState) {
                if (prevProps.valuemin !== this.props.valuemin||prevProps.valuemax !== this.props.valuemax) {
                  this.setState({valuemin:this.props.valuemin,valuemax:this.props.valuemax},()=>{
                    axios.get('http://127.0.0.1:5000/emailanalysis1?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax).then (res=>{
                      // console.log(res);
                       var x=res.data.split("&&");
                     // console.log(JSON.parse(x[0]) )
                       this.setState({template:JSON.parse(x[0]),graph1:JSON.parse(x[1]),graph2:JSON.parse(x[2]),graph3:JSON.parse(x[3]),graph4:JSON.parse(x[4]),graph5:JSON.parse(x[5])});
                       this.setState({template1:JSON.parse(x[6]),graph11:JSON.parse(x[7]),graph21:JSON.parse(x[8]),graph31:JSON.parse(x[9]),graph41:JSON.parse(x[10]),graph51:JSON.parse(x[11])});
                       this.setState({results:JSON.parse(x[12])})
                     })
                //    console.log("hello  state phone"+this.state.valuemin,this.state.valuemax)
              })
               //  console.log("graph test ",this.state.template.slice(0, 2))
                }
                } 

           async componentDidMount(){
              
            axios.get('http://127.0.0.1:5000/emailanalysis?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax).then (res=>{
               // console.log(res);
                var x=res.data.split("&&");
              // console.log(JSON.parse(x[0]) )
                this.setState({template:JSON.parse(x[0]),graph1:JSON.parse(x[1]),graph2:JSON.parse(x[2]),graph3:JSON.parse(x[3]),graph4:JSON.parse(x[4]),graph5:JSON.parse(x[5])});
                this.setState({template1:JSON.parse(x[6]),graph11:JSON.parse(x[7]),graph21:JSON.parse(x[8]),graph31:JSON.parse(x[9]),graph41:JSON.parse(x[10]),graph51:JSON.parse(x[11])});
                this.setState({template2:JSON.parse(x[12]),graph12:JSON.parse(x[13]),graph22:JSON.parse(x[14]),graph32:JSON.parse(x[15]),graph42:JSON.parse(x[16]),graph52:JSON.parse(x[17])});
                this.setState({results:JSON.parse(x[18])})
              })
            }
        render() {
            const minv=this.props.valuemin;
            const maxv=this.props.valuemax;
         //console.log("hello"+this.state.width,this.state.height)
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
              
               
               
           
              <div  style={{backgroundColor: "lightblue",fontSize:"10px"}}>  {"Email analysis"}</div>
            { /*    <VictoryChart 
    height={this.state.height} width={this.state.width} 
                 > preserveAspectRatio="xMidYMid meet"*/}
                 <div   style={{  width: '100%',height:'33%',display:  "flex" } }>  
                 <svg
            x={0 }
            y={0 }
            width={this.state.width }
            height={(this.state.height-20) /3}
            viewBox="0 0 1000 400"
            preserveAspectRatio="none"
            fillOpacity="0.8">
             
            <g>
            
                  <VictoryChart width={1000}
            height={300}standalone={false} padding={{ left: 50,right:20, bottom: 60,top:20 }}
     >
                     
                    
      
          
          
                     <VictoryLine data={this.state.template} x="index" y="value" style={{
          data: { stroke: "black" }
         
        }} />
                    
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
                     <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: 20 } ,axisLabel: {fontSize:  25, padding: 30}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="email send freq"/>
                 <VictoryAxis  offsetY={50} style={{ tickLabels: { fontSize: 30 } ,axisLabel: {fontSize: 30, padding: 30}}}domain={{x:[1,]}}  label="email send freq distribution"/>
               
                  
                    
                   </VictoryChart>
                
                   </g>
                  
                   </svg>
                   <div className="box" style={{ padding: '5px',display:"inline-block",width: '40%',height:'90%',border: '1px solid white',overflow:'auto', fontSize:      '6px',textAlign: 'justify'}}>
                   <div>{"wasserstein distance"}</div>  
      <div><span style={{color:"black"}}>{"template"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  0.00"}</div>
                   <div><span style={{color:"red"}}>{"graph1"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[0]}</div>
                   <div><span style={{color:"blue"}}>{"graph2"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[1]}</div>
                   <div><span style={{color:"green"}}>{"graph3"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[2]}</div>
                   <div><span style={{color:"brown"}}>{"graph4"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[3]}</div>
                   <div><span style={{color:"gold"}}>{"graph5"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[4]}</div>
                  
                
                  </div>
                   </div>
                   <div   style={{  width: '100%',height:'33%',display:  "flex" } }>  
                 <svg
            x={0 }
            y={0 }
            width={this.state.width }
            height={(this.state.height-20)/3 }
            viewBox="0 0 1000 400"
            preserveAspectRatio="none"
            fillOpacity="0.8">
             
            <g>
            
                  <VictoryChart width={1000}
            height={300}standalone={false} padding={{ left: 50,right:20, bottom: 60,top:20 }}
     >
                     
                    
      
          
          
                     <VictoryLine data={this.state.template1} x="index" y="value" style={{
          data: { stroke: "black" }
         
        }} />
                    
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
                   
                   
                     <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: 20 } ,axisLabel: {fontSize:  25, padding: 30}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="email receive freq"/>
                 <VictoryAxis  offsetY={50} style={{ tickLabels: { fontSize: 30 } ,axisLabel: {fontSize: 30, padding: 30}}}domain={{x:[1,]}}  label="email receive freq distribution"/>
               
                    
                   </VictoryChart>
                   </g>
                   </svg>
                   <div className="box" style={{ padding: '5px',display:"inline-block",width: '40%',height:'90%',border: '1px solid white',overflow:'auto', fontSize:      '1vw',fontSize:      '1vh',textAlign: 'justify'}}>
                   <div>{"wasserstein distance"}</div>  
                   <div><span style={{color:"black"}}>{"template"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  0.00"}</div>
                   <div><span style={{color:"red"}}>{"graph1"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[5]}</div>
                   <div><span style={{color:"blue"}}>{"graph2"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[6]}</div>
                   <div><span style={{color:"green"}}>{"graph3"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[7]}</div>
                   <div><span style={{color:"brown"}}>{"graph4"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[8]}</div>
                   <div><span style={{color:"gold"}}>{"graph5"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[9]}</div>
                  
                
                  </div>
                   </div>
                   <div   style={{  width: '100%',height:'33%',display:  "flex" } }>  
             <svg
        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20)/3}
        viewBox="0 0 1000 400"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
        
              <VictoryChart width={1000}
        height={300}standalone={false} padding={{ left: 50,right:20, bottom: 60,top:20 }}
 >
                 
                
  
      
      
                 <VictoryLine data={this.state.template2.slice(minv,maxv)} x="index" y="value" style={{
      data: { stroke: "black" }
     
    }} />
                
                 <VictoryLine data={this.state.graph12.slice(minv,maxv)} x="index" y="value"  style={{
      data: { stroke: "red" }
     
    }}/>
                 <VictoryLine data={this.state.graph22.slice(minv,maxv)} x="index" y="value"  style={{
      data: { stroke: "blue" }
     
    }}/>
                
                <VictoryLine data={this.state.graph32.slice(minv,maxv)} x="index" y="value"  style={{
      data: { stroke: "green" }
     
    }}/>
                <VictoryLine data={this.state.graph42.slice(minv,maxv)} x="index" y="value" style={{
      data: { stroke: "brown" }
     
    }} />
                
                <VictoryLine data={this.state.graph52.slice(minv,maxv)} x="index" y="value" style={{
      data: { stroke: "gold" }
     
    }}/>
               
                 <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: 20 } ,axisLabel: {fontSize: 25, padding: 30}}} domain={{y:[-2,]}}   tickFormat={(t) => `${Math.round(t)}`} label="email  freq"/>
                 <VictoryAxis  offsetY={50} style={{ tickLabels: { fontSize: 30 } ,axisLabel: {fontSize: 30, padding: 30}}} label="email communication freq distribution"/>
               
              
                
               </VictoryChart>
               </g>
               </svg>
               <div className="box" style={{ padding: '5px',display:"inline-block",width: '40%',height:'90%',border: '1px solid white',overflow:'auto', fontSize:      '1vw',fontSize:      '1vh',textAlign: 'justify'}}>
               <div>{"wasserstein distance"}</div>  
                   <div><span style={{color:"black"}}>{"template"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  0.00"}</div>
                   <div><span style={{color:"red"}}>{"graph1"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[10]}</div>
                   <div><span style={{color:"blue"}}>{"graph2"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[11]}</div>
                   <div><span style={{color:"green"}}>{"graph3"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[12]}</div>
                   <div><span style={{color:"brown"}}>{"graph4"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[13]}</div>
                   <div><span style={{color:"gold"}}>{"graph5"}</span>{" <-> "} <span style={{color:"black"}}>{"template"}</span>{":  "+results[14]}</div>
                  
                  </div>
               </div>
              </Rnd>
              </div>
             
             
            )
        }
    }
    