import React, {Component, ReactFragment} from "react";
import TopBar from "./TopBar";
import SearchResultList from "./SearchResultList";

export default class HomePage extends Component {
    render() {
        return (
            <div style={{flexDirection:"column", align:"center"}}>
                <TopBar style={{marginBottom:500}}/>
                <h1>UwU</h1>
                <SearchResultList/>
            </div>
        )
    }
}
