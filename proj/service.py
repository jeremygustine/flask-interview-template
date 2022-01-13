
from injector import inject

from proj.database import NotebookDatabase


class NotebookService:

    @inject
    def __init__(self, db: NotebookDatabase):
        self.db = db

    def insert_notebook(self, notebook):
        return self.db.insert(notebook)

    def get_all_notebooks(self):
        return self.db.get_all()

    def get_notebook_by_id(self, id):
        #TODO call get on the db object and provide the id
        pass