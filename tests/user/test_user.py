import requests


class TestUserValidation:

    def test_login_non_existent_user(self, user_url, created_user_data):
        username, password = created_user_data
        deletion_response = requests.delete(f'{user_url}/{username}')
        user_login_url = f'{user_url}/login?username={username}&password={password}'
        login_response = requests.get(user_login_url)

        assert deletion_response.status_code == 200
        assert login_response.status_code == 400

    def test_create_user_with_invalid_data(
            self, user_create_with_list_url, invalid_create_user_data
    ):
        response = requests.post(
            url=user_create_with_list_url, json=invalid_create_user_data
        )
        assert 400 <= response.status_code < 500
