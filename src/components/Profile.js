import React from 'react';
//Components
import Login from "./Login"
import UserProfile from "./UserProfile"

const Profile = () => {
    return (
        localStorage.getItem("logged") == "true" ?
            <UserProfile/>
            :
            <Login/>
    )
}

export default Profile;
