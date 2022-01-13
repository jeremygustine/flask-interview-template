
from injector import inject

from NotebookDatabase import NotebookDatabase


class NotebookService:

    @inject
    def __init__(self, db: NotebookDatabase):
        self.db = db

    def insert_notebook(self, notebook):
        return self.db.insert(notebook)