import React, {Component} from "react";
import {GridList, GridListTile} from "@material-ui/core"
import SearchResult from "./SearchResult";
import PlaceHolder from "./PlaceHolder";

export default class SearchResultList extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        let toRet;
        console.log(`SearchResultList results= ${this.props.results}`)
        if (this.props.results == null) {
            toRet = <PlaceHolder/>
        } else {
            let docs = this.props.results.docs;
            console.log(docs[0])
            toRet = docs.map((result) =>
                <GridListTile style={{width: "100%"}}>
                    <SearchResult class_title="Computer Arch" data={result}/>
                </GridListTile>
            )
        }
        return (
            <GridList style={{justifyContent: "center", width: "100%"}}>
                {toRet}
            </GridList>
        );
    }

}