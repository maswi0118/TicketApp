import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    page: []
}

export const useTickets = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [state, setState] = useState(initialState)
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);
    const [isLoadingNext, setIsLoadingNext] = useState(false)
    const [isLoadingPrevious, setIsLoadingPrevious] = useState(false)
    const [pageNumber, setPageNumber] = useState(0);

    const fetchTickets = async () => {
        try {
            setError(false);
            setLoading(true);

            const success = await API.fetchTickets();

            await setState(success);

        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    useEffect(()  => {

        fetchTickets()
    }, []);
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


    return { state, setIsLoading };
};