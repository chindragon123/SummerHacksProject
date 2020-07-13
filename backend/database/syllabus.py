import json


class Syllabus:
    def __init__(self, pdf_path, text_path):
        self.pdf_path = pdf_path
        self.text_path = text_path

        # Things to index
        self.fields = {
            # Basic stuff
            "class_title": None,  # Data Structures
            "course_number": None,  # CS 314H
            "unique_number": None,  # 51090
            "instructor_name": None,  # Calvin Lin
            "semester": None,  # Fall
            "year": None,  # 2019
            "days": None,  # MWF
        }

    @staticmethod
    def from_pdf(self):
        # TODO All the the NLP work goes here
        pass

    def from_json(self, json_obj):
        for key in self.fields.keys():
            self.fields[key] = json_obj[key]

    def to_json(self):
        """
        Meant to be called by fetch API

        Create a JSON object that can be returned and then rendered by frontend
        :return:
        """
        result = {
            "file_loc": self.pdf_path,
        }
        result.update(self.fields)

        return result
