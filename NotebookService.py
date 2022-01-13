
from injector import inject

from NotebookDatabase import NotebookDatabase


class NotebookService:
    @inject
    def __init__(self, db: NotebookDatabase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def insert_notebook(self, notebook):
        self.db.insert(notebook)