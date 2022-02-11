import API from "../../Api"
import {Wrapper, Content, Block, ContentRegister, Container} from "./Login.styles";
import {useEffect, useState} from "react";
import MoreButton from "../MoreButton";
import { useLogin } from "../../hooks/useLogin"
import {useRegister} from "../../hooks/useRegister";

const Login = () => {
    const { setIsLogging, username, setUsername, password, setPassword } = useLogin();
    const { setIsRegistering, RUsername, setRUsername, RPassword, setRPassword, email, setEmail, firstName, setFirstName, lastName, setLastName, phoneNumber, setPhoneNumber} = useRegister();
    return (
        <Wrapper>
            <Content>
                <h1>Sign in!</h1>
                <Block>
                    <input
                        type={"text"}
                        placeholder={'username'}
                        onChange={event => setUsername(event.currentTarget.value)}
                        value={username}
                    />
                    <input
                        type={"password"}
                        placeholder={'password'}
                        onChange={event => setPassword(event.currentTarget.value)}
                        value={password}
                    />
                    <MoreButton text={'Sign in'} callback={() => setIsLogging(true)}/>
                </Block>
            </Content>
            <ContentRegister>
                <h1>Sign up!</h1>
                <Block>
                <input
                    type={"text"}
                    placeholder={'username'}
                    onChange={event => setRUsername(event.currentTarget.value)}
                    value={RUsername}
                />
                <input
                    type={"password"}
                    placeholder={'password'}
                    onChange={event => setRPassword(event.currentTarget.value)}
                    value={RPassword}
                />
                <input
                    type={"text"}
                    placeholder={'email'}
                    onChange={event => setEmail(event.currentTarget.value)}
                    value={email}
                />
                <input
                    type={"text"}
                    placeholder={'first name'}
                    onChange={event => setFirstName(event.currentTarget.value)}
                    value={firstName}
                />
                <input
                    type={"text"}
                    placeholder={'last name'}
                    onChange={event => setLastName(event.currentTarget.value)}
                    value={lastName}
                />
                <input
                    type={"number"}
                    placeholder={'phone number'}
                    onChange={event => setPhoneNumber(event.currentTarget.value)}
                    value={phoneNumber}
                />
                <MoreButton text={'Sign Up'} callback={() => setIsRegistering(true)}/>
                </Block>
            </ContentRegister>
        </Wrapper>
    )
}

export default Login