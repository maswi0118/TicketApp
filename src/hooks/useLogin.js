import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    response: "False"
}

export const useLogin = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLogging, setIsLogging] = useState(false);
    const [isLogged, setIsLogged] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    const fetchLogin = async (username, password) => {
        try {
            setError(false);
            setLoading(true);

            const success = await API.fetchLogin(username, password);
            console.log(success)

            await setIsLogged(success);


            if (success.response == "True") {
                await localStorage.setItem("logged", "true");
                await localStorage.setItem("username", username);
                await alert("Signed in Successfully");
                await window.location.reload();
            } else {
                await alert("Something went wrong");
            }

        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    useEffect(()  => {
        if (!isLogging) return
        fetchLogin(username, password)
        setIsLogging(false)
    }, [isLogging]);


    return {  setIsLogging, username, setUsername, password, setPassword};
};