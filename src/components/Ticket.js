import React from 'react';
import {Wrapper} from "./Login/Login.styles";
import {useTickets} from "../hooks/useTickets";
import Grid from "./Grid";
import Thumb from "./Thumb";
import NoImage from "../images/noImage.png";
import Spinner from "./Spinner";
import MoreButton from "./MoreButton";
import Ticket from "./Ticket";

const Tickets = () => {
    const { state, loading, error, setIsLoadingNext, setIsLoadingPrevious, pageNumber } = useTickets();

    console.log(state)
    console.log(state.page.length)


        return (
        <Wrapper>
            <Grid header='Your Tickets'>
                {state.page.length > 0  ? state.page[pageNumber].map(event => (
                    <Ticket
                        key={event.eid}
                        image={NoImage}
                        artistName={event.artistName}
                        eventName={event.name}
                        date={event.date}
                        genre={event.genre}
                    />
                )) : <a>No tickets available</a>}
            </Grid>
            {loading && <Spinner/>}
            {state.page.length > pageNumber + 1 && !loading && (
                <MoreButton text={'Next Page'} callback={() => setIsLoadingNext(true)}/>
            )}
            {pageNumber > 0 && !loading && (
                <MoreButton text={'Previous Page'} callback={() => setIsLoadingPrevious(true)}/>
            )}
        </Wrapper>
    )
}

export default Tickets