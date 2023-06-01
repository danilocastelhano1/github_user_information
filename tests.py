import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import mock_open

import requests_mock
import builtins

from requests import HTTPError

from http import HTTPStatus

from src.github import GitHubRequest

from settings import GITHUB_URL
from settings import GITHUB_USER_PATH

from src.file import FileSave
from src.models import GithubUser


class TestGithubService(unittest.TestCase):

    def test_should_raise_error_when_username_not_informed(self):
        with self.assertRaises(KeyError):
            GitHubRequest().get_github_user_information("")

    def test_should_raise_http_error_when_username_is_informed_but_wrong(self):
        username: str = "danilocastelhano11"

        with requests_mock.Mocker() as m:
            m.get(
                url=GITHUB_URL + GITHUB_USER_PATH + username,
                json={
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"
                },
                status_code=HTTPStatus.NOT_FOUND
            )
            with self.assertRaises(HTTPError):
                GitHubRequest().get_github_user_information(username)

    def test_should_success_when_username_informed_correctly(self):
        username: str = "danilocastelhano1"

        with requests_mock.Mocker() as m:
            m.get(
                url=GITHUB_URL + GITHUB_USER_PATH + username,
                json={
                    "id": 52941839,
                    "login": "danilocastelhano1",
                },
                status_code=HTTPStatus.OK
            )
            FileSave.save_to_file = mock.Mock(return_value=f"/{username}.txt")
            GithubUser.from_json = mock.Mock(return_value={"id": 123, "login": "danilocastelhano1"})

            file_path = GitHubRequest().get_github_user_information(username)
            self.assertEqual(f"/{username}.txt", file_path)


class TestFileSave(unittest.TestCase):

    def test_should_generate_file_correctly(self):
        github_user_model = GithubUser(
            login="teste_user_1",
            name="test",
            url="http://127.0.0.1",
            public_repos=3,
            followers=1,
            following=0,
            repos_url="http://127.0.0.1/repos")

        with patch('builtins.open', new=mock_open(read_data='Fooooo')) as _file:
            filepath = FileSave().save_to_file(github_user_model=github_user_model)
            self.assertIsNotNone(filepath)
