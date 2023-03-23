from select import select
from azure.cosmosdb.table.tableservice import TableService

# Ansluter till vår table storage service
table_service = TableService(account_name="storagehub2", account_key= "Ibinav35Kvz9a4Zf2HMPB3naZhU2KTXzg+FasHIw+F6v9q+aHnz3GdV9N7UELXP8Kzvu5LLlhuhhYwixyTkp4w==")

# Vår tabell
Data = "SensorData"
# Filterar ut de värden vi vill ha från tabllen
tasks = table_service.query_entities(Data, filter="PartitionKey eq 'tasksSeattle'", select='Temperatur , Luftfuktighet')
Table = {"Temperatur" : [], "Luftfuktighet" : []}

# Lister ut alla värden från tabllen
for task in tasks:
    Table["Temperatur"].append(task['Temperatur']) 
    Table["Luftfuktighet"].append(task['Luftfuktighet'])

# Skriveer ut sista värdet i tabllen
print("Sista v" u"ä" "rdet fr" u"å" "n tabellen " + Data,":")
print("Temperauter: ", list(Table['Temperatur'])[-1])
print("Luftfuktighet: ", list(Table['Luftfuktighet'])[-1])