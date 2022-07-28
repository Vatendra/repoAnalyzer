import datetime

import requests
import re
import config


class Github:
    def __init__(self, url):
        self.url = url
        if config.GITHUB_USERNAME == '':
            self.gh_session = requests.Session()
        else:
            self.gh_session = requests.Session()
            self.gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_PASSWORD)
        self.response = self.gh_session.get(self.url).json()

    def created_since_months(self):
        """Returns the number of months since the repository was created"""
        created_at = self.response['created_at']
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')).days / 30
        return round(no_of_months)

    def updated_since_months(self):
        """Returns the number of months since the repository was updated"""
        updated_at = self.response['updated_at']
        current_date = datetime.datetime.now()
        no_of_months = (current_date - datetime.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')).days / 30
        return round(no_of_months)

    def get_forks_count(self):
        """Returns the number of forks to the repository"""
        return self.response['forks_count']

    def get_open_issues_count(self):
        return self.response['open_issues_count']

    def get_commits_count(self):
        """Returns the number of commits to the repository"""
        commits_count = re.search('\d+$', requests.get(f'{self.url}/commits?per_page=1').links['last']['url']).group()
        return int(commits_count)

    def get_contributors_count(self):
        """Returns the number of contributors to the repository"""
        contributors_url = self.url + '/stats/contributors'
        response = self.gh_session.get(contributors_url).json()
        return len(response)

    def get_data(self):
        data = {'url': self.url, 'commits': self.get_commits_count(), 'contributors': self.get_contributors_count(),
                'forks': self.get_forks_count(), 'issues': self.get_open_issues_count(),
                'created_since_months': self.created_since_months(), 'updated_since_months': self.updated_since_months()
                }


test = Github('https://api.github.com/repos/jquery/jquery')
# print(test.created_since_months())
# print(test.updated_since_months())
print(test.get_contributors_count())
print(test.get_commits_count())
# print(test.get_forks_count())
