import json
import config

connex_app = config.connex_app
connex_app.add_api('swagger.yml')
connex_app = connex_app.app

client = connex_app.test_client()


def test_director_read_all():
    url = 'api/directors'

    response = client.get(url)
    data = json.loads(response.get_data())
    assert isinstance(data, list) is True
    assert response.status_code == 200

def test_movie_read_all():
    url = 'api/movies'

    response = client.get(url)
    data = json.loads(response.get_data())
    assert isinstance(data, list) is True
    assert response.status_code == 200

def test_director_create():
    url = 'api/directors'
    # url = 'http://h8ocbc2-milestone1-010.herokuapp.com/api/directors'
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    
    mock_request_data = {
        "department": "Directing",
        "gender": 2,
        "name": "Erica Masudah",
        "uid": 13038782
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    data = json.loads(response.get_data())
    assert response.status_code == 201

# def test_movie_create():
#     url = 'api/directors'
#     # url = 'http://h8ocbc2-milestone1-010.herokuapp.com/api/directors'
#     mock_request_headers = {
#         'Content-Type': 'application/json'
#     }
    
#     mock_request_data = {
#         "department": "Directing",
#         "gender": 2,
#         "name": "Erica Masudah",
#         "uid": 13038782
#     }

#     response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
#     data = json.loads(response.get_data())
#     assert response.status_code == 201
    

