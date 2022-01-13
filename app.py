from flask import Flask, request, jsonify
from flask_injector import FlaskInjector
from injector import inject

from NotebookService import NotebookService
from dependencies import configure

app = Flask(__name__)


@inject
@app.route('/data')
def get_data(service: NotebookService):
    print(f"MyService instance is {service}")  # We want to see the object that gets created
    return service.get_data()


@app.route('/notebooks/', methods=['POST'])
def insert_notebook(service: NotebookService):
    data = request.json
    return jsonify(data)


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])