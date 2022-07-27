"""Resolve URL into api_url and repo_name."""
from urllib.parse import urlparse


class Resolve:
    def __init__(self, url):
        self.url = url
        self.__add_https()
        self.__remove_backslash()

    def __add_https(self):
        """Add https:// to URL if it is missing."""
        if not self.url.startswith("https://"):
            self.url = "https://" + self.url
        return self.url

    def __remove_backslash(self):
        """Remove backslash from URL."""
        if self.url.endswith("/"):
            self.url = self.url[:-1]
        return self.url

    def __get_domain(self):
        """Return domain name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.netloc

    def __get_path(self):
        """Return repo name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path

    def __get_repo_name(self):
        """Return repo name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path.split("/")[-1]

    def __get_repo_owner(self):
        """Return repo owner from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path.split("/")[-2]

    def get_api_url(self):
        """Return API URL along with repo provider."""
        domain = self.__get_domain()
        if domain.startswith("www."):
            domain = domain[4:]
        if domain == "bitbucket.org":
            return 'bitbucket', "https://api.bitbucket.org/2.0/repositories" + self.__get_path()
        elif domain == "github.com":
            return 'github', "https://api.github.com/repos/" + self.__get_repo_owner() + "/" + self.__get_repo_name()
        elif domain == "gitlab.com":
            return 'gitlab', "https://gitlab.com/api/v4/projects/" + self.__get_repo_owner() + "%2F" + self.__get_repo_name()
        elif domain == "npmjs.com":
            return 'npm', "https://registry.npmjs.org/" + self.__get_repo_name()
        elif domain == "pypi.org":
            return 'pypi', "https://pypi.org/pypi/" + self.__get_repo_name() + "/json"
        else:
            return 'none', 'invalid'
