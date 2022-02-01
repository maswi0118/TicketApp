import styled from 'styled-components'


export const BarItem = styled.a`
  color: white;
  font-size: var(--fontBig);
  text-decoration: none;
  --button-hover-bg: black;
  transition: all 0.2s;
  &:hover {
    background-color: darkgrey;
    border-radius: 2px;
    padding: 7px;
  }
  
  @media screen and (max-width: 720px) {
    font-size: 0;
  }
`

export const MenuBarItem = styled.a`
  color: white;
  font-size: var(--fontBig);
  text-decoration: none;
  --button-hover-bg: black;
  transition: all 0.2s;
  &:hover {
    background-color: darkgrey;
    border-radius: 2px;
    padding: 7px;
  }
  
  @media screen and (min-width: 720px) {
    font-size: 0;
  }
`

export const Bar = styled.ul`
    display: grid;
    grid-template-columns: repeat(5, auto);
    grid-gap: 20px;
    list-style: none;
    text-align: center;
    width: 50vw;
    justify-content: end;
    margin-right: 2rem;
  
  @media screen and (max-width: 720px) {
    grid-gap: 0;
  }
`

export const MenuBar = styled.div`
  width: 70px;
  
  img{
    width: 30px;
    transition: all 0.3s ease-out;
    &:hover{
      background-color: darkgrey;
      border-radius: 2px;
      padding: 5px;
    }    
  }
  
  li{
    margin-top: 15px;
    font-size: var(--fontSuperBig);
  }
  
  @media screen and (min-width: 720px) {
    img{
      width: 0;
      margin-bottom: 0;
      padding: 0;
    }
    li {
      margin-top: 0;
      height: 0;
    }
  }
`