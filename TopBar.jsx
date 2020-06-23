import React, {Component} from "react";
import AppBar from "@material-ui/core/AppBar";
import {IconButton, Toolbar, Typography, InputBase} from "@material-ui/core";
import {ArrowForwardIos, Search, AccountCircle} from "@material-ui/icons"
import {ActionAccountCircle} from "material-ui/svg-icons/index.es";
import {orange} from "@material-ui/core/colors";


export default class TopBar extends Component {
    render() {
        return (
            <div>
                <AppBar color="orange">
                    <Toolbar>
                        <IconButton edge="start" className="menuButton" color="inherit" aria-label="menu">
                            <ArrowForwardIos/>
                        </IconButton>
                        <Typography style={styles.title} variant="h6">ClassFinder</Typography>
                        <div style={styles.searchBar} className="searchBar">
                            <Search/>
                            <InputBase style={{width: "100%"}} aria-colindex={10}
                                       placeholder="What are you interested in?"/>
                        </div>
                        <IconButton edge="right">
                            <AccountCircle/>
                        </IconButton>
                    </Toolbar>
                </AppBar>
            </div>
        );
    }
}

const styles = {
    menuButton: {
        marginRight: 10
    },
    title: {
        marginRight: 10
    },
    searchBar: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        position: "relative",
        flexGrow: 1,
        width: "100%",
    }
}