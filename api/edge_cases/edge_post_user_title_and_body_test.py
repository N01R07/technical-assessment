"""Test for edge case: POST /posts with empty title and body - Expecting a successful creation with default values or an error response."""
def test_post_user_title_and_body_empty(playwright):
    request = playwright.request.new_context()
    payload = {}
    response = request.post("https://jsonplaceholder.typicode.com/posts", data=payload)

    assert response.status == 201
    print(response.status)

    json_data = response.json()
    assert json_data["title"] == payload["title"]
    assert json_data["body"] == payload["body"]
    assert "id" in json_data

    print(f"\nStatus: {response.status}")
    print(f"New Post ID: {json_data['id']}")

    request.dispose()

if __name__ == "__main__":
    raise Exception("This test is meant to be run with a test runner like pytest, not directly.")