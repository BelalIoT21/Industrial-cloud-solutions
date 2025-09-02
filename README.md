# Industrial Cloud Solutions ☁️🏭

A comprehensive cloud-based industrial IoT solution built on Microsoft Azure, designed for real-time sensor data ingestion, processing, and storage. This system provides scalable infrastructure for monitoring industrial equipment and environmental conditions through advanced cloud services.

![Azure IoT](https://img.shields.io/badge/Azure-IoT%20Solutions-blue)
[![Python](https://img.shields.io/badge/Python-3.6%2B-brightgreen)](https://python.org)
[![Azure Functions](https://img.shields.io/badge/Azure-Functions-orange)](https://azure.microsoft.com/services/functions/)
[![Event Hub](https://img.shields.io/badge/Azure-Event%20Hub-red)](https://azure.microsoft.com/services/event-hubs/)
[![Table Storage](https://img.shields.io/badge/Azure-Table%20Storage-lightblue)](https://azure.microsoft.com/services/storage/tables/)
[![GitHub stars](https://img.shields.io/github/stars/BelalIoT21/Industrial-cloud-solutions)](https://github.com/BelalIoT21/Industrial-cloud-solutions/stargazers)

## 🎯 Overview

Industrial Cloud Solutions provides a robust, scalable, and enterprise-ready platform for Industrial IoT (IIoT) applications. Built on Microsoft Azure's cloud infrastructure, this solution enables seamless data flow from industrial sensors to cloud storage, with real-time processing capabilities for monitoring temperature, humidity, and other critical environmental parameters.

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐    ┌──────────────────┐
│   IoT Devices   │───▶│   Azure IoT Hub  │───▶│   Azure Event Hub   │───▶│ Azure Functions  │
│  (Sensors)      │    │                  │    │                     │    │  (Processing)    │
└─────────────────┘    └──────────────────┘    └─────────────────────┘    └─────────┬────────┘
                                                                                      │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐              │
│   Data Analytics│◀───│  Table Storage   │◀───│   Processed Data    │◀─────────────┘
│   & Reporting   │    │   Repository     │    │    Validation       │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
```

## ✨ Key Features

### 🔄 Real-Time Data Ingestion
- **Azure Event Hub Integration**: High-throughput data ingestion from multiple IoT devices
- **Scalable Message Processing**: Handle millions of events per second
- **Device-to-Cloud Communication**: Secure and reliable data transmission
- **Multi-Protocol Support**: MQTT, AMQP, and HTTPS protocols

### ⚡ Serverless Processing
- **Azure Functions**: Event-driven, serverless compute platform
- **Automatic Scaling**: Scale based on incoming data volume
- **Cost-Effective**: Pay-per-execution pricing model
- **Real-Time Triggers**: Instant processing of incoming sensor data

### 📊 Data Storage & Management
- **Azure Table Storage**: NoSQL storage for structured sensor data
- **High Availability**: 99.9% SLA with geo-redundant options
- **Flexible Schema**: Easy adaptation to new sensor types
- **Query Optimization**: Fast data retrieval and analysis

### 🌡️ Sensor Data Processing
- **Temperature Monitoring**: Real-time temperature data processing
- **Humidity Tracking**: Environmental humidity level monitoring
- **Data Validation**: Input validation and error handling
- **Historical Analytics**: Time-series data analysis capabilities

### 🔒 Enterprise Security
- **Azure Active Directory**: Identity and access management
- **End-to-End Encryption**: Data encryption in transit and at rest
- **Role-Based Access**: Granular permission management
- **Compliance Ready**: Industry standard compliance support

## 📋 Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Monitoring](#monitoring)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🔧 Prerequisites

### Azure Resources
- **Azure Subscription**: Active Azure account with appropriate permissions
- **Resource Group**: Dedicated resource group for the solution
- **Storage Account**: For Table Storage and function storage needs
- **Event Hub Namespace**: For high-throughput data ingestion
- **IoT Hub**: For device management and connectivity
- **Function App**: For serverless compute capabilities

### Development Environment
- **Python 3.6+**: Compatible Python runtime environment
- **Azure CLI**: Latest version for resource management
- **Azure Functions Core Tools**: Version 4.x for local development
- **Visual Studio Code**: Recommended IDE with Azure extensions

### Azure CLI Installation
```bash
# Windows (using PowerShell)
Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'

# macOS (using Homebrew)
brew update && brew install azure-cli

# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

### Azure Functions Core Tools
```bash
# Install globally via npm
npm install -g azure-functions-core-tools@4 --unsafe-perm true

# Verify installation
func --version
```

## 🚀 Installation

### 1. Clone Repository
```bash
# Clone the repository
git clone https://github.com/BelalIoT21/Industrial-cloud-solutions.git

# Navigate to project directory
cd Industrial-cloud-solutions

# Explore project structure
ls -la "Examination tasks/"
```

### 2. Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv industrial-iot-env

# Activate virtual environment
# Windows
industrial-iot-env\Scripts\activate
# macOS/Linux
source industrial-iot-env/bin/activate

# Install required packages
pip install -r "Examination tasks/Azure Function/requirements.txt"

# Additional packages for development
pip install azure-iot-device azure-cosmosdb-table azure-functions azure-eventHub
```

### 3. Azure Resource Setup
```bash
# Login to Azure
az login

# Set default subscription
az account set --subscription "Your-Subscription-ID"

# Create resource group
az group create --name "industrial-iot-rg" --location "East US"

# Create storage account
az storage account create \
  --name "industrialiotstorage" \
  --resource-group "industrial-iot-rg" \
  --location "East US" \
  --sku "Standard_LRS"

# Create Event Hub namespace
az eventhubs namespace create \
  --name "industrial-iot-eventhub" \
  --resource-group "industrial-iot-rg" \
  --location "East US" \
  --sku "Standard"

# Create Event Hub
az eventhubs eventhub create \
  --name "sensor-data-hub" \
  --namespace-name "industrial-iot-eventhub" \
  --resource-group "industrial-iot-rg"

# Create IoT Hub
az iot hub create \
  --name "industrial-iot-hub" \
  --resource-group "industrial-iot-rg" \
  --location "East US" \
  --sku "S1"
```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# Azure IoT Hub Configuration
IOT_HUB_CONNECTION_STRING=HostName=industrial-iot-hub.azure-devices.net;DeviceId=sensor-device-01;SharedAccessKey=your-device-key

# Azure Event Hub Configuration
EVENT_HUB_CONNECTION_STRING=Endpoint=sb://industrial-iot-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your-eventhub-key
EVENT_HUB_NAME=sensor-data-hub

# Azure Storage Configuration
STORAGE_ACCOUNT_NAME=industrialiotstorage
STORAGE_ACCOUNT_KEY=your-storage-account-key
TABLE_NAME=SensorData

# Azure Function Configuration
FUNCTIONS_WORKER_RUNTIME=python
AzureWebJobsStorage=DefaultEndpointsProtocol=https;AccountName=industrialiotstorage;AccountKey=your-key

# Application Settings
SENSOR_READING_INTERVAL=3
TEMPERATURE_MIN=20
TEMPERATURE_MAX=30
HUMIDITY_MIN=60
HUMIDITY_MAX=80
```

### IoT Device Configuration
Update `Examination tasks/d2cMsgSender.py`:

```python
import random
import time
import os
import json
from azure.iot.device import IoTHubDeviceClient, Message
from datetime import datetime

# Configuration
CONNECTION_STRING = os.getenv('IOT_HUB_CONNECTION_STRING', '<YOUR_IOTHUB_DEVICE_CONNECTION_STRING>')
READING_INTERVAL = int(os.getenv('SENSOR_READING_INTERVAL', 3))

def iothub_client_init():
    """Initialize IoT Hub client"""
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print("IoT Hub client initialized successfully")
        return client
    except Exception as e:
        print(f"Error initializing IoT Hub client: {e}")
        return None

def generate_sensor_data():
    """Generate realistic sensor data"""
    temperature = round(random.uniform(18.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 90.0), 2)
    pressure = round(random.uniform(980.0, 1020.0), 2)
    timestamp = datetime.utcnow().isoformat()
    
    return {
        "deviceId": "sensor-device-01",
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "location": "Factory Floor A",
        "sensorType": "Environmental"
    }

def send_telemetry():
    """Send telemetry data to IoT Hub"""
    client = iothub_client_init()
    if not client:
        return
    
    try:
        print("Starting telemetry transmission...")
        print("Press Ctrl-C to stop")
        
        while True:
            # Generate sensor data
            sensor_data = generate_sensor_data()
            
            # Create message
            message = Message(json.dumps(sensor_data))
            message.content_encoding = "utf-8"
            message.content_type = "application/json"
            
            # Add message properties
            message.custom_properties["temperatureAlert"] = "true" if sensor_data["temperature"] > 30 else "false"
            message.custom_properties["humidityAlert"] = "true" if sensor_data["humidity"] > 80 else "false"
            
            # Send message
            print(f"Sending: {json.dumps(sensor_data, indent=2)}")
            client.send_message(message)
            print("✓ Message sent successfully")
            
            time.sleep(READING_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n🛑 Telemetry transmission stopped by user")
    except Exception as e:
        print(f"❌ Error sending telemetry: {e}")
    finally:
        client.shutdown()

if __name__ == '__main__':
    send_telemetry()
```

### Table Storage Reader Configuration
Update `Examination tasks/tableStrogeReader.py`:

```python
import os
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import pandas as pd
from datetime import datetime, timedelta

# Configuration
STORAGE_ACCOUNT_NAME = os.getenv('STORAGE_ACCOUNT_NAME', '<YOUR_STORAGE_ACCOUNT_NAME>')
STORAGE_ACCOUNT_KEY = os.getenv('STORAGE_ACCOUNT_KEY', '<YOUR_STORAGE_ACCOUNT_KEY>')
TABLE_NAME = os.getenv('TABLE_NAME', 'SensorData')

class SensorDataReader:
    def __init__(self):
        """Initialize Table Storage connection"""
        self.table_service = TableService(
            account_name=STORAGE_ACCOUNT_NAME,
            account_key=STORAGE_ACCOUNT_KEY
        )
        self.table_name = TABLE_NAME
        
    def get_latest_readings(self, limit=10):
        """Get latest sensor readings"""
        try:
            tasks = self.table_service.query_entities(
                self.table_name,
                select='PartitionKey,RowKey,Timestamp,Temperature,Humidity,DeviceId',
                num_results=limit
            )
            
            readings = []
            for task in tasks:
                reading = {
                    'DeviceId': getattr(task, 'DeviceId', 'Unknown'),
                    'Temperature': getattr(task, 'Temperature', 0),
                    'Humidity': getattr(task, 'Humidity', 0),
                    'Timestamp': getattr(task, 'Timestamp', datetime.now())
                }
                readings.append(reading)
            
            return readings
            
        except Exception as e:
            print(f"Error reading from table storage: {e}")
            return []
    
    def get_readings_by_time_range(self, start_time, end_time):
        """Get readings within specific time range"""
        try:
            filter_query = f"Timestamp ge datetime'{start_time.isoformat()}' and Timestamp le datetime'{end_time.isoformat()}'"
            
            tasks = self.table_service.query_entities(
                self.table_name,
                filter=filter_query,
                select='Temperature,Humidity,Timestamp,DeviceId'
            )
            
            return list(tasks)
            
        except Exception as e:
            print(f"Error querying time range: {e}")
            return []
    
    def get_temperature_alerts(self, threshold=30.0):
        """Get readings with high temperature alerts"""
        try:
            filter_query = f"Temperature gt {threshold}"
            
            alerts = self.table_service.query_entities(
                self.table_name,
                filter=filter_query
            )
            
            return list(alerts)
            
        except Exception as e:
            print(f"Error getting temperature alerts: {e}")
            return []
    
    def export_to_csv(self, filename=None):
        """Export sensor data to CSV file"""
        if not filename:
            filename = f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            all_readings = self.get_latest_readings(1000)  # Get last 1000 readings
            
            if all_readings:
                df = pd.DataFrame(all_readings)
                df.to_csv(filename, index=False)
                print(f"✓ Data exported to {filename}")
                return filename
            else:
                print("No data available to export")
                return None
                
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return None

# Usage example
if __name__ == '__main__':
    reader = SensorDataReader()
    
    # Get latest readings
    print("📊 Latest Sensor Readings:")
    latest = reader.get_latest_readings(5)
    for reading in latest:
        print(f"🌡️ Temperature: {reading['Temperature']}°C | 💧 Humidity: {reading['Humidity']}% | 📅 {reading['Timestamp']}")
    
    # Get temperature alerts
    print("\n🚨 High Temperature Alerts:")
    alerts = reader.get_temperature_alerts(25.0)
    for alert in alerts[:5]:  # Show first 5 alerts
        temp = getattr(alert, 'Temperature', 'N/A')
        timestamp = getattr(alert, 'Timestamp', 'N/A')
        device = getattr(alert, 'DeviceId', 'Unknown')
        print(f"🔥 Device: {device} | Temperature: {temp}°C | Time: {timestamp}")
    
    # Export to CSV
    print("\n📁 Exporting data to CSV...")
    filename = reader.export_to_csv()
```

### Azure Function Configuration
Update `Examination tasks/Azure Function/EventHubTrigger1/__init__.py`:

```python
import logging
import json
import os
from datetime import datetime
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

# Configuration
STORAGE_ACCOUNT_NAME = os.getenv('STORAGE_ACCOUNT_NAME')
STORAGE_ACCOUNT_KEY = os.getenv('STORAGE_ACCOUNT_KEY')
TABLE_NAME = os.getenv('TABLE_NAME', 'SensorData')

def main(events: func.EventHubEvent):
    """Process Event Hub messages and store in Table Storage"""
    
    # Initialize table service
    table_service = TableService(
        account_name=STORAGE_ACCOUNT_NAME,
        account_key=STORAGE_ACCOUNT_KEY
    )
    
    # Ensure table exists
    table_service.create_table(TABLE_NAME, fail_on_exist=False)
    
    for event in events:
        try:
            # Parse event data
            event_body = event.get_body().decode('utf-8')
            sensor_data = json.loads(event_body)
            
            logging.info(f'Processing sensor data: {sensor_data}')
            
            # Extract sensor values
            device_id = sensor_data.get('deviceId', 'unknown-device')
            temperature = sensor_data.get('temperature', 0)
            humidity = sensor_data.get('humidity', 0)
            pressure = sensor_data.get('pressure', 0)
            timestamp = sensor_data.get('timestamp', datetime.utcnow().isoformat())
            location = sensor_data.get('location', 'Unknown')
            
            # Create entity for Table Storage
            entity = Entity()
            entity.PartitionKey = f'device-{device_id}'
            entity.RowKey = f'{datetime.utcnow().strftime("%Y%m%d%H%M%S")}-{device_id}'
            entity.DeviceId = device_id
            entity.Temperature = float(temperature)
            entity.Humidity = float(humidity)
            entity.Pressure = float(pressure) if pressure else 0
            entity.Location = location
            entity.Timestamp = timestamp
            entity.ProcessedAt = datetime.utcnow().isoformat()
            
            # Add alert flags
            entity.TemperatureAlert = temperature > 30
            entity.HumidityAlert = humidity > 80
            entity.AlertLevel = get_alert_level(temperature, humidity)
            
            # Insert entity into Table Storage
            table_service.insert_entity(TABLE_NAME, entity)
            
            logging.info(f'✓ Successfully stored data for device {device_id}')
            
            # Log alerts
            if entity.TemperatureAlert:
                logging.warning(f'🔥 High temperature alert: {temperature}°C for device {device_id}')
            
            if entity.HumidityAlert:
                logging.warning(f'💧 High humidity alert: {humidity}% for device {device_id}')
                
        except Exception as e:
            logging.error(f'❌ Error processing event: {str(e)}')
            logging.error(f'Event data: {event.get_body().decode("utf-8")}')

def get_alert_level(temperature, humidity):
    """Determine alert level based on sensor values"""
    if temperature > 35 or humidity > 90:
        return 'CRITICAL'
    elif temperature > 30 or humidity > 80:
        return 'WARNING'
    elif temperature < 15 or humidity < 30:
        return 'LOW'
    else:
        return 'NORMAL'
```

## 🚀 Deployment

### Local Development
```bash
# Start Azure Function locally
cd "Examination tasks/Azure Function"

# Install dependencies
pip install -r requirements.txt

# Start function host
func start --python

# Test the function locally
func new --name EventHubTrigger1 --template "Azure Event Hub trigger"
```

### Azure Function Deployment
```bash
# Create Function App
az functionapp create \
  --resource-group industrial-iot-rg \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.9 \
  --functions-version 4 \
  --name industrial-iot-functions \
  --storage-account industrialiotstorage

# Configure application settings
az functionapp config appsettings set \
  --name industrial-iot-functions \
  --resource-group industrial-iot-rg \
  --settings \
    STORAGE_ACCOUNT_NAME=industrialiotstorage \
    STORAGE_ACCOUNT_KEY=your-storage-key \
    TABLE_NAME=SensorData \
    EVENT_HUB_CONNECTION_STRING=your-eventhub-connection

# Deploy function
func azure functionapp publish industrial-iot-functions
```

### Infrastructure as Code (ARM Template)
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "solutionName": {
      "type": "string",
      "defaultValue": "industrial-iot"
    }
  },
  "variables": {
    "storageAccountName": "[concat(parameters('solutionName'), 'storage')]",
    "iotHubName": "[concat(parameters('solutionName'), '-hub')]",
    "eventHubNamespaceName": "[concat(parameters('solutionName'), '-eventhub')]",
    "functionAppName": "[concat(parameters('solutionName'), '-functions')]"
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-06-01",
      "name": "[variables('storageAccountName')]",
      "location": "[resourceGroup().location]",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2"
    },
    {
      "type": "Microsoft.Devices/IotHubs",
      "apiVersion": "2021-07-02",
      "name": "[variables('iotHubName')]",
      "location": "[resourceGroup().location]",
      "sku": {
        "name": "S1",
        "capacity": 1
      }
    }
  ]
}
```

### Docker Deployment
```dockerfile
# Dockerfile for IoT simulator
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY "Examination tasks/" ./examination-tasks/

ENV IOT_HUB_CONNECTION_STRING=""
ENV SENSOR_READING_INTERVAL=3

CMD ["python", "examination-tasks/d2cMsgSender.py"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  iot-simulator:
    build: .
    environment:
      - IOT_HUB_CONNECTION_STRING=${IOT_HUB_CONNECTION_STRING}
      - SENSOR_READING_INTERVAL=5
    restart: unless-stopped
    
  data-reader:
    build: .
    command: python examination-tasks/tableStrogeReader.py
    environment:
      - STORAGE_ACCOUNT_NAME=${STORAGE_ACCOUNT_NAME}
      - STORAGE_ACCOUNT_KEY=${STORAGE_ACCOUNT_KEY}
      - TABLE_NAME=SensorData
    volumes:
      - ./exports:/app/exports
    depends_on:
      - iot-simulator
```

## 📊 Usage Examples

### Running the IoT Simulator
```bash
# Set environment variables
export IOT_HUB_CONNECTION_STRING="HostName=your-hub.azure-devices.net;DeviceId=sensor-01;SharedAccessKey=your-key"

# Run the simulator
python "Examination tasks/d2cMsgSender.py"

# Output:
# Starting telemetry transmission...
# Sending: {
#   "deviceId": "sensor-device-01",
#   "timestamp": "2024-01-15T10:30:00.123Z",
#   "temperature": 23.45,
#   "humidity": 67.8,
#   "pressure": 1013.25
# }
# ✓ Message sent successfully
```

### Reading Stored Data
```bash
# Set environment variables
export STORAGE_ACCOUNT_NAME="industrialiotstorage"
export STORAGE_ACCOUNT_KEY="your-storage-key"

# Run the data reader
python "Examination tasks/tableStrogeReader.py"

# Output:
# 📊 Latest Sensor Readings:
# 🌡️ Temperature: 23.45°C | 💧 Humidity: 67.8% | 📅 2024-01-15T10:30:00
# 🌡️ Temperature: 24.12°C | 💧 Humidity: 65.3% | 📅 2024-01-15T10:33:00
```

### API Integration Example
```python
import requests
import json
from datetime import datetime, timedelta

class IndustrialIoTAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
    
    def get_device_status(self, device_id):
        """Get current device status"""
        response = requests.get(
            f"{self.base_url}/devices/{device_id}/status",
            headers=self.headers
        )
        return response.json()
    
    def get_sensor_data(self, device_id, hours=24):
        """Get sensor data for specified time period"""
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=hours)
        
        params = {
            'start': start_time.isoformat(),
            'end': end_time.isoformat()
        }
        
        response = requests.get(
            f"{self.base_url}/devices/{device_id}/data",
            params=params,
            headers=self.headers
        )
        return response.json()
    
    def create_alert_rule(self, device_id, condition, threshold):
        """Create new alert rule"""
        data = {
            'deviceId': device_id,
            'condition': condition,
            'threshold': threshold,
            'enabled': True
        }
        
        response = requests.post(
            f"{self.base_url}/alerts/rules",
            json=data,
            headers=self.headers
        )
        return response.json()

# Usage example
api = IndustrialIoTAPI("https://your-api-endpoint.azurewebsites.net/api", "your-api-key")

# Get device status
status = api.get_device_status("sensor-device-01")
print(f"Device Status: {status}")

# Get last 24 hours of data
data = api.get_sensor_data("sensor-device-01", hours=24)
print(f"Retrieved {len(data)} sensor readings")

# Create temperature alert
alert_rule = api.create_alert_rule("sensor-device-01", "temperature", 30.0)
print(f"Alert rule created: {alert_rule}")
```

## 📈 Monitoring & Analytics

### Azure Monitor Integration
```python
from azure.monitor.query import LogsQueryClient, MetricsQueryClient
from azure.identity import DefaultAzureCredential

class IoTMonitoring:
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.logs_client = LogsQueryClient(self.credential)
        self.metrics_client = MetricsQueryClient(self.credential)
    
    def query_function_logs(self, time_range="PT1H"):
        """Query Azure Function execution logs"""
        query = """
        FunctionAppLogs
        | where TimeGenerated > ago(1h)
        | where FunctionName == "EventHubTrigger1"
        | project TimeGenerated, Level, Message
        | order by TimeGenerated desc
        """
        
        result = self.logs_client.query_workspace(
            workspace_id="your-workspace-id",
            query=query,
            timespan=time_range
        )
        
        return result.tables[0].rows
    
    def get_iot_hub_metrics(self):
        """Get IoT Hub telemetry metrics"""
        metrics = self.metrics_client.query_resource(
            resource_uri="/subscriptions/{subscription}/resourceGroups/{rg}/providers/Microsoft.Devices/IotHubs/{hub}",
            metric_names=["d2c.telemetry.ingress.allProtocols", "d2c.telemetry.ingress.success"],
            granularity="PT1M"
        )
        
        return metrics
```

### Custom Dashboard with Power BI
```python
# Power BI integration for custom dashboards
import requests
import json

class PowerBIDashboard:
    def __init__(self, workspace_id, dataset_id, access_token):
        self.workspace_id = workspace_id
        self.dataset_id = dataset_id
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        self.base_url = "https://api.powerbi.com/v1.0/myorg"
    
    def push_sensor_data(self, sensor_readings):
        """Push sensor data to Power BI dataset"""
        url = f"{self.base_url}/groups/{self.workspace_id}/datasets/{self.dataset_id}/rows"
        
        # Transform data for Power BI
        power_bi_data = {
            "rows": [
                {
                    "DeviceId": reading['DeviceId'],
                    "Temperature": reading['Temperature'],
                    "Humidity": reading['Humidity'],
                    "Timestamp": reading['Timestamp'],
                    "Location": reading.get('Location', 'Unknown')
                }
                for reading in sensor_readings
            ]
        }
        
        response = requests.post(url, json=power_bi_data, headers=self.headers)
        return response.status_code == 200
```

## 🔍 Troubleshooting

### Common Issues and Solutions

#### Connection String Issues
```python
def validate_connection_string(connection_string, connection_type):
    """Validate Azure connection strings"""
    required_components = {
        'iot_hub': ['HostName', 'DeviceId', 'SharedAccessKey'],
        'storage': ['DefaultEndpointsProtocol
