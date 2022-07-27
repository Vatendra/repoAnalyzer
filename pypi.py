import requests
import main


class Pypi:
    def __init__(self, url):
        self.url = url
        self.pypi_session = requests.Session()
        self.response = self.pypi_session.get(self.url).json()

    def get_repository_url(self):
        print(self.response['info']['project_urls']['Source'])
        return self.response['info']['project_urls']['Source']

    def get_data(self):
        repo_url = self.get_repository_url()
        data = main.Main(repo_url).get_data()
        return data
