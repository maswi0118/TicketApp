import React from 'react';
//API
import SPOTIFY_API from'../SpotifyApi';
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
//Image
import NoImage from '../images/noImage.png';

const Home = () => {
    const { state, loading, error, setSearchTerm } = useHomeFetch();

    console.log(state)

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
                {state != null ? state.artists.items.map(artist => (
                    <Thumb
                        key={artist.id}
                        clickable
                        image={artist.images.length > 0 ? artist.images[0].url : NoImage}
                        artistId={artist.id}
                    />
                )) : null}
            </Grid>
            <Spinner/>
            <MoreButton text={'Load More'}/>
        </>
    );
}

export default Home;