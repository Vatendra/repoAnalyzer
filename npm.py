import requests
import main


class Npm:
    def __init__(self, url):
        self.url = url
        self.npm_session = requests.Session()
        self.response = self.npm_session.get(self.url).json()

    def get_repository_url(self):
        url = self.response['repository']['url']
        url = url.replace('git://', 'https://')
        if url.endswith('.git'):
            url = url[:-4]
        return url

    def get_data(self):
        repo_url = self.get_repository_url()
        data = main.Main(repo_url).get_data()
        return data
