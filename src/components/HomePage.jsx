import React, {Component, ReactFragment, useState} from "react";
import TopBar from "./TopBar";
import SearchResultList from "./SearchResultList";
import SearchResult from "./SearchResult";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            search_results: null
        }
    }

    setSearchResults = (documents) => {
        console.log("Setting search")
        let response = documents.response
        console.log(response)
        this.setState({
            search_results: response
        })
    }

    render() {
        return (
            <div style={{
                width: "100%",
                display: "inline-block",
                flexDirection: "row",
                alignItems: "center",
                justifyContent: "center"
            }}>
                <TopBar onSearch={this.setSearchResults} setSearchResults={this.setSearchResults}/>
                <SearchResultList results={this.state.search_results}/>
            </div>
        )
    }
}
