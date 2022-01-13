from injector import singleton
from proj.database import NotebookDatabase
from proj.service import NotebookService


def configure(binder):
    binder.bind(NotebookService, to=NotebookService, scope=singleton)
    binder.bind(NotebookDatabase, to=NotebookDatabase, scope=singleton)
