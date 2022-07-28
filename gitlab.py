import requests
import resolve


class Gitlab:
    def __init__(self, url):
        self.url = url
        self.gl_session = requests.Session()
        self.response = self.gl_session.get(self.url).json()

    def get_forks_count(self):
        return self.response['forks_count']

    def get_data(self):
        data = {'url': self.url, 'forks': self.get_forks_count()}
        return data
