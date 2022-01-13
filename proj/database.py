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

    def get_all(self):
        return self.notebook_db

    def get(self, id):
        for notebook in self.notebook_db:
            if id == notebook['id']:
                return notebook
            else:
                return None





