import pytest
from flask import Flask, request
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_post_notebook(client):
    test_book_title = 'my testing book title'
    response = client.post('/notebooks', json={
        'title': 'my testing book title'
    })
    assert response.status_code == 201
    assert response.get_json()['title'] == test_book_title
