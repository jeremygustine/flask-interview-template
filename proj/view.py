from flask import request, jsonify
import sys
from proj.service import NotebookService


def insert_notebook(service: NotebookService):
    # TODO validate title is present in request
    notebook = request.json
    print(f'Received request: {notebook}', file=sys.stdout)
    inserted_notebook = service.insert_notebook(notebook)
    return jsonify(inserted_notebook), 201


def get_all_notebooks(service: NotebookService):
    print(f'Path is: {request.path}', file=sys.stdout)
    notebooks = service.get_all_notebooks()
    return jsonify(notebooks), 200


def get_notebook_by_id(id):
    print(f'Id: {id}', file=sys.stdout)
    # TODO return a single jsonified-notebook object
    return jsonify({}), 200
