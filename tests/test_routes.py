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


# class AlbumRouteTests(unittest.TestCase):
#     def setup(self):
#         app.config["TESTING"] = True
#         app.config["WTF_CSRF_ENABLED"] = False
#         app.config["DEBUG"] = False

#         self.app = app.test_client()
#         print(setup)
#         self.assertEqual(app.debug, False)

#     def tearDown(self):
#         pass
#         return super().tearDown()
    

#     ##################
#     ## Album Routes ##
#     ##################

#     def test_show_main(self):
#         response = self.app.get('/albums', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)

#     def test_show_alt(self):
#         response = self.app.get('/albums/show', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)

#     def test_update(self):
#         response = self.app.get('/albums/edit', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)

#     def test_new(self):
#         response = self.app.get('/albums/new')
#         self.assertEqual(response.status_code, 200)

#     def test_delete(self):
#         response = self.app.get('/albums/delete', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)