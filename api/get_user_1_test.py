def test_one_user(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert "name" in json_data
    
    print(f'\nStatus: {response.status}')
    print(f'User ID: {json_data["id"]}')
    print(f'User Name: {json_data["name"]}')

    request.dispose()

if __name__ == "__main__":
    raise Exception("This test is meant to be run with a test runner like pytest, not directly.")