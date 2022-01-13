from flask import Flask, request, jsonify
from flask_injector import FlaskInjector
from injector import inject
import sys

from NotebookService import NotebookService
from dependencies import configure

app = Flask(__name__)


@app.route('/notebooks/', methods=['POST'])
def insert_notebook(service: NotebookService):
    # TODO validate title is present in request
    notebook = request.json
    print(f'Received request: {notebook}', file=sys.stdout)
    inserted_notebook = service.insert_notebook(notebook)
    return jsonify(inserted_notebook), 201


# TODO get_all_notebooks
# TODO get_notebook_by_id
# TODO update notebook title
# TODO add validation

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])