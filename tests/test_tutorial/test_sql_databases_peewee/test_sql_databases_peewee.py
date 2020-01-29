import time
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from starlette.testclient import TestClient

from ...utils import skip_py36

openapi_schema = {
    "openapi": "3.0.2",
    "info": {"title": "FastAPI", "version": "0.1.0"},
    "paths": {
        "/users/": {
            "get": {
                "summary": "Read Users",
                "operationId": "read_users_users__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {"title": "Skip", "type": "integer", "default": 0},
                        "name": "skip",
                        "in": "query",
                    },
                    {
                        "required": False,
                        "schema": {"title": "Limit", "type": "integer", "default": 100},
                        "name": "limit",
                        "in": "query",
                    },
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Read Users Users  Get",
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/User"},
                                }
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            },
            "post": {
                "summary": "Create User",
                "operationId": "create_user_users__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/UserCreate"}
                        }
                    },
                    "required": True,
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/User"}
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            },
        },
        "/users/{user_id}": {
            "get": {
                "summary": "Read User",
                "operationId": "read_user_users__user_id__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {"title": "User Id", "type": "integer"},
                        "name": "user_id",
                        "in": "path",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/User"}
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            }
        },
        "/users/{user_id}/items/": {
            "post": {
                "summary": "Create Item For User",
                "operationId": "create_item_for_user_users__user_id__items__post",
                "parameters": [
                    {
                        "required": True,
                        "schema": {"title": "User Id", "type": "integer"},
                        "name": "user_id",
                        "in": "path",
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ItemCreate"}
                        }
                    },
                    "required": True,
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Item"}
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            }
        },
        "/items/": {
            "get": {
                "summary": "Read Items",
                "operationId": "read_items_items__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {"title": "Skip", "type": "integer", "default": 0},
                        "name": "skip",
                        "in": "query",
                    },
                    {
                        "required": False,
                        "schema": {"title": "Limit", "type": "integer", "default": 100},
                        "name": "limit",
                        "in": "query",
                    },
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Read Items Items  Get",
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Item"},
                                }
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            }
        },
        "/slowusers/": {
            "get": {
                "summary": "Read Slow Users",
                "operationId": "read_slow_users_slowusers__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {"title": "Skip", "type": "integer", "default": 0},
                        "name": "skip",
                        "in": "query",
                    },
                    {
                        "required": False,
                        "schema": {"title": "Limit", "type": "integer", "default": 100},
                        "name": "limit",
                        "in": "query",
                    },
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Read Slow Users Slowusers  Get",
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/User"},
                                }
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            }
        },
    },
    "components": {
        "schemas": {
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/ValidationError"},
                    }
                },
            },
            "Item": {
                "title": "Item",
                "required": ["title", "id", "owner_id"],
                "type": "object",
                "properties": {
                    "title": {"title": "Title", "type": "string"},
                    "description": {"title": "Description", "type": "string"},
                    "id": {"title": "Id", "type": "integer"},
                    "owner_id": {"title": "Owner Id", "type": "integer"},
                },
            },
            "ItemCreate": {
                "title": "ItemCreate",
                "required": ["title"],
                "type": "object",
                "properties": {
                    "title": {"title": "Title", "type": "string"},
                    "description": {"title": "Description", "type": "string"},
                },
            },
            "User": {
                "title": "User",
                "required": ["email", "id", "is_active"],
                "type": "object",
                "properties": {
                    "email": {"title": "Email", "type": "string"},
                    "id": {"title": "Id", "type": "integer"},
                    "is_active": {"title": "Is Active", "type": "boolean"},
                    "items": {
                        "title": "Items",
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Item"},
                        "default": [],
                    },
                },
            },
            "UserCreate": {
                "title": "UserCreate",
                "required": ["email", "password"],
                "type": "object",
                "properties": {
                    "email": {"title": "Email", "type": "string"},
                    "password": {"title": "Password", "type": "string"},
                },
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": ["loc", "msg", "type"],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "msg": {"title": "Message", "type": "string"},
                    "type": {"title": "Error Type", "type": "string"},
                },
            },
        }
    },
}


@pytest.fixture(scope="module")
def client():
    # Import while creating the client to create the DB after starting the test session
    from sql_databases_peewee.sql_app.main import app

    test_db = Path("./test.db")
    with TestClient(app) as c:
        yield c
    test_db.unlink()


@skip_py36
def test_openapi_schema(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json() == openapi_schema


@skip_py36
def test_create_user(client):
    test_user = {"email": "johndoe@example.com", "password": "secret"}
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200
    data = response.json()
    assert test_user["email"] == data["email"]
    assert "id" in data
    response = client.post("/users/", json=test_user)
    assert response.status_code == 400


@skip_py36
def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "id" in data


@skip_py36
def test_inexistent_user(client):
    response = client.get("/users/999")
    assert response.status_code == 404


@skip_py36
def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data[0]
    assert "id" in data[0]


time.sleep = MagicMock()


@skip_py36
def test_get_slowusers(client):
    response = client.get("/slowusers/")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data[0]
    assert "id" in data[0]


@skip_py36
def test_create_item(client):
    item = {"title": "Foo", "description": "Something that fights"}
    response = client.post("/users/1/items/", json=item)
    assert response.status_code == 200
    item_data = response.json()
    assert item["title"] == item_data["title"]
    assert item["description"] == item_data["description"]
    assert "id" in item_data
    assert "owner_id" in item_data
    response = client.get("/users/1")
    assert response.status_code == 200
    user_data = response.json()
    item_to_check = [it for it in user_data["items"] if it["id"] == item_data["id"]][0]
    assert item_to_check["title"] == item["title"]
    assert item_to_check["description"] == item["description"]
    response = client.get("/users/1")
    assert response.status_code == 200
    user_data = response.json()
    item_to_check = [it for it in user_data["items"] if it["id"] == item_data["id"]][0]
    assert item_to_check["title"] == item["title"]
    assert item_to_check["description"] == item["description"]


@skip_py36
def test_read_items(client):
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert data
    first_item = data[0]
    assert "title" in first_item
    assert "description" in first_item
