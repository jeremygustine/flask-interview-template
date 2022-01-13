
from injector import inject

from proj.database import NotebookDatabase


class NotebookService:

    @inject
    def __init__(self, db: NotebookDatabase):
        self.db = db

    def insert_notebook(self, notebook):
        return self.db.insert(notebook)