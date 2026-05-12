"""Test for edge case: GET /users/0 - Expecting a user with ID 0, which may not exist in the API."""
def test_get_user_0(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/users/0")

    assert response.status == 200 # set to 404 if you want to test for non-existent user
    json_data = response.json()
    assert json_data["id"] == 0
    assert "name" in json_data
    
    print(f'\nStatus: {response.status}')
    print(f'User ID: {json_data["id"]}')
    print(f'User Name: {json_data["name"]}')

    request.dispose()

if __name__ == "__main__":
    raise Exception("This test is meant to be run with a test runner like pytest, not directly.")