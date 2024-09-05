from typing import Optional, Union, Annotated

from fastapi import FastAPI, Body
from fastapi.testclient import TestClient

app = FastAPI()
SENTINEL = 1234567890


@app.post("/api1")
def api1(integer_or_null: Annotated[int | None, Body(embed=True)] = SENTINEL) -> dict:
    return {"received": integer_or_null}


@app.post("/api2")
def api2(
    integer_or_null: Annotated[Optional[int], Body(embed=True)] = SENTINEL
) -> dict:
    return {"received": integer_or_null}


@app.post("/api3")
def api3(
    integer_or_null: Annotated[Union[int, None], Body(embed=True)] = SENTINEL
) -> dict:
    return {"received": integer_or_null}


client = TestClient(app)


def test_api1_integer():
    response = client.post("/api1", json={"integer_or_null": 100})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": 100}


def test_api1_null():
    response = client.post("/api1", json={"integer_or_null": None})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": None}


def test_api2_integer():
    response = client.post("/api2", json={"integer_or_null": 100})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": 100}


def test_api2_null():
    response = client.post("/api2", json={"integer_or_null": None})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": None}


def test_api3_integer():
    response = client.post("/api3", json={"integer_or_null": 100})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": 100}


def test_api3_null():
    response = client.post("/api3", json={"integer_or_null": None})
    assert response.status_code == 200, response.text
    assert response.json() == {"received": None}
