import React, { Component } from 'react';
import '../../../App.css';
import { Rnd } from 'react-rnd';
import axios from 'axios';

import {VictoryBar,VictoryLine, VictoryChart,VictoryAxis,VictoryContainer,VictoryLabel} from 'victory';




export default class Subprocu extends Component {
    constructor(props) {
        super(props);
       
      }
      state ={
        freq:[],
        weight:[],
        x: 100,
        y: 180,
        width: 150,
        height: 100,
        valuemin:0,
        valuemax:365,
      }
      async componentDidUpdate(prevProps, prevState) {
        if (prevProps.valuemin !== this.props.valuemin||prevProps.valuemax !== this.props.valuemax) {
          this.setState({valuemin:this.props.valuemin,valuemax:this.props.valuemax},()=>{
            axios.get('http://127.0.0.1:5000/procurementanalysis?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax).then (res=>{
              // console.log(res);
               var x=res.data.split("&&");
             // console.log(JSON.parse(x[0]) )
               this.setState({freq:JSON.parse(x[0]),weight:JSON.parse(x[1])},()=>{console.log(this.state.freq)});
              
             })
            })
            //  console.log("graph test ",this.state.template.slice(0, 2))
             }
             }
             componentDidMount(){
          
                axios.get('http://127.0.0.1:5000/procurementanalysis?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax).then (res=>{
                   // console.log(res);
                    var x=res.data.split("&&");
                  // console.log(JSON.parse(x[0]) )
                  this.setState({freq:JSON.parse(x[0]),weight:JSON.parse(x[1])});
              
                  })
                }     


    render() {
        const minv=this.props.valuemin;
        const maxv=this.props.valuemax;
        
        const style = {
         display:  "inline-block",
         alignItems: "center",
         justifyContent: "center",
         border: "solid 1px #ddd",
         background: "#f0f0f0"
       };
        return (
            <div >
             
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
          > 
           <div  style={{backgroundColor: "lightblue",fontSize:"10px"}}>  {"Procurement analysis"}</div>
           <div>
             <svg
        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20) /2}
        viewBox="0 0 1000 400"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>
        <VictoryChart width={1000}
        height={300}standalone={false} domainPadding={100}
 >
<VictoryBar data={this.state.freq} x="index" y="value" labels={({ datum }) => datum.value}
  labelComponent={<VictoryLabel renderInPortal dy={-20} style={{  fontSize: 60 }}/>} />
   <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: 20 } ,axisLabel: {fontSize:  25, padding: 30}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="procurement freq "/>
                 <VictoryAxis  offsetY={50} style={{ tickLabels: { fontSize: 30 } ,axisLabel: {fontSize: 30, padding: 40}}}  label="procurement freq  distribution"/>
               
</VictoryChart>
        </g>
               </svg>
              
               </div>


               <div>
             <svg
        x={0 }
        y={0 }
        width={this.state.width }
        height={(this.state.height-20) /2}
        viewBox="0 0 1000 400"
        preserveAspectRatio="none"
        fillOpacity="0.8">
         
        <g>

        <VictoryChart width={1000}
        height={300}standalone={false} domainPadding={100}
 >
<VictoryBar data={this.state.weight} x="index" y="value" labels={({ datum }) => datum.value}
  labelComponent={<VictoryLabel renderInPortal dy={-20} style={{  fontSize: 60 }}/>} />
   <VictoryAxis dependentAxis style={{ tickLabels: { fontSize: 15, padding: -10 } ,axisLabel: {fontSize:  25, padding: 30}}} domain={{y:[0,]}}   tickFormat={(t) => `${Math.round(t)}`} label="procurement weight "/>
                 <VictoryAxis  offsetY={50} style={{ tickLabels: { fontSize: 30 } ,axisLabel: {fontSize: 30, padding: 40}}}  label="procurement weight  distribution"/>
               
</VictoryChart>
        </g>
               </svg>
              
               </div>

          </Rnd>      
            </div>
        )
    }
}
