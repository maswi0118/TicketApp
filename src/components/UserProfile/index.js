import React from 'react'
import { Wrapper, Content } from './UserProfile.styles'
import {useHref} from "react-router-dom";

function UserProfile() {
    console.log(localStorage.getItem("logged"))

    return (
        <Wrapper>
            <Content>
                <a>zalogowany?: tak</a>
            </Content>
            <a href={"/profile"}><button type="submit" onClick={() => {localStorage.setItem("logged", "false")}}>wyloguj</button></a>
        </Wrapper>
    )
};

export default UserProfile