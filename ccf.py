import math


class Ccf:
    def __init__(self, data):
        self.data = data

    def get_individual_score(self):
        """ Return individual score """
        individual_score = 0
        if self.data['created_since_months'] >= 12:
            individual_score += 1
        if self.data['updated_since_months'] < 6:
            individual_score += 1
        if self.data['forks'] >= 100:
            individual_score += 1
        if self.data['commits'] >= 1000:
            individual_score += 1
        if self.data['contributors'] >= 10:
            individual_score += 1
        return individual_score

    def normalize_contributors(self):
        """ Return normalized contributors """
        if self.data['contributors'] == 0:
            return 0
        normalized_contributors = math.log(self.data['contributors'], 10) / 2
        if normalized_contributors > 1:
            normalized_contributors = 1
        return round(normalized_contributors, 2)

    def normalize_last_update(self):
        """ Return normalized last update """
        if self.data['created_since_months'] == 0:
            return 0
        return 1 - self.data['updated_since_months'] / self.data['created_since_months']

    def normalize_forks(self):
        """ Return normalized forks """
        if self.data['forks'] == 0:
            return 0
        normalized_forks = math.log(self.data['forks'], 100) / 2
        if normalized_forks > 1:
            normalized_forks = 1
        return round(normalized_forks, 2)

    def normalize_commits(self):
        """ Return normalized commits """
        if self.data['commits'] == 0:
            return 0
        normalized_commits = math.log(self.data['commits']/10, 50) /2
        if normalized_commits > 1:
            normalized_commits = 1
        return round(normalized_commits, 2)

    def normalize_duration(self):
        """ Return normalized duration """
        if self.data['created_since_months'] == 0:
            return 0
        normalized_duration = math.log(self.data['created_since_months'], 10) / 2
        if normalized_duration > 1:
            normalized_duration = 1
        return round(normalized_duration, 2)

    def get_ccf_score(self):
        """ Return ccf score """
        ccf_score = 0
        ccf_score += self.normalize_contributors()
        ccf_score += self.normalize_last_update()
        ccf_score += self.normalize_forks()
        ccf_score += self.normalize_commits()
        ccf_score += self.normalize_duration()
        ccf_score += self.get_individual_score()
        return round(ccf_score, 2)

