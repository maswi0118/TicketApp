import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    page: []
}

export const useHomeFetch = () => {
    const [searchTern, setSearchTerm] = useState('')
    const [state, setState] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);
    const [isLoadingNext, setIsLoadingNext] = useState(false)
    const [isLoadingPrevious, setIsLoadingPrevious] = useState(false)
    const [pageNumber, setPageNumber] = useState(0);


    console.log(searchTern)

    const fetchEvents= async (searchTerm) => {
        try {
            setError(false);
            setLoading(true);

            const events = await API.fetchEvents(searchTerm);


            setState(events)


        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    //Initial and search
    useEffect(() => {
        setState(initialState);
        fetchEvents(searchTern);
    }, [searchTern])

    useEffect(() => {
        if (!isLoadingNext) return
        setPageNumber(pageNumber + 1)
        setIsLoadingNext(false)
    }, [isLoadingNext, pageNumber]);

    useEffect(() => {
        if (!isLoadingPrevious) return
        setPageNumber(pageNumber - 1)
        setIsLoadingPrevious(false)
    }, [isLoadingPrevious, pageNumber]);

    return { state, loading, error, setSearchTerm, searchTern, setIsLoadingNext, setIsLoadingPrevious, pageNumber };
};