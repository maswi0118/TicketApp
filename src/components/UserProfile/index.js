import React from 'react'
import { Wrapper, Content } from './UserProfile.styles'
import Button from "../Button";
import {useAddMoney} from "../../hooks/useAddMoney";

function UserProfile() {
    const { setIsTransferring, amount, setAmount } = useAddMoney()

    return (
        <Wrapper>
            <Content>
                <a>zalogowany?: tak</a>
            </Content>
            <Content>
                <h3>Add Money</h3>
                <input
                    type={"number"}
                    placeholder={'amount'}
                    onChange={event => setAmount(event.currentTarget.value)}
                    value={amount}
                />
                <Button text={'Transfer'} callback={() => setIsTransferring(true)}/>
            </Content>
            <a href={"/profile"}><button type="submit" onClick={() => {localStorage.setItem("logged", "false")}}>wyloguj</button></a>
        </Wrapper>
    )
};

export default UserProfile