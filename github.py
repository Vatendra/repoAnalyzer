import datetime
import requests
import re


class Github:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.response = self.session.get(self.url).json()
        self.data = {}

    def created_since_months(self):
        """Returns the number of months since the repository was created"""
        created_at = self.response['created_at']
        self.data['created_on'] = created_at[:10]
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')).days / 30
        return round(no_of_months)

    def updated_since_months(self):
        """Returns the number of months since the repository was updated"""
        updated_at = self.response['updated_at']
        self.data['last_updated'] = updated_at[:10]
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')).days / 30
        return round(no_of_months)

    def get_forks_count(self):
        """Returns the number of forks to the repository"""
        return self.response['forks_count']

    def get_commits_count(self):
        """Returns the number of commits to the repository"""
        commits_count = re.search('\d+$', requests.get(f'{self.url}/commits?per_page=1').links['last']['url']).group()
        return int(commits_count)

    def get_contributors_count(self):
        """Returns the number of contributors to the repository"""
        contributors_url = self.url + '/contributors'
        contributors_count = 0
        page = 0
        while contributors_url:
            page += 1
            contributors_response = requests.get(contributors_url + '?page=' + str(page) + '&per_page=100').json()
            contributors_count += len(contributors_response)
            if len(contributors_response) < 100:
                return contributors_count
        return contributors_count

    def get_data(self):
        """Returns the data of the repository"""
        data = {'created_since_months': self.created_since_months(), 'updated_since_months': self.updated_since_months(),
                'forks': self.get_forks_count(),
                'contributors': self.get_contributors_count(), 'commits': self.get_commits_count(),
                'created_on': self.data['created_on'], 'last_updated': self.data['last_updated']}
        return data
