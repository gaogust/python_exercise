
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
table_service = TableService(connection_string='')
tasks = table_service.query_entities('', filter="AppName eq 'Chinese-iOS'")
for task in tasks:
    print(task.SessionId)
