import requests


class Bitbucket:
    def __init__(self, url):
        self.url = url
        self.bb_session = requests.Session()
        self.response = self.bb_session.get(self.url).json()

    def get_commits_count(self):
        commits_url = self.response['links']['commits']['href']
        response = self.bb_session.get(commits_url).json()
        return len(response['values'])

    def get_forks_count(self):
        forks_url = self.response['links']['forks']['href']
        response = self.bb_session.get(forks_url).json()
        return len(response['values'])

    def get_data(self):
        data = {'url': self.url, 'commits': self.get_commits_count(), 'forks': self.get_forks_count()}
        return data
