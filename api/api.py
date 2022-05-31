from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
client = MongoClient('mongodb://mongodb:27017/')
db = client.test_database

@app.route('/', methods = ['GET'])
def index():
    listStudents = db.students.find()

    item = {}
    data = []
    for element in listStudents:
        item = {
            'id': str(element['_id']),
            'name': str(element['name']),
            'birth': str(element['birth']),
            'university': str(element['university']),
            'major': str(element['major'])
        }
        data.append(item)

    return jsonify(
        data
    )

@app.route('/student', methods = ['POST'])
def student():
    student = request.json
    db.students.insert_one(student)

    return 'Saved!', 201