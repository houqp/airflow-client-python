<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# airflow-client
Apache Airflow management API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://airflow.apache.org](https://airflow.apache.org)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/apache/airflow-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/apache/airflow-client-python.git`)

Then import the package:
```python
import airflow_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import airflow_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import airflow_client
from airflow_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_client.Configuration(
    host = "http://localhost/api/v1"
)



# Enter a context with an instance of the API client
with airflow_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.ConfigApi(api_client)
    
    try:
        # Get current configuration
        api_response = api_instance.get_config()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /config | Get current configuration
*ConnectionApi* | [**delete_connection**](docs/ConnectionApi.md#delete_connection) | **DELETE** /connections/{connection_id} | Delete a connection entry
*ConnectionApi* | [**get_connection**](docs/ConnectionApi.md#get_connection) | **GET** /connections/{connection_id} | Get a connection entry
*ConnectionApi* | [**get_connections**](docs/ConnectionApi.md#get_connections) | **GET** /connections | Get all connection entries
*ConnectionApi* | [**patch_connection**](docs/ConnectionApi.md#patch_connection) | **PATCH** /connections/{connection_id} | Update a connection entry
*ConnectionApi* | [**post_connection**](docs/ConnectionApi.md#post_connection) | **POST** /connections | Create connection entry
*DAGApi* | [**get_dag**](docs/DAGApi.md#get_dag) | **GET** /dags/{dag_id} | Get basic information about a DAG
*DAGApi* | [**get_dag_details**](docs/DAGApi.md#get_dag_details) | **GET** /dags/{dag_id}/details | Get a simplified representation of DAG
*DAGApi* | [**get_dag_source**](docs/DAGApi.md#get_dag_source) | **GET** /dagSources/{file_token} | Get source code using file token
*DAGApi* | [**get_dags**](docs/DAGApi.md#get_dags) | **GET** /dags | Get all DAGs
*DAGApi* | [**get_task**](docs/DAGApi.md#get_task) | **GET** /dags/{dag_id}/tasks/{task_id} | Get simplified representation of a task
*DAGApi* | [**get_tasks**](docs/DAGApi.md#get_tasks) | **GET** /dags/{dag_id}/tasks | Get tasks for DAG
*DAGApi* | [**patch_dag**](docs/DAGApi.md#patch_dag) | **PATCH** /dags/{dag_id} | Update a DAG
*DAGApi* | [**post_clear_task_instances**](docs/DAGApi.md#post_clear_task_instances) | **POST** /dags/{dag_id}/clearTaskInstances | Clears a set of task instances associated with the DAG for a specified date range.
*DAGRunApi* | [**airflow_api_connexion_endpoints_dag_run_endpoint_post_dag_run**](docs/DAGRunApi.md#airflow_api_connexion_endpoints_dag_run_endpoint_post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a DAG Run
*DAGRunApi* | [**delete_dag_run**](docs/DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG Run
*DAGRunApi* | [**get_dag_run**](docs/DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG Run
*DAGRunApi* | [**get_dag_runs**](docs/DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | Get all DAG Runs
*DAGRunApi* | [**get_dag_runs_batch**](docs/DAGRunApi.md#get_dag_runs_batch) | **POST** /dags/~/dagRuns/list | Get all DAG Runs from all DAGs
*EventLogApi* | [**get_event_log**](docs/EventLogApi.md#get_event_log) | **GET** /eventLogs/{event_log_id} | Get a log entry
*EventLogApi* | [**get_event_logs**](docs/EventLogApi.md#get_event_logs) | **GET** /eventLogs | Get all log entries from event log
*ImportErrorApi* | [**get_import_error**](docs/ImportErrorApi.md#get_import_error) | **GET** /importErrors/{import_error_id} | Get an import error
*ImportErrorApi* | [**get_import_errors**](docs/ImportErrorApi.md#get_import_errors) | **GET** /importErrors | Get all import errors
*MonitoringApi* | [**get_health**](docs/MonitoringApi.md#get_health) | **GET** /health | Returns the status of Airflow&#39;s metadatabase and scheduler
*MonitoringApi* | [**get_version**](docs/MonitoringApi.md#get_version) | **GET** /version | Get version information
*PoolApi* | [**delete_pool**](docs/PoolApi.md#delete_pool) | **DELETE** /pools/{pool_name} | Delete a pool
*PoolApi* | [**get_pool**](docs/PoolApi.md#get_pool) | **GET** /pools/{pool_name} | Get a pool
*PoolApi* | [**get_pools**](docs/PoolApi.md#get_pools) | **GET** /pools | Get all pools
*PoolApi* | [**patch_pool**](docs/PoolApi.md#patch_pool) | **PATCH** /pools/{pool_name} | Update a pool
*PoolApi* | [**post_pool**](docs/PoolApi.md#post_pool) | **POST** /pools | Create a pool
*TaskInstanceApi* | [**get_extra_links**](docs/TaskInstanceApi.md#get_extra_links) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | Get extra links for task instance
*TaskInstanceApi* | [**get_log**](docs/TaskInstanceApi.md#get_log) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Get logs for a task instance
*TaskInstanceApi* | [**get_task_instance**](docs/TaskInstanceApi.md#get_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get a task instance
*TaskInstanceApi* | [**get_task_instances**](docs/TaskInstanceApi.md#get_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | Get a list of task instance of DAG
*TaskInstanceApi* | [**get_task_instances_batch**](docs/TaskInstanceApi.md#get_task_instances_batch) | **POST** /dags/~/dagRuns/~/taskInstances/list | Get list of task instances from all DAGs and DAG Runs.
*VariableApi* | [**delete_variable**](docs/VariableApi.md#delete_variable) | **DELETE** /variables/{variable_key} | Delete variable
*VariableApi* | [**get_variable**](docs/VariableApi.md#get_variable) | **GET** /variables/{variable_key} | Get a variable by key
*VariableApi* | [**get_variables**](docs/VariableApi.md#get_variables) | **GET** /variables | Get all variables
*VariableApi* | [**patch_variable**](docs/VariableApi.md#patch_variable) | **PATCH** /variables/{variable_key} | Update a variable by key
*VariableApi* | [**post_variables**](docs/VariableApi.md#post_variables) | **POST** /variables | Create a variable
*XComApi* | [**get_xcom_entries**](docs/XComApi.md#get_xcom_entries) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | Get all XCom entries
*XComApi* | [**get_xcom_entry**](docs/XComApi.md#get_xcom_entry) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Get an XCom entry


## Documentation For Models

 - [ClassReference](docs/ClassReference.md)
 - [ClearTaskInstance](docs/ClearTaskInstance.md)
 - [CollectionInfo](docs/CollectionInfo.md)
 - [Config](docs/Config.md)
 - [ConfigOption](docs/ConfigOption.md)
 - [ConfigSection](docs/ConfigSection.md)
 - [Connection](docs/Connection.md)
 - [ConnectionAllOf](docs/ConnectionAllOf.md)
 - [ConnectionCollection](docs/ConnectionCollection.md)
 - [ConnectionCollectionItem](docs/ConnectionCollectionItem.md)
 - [CronExpression](docs/CronExpression.md)
 - [DAG](docs/DAG.md)
 - [DAGCollection](docs/DAGCollection.md)
 - [DAGDetail](docs/DAGDetail.md)
 - [DAGDetailAllOf](docs/DAGDetailAllOf.md)
 - [DAGRun](docs/DAGRun.md)
 - [DAGRunCollection](docs/DAGRunCollection.md)
 - [DagState](docs/DagState.md)
 - [Error](docs/Error.md)
 - [EventLog](docs/EventLog.md)
 - [EventLogCollection](docs/EventLogCollection.md)
 - [ExtraLink](docs/ExtraLink.md)
 - [ExtraLinkCollection](docs/ExtraLinkCollection.md)
 - [HealthInfo](docs/HealthInfo.md)
 - [HealthStatus](docs/HealthStatus.md)
 - [ImportError](docs/ImportError.md)
 - [ImportErrorCollection](docs/ImportErrorCollection.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [ListDagRunsForm](docs/ListDagRunsForm.md)
 - [ListTaskInstanceForm](docs/ListTaskInstanceForm.md)
 - [MetadatabaseStatus](docs/MetadatabaseStatus.md)
 - [Pool](docs/Pool.md)
 - [PoolCollection](docs/PoolCollection.md)
 - [RelativeDelta](docs/RelativeDelta.md)
 - [SLAMiss](docs/SLAMiss.md)
 - [SLAMissCollection](docs/SLAMissCollection.md)
 - [ScheduleInterval](docs/ScheduleInterval.md)
 - [SchedulerStatus](docs/SchedulerStatus.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [TaskCollection](docs/TaskCollection.md)
 - [TaskExtraLinks](docs/TaskExtraLinks.md)
 - [TaskFail](docs/TaskFail.md)
 - [TaskInstance](docs/TaskInstance.md)
 - [TaskInstanceCollection](docs/TaskInstanceCollection.md)
 - [TaskInstanceReference](docs/TaskInstanceReference.md)
 - [TaskInstanceReferenceCollection](docs/TaskInstanceReferenceCollection.md)
 - [TaskState](docs/TaskState.md)
 - [TimeDelta](docs/TimeDelta.md)
 - [TriggerRule](docs/TriggerRule.md)
 - [Variable](docs/Variable.md)
 - [VariableAllOf](docs/VariableAllOf.md)
 - [VariableCollection](docs/VariableCollection.md)
 - [VariableCollectionItem](docs/VariableCollectionItem.md)
 - [VersionInfo](docs/VersionInfo.md)
 - [WeightRule](docs/WeightRule.md)
 - [XCom](docs/XCom.md)
 - [XComCollection](docs/XComCollection.md)
 - [XComCollectionItem](docs/XComCollectionItem.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

dev@airflow.apache.org


