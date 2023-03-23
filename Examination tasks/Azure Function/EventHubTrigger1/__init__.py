from typing import List
import logging
import uuid
from azure.cosmosdb.table.tableservice import TableService
import azure.functions as func
import json


def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s', event.get_body().decode('utf-8'))
        Temperatur = json.loads(event.get_body().decode('utf-8'))
        temp1 = Temperatur["temperature"]
        luftf = Temperatur["humidity"]

    rowKey = str(uuid.uuid4())
    
    table_service = TableService(account_name="storagehub2", account_key= "Ibinav35Kvz9a4Zf2HMPB3naZhU2KTXzg+FasHIw+F6v9q+aHnz3GdV9N7UELXP8Kzvu5LLlhuhhYwixyTkp4w==")

    task = {}
    task['PartitionKey'] = 'tasksSeattle'
    task['RowKey'] = rowKey
    task['Temperatur'] = temp1
    task['Luftfuktighet'] = luftf
    logging.info("ladde till data %s", task)
    table_service.insert_entity("SensorData", task)