import React from 'react'
import { Wrapper, Content } from './Login.styles'

class Login extends React.Component {

    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
        localStorage.setItem("logged", "true");
        console.log(localStorage.getItem("logged"))
        event.preventDefault();
  }

  render() {
        console.log(localStorage.getItem("logged"))
        return (
            <Wrapper>
                <Content>
                    <a>zalogowany?: nie</a>
                    <form action="http://127.0.0.1:5000/auth/login" method="POST" onSubmit={this.handleSubmit}>
                        <input type="text" name="username"/>
                        <input type="text" name="password"/>
                        <input type="submit" value="Sign in"/>
                    </form>
                </Content>
                <Content>
                    <a>zalogowany?: nie</a>
                    <a href={"/profile"}>
                        <button type="submit" onClick={
                            () => {
                                localStorage.setItem("logged", "true")
                            }}>
                            zarejestruj
                        </button>
                    </a>
                </Content>
            </Wrapper>
        )
    }
};

export default Login