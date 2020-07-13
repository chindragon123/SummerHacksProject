import React, {Component} from "react";
import {Card, CardContent, Typography} from "@material-ui/core";
import {Link} from "react-router-dom"
import {EditorMergeType} from "material-ui/svg-icons/index.es";

export default class SearchResult extends Component {
    constructor(props) {
        super(props)
        this.props = props
    }

    render() {
        return (
            <Card variant={"outlined"}>
                <CardContent>
                    <Typography variant={"h5"} style={{display: "inline-block", marginRight: "1%"}}>
                        {/* Append the syllabus  */}
                        <a href={`https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/download/${this.props.data.syllabus_id}`}
                           target={"_blank"} rel={"noopener noreferrer"}>{this.props.data.course_title}</a>
                    </Typography>
                    <Typography style={{
                        display: "inline-block",
                        marginRight: 10
                    }}>{this.props.data.course_letter_and_number} </Typography>
                    <Typography color="textSecondary"
                                style={{display: "inline-block"}}>{`${this.props.data.semester} ${this.props.data.year}`}</Typography>
                    <Typography color="textPrimary">{this.props.data.instructor_name}</Typography>
                    <Typography variant={"body2"}>
                        Description? (Like how google does it?)
                    </Typography>
                    <Typography variant="h5">
                        Keywords?
                    </Typography>
                </CardContent>
            </Card>
        );
    }
}