import pandas as pd

class Result:
    def __init__(self, type_issue,date_test,name_project,module,type_test,environment,device,level_test,url,result):
        self.type_issue = type_issue
        #self.id_issue
        self.date_test = date_test
        self.name_project = name_project
        self.module = module
        self.type_test = type_test
        self.environment = environment
        self.device = device
        self.level_test = level_test
        self.url = url
        self.result = result

    def get_result(self):
        data = {
            'type_issue': [self.type_issue],
            'date_test': [self.date_test],
            'name_project': [self.name_project],
            'module': [self.module],
            'type_test': [self.type_test],
            'environment': [self.environment],
            'device': [self.device],
            'level_test': [self.level_test],
            'url': [self.url],
            'result': [self.result]
        }
        return pd.DataFrame(data)