import json


class Syllabus:
    def __init__(self, pdf_path, text_path):
        self.pdf_path = pdf_path
        self.text_path = text_path

    def extract(self):
        # TODO All the the NLP work goes here
        self.class_title = None  # Data Structures
        self.course_number = None  # CS 314
        self.unique_number = None  # 510225
        self.instructor_name = None  # Calvin Lin

    def to_json(self):
        """
        Create a JSON object that can be returned and then rendered by frontend
        :return:
        """
