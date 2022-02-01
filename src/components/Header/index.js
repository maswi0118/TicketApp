import React from 'react';

import TicketLogo from '../../images/pojscie_logo.png';

import {Wrapper, Content, LogoImg} from "./Header.styles";

import Menu from "../Menu";


const Header = () => (
    <Wrapper>
        <Content>
            <LogoImg src={TicketLogo} alt='ticket-logo'/>
            <Menu/>
        </Content>
    </Wrapper>
);

export default Header;
