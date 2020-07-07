import React, {Component} from "react";
import {Card, CardContent, Typography} from "@material-ui/core";
import {Link} from "react-router-dom"
import {EditorMergeType} from "material-ui/svg-icons/index.es";

export default class SearchResult extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Card variant={"outlined"}>
                <CardContent>
                    <Typography variant={"h5"} style={{display: "inline-block", marginRight: "1%"}}>
                        <a href={"https://www.google.com"} target={"_blank"} rel={"noopener noreferrer"}>Class Name</a>
                    </Typography>
                    <Typography style={{display: "inline-block"}}>CS 439</Typography>
                    <Typography color="textSecondary">Summer 2020</Typography>
                    <Typography variant={"body2"}>
                        This class is somewhat hard, equal to 50 hour workweeks
                    </Typography>
                </CardContent>
            </Card>
        );
    }
}