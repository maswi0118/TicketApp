import React from 'react';

import TicketLogo from '../../images/pojscie_logo.png';
import SpotifyLogo from '../../images/Spotify_Logo_RGB_White.png';

import {Wrapper, Content, LogoImg, SpotifyImg} from "./Header.styles";

const Header = () => (
    <Wrapper>
        <Content>
            <LogoImg src={TicketLogo} alt='ticket-logo'/>
            <SpotifyImg src={SpotifyLogo} alt='ticket-green'/>
        </Content>
    </Wrapper>
);

export default Header;
