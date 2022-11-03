import pytest
import requests

def test_hello():
    r = requests.get("http://localhost:8000/hello")
    assert r.status_code == 200

def test_status():
    r = requests.get("http://localhost:8000/status")
    assert r.json() == 1

def test_dict():
    r = requests.get("http://localhost:8000/dict")
    assert "data" in r.json() 

def test_weather():
    r = requests.get("http://localhost:8000/weather")
    assert r.json()=="Sunny"