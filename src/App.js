
import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom';
import './App.css';
import Navbar from "./components/Navbar";
import SeedMatch from './components/SeedMatch/SeedMatch';
import TemplateMatch from './components/TemplateMatch/TemplateMatch';
import BlindMatch from './components/BlindMatch/BlindMatch';

class App extends Component {
  render(){
  return (

    <React.Fragment>
     <Navbar/> <Switch>
    <Route exact path="/" component={TemplateMatch}/>
     <Route path="/seedMatch" component={SeedMatch}/>
      <Route path="/blindMatch" component={BlindMatch}/>
    
     
      
     
        </Switch>
    

    </React.Fragment>
  );
}
}

export default App;
