from flask import request, jsonify
import sys
from proj.service import NotebookService


def insert_notebook(service: NotebookService):
    # TODO validate title is present in request
    notebook = request.json
    print(f'Received request: {notebook}', file=sys.stdout)
    inserted_notebook = service.insert_notebook(notebook)
    return jsonify(inserted_notebook), 201
