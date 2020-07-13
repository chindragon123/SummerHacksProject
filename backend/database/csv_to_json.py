"""
Create a list of JSON objects that can be imported directly into SOLR
"""
import os
import json

import pandas as pd

if __name__ == '__main__':
    courses_info = pd.read_csv("courses.csv")
    print(courses_info)

    # Need to clean out malformed rows
    courses_info = courses_info[courses_info["instructor_name"].str.contains(",")]


    def get_text(id):
        text_file = f"./syllabi_text/syllabus_{id}.txt"
        if not os.path.exists(text_file):
            return ""
        with open(text_file) as f:
            return f.read()


    def split_year_sem(year_sem):
        year = year_sem.split(",")[0].strip()
        sem = year_sem.split(",")[1].strip()
        return year, sem


    def split_instructor_name(instructor_full):
        assert "," in instructor_full, instructor_full
        last, first = instructor_full.split(",")
        return first.strip(), last.strip()


    year_sem_split = courses_info["semester"].apply(split_year_sem)
    courses_info["semester"] = [sem for year, sem in year_sem_split]
    courses_info["year"] = [year for year, sem in year_sem_split]

    courses_info["course_letter_and_number"] = courses_info["course_letter"] + " " + courses_info["course_number"]

    instructors_first_last = courses_info["instructor_name"].apply(split_instructor_name)
    courses_info["instructor_first_name"] = [first for first, last in instructors_first_last]
    courses_info["instructor_last_name"] = [last for first, last in instructors_first_last]

    courses_info["syllabus_text"] = courses_info["id"].astype("int").apply(get_text)

    # id is a key thing for solr... so we're going to have to rename our id
    courses_info["syllabus_id"] = courses_info["id"]

    courses_info = courses_info.drop(columns=["id"])

    print(courses_info)
    print(courses_info.columns)

    courses_info = courses_info.astype({
        "semester": "str",
        "course_letter": "str",
        "course_number": "str",
        "course_title": "str",
        "unique_number": "int",
        "instructor_name": "str",
        "syllabus_id": "int",
        "year": "int",
        "course_letter_and_number": "str",
        "instructor_first_name": "str",
        "instructor_last_name": "str",
        "syllabus_text": "str"
    })

    classes = courses_info.to_json("courses.json", orient="records")
