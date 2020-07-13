import React, {Component} from "react";
import AppBar from "@material-ui/core/AppBar";
import {IconButton, Toolbar, Typography, InputBase} from "@material-ui/core";
import {ArrowForwardIos, Search, AccountCircle} from "@material-ui/icons"
import {ActionAccountCircle} from "material-ui/svg-icons/index.es";
import {orange} from "@material-ui/core/colors";


export default class TopBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            query: ""
        }
    }

    handleQuery = (keypress) => {
        if (keypress.key === "Enter") {
            console.log("Enter pressed?")
            console.log(this.state.query)
            let url = "http://192.168.1.139:42069/search/" + encodeURIComponent(this.state.query)
            console.log(`Fetching URL: ${url}`)
            fetch(url,
                {mode: "cors"})
                .then(res => res.json())
                .then(
                    (result) => {
                        console.log("Ok")
                        // TODO Set search results
                        console.log(result)
                        this.props.onSearch(result)
                    },
                    (error) => {
                        console.log("Error")
                        //Handle error
                        console.error(error)
                    }
                )
        } else {
            // Nothing much to do I guess :/
        }

    }

    handleOnChange = (query) => {
        // console.log(query.target.value)
        this.setState({query: query.target.value})
    }

    render() {
        return (
            <div style={{height: 0}}>
                <AppBar color="default">
                    <Toolbar>
                        <IconButton edge="start" className="menuButton" color="inherit" aria-label="menu">
                            <ArrowForwardIos/>
                        </IconButton>
                        <Typography style={styles.title} variant="h6">ClassFinder</Typography>
                        <div style={styles.searchBar} className="searchBar">
                            <Search/>
                            <InputBase onKeyPress={this.handleQuery} onSubmit={this.handleQuery}
                                       onChange={this.handleOnChange} style={{width: "100%"}} aria-colindex={10}
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