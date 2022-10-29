
from flask import Flask ,jsonify,request


app = Flask(__name__)

tasks = [{"id":1,"title":"python","description":"learning","done":False}]

@app.route("/add-data",methods=['POST'])
def add_task():
  if not request.json:
    return jsonify({
        "status":"error",
        "message":"please provide the data"
    },400)

contact = {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json ['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False    
}