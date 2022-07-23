"""Resolve URL into api_url and repo_name."""
from urllib.parse import urlparse


class Resolve:
    def __init__(self, url):
        self.url = url
        self.add_https()
        self.remove_backslash()

    def add_https(self):
        """Add https:// to URL if it is missing."""
        if not self.url.startswith("https://"):
            self.url = "https://" + self.url
        return self.url

    def remove_backslash(self):
        """Remove backslash from URL."""
        if self.url.endswith("/"):
            self.url = self.url[:-1]
        return self.url

    def get_domain(self):
        """Return domain name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.netloc

    def get_path(self):
        """Return repo name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path

    def get_repo_name(self):
        """Return repo name from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path.split("/")[-1]

    def get_repo_owner(self):
        """Return repo owner from URL."""
        parsed_url = urlparse(self.url)
        return parsed_url.path.split("/")[-2]

    def get_api_url(self):
        """Return API URL along with repo provider."""
        domain = self.get_domain()
        if domain.startswith("www."):
            domain = domain[4:]
        print(domain)
        if domain == "bitbucket.org":
            return "https://api.bitbucket.org/2.0/repositories" + self.get_path()
        elif domain == "github.com":
            return "https://api.github.com/repos" + self.get_path()
        elif domain == "gitlab.com":
            return "https://gitlab.com/api/v4/projects/" + self.get_repo_owner() + "%2F" + self.get_repo_name()
        elif domain == "npmjs.com":
            return "https://registry.npmjs.org/" + self.get_repo_name()
        elif domain == "pypi.org":
            return "https://pypi.org/pypi/" + self.get_repo_name() + "/json"
        else:
            return "Invalid URL"
