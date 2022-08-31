from proj.service import NotebookDatabase


def test_insert():
    subject = NotebookDatabase()
    assert len(subject.notebook_db) == 0
    result = subject.insert({'title': 'test notebook'})
    assert len(subject.notebook_db) == 1
    assert result == {'id': 1, 'title': 'test notebook'}

# TODO get_all_notebooks
# TODO get_notebook_by_id
# TODO update notebook title
# TODO delete notebook
# TODO add validation