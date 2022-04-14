from django.test import TestCase
import requests


def test_get_the_api_response():
    url = "http://localhost:8080/helloworld"
    r = requests.get(url)

    print(r)
    print(r.text)
    assert r.status_code == 200



