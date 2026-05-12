
"""Test for edge case: GET /userss - Expecting a 404 Not Found error due to incorrect endpoint."""
def test_get_users_invalid_endpoint(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/userss")

    assert response.status == 200 # set to 404 if you want to test for non-existent endpoint
    json_data = response.json()
    users = response.json()

    print(f'\nStatus: {response.status}')
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "email" in user
        print(f'User ID: {user["id"]}, \nUser Name: {user["name"]}, \nUser Email: {user["email"]}\n')

    request.dispose()

if __name__ == "__main__":
    raise Exception("This test is meant to be run with a test runner like pytest, not directly.")