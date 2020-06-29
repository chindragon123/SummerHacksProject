import React, {Component} from "react";
import {GridList, GridListTile, Card} from "@material-ui/core"
import SearchResult from "./SearchResult";
import PlaceHolder from "./PlaceHolder";

export default class SearchResultList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            results: []
        }
    }

    render() {
        let toRet;
        if (!this.state.results.length) {
            toRet = <PlaceHolder/>
        } else {
            const resultItems = this.state.results.map((result) =>
                <GridListTile>{result}</GridListTile>
            )
            toRet = resultItems
        }
        return (
            <GridList cellHeight={160} cols={1} style={{justifyContent: "center"}}>
                {toRet}
            </GridList>
        );
    }

}