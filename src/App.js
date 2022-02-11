import React, {useState} from 'react';
import create from 'zustand'
//Routing
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
//Components
import Header from "./components/Header";
import Home from "./components/Home";
import Events from "./components/Events";
import NotFound from "./components/NotFound/index";
import UserTickets from "./components/UserTickets";
import Profile from "./components/Profile";


//Styles
import {GlobalStyle} from "./GlobalStyle";

const App = () => (
    <Router>
        <Header/>
        <Routes>
            <Route path='/' element={<Home/>}/>
            <Route path='/eventId' element={<Events/>}/>
            <Route path='/tickets' element={<UserTickets/>}/>
            <Route path='/profile' element={<Profile/>}/>
            <Route path='/*' element={<NotFound/>}/>
        </Routes>
      <GlobalStyle/>
    </Router>
);

export default App;
