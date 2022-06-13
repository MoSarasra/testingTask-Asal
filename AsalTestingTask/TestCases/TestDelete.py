# Asal python testing task / by mohammad Alsarasra
import requests
import pytest
import json

# Post Test Cases
row_url = 'https://jsonplaceholder.typicode.com'
posts_url = row_url + '/posts'


# delete post 1
def test_delete_clean_data():
    response = requests.delete(posts_url + '/1')
    assert response.status_code == 200
