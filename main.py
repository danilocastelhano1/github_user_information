"""
Main class, responsible for get the args in the command line and send to GITHUB and store a text file.
"""

import argparse

from requests.exceptions import HTTPError

from src.github import GitHubRequest

parser = argparse.ArgumentParser()
parser.add_argument('--username', dest='github_username', type=str, help='Name of username on Github')
args = parser.parse_args()

try:
    file_path: str = GitHubRequest().get_github_user_information(args.github_username)
    print(f"Arquivo gerado com sucesso em: {file_path}")
except (KeyError, HTTPError) as error:
    print(error)
