from flask import Flask, request, jsonify
from flask_injector import FlaskInjector
from injector import inject
import sys
from proj import view
from dependencies import configure

app = Flask(__name__)

app.add_url_rule('/notebooks', view_func=view.insert_notebook, methods=['POST'])

# TODO get_all_notebooks
# TODO get_notebook_by_id
# TODO update notebook title
# TODO add validation

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])
