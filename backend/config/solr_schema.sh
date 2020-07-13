#!/bin/bash
curl "http://localhost:8983/solr/syllabi/update/json/docs"\
"?split=/classes"\
"&f=semester:/classes/semester"\
"&f=course_letter:/classes/course_letter"\
"&f=course_number:/classes/course_number"\
"&f=course_title:/classes/course_title"\
"&f=unique_number:/classes/unique_number"\
"&f=instructor_name:/classes/instructor_name"\
"&f=id:/classes/id"\
"&f=year:/classes/year"\
"&f=course_letter_and_number:/classes/course_letter_and_number"\
"&f=instructor_first_name:/classes/instructor_first_name"\
"&f=instructor_last_name:/classes/instructor_last_name"\
"&f=syllabus_text:/classes/syllabus_text"\
-H "Content-type:application/json" \
-d courses.json