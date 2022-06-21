from flask import Flask
from flask import request, jsonify
from faker import Faker
import csv
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Start page'


@app.route('/requirements/', methods=['GET'])
def requirements():
    with open('requirements.txt', 'r+') as file_to_read:
        data_req = file_to_read.read()
    return data_req


@app.route('/generate-users/', methods=['GET'])
def generate_users():
    page = request.args.get('count', default=100)
    new_list = []
    fake = Faker(['it_IT', 'en_US'])
    for i in range(page):
        new_list.append(fake.email())
        new_list.append(fake.unique.first_name())
    return jsonify(new_list)


@app.route('/mean/', methods=['GET'])
def mean():
    with open('hw.csv', newline='') as fin:
        reader = csv.DictReader(fin)
        count = 0
        sum_height = 0
        sum_weight = 0
        for row in reader:
            count += 1
            sum_height += float(row[' "Height(Inches)"'])
            sum_weight += float(row[' "Weight(Pounds)"'])
        aver_height = (sum_height / count) * 2.54
        aver_weight = (sum_weight / count) * 0.45
    return jsonify('Average height:', aver_height, 'Average weight: ', aver_weight)

@app.route('/space/', methods=['GET'])
def space_e():
    r = requests.get('http://api.open-notify.org/astros.json')
    i = r.json()["number"]
    return jsonify('Number of astronauts:', i)
