# Asal python testing task / by mohammad Alsarasra
import requests
import pytest

# Get Test Cases


row_url = 'https://jsonplaceholder.typicode.com'
posts_url = row_url + '/posts'


# 1. make sure that the response is ok
def test_posts_status_code_verification():
    response = requests.get(posts_url)
    response_status = response.status_code
    assert response_status == 200


# 2. make sure that the response is ok for url/post num 1
def test_posts_status_code_when_id_equals_one():
    response = requests.get(posts_url + '/1')  # posts url for post num 1
    response_status = response.status_code
    assert response_status == 200


# 3. make sure that response equals expected where post 1 id must equals 1
def test_response_payload_for_posts_id_equals_one():
    response = requests.get(posts_url + '/1')  # posts url for post num 1
    response_info = response.json()  # gets data
    assert response_info['id'] == 1  # gets data: key = id / value = 1 and check


# 4. make sure that the response is ok for url/comments where post is =1
def test_comments_status_code_when_id_equals_one():
    response = requests.get(row_url + '/comments?postId=1')  # posts url for post num 1
    response_status = response.status_code
    assert response_status == 200


# 5.make sure that number of Ids equal 100
def test_number_of_posts():
    response = requests.get(posts_url + '/100')
    response_info = response.json()
    assert response_info['id'] == 100


# 6.check body of a certain id
def test_body_of_a_post():
    response = requests.get(posts_url + '/97')  # id =97
    response_info = response.json()
    assert response_info[
               'body'] == "eum non blanditiis soluta porro quibusdam voluptas\nvel voluptatem qui placeat dolores qui velit aut\nvel inventore aut cumque culpa explicabo aliquid at\nperspiciatis est et voluptatem dignissimos dolor itaque sit nam"


# 7.check userid of a certain id

def test_userid_of_a_certain_id():
    response = requests.get(posts_url + '/93')
    response_info = response.json()
    assert response_info['userId'] == 10


# 8.test connection
def test_connection():
    response = requests.get(row_url)
    response_info = response.headers
    assert response_info['Connection'] == 'keep-alive'


# 9. response 404 not found when id is not existed

def test_not_found_check():
    response = requests.get(posts_url + '/150')
    response_status = response.status_code
    assert response_status == 404


# 10. check body  in a negative way

def test_body_is_not_right():
    response = requests.get(posts_url + '/82')
    response_info = response.json()
    assert response_info[
               'body'] != "est molestiae facilis quis tempora numquam nihil qui\nvoluptate sapiente consequatur est qui\nnecessitatibus autem aut ipsa aperiam modi dolore numquam\nreprehenderit eius rem quibusdam"


