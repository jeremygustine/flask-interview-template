from injector import singleton
from NotebookDatabase import NotebookDatabase
from NotebookService import NotebookService


def configure(binder):
    binder.bind(NotebookService, to=NotebookService, scope=singleton)
    binder.bind(NotebookDatabase, to=NotebookDatabase, scope=singleton)
