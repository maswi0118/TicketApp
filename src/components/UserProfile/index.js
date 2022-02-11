import React from 'react'
import {Wrapper, Content, Logout} from './UserProfile.styles'
import Button from "../Button";
import {useAddMoney} from "../../hooks/useAddMoney";
import {useBalance} from "../../hooks/useBalance";
import Grid from "../Grid";

function UserProfile() {
    const { setIsTransferring, amount, setAmount } = useAddMoney()
    const { state } = useBalance()

    return (
        <Wrapper>
            <Grid header={""}>
                <Content>
                    <h1>Your Profile</h1>
                </Content>
                <Content>
                    <div>
                        <h2>Welcome {localStorage.getItem("username")}!</h2>
                        <h5>email Address: {state.email}</h5>
                        <h5>Phone Number: {state.phone}</h5>
                    </div>
                </Content>
                <Content>
                    <div class>
                        <h3>Add Money</h3>
                        <h5>Balance: {state.balance} PLN</h5>
                        <input
                            type={"number"}
                            placeholder={'amount'}
                            onChange={event => setAmount(event.currentTarget.value)}
                            value={amount}
                        />
                        <Button text={'Transfer'} callback={() => setIsTransferring(true)}/>
                    </div>
                </Content>
                <Content>
                    <Logout>
                        <a href={"/profile"}><button type="submit" onClick={() => {localStorage.setItem("logged", "false"); localStorage.removeItem("username")}}>Sign out</button></a>
                    </Logout>
                </Content>
            </Grid>
        </Wrapper>
    )
};

export default UserProfile