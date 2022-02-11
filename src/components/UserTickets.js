import React from 'react';
import {Wrapper} from "./Login/Login.styles";
import {useTicket} from "../hooks/useTickets";
import Grid from "./Grid";
import Thumb from "./Thumb";
import NoImage from "../images/noImage.png";
import Spinner from "./Spinner";
import MoreButton from "./MoreButton";
import Ticket from "./Ticket";

const UserTickets = () => {
    const { state, loading, error, setIsLoadingNext, setIsLoadingPrevious, pageNumber, setIsLoading } = useTicket();

    console.log(state)
    console.log(state.page.length)
    console.log(state.page[0])


        return (
            <>
                <Wrapper>
                    <Grid header='Incomming Events'>
                        {state.page.length > 0  ? state.page[pageNumber].map(event => (
                            <Ticket
                                key={event.tid}
                                image={NoImage}
                                artistName={event.artistName}
                                eventName={event.name}
                                date={event.date}
                                genre={event.genre}
                                id={event.tid}
                            />
                        )) : null}
                    </Grid>
                    {loading && <Spinner/>}
                    {state.page.length > pageNumber + 1 && !loading && (
                        <MoreButton text={'Next Page'} callback={() => setIsLoadingNext(true)}/>
                    )}
                    {pageNumber > 0 && !loading && (
                        <MoreButton text={'Previous Page'} callback={() => setIsLoadingPrevious(true)}/>
                    )}
                    {state.page.length == 0 && (
                        <h1>No tickets available</h1>
                    )}
                </Wrapper>
            </>
    )
};

export default UserTickets