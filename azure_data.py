# from azure.cosmosdb.table import TableService
# #from azure.cosmosdb.table.models import Entity
# #table_service = TableService(account_name='mtutorlog', account_key='5g/uyxepfdZxjrHETQZ0jDj6y6nsU/t6HAMZdPIr16X5BmBCaLlgb1ybsmpwY6jhNHXP6CXrHYdzS0QLTtyXFw==')
# table_service = TableService(connection_string=r'DefaultEndpointsProtocol=https;AccountName=mtutorlog;AccountKey=5g/uyxepfdZxjrHETQZ0jDj6y6nsU/t6HAMZdPIr16X5BmBCaLlgb1ybsmpwY6jhNHXP6CXrHYdzS0QLTtyXFw==;EndpointSuffix=ix=core.windows.net')
# print("2")
# tasks = table_service.query_entities('SystemTelementry20171202', filter="AppName eq 'Chinese-iOS'")  #query a set of entities
# print("3")
# for task in tasks:
#     print(task.description)
#     print(task.priority)
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
table_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=mtutorlog;AccountKey=5g/uyxepfdZxjrHETQZ0jDj6y6nsU/t6HAMZdPIr16X5BmBCaLlgb1ybsmpwY6jhNHXP6CXrHYdzS0QLTtyXFw==;EndpointSuffix=core.windows.net')
tasks = table_service.query_entities('SystemTelementry20171202', filter="AppName eq 'Chinese-iOS'")
for task in tasks:
    print(task.SessionId)