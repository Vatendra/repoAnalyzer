import resolve
import github


class Main:
    def __init__(self, url):
        self.url = url
        self.provider, self.api_url = resolve.Resolve(self.url).get_api_url()

    def get_data(self):
        """ Return data from API """
        if self.provider == "bitbucket":
            pass
        elif self.provider == "github":
            return github.Github(self.api_url).get_data()
        elif self.provider == "gitlab":
            pass
        elif self.provider == "npm":
            pass
        elif self.provider == "pypi":
            pass
        else:
            return
        data = {'url': self.url, 'commits': 13, 'contributors': 10, 'forks': 3, 'issues': 5, 'rating': 4,
                'verdict': True}
        return data
