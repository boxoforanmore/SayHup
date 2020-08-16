import os
import sys
import tempfile
import unittest
import pytest

sys.path.append("./../")

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

#################
## Error Pages ##
#################
def test_404_page(client):
    rv = client.get('/404')
    assert rv.status_code == 404

def test_401_page(client):
    rv = client.get('/401')
    assert rv.status_code == 404


##################
## Landing Page ##
##################
def test_landing_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_landing_page_as_index(client):
    rv = client.get('/index')
    assert rv.status_code == 200

def test_landing_page_as_home(client):
    rv = client.get('/home')
    assert rv.status_code == 200


#################
## Album Pages ##
#################
def test_albums_show(client):
    rv = client.get('/albums')
    assert rv.status_code == 200

def test_albums_show_as_show(client):
    rv = client.get('/albums/show')
    assert rv.status_code == 200

def test_albums_update(client):
    rv = client.get('/albums/create')
    assert rv.status_code == 200

def test_albums_update(client):
    rv = client.get('/albums/update')
    assert rv.status_code == 200

def test_albums_delete(client):
    rv = client.get('/albums/delete')
    assert rv.status_code == 200