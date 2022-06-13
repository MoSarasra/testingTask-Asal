# Asal python testing task / by mohammad Alsarasra
import requests
import pytest
import json

# Post Test Cases
row_url = 'https://jsonplaceholder.typicode.com'
posts_url = row_url + '/posts'


# read input json file / method
def file_reader(localLink):
    file = open(localLink, 'r')
    json_input = json.loads(file.read())
    return json_input


# make Post request with new local data

def test_post_new_data():
    response = requests.post(posts_url, file_reader(
        'C:\\Users\\CS NET GAMES\\PycharmProjects\\AsalTestingTask\\jData\\cleanData.json'))
    assert response.status_code == 201


# post missing data
def test_post_missing_data():
    response = requests.post(posts_url, file_reader(
        'C:\\Users\\CS NET GAMES\\PycharmProjects\\AsalTestingTask\\jData\\missingData.json'))
    assert response.status_code == 201


# post invalid data

def test_post_invalid_data():
    response = requests.post(posts_url, file_reader(
        'C:\\Users\\CS NET GAMES\\PycharmProjects\\AsalTestingTask\\jData\\invalidDataTypeData.json'))
    assert response.status_code == 201


# extra key /value data
def test_extra_keys():
    response = requests.post(posts_url, file_reader(
        'C:\\Users\\CS NET GAMES\\PycharmProjects\\AsalTestingTask\\jData\\extra.json'))
    assert response.status_code == 201


# missed key /value data
def test_missed_keys():
    response = requests.post(posts_url, file_reader(
        'C:\\Users\\CS NET GAMES\\PycharmProjects\\AsalTestingTask\\jData\\missedKey.json'))
    assert response.status_code == 201

