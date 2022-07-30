import datetime
import requests


class Bitbucket:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.response = self.session.get(self.url).json()
        self.__contributors = set()
        self.data = {}

    def created_since_months(self):
        """Returns the number of months since the repository was created"""
        date_created = self.response['created_on'][:10]
        self.data['created_on'] = date_created
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(date_created, '%Y-%m-%d')).days / 30
        return round(no_of_months)

    def updated_since_months(self):
        """Returns the number of months since the repository was updated"""
        date_updated = self.response['updated_on'][:10]
        self.data['last_updated'] = date_updated
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(date_updated, '%Y-%m-%d')).days / 30
        return round(no_of_months)

    def get_forks_count(self):
        """Returns the number of forks"""
        fork_url = self.response['links']['forks']['href']
        fork_count = 0
        while fork_url:
            fork_response = self.session.get(fork_url).json()
            fork_count += len(fork_response['values'])
            if 'next' in fork_response:
                fork_url = fork_response['next']
            else:
                return fork_count
        return fork_count

    def get_commits_count(self):
        """Returns the number of commits"""
        commits_url = self.response['links']['commits']['href']
        commits_count = 0
        while commits_url:
            commits_response = self.session.get(commits_url).json()
            commits_count += len(commits_response['values'])
            for value in commits_response['values']:
                self.__contributors.add(value['author']['raw'])
            if 'next' in commits_response:
                commits_url = commits_response['next']
            else:
                return commits_count
        return commits_count

    def get_contributors_count(self):
        """Returns the number of contributors"""
        return len(self.__contributors)

    def get_data(self):
        """Returns the data of the repository"""
        data = {'created_since_months': self.created_since_months(), 'updated_since_months': self.updated_since_months(),
                'forks': self.get_forks_count(), 'commits': self.get_commits_count(),
                'contributors': self.get_contributors_count(), 'created_on': self.data['created_on'],
                'last_updated': self.data['last_updated']}
        return data
