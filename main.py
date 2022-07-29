from bitbucket import Bitbucket
from github import Github
from gitlab import Gitlab
from npm import Npm
from pypi import Pypi
from resolve import Resolve
from criticalscore import CriticalScore


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
        data['critical_score'] = 1  # CriticalScore(data).get_result()
        return data
