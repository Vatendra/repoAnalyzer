import datetime
from bs4 import BeautifulSoup
import re

import requests


class Gitlab:
    def __init__(self, url):
        self.url = url
        self.gl_session = requests.Session()
        self.response = self.gl_session.get(self.url).json()

    def created_since_months(self):
        """Returns the number of months since the project was created"""
        created_at = datetime.datetime.strptime(self.response['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        current_date = datetime.datetime.now()
        no_of_months = (current_date - created_at).days / 30
        return round(no_of_months)

    def updated_since_months(self):
        """Returns the number of months since the project was updated"""
        updated_at = datetime.datetime.strptime(self.response['last_activity_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        current_date = datetime.datetime.now()
        no_of_months = (current_date - updated_at).days / 30
        return round(no_of_months)

    def get_forks_count(self):
        """Returns the number of forks"""
        return self.response['forks_count']

    def __scrap(self, url):
        request = requests.get(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        stats = soup.find('nav', class_='project-stats')
        a = stats.find('a')
        commits_count = a.text.split(' ')[0]
        commits_count = commits_count.replace(',', '')
        return int(commits_count)

    def get_commits_count(self):
        """Returns the number of commits"""
        repo_url = self.url.replace('/api/v4/projects', '')
        repo_url = repo_url.replace('%2F', '/')
        return self.__scrap(repo_url)

    def get_data(self):
        data = {'url': self.url, 'forks': self.get_forks_count()}
        return data


test = Gitlab('https://gitlab.com/api/v4/projects/fdroid%2Ffdroiddata')
print(test.created_since_months())
print(test.updated_since_months())
print(test.get_forks_count())
print(test.get_commits_count())
