import React from 'react';
//API
//Config

//Components
import MainImage from "./MainImage";
import Grid from "./Grid";
import Thumb from "./Thumb";
import Spinner from "./Spinner"
import SearchBar from "./SearchBar";
import MoreButton from "./MoreButton"
//Hook
import { useHomeFetch } from "../hooks/useHomeFetch";
import { usePurchase } from "../hooks/usePurchase";
//Image
import NoImage from '../images/noImage.png';

const Home = () => {
    const { state, loading, error, setSearchTerm, setIsLoadingNext, setIsLoadingPrevious, pageNumber } = useHomeFetch();

    console.log(state)
    console.log(state.page.length)

    return(
        <>
            {`https://thewhitonline.com/wp-content/uploads/2021/04/festival-2.jpeg` ? (
               < MainImage
                    // image={state.artists.items[0].images[0].url}
                    // image={`https://i.scdn.co/image/ab6761610000e5eb5d2466b5333659e1941bb75e`}
                    image={`https://thewhitonline.com/wp-content/uploads/2021/04/festival-2.jpeg`}
                    title={`PoojścieApp`}
                    text={`Bilet se kup`}
                />
            ) : null }
            <SearchBar setSearchTerm={setSearchTerm}/>
            <Grid header='Incomming Events'>
                {state.page.length > 0  ? state.page[pageNumber].map(event => (
                    <Thumb
                        key={event.eid}
                        image={NoImage}
                        artistName={event.artistName}
                        eventName={event.name}
                        date={event.date}
                        price={event.price}
                        genre={event.genre}
                        eid={event.eid}
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
        </>
    );
};

export default Home;