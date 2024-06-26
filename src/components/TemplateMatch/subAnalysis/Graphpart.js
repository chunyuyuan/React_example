import React, { Component } from 'react';
import { Rnd } from 'react-rnd';
import axios from 'axios';
import Select from 'react-select';
import Switch from "react-switch";
import Checkbox from '../CheckBox';
import {VictoryLine,VictoryTheme, VictoryChart,VictoryAxis,VictoryContainer,VictoryBar,VictoryLabel} from 'victory';
import Graphshape from './Graphshape'
import Graphattr from './Graphattr'
const checkboxes1 = [
    {
      name: ' Person ',
      key: 'Person',
    
    },
    {
      name: ' Procurement ',
      key: 'Procurement',
 
    },
    {
        name: ' Travel ',
        key: 'Travel',
      
      },
    {
      name: ' Co-authorship ',
      key: 'Co-authorship',
  
    },
    {
      name: ' Demographics ',
      key: 'Demographics',
   
    },
   
   
  ];
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
  export default class Graphpart extends Component {
    constructor(props) {
      super(props);
    
     this. state ={
        width: 200,
        height: 100,
        x: 70,
        y: 180,
        g1:false,
        demog:false,
        travel:false,
        item: false,
        book:false,
        valuemin:0,
        valuemax:365,
        grapht:"",
        graph2:"",
        graph1:"",
        graph3:"",
        graph4:"",
        graph5:"",
        checked:false,
        selectvalue:'Degree Centrality',
        valuea:"",
        valueb:"",
        valuec:"",
        valued:"",
        valuee:"",
        valueg:"",
        value:"",
        valuerate:"",
      
            checkedItems1: new Map(),
          
            
          
  
    }
    
    }
    handleChangeselect=(event)=>{
     // console.log(event)
      this.setState({ selectvalue:event.value});
    }
  handleChange=(event) => {
   
    this.setState({ checked:event});
  }

    



handleChangecheckitem(e) {
    const isChecked = e.target.checked;
    this.setState({item:isChecked},()=>{this.getJoke()})

}

handleChangecheckbook(e) {
    const isChecked = e.target.checked;
    this.setState({book:isChecked},()=>{this.getJoke()})

}
handleChangechecktravel(e) {
    const isChecked = e.target.checked;
    this.setState({travel:isChecked},()=>{this.getJoke()})

}
handleChangecheckfinance(e) {
    const isChecked = e.target.checked;
    this.setState({demog:isChecked},()=>{this.getJoke()})

}

  componentDidMount(){
    var arr=this.props.graphcheckv;
   // console.log(arr)
    var g=arr.csvcheck.has(" Graphs ")?arr.csvcheck.get(" Graphs "):false;
    this.setState({ g1:g})
  
this.getJoke();
    
  }
  getJoke() {
    axios.get('http://127.0.0.1:5000/graphanalysis?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax+'&book='+this.state.book+'&item='+this.state.item+'&travel='+this.state.travel+'&demog='+this.state.demog+'&selectvalue='+this.state.selectvalue+'&checked='+this.state.checked).then (res=>{
      var x=res.data.split("&&");            
     
      this.setState({ grapht:x[0],graph1:x[1],graph2:x[2],graph3:x[3],graph4:x[4],graph5:x[5]})
     // console.log(this.state.gr)
    // this.setState({ value:x[6]},()=>{console.log(x[6])})
     
  }).catch(({response}) => {
   
    console.log(response);
});
axios.get('http://127.0.0.1:5000/graphanalysis1?valuemin=$'+this.state.valuemin+'&valuemax=$'+this.state.valuemax+'&book='+this.state.book+'&item='+this.state.item+'&travel='+this.state.travel+'&demog='+this.state.demog+'&selectvalue='+this.state.selectvalue+'&checked='+this.state.checked).then (res=>{
    var x=res.data.split("&&");            
  // console.log(JSON.parse(x[0]))
   // this.setState({ grapht:x[0],graph1:x[1],graph2:x[2],graph3:x[3],graph4:x[4],graph5:x[5]})
    console.log("hello "+x[1])

   this.setState({ value:JSON.parse(x[0]),valuerate:x[1]})
  
   
}).catch(({response}) => {
 
  console.log(response);
});
  }


  componentDidUpdate(prevProps, prevState) {
    if ((prevProps.graphcheckv !== this.props.graphcheckv)||(prevState.selectvalue!=this.state.selectvalue||prevState.checked!=this.state.checked||prevState.checkedItems1!=this.state.checkedItems1)) {
               
    var arr=this.props.graphcheckv;
  
    var g=arr.csvcheck.has(" Graphs ")?arr.csvcheck.get(" Graphs "):false;
    this.setState({ g1:g})
  //  this.setState({book: this.state.checkedItems1.has(" Co-authorship ")?this.state.checkedItems1.get(" Co-authorship "):false});
 
  //  this.setState({travel: this.state.checkedItems1.has(" Travel ")?this.state.checkedItems1.get(" Travel "):false});
 
//this.setState({item: this.state.checkedItems1.has(" Procurement ")?this.state.checkedItems1.get(" Procurement "):false});
   // this.setState({demog: this.state.checkedItems1.has(" Demographics ")?this.state.checkedItems1.get(" Demographics "):false});
 
   // if (prevState.selectvalue!=this.state.selectvalue||prevState.checked!=this.state.checked||prevState.valuemin != this.props.graphcheckv.slidervaluemin||prevState.valuemax !=this.props.graphcheckv.slidervaluemax) {
    this.setState({valuemin:arr.slidervaluemin,valuemax:arr.slidervaluemax},()=>{
   console.log(this.state.valuemin)
   this.getJoke();
    })
  //}
 
 };
  }
 
    render() {
      const barcolor=['#000000','#000000','#000000','#000000','red']
      const style = {
        display:  "inline-block",
        alignItems: "center",
        justifyContent: "center",
        border: "solid 1px #ddd",
        background: "#f0f0f0"
      };
      const arr=["Water and other public services" ,"Electricity" ,"Household furnishings" ,"Natural gas" ,"Miscellaneous" ,"Gifts" ,"Healthcare" ,"Restaurants" ,"Alcohol" ,"Home maintenance" ,"Housekeeping supplies" ,"Money income before taxes" ,"Personal insurance and pensions" ,"Reading" ,"Transportation" ,"Education" ,"Telephone services" ,"Lodging away from home" ,"Groceries" ,"Donations" ,"Entertainment" ,"Apparel and services" ,"Personal taxes" ,"Mortgage payments" ,"Rented dwellings" ,"Personal care products and services" ,"Tobacco" ,"Household operations" ,"Property taxes"];
     
      const rendercancel = ()=> {
        
     
        return ".box";
    
       // return ".box2";
  }
      
        const g1=this.state.g1;
        const data2=this.state.graph2.substring(2,this.state.graph2.length-1 );
       // console.log(data)
       const data1=this.state.graph1.substring(2,this.state.graph1.length-1 );
       const data3=this.state.graph3.substring(2,this.state.graph3.length-1 );
       const data4=this.state.graph4.substring(2,this.state.graph4.length-1 );
       const data5=this.state.graph5.substring(2,this.state.graph5.length-1 );
     
     
        const datat=this.state.grapht.substring(2,this.state.grapht.length-1 );;
       // const data = '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'
//const data1=`data:image/jpeg;base64,${data}`

const Example = ({ data }) => <img src={`data:image/jpeg;base64,${data}`} style={{height: '100%', width: '100%'}}/>

         /*   const g2=arr.csvcheck.has(" Q1-Graph2.csv ")?arr.csvcheck.get(" Q1-Graph2.csv "):false;
        const g3=arr.csvcheck.has(" Q1-Graph3.csv ")?arr.csvcheck.get(" Q1-Graph3.csv "):false;
        const g4=arr.csvcheck.has(" Q1-Graph4.csv ")?arr.csvcheck.get(" Q1-Graph4.csv "):false;
        const g5=arr.csvcheck.has(" Q1-Graph5.csv ")?arr.csvcheck.get(" Q1-Graph5.csv "):false;
        const gt=arr.csvcheck.has(" CGCS-Template.csv ")?arr.csvcheck.get(" CGCS-Template.csv "):false;
     */
        let part1;
        let part2;
        let part3;
        let part4;
   
    
     const options = [
          { value: 'Degree Centrality', label: 'Degree Centrality' },
          { value: 'Eigenvector Centrality', label: 'Eigenvector Centrality' },
          { value: 'Closeness Centrality', label: 'Closeness Centrality' },
          { value: 'Betweenness Centrality', label: 'Betweenness Centrality' },
          { value: 'Katz Centrality', label: 'Katz Centrality' },
          { value: 'Harmonic Centrality', label: 'Harmonic Centrality' },
          { value: 'Pagerank', label: 'Pagerank' },
         

        ]

        

        const styles1 = {
          control: (base) => ({
            ...base,
            height: 25,
            minHeight: 25,
            fontSize: '9px',
          }),
          dropdownIndicator: (base) => ({
            ...base,
            paddingTop: 0,
            paddingBottom: 0,
            height: 20,
            minHeight: 15,  
          }),
          clearIndicator: (base) => ({
            ...base,
            paddingTop: 0,
            paddingBottom:0,
            height: 20,
            
          }),
        };
let switchtext='average value'
    if(this.state.checked){
      switchtext='max value'
    }else{
      switchtext='average value'
    }


  
      
    



      
        part1= <Rnd
        style={style}
       size={{ width: this.state.width,  height: this.state.height  }}
       position={{  x: 26, y: 32}}
       onDragStop={(e, d) => { this.setState({ x: d.x, y: d.y },()=>{console.log(this.state.x,this.state.y)}) }}
       onResize={(e, direction, ref, delta, position) => {
         this.setState({
           width: ref.offsetWidth,
           height: ref.offsetHeight,
           ...position,
         });
       }}
       minWidth={'60%'}
       minHeight={'85%'}
       bounds="window"
       cancel ={ rendercancel()}
     >

<div className="box" style={{ width: '100%',height:'6%',backgroundColor: "white",fontSize:"18px",display:  "flex"}}>
  <div style={{color:"red", width:'20%',display:  "flex", justifyContent:'center', alignItems:'center'}}><li >{"person"}</li></div>
  
                 <div style={{color:"blue", width:"20%",display:  "flex", justifyContent:'center', alignItems:'center'}}><li >{"item"}</li><div style={{width:'20%', display: 'flex',  justifyContent:'center', alignItems:'center'}}><Checkbox  name={checkboxes1[1].name} checked={this.state.item} onChange={this.handleChangecheckitem.bind(this)}/></div></div>
               
                 <div style={{color:"brown", width:"20%",display:  "flex", justifyContent:'center', alignItems:'center'}}><li >{"travel"}</li><div style={{width:'20%', display: 'flex',  justifyContent:'center', alignItems:'center'}}><Checkbox  name={checkboxes1[2].name} checked={this.state.travel} onChange={this.handleChangechecktravel.bind(this)}/></div></div>
                
                 <div style={{color:"green", width:"20%",display:  "flex", justifyContent:'center', alignItems:'center'}}><li >{"book"}</li><div style={{width:'20%', display: 'flex',  justifyContent:'center', alignItems:'center'}}><Checkbox  name={checkboxes1[3].name} checked={this.state.book} onChange={this.handleChangecheckbook.bind(this)}/></div></div>
                 <div style={{color:"grey", width:"20%",display:  "flex", justifyContent:'center', alignItems:'center'}}><li >{"finance"}</li><div style={{width:'20%', display: 'flex',  justifyContent:'center', alignItems:'center'}}><Checkbox  name={checkboxes1[4].name} checked={this.state.demog} onChange={this.handleChangecheckfinance.bind(this)}/></div></div>
                  
                
</div>

<div className="box" style={{  width: '100%',height:'94%',display:  "flex" } }>
<div className="box"style={{  width: '100%',height:'99%',display:  "inline-block" } }> 
<div
   className="box"
   style={{  width: '100%',height:'50%' ,border: '1px solid white', display:  "flex" }}
 >
   
   <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white' ,  backgroundImage: "url(${data1} )",
   backgroundPosition: 'center',
   backgroundSize: 'cover',
   backgroundRepeat: 'no-repeat'}}
 >

<Example data={datat} />
  
 </div>
 <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white', position: 'relative'
    }}
 >


   <Example data={data1} />
  
 </div>
 <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white' }}
 >

<Example data={data2} />
  
 </div>

   
 </div>
 <div
   className="box"
   style={{  width: '100%',height:'50%', border: '1px solid white',display:  "flex" }}
 >
 <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white' }}
 >

<Example data={data3} />
   
 </div>
 <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white' }}
 >

<Example data={data4} />
   
 </div>
 <div
   className="box"
   style={{  width: '33.3%',height:'100%' ,border: '1px solid white' }}
 >

<Example data={data5} />
  
 </div>
   
 </div>
 </div>
 
 
 
 </div>
</Rnd>
       

    part2=<Graphshape data={this.state.value}  timemin={this.state.valuemin} timemax={this.state.valuemax}/>
   

     /*  if(gt){
        part2=<Rnd
        default={{
          x: 240,
          y: 75,
          width: 165,
          height: 120,
        }}
        minWidth={165}
        minHeight={ 120}
        bounds="window"
      >
        <Box value={" Q1-Graph1.csv"}/>
        
      </Rnd>
       }else{
        part2=null;
       }


       if(g2){
part3=   <Rnd
default={{
  x: 410,
  y: 75,
  width: 165,
  height: 120,
}}
minWidth={165}
minHeight={ 120}
bounds="window"
>
<Box value={" Q1-Graph2.csv"}/>

</Rnd>
    }else{
      part3= null; 
    }

    if(g3){
part4= <Rnd
default={{
  x: 580,
  y: 75,
  width: 165,
  height: 120,
}}
minWidth={165}
minHeight={ 120}
bounds="window"
>
<Box value={" Q1-Graph3.csv"}/>

</Rnd>
    }else{
      part4=  null;
    }

    if(g4){
part5=  <Rnd
default={{
  x: 750,
  y: 75,
  width:165,
  height: 120,
}}
minWidth={165}
minHeight={ 120}
bounds="window"
>
<Box value={" Q1-Graph4.csv"}/>

</Rnd>
    }else{
        part5=   null;   
    }

    if(g5){
        part6= 
        <Rnd
          default={{
            x: 920,
            y: 75,
            width:165,
            height: 120,
          }}
          minWidth={165}
          minHeight={ 120}
          bounds="window"
        >
          <Box value={" Q1-Graph5.csv"}/>
         
        </Rnd>
    }else{
        part6=null
    } {part2}
    {part3}
    {part4}
    {part5}
    {part6} */

        return (
  <div
    style={{
      width: '80px',
      height: '40px',
    }}
  >
    {part1}
    {part2}
    { part3}
   
    
   
  
  </div>
)}};