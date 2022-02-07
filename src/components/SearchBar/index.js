import React, {useState, useEffect, useRef} from 'react';
//Image
import searchIcon from '../../images/searchIcon.png'
//Styles
import { Wrapper, Content} from "./SearchBar.styles";

const SearchBar = ({ setSearchTerm }) => {
    const [state, setState] = useState('');
    const initial = useRef(true);

    useEffect(() => {
        if (initial.current) {
            initial.current = false;
            return;
        }

        const timer = setTimeout(() => {
            setSearchTerm(state);
        }, 500)
        return () => clearTimeout(timer)
    }, [setSearchTerm, state])

    return(
        <Wrapper>
            <Content>
                <img src={searchIcon} alt='searchIcon'/>
                <input
                    type={"text"}
                    placeholder={'Search events'}
                    onChange={event => setState(event.currentTarget.value)}
                    value={state}
                />
            </Content>
        </Wrapper>
    );
};

export default SearchBar
