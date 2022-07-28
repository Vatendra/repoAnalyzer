import datetime

import requests


class Bitbucket:
    def __init__(self, url):
        self.url = url
        self.bb_session = requests.Session()
        self.response = self.bb_session.get(self.url).json()
        commits_url = self.response['links']['commits']['href']
        self.commits_response = self.bb_session.get(commits_url).json()

    def created_since_months(self):
        """Returns the number of months since the repository was created"""
        date_created = self.response['created_on'][:10]
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(date_created, '%Y-%m-%d')).days / 30
        return round(no_of_months)

    def updated_since_months(self):
        """Returns the number of months since the repository was updated"""
        date_updated = self.response['updated_on'][:10]
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(date_updated, '%Y-%m-%d')).days / 30
        return round(no_of_months)

    def get_forks_count(self):
        """Returns the number of forks"""
        fork_url = self.response['links']['forks']['href']
        fork_count = 0
        while fork_url:
            fork_response = self.bb_session.get(fork_url).json()
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
            commits_response = self.bb_session.get(commits_url).json()
            commits_count += len(commits_response['values'])
            if 'next' in commits_response:
                commits_url = commits_response['next']
            else:
                return commits_count
        return commits_count

    def get_data(self):
        data = {'url': self.url, 'created_since_months': self.created_since_months(),
                'updated_since_months': self.updated_since_months()
                }


test = Bitbucket('https://api.bitbucket.org/2.0/repositories/hgarcia/node-bitbucket-api')
print(test.get_forks_count())
print(test.created_since_months())
print(test.updated_since_months())
print(test.get_commits_count())
