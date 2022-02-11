import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    response: "False"
}

export const useAddMoney = () => {
    const [amount, setAmount] = useState(0)
    const [isTransferring, setIsTransferring] = useState(false);
    const [isTransferred, setIsTransferred] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    const fetchAddMoney = async (amount) => {
        try {

            setError(false);
            setLoading(true);

            const success = await API.fetchAddMoney(amount);

            await setIsTransferred(success);

            console.log(success)
            if (success == true ) {
                await alert("Money transferred successfully!")
            } else {
                await alert("Something went wrong")
            }

        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    useEffect(()  => {
        if (!isTransferring) return
        fetchAddMoney(amount)
        setIsTransferring(false)
    }, [isTransferring]);


    return {  setIsTransferring, amount, setAmount };
};