import styled from 'styled-components'

export const Wrapper = styled.div`
  position: center;
  padding-top: 200px;
  text-align: center;
  margin-right: 200px;
  margin-left: 200px;
  h1 {
    color: var(--darkGray);
  }
  @media screen and (max-width: 720px) {
    margin-left: 20px;
    margin-right: 20px;
  }
`;

export const Content = styled.div`
    padding: 20px 20px 20px 20px;
    margin-bottom: 50px;
    display: flex;
    justify-content: space-around;
    // button {
    //   width: 200px;
    // }  
    background-color: gray;
    border-radius: 10px;
        h1 {
        display: flex;
        align-items: center;
    }
  input {
    margin: 4px;
  }

`;

export const Block = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
`;

export const ContentRegister = styled.div`
    padding: 20px 20px 20px 20px;
    margin-bottom: 50px;
    display: flex;
    justify-content: space-around;
    // button {
    //   width: 200px;
    // }  
    background-color: gray;
    border-radius: 10px;
    h1 {
        display: flex;
        align-items: center;
    }
  input {
    margin: 4px;
  }
`;

export const Container = styled.div`
    width: 500px;
    button {
      width: 200px;
    }
      input:invalid {
      border-color: red;
    }
  
`;