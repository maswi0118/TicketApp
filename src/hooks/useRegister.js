import { useState, useEffect, useRef } from 'react';
//API
import API from "../Api";

const initialState = {
    response: "False"
}

export const useRegister = () => {
    const [RUsername, setRUsername] = useState('');
    const [RPassword, setRPassword] = useState('');
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [isRegistering, setIsRegistering] = useState(false);
    const [isLogged, setIsLogged] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] =useState(false);

    const fetchRegister = async (RUsername, RPassword, email, firstname, lastname, phoneNumber) => {
        try {
            setError(false);
            setLoading(true);

            const success = await API.fetchRegister(RUsername, RPassword, email, firstname, lastname, phoneNumber);

            await setIsLogged(success);

            console.log(success)
            if (success == "true") {
                await localStorage.setItem("logged", "true");
                await localStorage.setItem("username", RUsername)
                await window.location.reload();
            } else {

            }

        } catch (error) {
            setError(true);
        }
        setLoading(false);
    };

    useEffect(()  => {
        if (!isRegistering) return
        fetchRegister(RUsername, RPassword, email, firstName, lastName, phoneNumber)
        setIsRegistering(false)
    }, [isRegistering]);


    return { setIsRegistering, RUsername, setRUsername, RPassword, setRPassword, email, setEmail, firstName, setFirstName, lastName, setLastName, phoneNumber, setPhoneNumber};
};