def test_put_user_title_and_body(playwright):
    request = playwright.request.new_context()
    updated_payload = {
        "definitelyFake": 1,
        "id": 1,
        "NAH": "Updated Title",
        "body": "Updated Body",
    }
    response = request.put("https://jsonplaceholder.typicode.com/posts/9999", data=updated_payload)

    assert response.status == 200
    print(response.status)

    json_data = response.json()
    assert json_data["title"] == "Updated Title"
    assert json_data["body"] == "Updated Body"

    print(f"\nStatus: {response.status}")
    print(f"Updated Data: {json_data['id']}")

    request.dispose()

if __name__ == "__main__":
    raise Exception("This test is meant to be run with a test runner like pytest, not directly.")