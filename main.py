import resolve
import github, bitbucket, gitlab, npm, pypi


class Main:
    def __init__(self, url):
        self.url = url
        self.provider, self.api_url = resolve.Resolve(self.url).get_api_url()

    def get_data(self):
        """ Return data from API """
        if self.provider == "bitbucket":
            return bitbucket.Bitbucket(self.api_url).get_data()
        elif self.provider == "github":
            return github.Github(self.api_url).get_data()
        elif self.provider == "gitlab":
            return gitlab.Gitlab(self.api_url).get_data()
        elif self.provider == "npm":
            return npm.Npm(self.api_url).get_data()
        elif self.provider == "pypi":
            print(self.api_url)
            return pypi.Pypi(self.api_url).get_data()
        else:
            return
        data = {'url': self.url, 'commits': 13, 'contributors': 10, 'forks': 3, 'issues': 5, 'rating': 4,
                'verdict': True}
        return data
