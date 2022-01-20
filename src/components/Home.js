import React, {useState, useEffect} from 'react';
//API
import SPOTIFY_API from'../SpotifyApi';
//Config

//Components
import MainImage from "./MainImage";
//Hook
import { useHomeFetch } from "../hooks/useHomeFetch";
//Image
import NoImage from '../images/noImage.png';

const Home = () => {
    const { state, loading, error } = useHomeFetch();

    console.log(state)

    return(
        <>
            {state.artists.items[0] ? (
               < MainImage
                    // image={`${state.artists.items[0].images[0].url}`}
                    // image={`https://i.scdn.co/image/ab6761610000e5eb5d2466b5333659e1941bb75e`}
                    image={`https://thewhitonline.com/wp-content/uploads/2021/04/festival-2.jpeg`}
                    title={`PoojścieApp`}
                    text={`Bilet se kup`}
                />
            ) : null }
        </>
    );
}

export default Home;