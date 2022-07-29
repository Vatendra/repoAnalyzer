import datetime
from bs4 import BeautifulSoup
import config
import requests


class Gitlab:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        if config.GITLAB_PRIVATE_TOKEN != '':
            self.response = self.session.get(url, headers={'PRIVATE-TOKEN': config.GITLAB_PRIVATE_TOKEN}).json()
        else:
            self.response = self.session.get(self.url).json()
        self.data = {}

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

    def get_contributors_count(self):
        """Returns the number of contributors"""
        contributors_url = self.url + '/members'
        page = 0
        contributors_count = 0
        while contributors_url:
            page += 1
            contributors_url = contributors_url + '?page=' + str(page) + '&per_page=100'
            response = self.session.get(contributors_url, headers={'PRIVATE-TOKEN': config.GITLAB_PRIVATE_TOKEN}).\
                json()
            contributors_count += len(response)
            print("length"+str(len(response)))
            if len(response) < 100:
                return contributors_count
        return contributors_count

    def get_data(self):
        """Returns the data of the repository"""
        data = {'created_since_months': self.created_since_months(), 'updated_since_months': self.updated_since_months(),
                'forks': self.get_forks_count(),
                'contributors': self.get_contributors_count(), 'commit_frequency': self.get_commits_count()/(self.get_created_since_months*4)
                }
        return data

