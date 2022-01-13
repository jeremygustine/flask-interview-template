from proj.service import NotebookService
from pytest_mock import MockerFixture


def test_insert_notebook(mocker):
    mock_db = mocker.Mock()
    mocker.patch.object(mock_db, 'insert', return_value='inserted notebook')
    subject = NotebookService(mock_db)

    notebook = {'title': 'test book'}
    result = subject.insert_notebook(notebook)
    assert result == 'inserted notebook'
