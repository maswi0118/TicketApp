import React , {Component} from "react";
import {BarItem, Bar, MenuBar, MenuBarItem} from "./Menu.styles";
import { Wrapper } from "../Header/Header.styles";
import MenuItems from "./MenuItems";
import Bars from '../../images/menu_bar.png';
import X from '../../images/x_menu.png';

class Menu extends Component {
    state = {clicked: true}

    handleClick = () => {
        this.setState({clicked: !this.state.clicked})
    }

    render() {
        return (
            <nav className="NavbarItems">
                <Bar className={this.state.clicked ? 'nav-menu active' : 'nav-menu'}>
                    <MenuBar onClick={this.handleClick}>
                        <img src={this.state.clicked ? Bars : X}/>
                        {this.state.clicked ?
                            <></> :
                            MenuItems.map((item, index) => {
                                return(
                                    <li key={index}>
                                        <MenuBarItem className={item.cName} href={item.url}>
                                            {item.title}
                                        </MenuBarItem>
                                    </li>
                                )
                            })
                        }
                    </MenuBar>
                    {MenuItems.map((item, index) => {
                        return(
                            <li key={index}>
                                <BarItem className={item.cName} href={item.url}>
                                    {item.title}
                                </BarItem>
                            </li>
                        )
                    })}
                </Bar>
            </nav>
        )
    }
};


export default Menu;