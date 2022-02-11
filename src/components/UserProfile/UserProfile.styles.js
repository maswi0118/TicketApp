import styled from 'styled-components'

export const Wrapper = styled.div`
      position: center;
      padding-top: 200px;
      justify-content: space-around;
      display: flex;
      background-color: gray;
`;



export const Content = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    text-align: center;
    background-color: gray;
    
    button {
      width: 200px;
      height: 20px;
    }
`;

export const Logout = styled.a`
  margin-top: 30px;
  display: flex;
  justify-content: center;
    button {
        width: 100px;
        height: 100px;
    }
`;