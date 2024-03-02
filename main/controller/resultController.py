import pandas as pd

class Result:
    def __init__(self, type_issue,date_test,name_project,module,type_test,environment,device,level_test,url,result):
        self.type_issue = type_issue
        self.id_issue
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
        df_result = pd.DataFrame()
        df_result['type_issue'] = self.type_issue
        df_result['date_test'] = self.date_test
        df_result['name_project'] = self.name_project
        df_result['module'] = self.module
        df_result['type_test'] = self.type_test
        df_result['environment'] = self.environment
        df_result['device'] = self.device
        df_result['level_test'] = self.level_test
        df_result['url'] = self.url
        df_result['result'] = self.result
        return df_result