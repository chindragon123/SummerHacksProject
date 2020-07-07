from flask import Flask
from markupsafe import escape

import pysolr

app = Flask(__name__)

solr = None


@app.route("/search/<query>")
def parse_query(query):
    assert solr is not None, "Solr instance need to be available"
    solr.search(query)


if __name__ == '__main__':
    # Connect to Solr
    global solr
    # TODO add HTTPS support
    solr = pysolr.Solr("http://localhost:8983/solr", always_commit=True)
    app.run(debug=1, port=42069, host="0.0.0.0")
