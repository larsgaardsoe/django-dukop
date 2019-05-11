def test_with_client(client):
    response = client.get('/en/')
    assert response.status_code == 200
