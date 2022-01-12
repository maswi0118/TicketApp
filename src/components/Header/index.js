import React from 'react';

import TicketLogo from '../../images/ticketImage.svg';
import GreenLogo from '../../images/ticketGreen.svg';

import {Wrapper, Content, LogoImg, GreenImg} from "./Header.styles";

const Header = () => (
    <Wrapper>
        <Content>
            <LogoImg src={TicketLogo} alt='ticket-logo'/>
            <GreenImg src={GreenLogo} alt='ticket-green'/>
        </Content>
    </Wrapper>
);

export default Header;
