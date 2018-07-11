import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import HeaderPart from './Header_part';
import CollegesList from './CollegesList';
import { Link } from 'react-router-dom';
class App extends Component {
// componentDidMount()
// {
//   fetch("http://localhost:8000/api-token-auth/",
// {
//   method: "post",
//   body:JSON.stringify({"username":"hanish","password":"lostlost"}),
//   headers:{
//     "Content-Type": "application/json",
//   }

// }).then(res=>{
//   console.log(res);
//   res.json()
// }).then(data=>{
//   document.cookie = `jwt=${data.token}; expires=Sun,Jun 18 2018 00:42:38; path=/`;

// })
// }

  render() {
    return (
      <div className="App">
      
          <HeaderPart title= "hanish" isLoggedIn={true}/>
 
        <CollegesList/>
       </div>
    );
  }
}

export default App;
