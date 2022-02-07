import { useState, useEffect, useRef } from 'react';
//API
import SPOTIFY_API from "../SpotifyApi";

const initialState = {
    artists: {items: []}
}

export const useHomeFetch = () => {
    const [searchTern, setSearchTerm] = useState('')
    const [state, setState] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    console.log(searchTern)

    const fetchArtists = async (artist) => {
        try {
            setError(false);
            setLoading(true);

            const artists = await SPOTIFY_API.fetchArtists(artist);

            // console.log(artists);

            setState(artists);


        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    //Initial and search
    useEffect(() => {
        setState(initialState);
        fetchArtists(searchTern);
    }, [searchTern])

    return { state, loading, error, setSearchTerm, searchTern };
};