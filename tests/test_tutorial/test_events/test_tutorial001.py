from docs_src.events.tutorial001 import app
from fastapi.testclient import TestClient


def test_events():
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200, response.text
        assert response.json() == {"name": "Fighters"}


def test_openapi_schema():
    with TestClient(app) as client:
        response = client.get("/openapi.json")
        assert response.status_code == 200, response.text
        assert response.json() == {
            "openapi": "3.1.0",
            "info": {"title": "FastAPI", "version": "0.1.0"},
            "paths": {
                "/items/{item_id}": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
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
                        "summary": "Read Items",
                        "operationId": "read_items_items__item_id__get",
                        "parameters": [
                            {
                                "required": True,
                                "schema": {"title": "Item Id", "type": "string"},
                                "name": "item_id",
                                "in": "path",
                            }
                        ],
                    }
                }
            },
            "components": {
                "schemas": {
                    "ValidationError": {
                        "title": "ValidationError",
                        "required": ["loc", "msg", "type"],
                        "type": "object",
                        "properties": {
                            "loc": {
                                "title": "Location",
                                "type": "array",
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
                                },
                            },
                            "msg": {"title": "Message", "type": "string"},
                            "type": {"title": "Error Type", "type": "string"},
                        },
                    },
                    "HTTPValidationError": {
                        "title": "HTTPValidationError",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                            }
                        },
                    },
                }
            },
        }
