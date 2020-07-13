"""
Sends a requests to update the schema in solr
"""
import requests

core_url = "http://localhost:8983/solr/syllabi"

if __name__ == '__main__':
    headers = {"content-type": "application/json"}
    with open("backend/config/syllabi_schema.json") as f:
        json_text = f.read()

    response = requests.post(f"{core_url}/schema", headers=headers, data=f"'{json_text}'")
    print(response)
    print(response.content)
