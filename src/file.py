import os

from typing import Tuple
from typing import Optional

from src.models import GithubUser

from src.mappers import GITHUB_USER_MAPPERS


class FileSave:
    def __mount_file_to_save(self, github_user_model: GithubUser) -> Tuple[str, str]:
        """
        Responsible for mounting the data to be stored in text file.
        :param github_user_model: GithubUser
        :return: Tuple[str, str]
        """
        header: str = ""
        body: str = ""

        for github_user_mapper in GITHUB_USER_MAPPERS:
            title: str = github_user_mapper.get("title")
            size: int = github_user_mapper.get("size")
            value: str = str(getattr(github_user_model, github_user_mapper.get("key")))

            header += title.ljust(size, " ")
            body += value.ljust(size, " ")

        return header, body

    def save_to_file(self, github_user_model: GithubUser) -> Optional[str]:
        """
        Responsible for storing the information in a text file.
        :param github_user_model: GithubUser
        :return: Optional[str]
        """
        header, body = self.__mount_file_to_save(github_user_model=github_user_model)

        file_name: str = f"{github_user_model.login}.txt"
        with open(file_name, "a") as file:
            file.truncate(0)  # clear a file before writing
            file.write(f"{header}\n")
            file.write(f"{body}\n")

        return os.path.abspath(file_name)
