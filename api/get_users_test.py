def test_all_users(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/users")

    assert response.status == 200
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