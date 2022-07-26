from bitbucket import Bitbucket
from github import Github
from gitlab import Gitlab
from npm import Npm
from pypi import Pypi
from resolve import Resolve
from ccf import Ccf


class Main:
    def __init__(self, url):
        self.url = url
        self.provider, self.api_url = Resolve(self.url).get_api_url()

    def get_data(self):
        """ Return data from API """
        data = {}
        if self.provider == "bitbucket":
            data = Bitbucket(self.api_url).get_data()
        elif self.provider == "github":
            data = Github(self.api_url).get_data()
        elif self.provider == "gitlab":
            data = Gitlab(self.api_url).get_data()
        elif self.provider == "npm":
            data = Npm(self.api_url).get_data()
        elif self.provider == "pypi":
            print(self.api_url)
            data = Pypi(self.api_url).get_data()
        else:
            return {}
        data['ccf_score'] = Ccf(data).get_ccf_score()
        data['image_path'] = "unsafe_repo.png"
        # have taken 4 as the base point for a repo to be safe
        if data['ccf_score'] > 4:
            data['image_path'] = "safe_repo.png"
        data['repo_name'] = Resolve(self.url).get_repo_name()
        return data
