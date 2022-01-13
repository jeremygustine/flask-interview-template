class NotebookDatabase:
    def __init__(self):
        self.notebook_db = []

    def insert(self, notebook):
        entity = {
            'id': len(self.notebook_db) + 1,
            'title': notebook['title']
        }
        self.notebook_db.append(entity)
        return entity
