import math


class CriticalScore:

    MAX_VALUES_DATA = {'created_since_months': 120, 'updated_since_months': 120, 'forks': 5000, 'contributors': 5000,
                       'commit_frequency': 1000}
    WEIGHT_VALUES_DATA = {'created_since_months': 1, 'updated_since_months': -1, 'forks': 1, 'contributors': 2,
                          'commit_frequency': 1}

    def __init__(self, data):
        # default values in case API doesn't return results
        self.data = data

    def get_result(self):
        param_log_sum = 0
        param_max_log = 0
        summation_param = 0
        summation_weight = 0
        critical_score = 0 

        for i in self.data:
            param_log_sum = math.log(1 + self.data[i])
            param_max_log = math.log(1 + max(self.data[i], CriticalScore.MAX_VALUES_DATA[i]))
            summation_param += (CriticalScore.WEIGHT_VALUES_DATA[i] * (param_log_sum / param_max_log))
            summation_weight += CriticalScore.WEIGHT_VALUES_DATA[i]
        
        critical_score = summation_weight * summation_param
        return critical_score
            
    