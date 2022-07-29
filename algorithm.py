import math

max_values_data = {'created_since_months' : 120, 'updated_since_months' : 120, 'forks_count':5000,  'contributors_count' : 5000, 'commit_frequency' :1000}
weight_values_data = {'created_since_months' : 1, 'updated_since_months' : -1, 'forks_count' : 1, 'contributors_count' : 2, 'commit_frequency' :1}

class Algorithm:

    def __init__(self, data):
        # default values in case API doesn't return results
        self.data = { 'created_since_months' : 0, 'updated_since_months' : 0, 'forks_count' : 0, 'commits_count' : 0, 'contributors_count' : 0, 'commit_frequency' :0 }
        
    def get_result(self):
        param_log_sum= 0
        param_max_log= 0
        summation_param= 0
        summation_weight= 0
        critical_score = 0 

        for i in self.data:
            param_log_sum = math.log(1 + self.data[i])
            param_max_log = math.log(1+max(self.data[i],max_values_data[i]))
            summation_param += (weight_values_data[i] * (param_log_sum/param_max_log))
            summation_weight += weight_values_data[i]
        
        critical_score = summation_weight * summation_param
        return critical_score
            
    