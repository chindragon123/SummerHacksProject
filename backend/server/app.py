from flask_cors import CORS
from flask import Flask
from markupsafe import escape
import requests
import urllib3
import pysolr

app = Flask(__name__)
cors = CORS(app)

solr = None


@app.route("/search/<query>")
def parse_query(query):
    payload = {
        "df": "syllabus_text",
        "q": query
    }
    res = requests.get("http://localhost:8983/solr/syllabi/select", params=payload)
    return res.json()


if __name__ == '__main__':
    # Connect to Solr
    # global solr
    # TODO add HTTPS support
    # solr = pysolr.Solr("http://localhost:8983/solr", always_commit=True)
    app.run(debug=1, port=42069, host="0.0.0.0")
