import React, { Component } from 'react'
import Select from 'react-select';
import '../../App.css';
import 'react-bootstrap-range-slider/dist/react-bootstrap-range-slider.css';
import ReactSlider from 'react-slider'

import { Rnd } from 'react-rnd';
import styled from 'styled-components';

const StyledSlider = styled(ReactSlider)`
    width: 100%;
    height: 18px;
`;
const StyledSlider1 = styled(ReactSlider)`
    width: 60%;
    height: 18px;
`;
const StyledSlider2 = styled(ReactSlider)`
    width: 5%;
    height: 18px;
`;

const StyledThumb = styled.div`
    height: 18px;
    line-height: 18px;
    width: 18px;
    font-size:10px;
    text-align: center;
    background-color: #000;
    color: #fff;
    border-radius: 50%;
    cursor: grab;
`;

const Thumb = (props, state) => { return(<StyledThumb {...props}>{state.valueNow}</StyledThumb>);};

const StyledTrack = styled.div`
    top: 0;
    bottom: 0;
    background: ${props => props.index === 2 ? '#00fddd' : props.index === 1 ? '#009ffd' : '#00fddd'};
    border-radius: 999px;
`;

const Track = (props, state) => <StyledTrack {...props} index={state.index} />;


const options = [
  { value: 'year', label: 'Year' },
  { value: 'month', label: 'Month' },
  { value: 'day', label: 'Day' },
];
export default class Slider extends Component {
  constructor(props){
    super(props);
    this.state={
      brandSelect: options[2],
      valuemin: 0,
      valuemax: 0,
       
    }
   
        this.handleChange1 = this.handleChange1.bind(this);
      
}
handleChange(event) {
  this.setState({brandSelect:  { value: event.value, label: event.label }},()=>{this.props.functionCallFromParent(this.state);}); // important
}
    
      handleChange1 (event){
        
        this.setState({ valuemin: event[0],valuemax: event[1]},()=>{console.log("finish");this.props.functionCallFromParent(this.state);});
      };
      
      handleChange2(event){
        
       console.log(event[0],event[1])  };
    
      render() {
      let checkselect=this.state.brandSelect.value;
     
     
      const renderAuthButton = ()=> {
        
        
            return <div ><StyledSlider
            max={365}
            defaultValue={[0, 365]}
            renderTrack={Track}
            renderThumb={Thumb}
            onChange={this.handleChange2}
            onAfterChange={this.handleChange1}
        /></div>;
         
        
      }
      let selectsize=600;
      const rendercancel = ()=> {
      
            selectsize=600;
            return ".block1";
        
    
    }
    const rendersize = ()=> {
      switch (checkselect) {
        case 'day':
         
          return 1000;
        case 'month':
         
          return 600
          case 'year':
            
            return 600
            default:
              return 600; 
    }
  }
  const style = {
    display:  "flex",
    alignItems: "center",
    justifyContent: "center",
    border: "solid 1px #ddd",
    background: "#f0f0f0"
  };
    
    
        return (
           <Rnd
      default={{
        x: 80,
        y: 5,
        width:rendersize,
        height: 20,
      }}
      style={style}
      minWidth={600}
      maxWidth={600}
      minHeight={ 20}
      maxHeight={ 20}
      bounds="window"
      cancel ={ rendercancel()}
    >
     
          <div  style={{width:'100%'}}>
        
         
 {renderAuthButton()} </div>
     

          </Rnd>
        


        );
    }
}
