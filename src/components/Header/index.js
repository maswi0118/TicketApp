import React from 'react';

import TicketLogo from '../../images/pojscie_logo.png';

import {Wrapper, Content, LogoImg} from "./Header.styles";

import Menu from "../Menu";


const Header = () => (
    <Wrapper>
        <Content>
            <a href="/"><LogoImg src={TicketLogo} alt='ticket-logo'/></a>
            <Menu/>
        </Content>
    </Wrapper>
);

export default Header;
