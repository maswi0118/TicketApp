import React from 'react';
//Styles
import { Wrapper } from  './MoreButton.styles'

const MoreButton = ({ text, callback }) => (
    <Wrapper type='button' onClick={callback}>
        {text}
    </Wrapper>
)

export default MoreButton
