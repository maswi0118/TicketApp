import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    balance: 0
}

export const useBalance = () => {
    const [state, setState] = useState(initialState)
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    const fetchBalance = async () => {
        try {
            setError(false);
            setLoading(true);

            const success = await API.fetchBalance();

            await setState(success);

        } catch (error) {
            setError(true);
        }
        setLoading(false)
    };

    useEffect(()  => {
        fetchBalance()
    }, []);

    return { state };
};