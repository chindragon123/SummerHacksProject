"""
Summarize text to go into the description field of a search result
"""

from transformers import pipeline
import json

if __name__ == '__main__':
    summarizer = pipeline(task="summarization")
    with open("courses.json") as f:
        syllabus_data = json.load(f)

    print(type(syllabus_data))
    to_summarize = syllabus_data[0]["syllabus_text"]
    print(to_summarize)

    print(f"Summary: {summarizer(to_summarize)}")
