import React, { Component } from 'react';
import '../../../App.css';
import { Rnd } from 'react-rnd';
import Subphone from './Subphone';
import Subemail from './Subemail';
import Subprocu from './Subprocu';
import Subdemo  from './Subdemo';
import Subtravel  from './Subtravel';
import Subbook from './Subbook';
  
  class Box extends Component {
 
    render() {
     
        return (
            <div
            className="box"
            style={{ margin: 0, height: '100%', paddingBottom: '40px' }}
          >
          <div  style={{backgroundColor: "lightblue"}}>  { this.props.value}</div>
            
          </div>
        );
  }
}

export default class SubAnalysis extends Component {

  
    render() {
        const arr=this.props.anacheckv;
        const slidervaluemin=arr.slidervaluemin;
        const  slidervaluemax =arr.slidervaluemax;
        
       
        const g1=arr.channelcheck.has(' Phone ')?arr.channelcheck.get(' Phone '):false;
        const g2=arr.channelcheck.has(' Email ')?arr.channelcheck.get(' Email '):false;
        const g3=arr.channelcheck.has(' Procurement ')?arr.channelcheck.get(' Procurement '):false;
        const g4=arr.channelcheck.has(' Co-authorship ')?arr.channelcheck.get(' Co-authorship '):false;
        const g5=arr.channelcheck.has(' Demographics ')?arr.channelcheck.get(' Demographics '):false;
        const gt=arr.channelcheck.has(' Travel ')?arr.channelcheck.get(' Travel '):false;
      let part1;
      let part2;
      let part3;
      let part4;
      let part5;
       let part6;
       if(g1){
        part1= <Subphone valuemin={slidervaluemin} valuemax={slidervaluemax}/>
       }else{
part1=null;
       }


       if(g2){
        part2= <Subemail valuemin={slidervaluemin} valuemax={slidervaluemax}/>
       }else{
        part2=null;
       }


       if(g3){
part3=   <Subprocu valuemin={slidervaluemin} valuemax={slidervaluemax}/>
    }else{
      part3= null; 
    }

    if(g4){
part4=  
<Subbook/>

    }else{
      part4=  null;
    }

    if(g5){
part5=  <Subdemo />
    }else{
        part5=   null;   
    }

    if(gt){
        part6= <Subtravel valuemin={slidervaluemin} valuemax={slidervaluemax}/>
   
    }else{
        part6=null
    }

        return (
            <div
            style={{
              width: '80px',
              height: '40px',
            }}
          >
             
   
             {part1}
    {part2}
    {part3}
    {part4}
    {part5}
    {part6}
   
   
  
              </div>
        )
    }
}
