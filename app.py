from flask import Flask, jsonify
import json
import requests

app = Flask(__name__)

@app.route("/docs")
def testRoute():
    content = "<h1>This will be the internal docs for the API</h1>"
    return  content

@app.route("/jobs", methods=['GET'])
def getJobs():
    try:
        url = "https://jsearch.p.rapidapi.com/search"
        querystring = {"query":"Python developer in Texas, USA","page":"1","num_pages":"1"}
        headers = {
            "X-RapidAPI-Key": "265d17cc4dmsh63aa91656fc0546p13b5b7jsne954c82ce26a",
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        return response.json()
    except:
        return jsonify({"status": 0, "message": "Get Request failed"})




app.run()
