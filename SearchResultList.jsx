import React, {Component} from "react";
import {GridList, GridListTile, Card} from "@material-ui/core"
import SearchResult from "./SearchResult";

export default class SearchResultList extends Component {
    state = {
        results: []
    }

    render() {
        return (
            <GridList cellHeight={160} cols={1}>
                <GridListTile>
                    <Card>Hi</Card>
                </GridListTile>
                <GridListTile>
                    <Card>Bye</Card>
                </GridListTile>
            </GridList>
        );
    }

}