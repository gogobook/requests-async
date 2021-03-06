import asyncio
import requests_async
import pytest


@pytest.mark.asyncio
async def test_get(server):
    url = "http://127.0.0.1:8000/"
    response = await requests_async.get(url)
    assert response.status_code == 200
    assert response.json() == {"method": "GET", "url": url, "body": ""}


@pytest.mark.asyncio
async def test_get_queryparams(server):
    url = "http://127.0.0.1:8000/"
    response = await requests_async.get(url, params={"a": "b"})
    assert response.status_code == 200
    assert response.json() == {"method": "GET", "url": url + "?a=b", "body": ""}


@pytest.mark.asyncio
async def test_head(server):
    url = "http://127.0.0.1:8000/"
    response = await requests_async.head(url)
    assert response.status_code == 200
    assert response.text == ""


@pytest.mark.asyncio
async def test_options(server):
    url = "http://127.0.0.1:8000/"
    response = await requests_async.options(url)
    assert response.status_code == 200
    assert response.json() == {"method": "OPTIONS", "url": url, "body": ""}


@pytest.mark.asyncio
async def test_delete(server):
    url = "http://127.0.0.1:8000/"
    response = await requests_async.delete(url)
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE", "url": url, "body": ""}


@pytest.mark.asyncio
async def test_post(server):
    url = "http://127.0.0.1:8000/echo_form_data"
    response = await requests_async.post(url)
    assert response.status_code == 200
    assert response.json() == {"method": "POST", "url": url, "form": {}}


@pytest.mark.asyncio
async def test_post_with_data(server):
    url = "http://127.0.0.1:8000/echo_form_data"
    response = await requests_async.post(url, data={"a": "b"})
    assert response.status_code == 200
    assert response.json() == {"method": "POST", "url": url, "form": {"a": "b"}}


@pytest.mark.asyncio
async def test_put_with_data(server):
    url = "http://127.0.0.1:8000/echo_form_data"
    response = await requests_async.put(url, data={"a": "b"})
    assert response.status_code == 200
    assert response.json() == {"method": "PUT", "url": url, "form": {"a": "b"}}


@pytest.mark.asyncio
async def test_patch_with_data(server):
    url = "http://127.0.0.1:8000/echo_form_data"
    response = await requests_async.patch(url, data={"a": "b"})
    assert response.status_code == 200
    assert response.json() == {"method": "PATCH", "url": url, "form": {"a": "b"}}
