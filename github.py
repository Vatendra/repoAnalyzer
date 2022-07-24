import requests


class Github:
    def __init__(self, url):
        self.url = url
        self.gh_session = requests.Session()
        self.response = self.gh_session.get(self.url).json()

    def get_forks_count(self):
        return self.response['forks_count']

    def get_open_issues_count(self):
        return self.response['open_issues_count']

    def get_commits_count(self):
        commits_url = self.response['commits_url']
        response = self.gh_session.get(commits_url).json()
        print(commits_url)
        return len(response)

    def get_contributors_count(self):
        contributors_url = self.response['contributors_url']
        response = self.gh_session.get(contributors_url).json()
        return len(response)

    def get_rating(self):
        rating = 0
        rating += self.get_commits_count() * 0.1
        rating += self.get_contributors_count() * 0.2
        rating += self.get_forks_count() * 0.3
        rating += self.get_open_issues_count() * 0.4
        return rating

    def get_verdict(self):
        if self.get_rating() > 5:
            return True
        else:
            return False

    def get_data(self):
        data = {'url': self.url, 'commits': self.get_commits_count(), 'contributors': self.get_contributors_count(), 'forks': self.get_forks_count(), 'issues': self.get_open_issues_count(), 'rating': self.get_rating(), 'verdict': self.get_verdict()}
        return data
