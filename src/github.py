import requests

from typing import Optional

from requests import Response
from requests.exceptions import HTTPError

from urllib.parse import urljoin

from src.models import GithubUser

from src.file import FileSave

from settings import GITHUB_URL
from settings import GITHUB_USER_PATH


from http import HTTPStatus


class GitHubRequest(object):
    def __init__(self) -> None:
        self.github_url: str = GITHUB_URL
        self.github_user_path: str = GITHUB_USER_PATH

    def __build_github_user_url(self, username: str) -> str:
        """
        Responsible for build a GITHUB URL
        :param username:
        :return: url built
        """
        path: str = f"{self.github_user_path}{username}"
        return urljoin(self.github_url, path)

    def get_github_user_information(self, username: str) -> Optional[str]:
        """
        Responsible for get the information on the GITHUB API and generate a .txt
        :param username:
        :return: Optional[str]
        """
        if not username:
            raise KeyError("Username not informed")

        url: str = self.__build_github_user_url(username=username)
        response: Response = requests.get(url=url)

        if response.status_code == HTTPStatus.OK:
            github_user_model = GithubUser.from_json(response.content)

            return FileSave().save_to_file(github_user_model=github_user_model)
        else:
            raise HTTPError(f"Request Error, status: {response.status_code}, error: {response.json()}")
