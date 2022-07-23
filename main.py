class Main:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        """ Return data from API """
        data = {'url': self.url, 'commits': 13, 'contributors': 10, 'forks': 3, 'issues': 5, 'rating': 4,
                'verdict': True}
        return data
