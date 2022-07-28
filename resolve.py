"""Resolve URL into api_url and repo_name."""
from urllib.parse import urlparse


class Resolve:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)

    def __get_repo_name(self) -> str:
        """Return repo name from URL."""
        return str(self.parsed_url.path.split('/')[2])

    def __get_repo_owner(self) -> str:
        """Return repo owner from URL."""
        return str(self.parsed_url.path.split('/')[1])

    def get_api_url(self):
        """Return API URL along with repo provider."""
        domain = self.parsed_url.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        if domain == "bitbucket.org":
            return 'bitbucket', "https://api.bitbucket.org/2.0/repositories/" + self.__get_repo_owner() + "/" +\
                   self.__get_repo_name()
        elif domain == "github.com":
            return 'github', "https://api.github.com/repos/" + self.__get_repo_owner() + "/" +\
                   self.__get_repo_name()
        elif domain == "gitlab.com":
            return 'gitlab', "https://gitlab.com/api/v4/projects/" + self.__get_repo_owner() + "%2F" +\
                   self.__get_repo_name()
        elif domain == "npmjs.com":
            print("https://registry.npmjs.org/" + self.__get_repo_name())
            return 'npm', "https://registry.npmjs.org/" + self.__get_repo_name()
        elif domain == "pypi.org":
            return 'pypi', "https://pypi.org/pypi/" + self.__get_repo_name() + "/json"
        else:
            return '', ''
