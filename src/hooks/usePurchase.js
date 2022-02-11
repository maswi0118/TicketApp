import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    response: "False"
}

export const usePurchase = () => {
    const [eid, setEid] = useState(null)
    const [isPurchasing, setIsPurchasing] = useState(false);
    const [isPurchased, setIsPurchased] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    const fetchPurchase = async (eid) => {
        try {
            setError(false);
            setLoading(true);

            const success = await API.fetchPurchase(eid);

            await setIsPurchased(success);

            console.log(success)
            if (success != false ) {
                await alert("Ticked purchased successfully")
            } else {
                await alert("Something went wrong, recharge your account or sign in")
            }

        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    useEffect(()  => {
        if (!isPurchasing) return
        fetchPurchase(eid)
        setIsPurchasing(false)
    }, [isPurchasing]);


    return {  setIsPurchasing, setEid };
};