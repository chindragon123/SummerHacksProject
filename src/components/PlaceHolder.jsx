import React, {Component} from "react";
import {Card, CardContent, Typography} from "@material-ui/core";

export default class PlaceHolder extends Component {
    /**
     * Placeholder to show before user types in query
     */
    constructor(props) {
        super(props);
    }

    render() {

        return (
            <Card>
                <CardContent>
                    <Typography color="textSecondary" style={{justifyContent:"center"}}>
                        Execute a query!
                    </Typography>
                </CardContent>
            </Card>
        )

    }
}