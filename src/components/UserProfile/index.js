import React from 'react'
import {Wrapper, Content, Logout} from './UserProfile.styles'
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
                <div class>
                    <h3>Add Money</h3>
                    <input
                        type={"number"}
                        placeholder={'amount'}
                        onChange={event => setAmount(event.currentTarget.value)}
                        value={amount}
                    />
                    <Button text={'Transfer'} callback={() => setIsTransferring(true)}/>
                </div>
            </Content>
            <Logout>
                <a href={"/profile"}><button type="submit" onClick={() => {localStorage.setItem("logged", "false"); localStorage.removeItem("username")}}>Sign out</button></a>
            </Logout>
        </Wrapper>
    )
};

export default UserProfile