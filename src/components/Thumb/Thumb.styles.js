import styled from 'styled-components'

export const Image = styled.img`
  width: 100%;
  max-width: 300px;
  height: 100%;
  max-height: 300px;
  transition: all 0.3s;
  object-fit: cover;
  border-radius: 20px;
  animation: animateThumb 0.5s;
  
  @media screen and (max-width: 720px) {
    width: 200px;
    height: 200px;
  }
  
  :hover {
    opacity: 0.8;
  }
  
  @keyframes animateThumb {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
`;

export const Details = styled.a`
  ;
`;