# Industrial Cloud Solutions

This repository contains code related to industrial cloud solutions, focusing on data ingestion, processing, and storage using Azure services. The included code snippets provides a system for processing sensor data (temperature and humidity) from IoT devices and storing it in Azure Table Storage. This also involves an Azure Function triggered by an Event Hub.

## Key Features & Benefits

*   **IoT Data Ingestion:**  Receives sensor data from IoT devices via Azure Event Hub.
*   **Data Processing:** Extracts temperature and humidity values from the incoming data.
*   **Data Storage:** Persists the processed data into Azure Table Storage for further analysis and reporting.
*   **Event-Driven Architecture:**  Utilizes Azure Functions for serverless, event-driven processing.
*   **Azure Integration:** Leverages several core Azure services including Event Hub, Functions, and Table Storage.

## Prerequisites & Dependencies

Before you can run this project, you'll need the following:

*   **Python 3.6+:** Ensure you have a compatible Python version installed.
*   **Azure Account:** You'll need an active Azure subscription.
*   **Azure CLI:** The Azure Command-Line Interface is required for managing Azure resources.
*   **Azure Functions Core Tools:**  Used for local development and deployment of Azure Functions. Install using `npm install -g azure-functions-core-tools@4 --unsafe-perm true`
*   **Python Packages:** Install the required Python packages using `pip install -r Examination tasks/Azure Function/requirements.txt`

## Installation & Setup Instructions

Follow these steps to set up and run the project:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/BelalIoT21/Industrial-cloud-solutions.git
    cd Industrial-cloud-solutions
    ```

2.  **Create Azure Resources:**

    *   Create an Azure Event Hub:  Configure an Event Hub in the Azure portal or using the Azure CLI to receive IoT device data.
    *   Create an Azure Storage Account:  Provision an Azure Storage Account for storing data in Table Storage.
    *   Create an Azure Function App:  Set up an Azure Function App to host the `EventHubTrigger1` function.

3.  **Configure the Azure Function:**

    *   **Connection Strings:**  Update the `CONNECTION_STRING` variable in `Examination tasks/d2cMsgSender.py` with your IoT Hub device connection string. This script simulates sending messages to Event Hub.
    *   **Storage Account Keys:** Modify the `table_service` initialization in `Examination tasks/tableStrogeReader.py` with your Storage Account name and key.  Also, update the `Examination tasks/Azure Function/EventHubTrigger1/__init__.py` file with the appropriate storage account connection details.
    *   **Event Hub Connection String:** Configure the Event Hub trigger in your Azure Function App with the connection string for the Event Hub.  This can be done through the Azure portal or using the Azure CLI.

4.  **Deploy the Azure Function:**

    *   Navigate to the Azure Function directory: `cd "Examination tasks/Azure Function"`
    *   Deploy using func azure functionapp publish <YOUR_FUNCTION_APP_NAME>

5.  **Run the IoT Device Simulator:**

    *   Execute `Examination tasks/d2cMsgSender.py` to simulate sending sensor data to the Event Hub.  Ensure the `CONNECTION_STRING` is correctly configured.

6.  **Verify Data Storage:**

    *   Check the Azure Table Storage to confirm that the processed sensor data is being stored correctly.

## Usage Examples & API Documentation

### Sending Data to Event Hub (d2cMsgSender.py)

This script simulates sending temperature and humidity data to the Event Hub.  You'll need to replace the placeholder `CONNECTION_STRING` with your actual device connection string.

```python
import random
import time
import os
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

CONNECTION_STRING = "<YOUR_IOTHUB_DEVICE_CONNECTION_STRING>" # Replace with your connection string

def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "Sending data to IoT Hub, press Ctrl-C to exit" )

        while True:
            # Simulate telemetry.
            temperature = random.randint(20, 30)
            humidity = random.randint(60, 80)
            msg_txt_formatted = "{\"temperature\": " + str(temperature) + ", \"humidity\": " + str(humidity) + "}"
            message = Message(msg_txt_formatted)

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to interrupt" )
    iothub_client_telemetry_sample_run()
```

### Reading Data from Table Storage (tableStrogeReader.py)

This script retrieves data from the Azure Table Storage. You'll need to update the `account_name` and `account_key` with your Storage Account credentials.

```python
from select import select
from azure.cosmosdb.table.tableservice import TableService

# Ansluter till vår table storage service
table_service = TableService(account_name="<YOUR_STORAGE_ACCOUNT_NAME>", account_key= "<YOUR_STORAGE_ACCOUNT_KEY>")

# Vår tabell
Data = "SensorData"
# Filterar ut de värden vi vill ha från tabllen
tasks = table_service.query_entities(Data, filter="PartitionKey eq 'tasksSeattle'", select='Temperatur , Luftfuktighet')
Table =[]
for task in tasks:
    Table.append([task.Temperatur,task.Luftfuktighet])

print(Table)
```

## Configuration Options

*   **IoT Hub Connection String:**  Configures the connection to the IoT Hub for sending data.  Set in `Examination tasks/d2cMsgSender.py`.
*   **Storage Account Credentials:**  Used to access the Azure Table Storage. Configure in `Examination tasks/tableStrogeReader.py` and `Examination tasks/Azure Function/EventHubTrigger1/__init__.py`.
*   **Event Hub Connection String:**  Configures the Event Hub trigger in the Azure Function. Set through the Azure portal or CLI.
*   **Table Name:** The name of the table in the storage account can be configured by changing `Data` Variable in `tableStrogeReader.py`

## Contributing Guidelines

We welcome contributions to this project! To contribute, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive messages.
4.  Submit a pull request to the main branch.

## License Information

License not specified. All rights reserved by the owner.

## Acknowledgments

This project utilizes the following third-party libraries and services:

*   Azure IoT SDK for Python
*   Azure Functions
*   Azure Event Hub
*   Azure Table Storage
