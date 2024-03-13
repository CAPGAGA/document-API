import httpx
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from app import app
from httpx import AsyncClient
from typing import Generator
import time
import os

self_url = os.getenv('LOCAL_ADDRESS', None)
if self_url is None:
    self_url = 'http://127.0.0.1:8000'



# client = TestClient(app)
# import unittest

# pytest_plugins = ('pytest_asyncio',)
# @pytest_asyncio.fixture()
# async def async_client() -> Generator:
#
#     async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as client:
#
#         yield client

# class CreateEditTest(unittest.IsolatedAsyncioTestCase):
#     async def test_user_create(self):
#         async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
#             response = await ac.post('/user/', json={"email": "test@mail.com", "password": "testpass"})
#         self.assertEqual(200, response.status_code)
#         data = response.json()
#         self.assertEqual('test@mail.com', data.get('user').get('email'))
#         self.assertEqual('testpass' + 'yeahhased', data.get('user').get('hashed_password'))
#
#     async def test_get_user(self):
#         async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
#             response = await ac.get('/user/test@mail.com/testpass')
#         self.assertEqual(200, response.status_code)
#         data = response.json()
#         self.assertEqual('test@mail.com', data.get('email'))
#         self.assertEqual('testpass' + 'yeahhased', data.get('hashed_password'))

# @pytest.mark.asyncio
# async def test_create_user(async_client: AsyncClient):
#     # async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
#     print(async_client)
#     response = await async_client.post('/user/', json={"email": "test@mail.com", "password": "testpass"})
#
# @pytest.mark.asyncio
# async def test_get_user(async_client: AsyncClient):
#     # async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
#     print(async_client)
#     time.sleep(5)
#     response = await async_client.get('/user/test@mail.com/testpass')


# def test_register_user():
#     response = client.post('/user/', json={'email':'test@mail.com','password':'testpass'})
#     assert response.status_code == 200
#     data = response.json()
#     assert data.get('email') == 'test@mail.com'
#     assert data.get('hashed_password') == 'testpass' + 'yeahhased'
#     # return data.get('user_token')
# #
# def test_get_user():
#     response = client.get('/user/token/vPWEhIQzDjTkhryk')
#     assert response.status_code == 200
#     data = response.json()
#     assert data.get('email') == 'test@mail.com'
#     assert data.get('hashed_password') == 'testpass' + 'yeahhased'
    # return data.get('user_token')

# @pytest.mark.asyncio
# async def test_create_user():
#     async with AsyncClient(transport=httpx.ASGITransport(app), base_url='http://127.0.0.1:8000') as ac:
#         response = await ac.post('/user/', json={"email": "test@mail.com", "password": "testpass"})
#     assert response.status_code == 200
#     data = response.json()
#     assert data.get('user').get('email') == 'test@mail.com'
#     assert data.get('user').get('hashed_password') == 'testpass' + 'yeahhased'
#
# @pytest.mark.asyncio
# async def test_get_user():
#     async with AsyncClient(transport=httpx.ASGITransport(app), base_url='http://127.0.0.1:8000') as ac:
#         response = await ac.get('/user/mail/test@mail.com/testpass')
#     assert response.status_code == 200
#     data = response.json()
#     assert data.get('email') == 'test@mail.com'
#     assert data.get('hashed_password') == 'testpass' + 'yeahhased'
#
# @pytest_asyncio.fixture()
# async def get_user_token():
#     async with AsyncClient(transport=httpx.ASGITransport(app), base_url='http://127.0.0.1:8000') as ac:
#         response = await ac.get('/user/mail/test@mail.com/testpass')
#     assert response.status_code == 200
#     data = response.json()
#     assert data.get('email') == 'test@mail.com'
#     assert data.get('hashed_password') == 'testpass' + 'yeahhased'
#     return data.get('user_token')
#
# @pytest.mark.asyncio
# async def test_create_document(get_user_token):
#     print(get_user_token)
#     async with AsyncClient(transport=httpx.ASGITransport(app), base_url='http://127.0.0.1:8000') as ac:
#         response = await ac.post(f'/documents/{get_user_token}', json={"title": "test_title", "contents": "test_contents"})
#     assert response.status_code == 201
#     data = response.json()
#     print(data)
#     assert data.get('title') == 'test_title'
#     assert data.get('contents') == 'test_contents'



# def test_edit_document(test_create_user, test_create_document):
#     print(test_create_document)
#     response = client.put(f'/documents/', json={"title": "edit_title", "contents": "edit_contents", 'document_id': ValueStorage.dock_id, 'user_token': ValueStorage.token})
#     assert response.status_code == 201
#     data = response.json()
#     assert data.get('document_id') == test_create_document
#     assert data.get('user_token') == test_create_user
#     assert data.get('title') == 'edit_title'
#     assert data.get('contents') == 'edit_contents'

import requests

def test_create_user():
    r = requests.post(f'{self_url}/user/', json={"email": "test@mail.com", "password": "testpass"})
    assert r.status_code == 200
    data = r.json()
    assert data.get('user').get('email') == 'test@mail.com'
    assert data.get('user').get('hashed_password') == 'testpass' + 'yeahhased'

def test_get_user():
    r = requests.get(f'{self_url}/user/mail/test@mail.com/testpass')
    assert r.status_code == 200
    data = r.json()
    assert data.get('email') == 'test@mail.com'
    assert data.get('hashed_password') == 'testpass' + 'yeahhased'

@pytest.fixture()
def get_user_token():
    r = requests.get(f'{self_url}/user/mail/test@mail.com/testpass')
    assert r.status_code == 200
    data = r.json()
    assert data.get('email') == 'test@mail.com'
    assert data.get('hashed_password') == 'testpass' + 'yeahhased'
    return data.get('user_token')

def test_create_document(get_user_token):
    r = requests.post(f'{self_url}/documents/{get_user_token}', json={"title": "test_title", "contents": "test_contents"})
    assert r.status_code == 201
    data = r.json()
    assert data.get('title') == 'test_title'
    assert data.get('contents') == 'test_contents'

@pytest.fixture()
def get_user_document(get_user_token):
    r = requests.get(f'{self_url}/documents/{get_user_token}')
    assert r.status_code == 200
    data = r.json()
    assert data[-1].get('title') in ('test_title', 'edit_title')
    assert data[-1].get('contents') in ('test_contents', 'edit_contents')
    return data[-1].get('id')

def test_edit_document(get_user_token, get_user_document):
    r = requests.put(f'{self_url}/documents/', json={"title": "edit_title", "contents": "edit_contents", 'user_token': get_user_token, 'document_id': get_user_document})
    assert r.status_code == 201
    data = r.json()
    print(data)
    assert data.get('title') == 'edit_title'
    assert data.get('contents') == 'edit_contents'

def test_delete_document(get_user_token, get_user_document):
    r = requests.delete(f'{self_url}/documents/', json={'user_token': get_user_token, 'document_id': get_user_document})
    assert r.status_code == 204

def test_delete_user(get_user_token):
    r = requests.delete(f'{self_url}/user/', json={'user_token': get_user_token})
    assert r.status_code == 200