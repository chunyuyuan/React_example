import React, { Component } from 'react';


import SubGraph from "./subAnalysis/SubGraph";
import SubAnalysis from "./subAnalysis/SubAnalysis";
import Slider from './Slider';
import '../../App.css';
import SideBar from "./Sidebar";
import Graphpart  from './subAnalysis/Graphpart';

  
     
export default class TemplateMatch extends Component {
    constructor(props){
        super(props);
        this.state={
            channelcheck:new Map(),
            csvcheck:new Map(),
           
            slidervaluemin:0,
            slidervaluemax:365,
           
           
        }
    }
    parentFunction=(data_from_child)=>{
     //  console.log( data_from_child);
     this.setState({csvcheck:data_from_child.checkedItems1});
     this.setState({channelcheck:data_from_child.checkedItems2},()=>{console.log();});
       
      
      
      
    }
    parentFunction1=(data_from_child)=>{
        
    
        this.setState({slidervaluemin:data_from_child.valuemin,slidervaluemax:data_from_child.valuemax},()=>{console.log("parent "+this.state.slidervaluemax);});
          
         
         
         
       }
       
    
    render() {
        
        let partslider;
       
            let c1=false;
            for (const [index, value] of this.state.channelcheck.entries()) {
               if(value===true){
                   c1=true;
                   break;
               }

              }
              let c2=false;
              for (const [index, value] of this.state.csvcheck.entries()) {
                 if(value===true){
                     c2=true;
                     break;
                 }
  
                }
           if(c1||c2){
            partslider= <Slider functionCallFromParent={this.parentFunction1.bind(this)}/>;
        }else{
            partslider=null;
        }

        return (
            <div id="App" style={{display:'inline-block'}}>
            
          
            <SideBar pageWrapId={"page-wrap"} outerContainerId={"App"} functionCallFromParent={this.parentFunction.bind(this)}/>
             <div id="page-wrap">
               <React.Fragment>
             
              <React.Fragment>
              
             <Graphpart graphcheckv = {this.state} />
             <Slider functionCallFromParent={this.parentFunction1.bind(this)}/>;
              <SubGraph graphcheckv = {this.state}/>
              </React.Fragment>
              <React.Fragment>
             <SubAnalysis anacheckv = {this.state}/>
             </React.Fragment>

            

          
      
         
         </React.Fragment>
            </div>
          </div>
           
           
        );
    }
}
