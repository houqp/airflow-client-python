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

# airflow_client.MonitoringApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](MonitoringApi.md#get_health) | **GET** /health | Returns the status of Airflow&#39;s metadatabase and scheduler
[**get_version**](MonitoringApi.md#get_version) | **GET** /version | Get version information


# **get_health**
> HealthInfo get_health()

Returns the status of Airflow's metadatabase and scheduler

### Example

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
with airflow_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.MonitoringApi(api_client)
    
    try:
        # Returns the status of Airflow's metadatabase and scheduler
        api_response = api_instance.get_health()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthInfo**](HealthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns info about metadatabase and last heart beat. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionInfo get_version()

Get version information

### Example

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
with airflow_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = airflow_client.MonitoringApi(api_client)
    
    try:
        # Get version information
        api_response = api_instance.get_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return current configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

