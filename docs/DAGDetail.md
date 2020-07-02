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

# DAGDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] [readonly] 
**root_dag_id** | **str** |  | [optional] [readonly] 
**is_paused** | **bool** |  | [optional] 
**is_subdag** | **bool** |  | [optional] [readonly] 
**fileloc** | **str** |  | [optional] [readonly] 
**file_token** | **str** | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  | [optional] [readonly] 
**owners** | **list[str]** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**schedule_interval** | [**ScheduleInterval**](ScheduleInterval.md) |  | [optional] 
**tags** | [**list[Tag]**](Tag.md) |  | [optional] [readonly] 
**timezone** | **str** |  | [optional] 
**catchup** | **bool** |  | [optional] [readonly] 
**orientation** | **str** |  | [optional] [readonly] 
**concurrency** | **float** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**dag_run_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**doc_md** | **str** |  | [optional] [readonly] 
**default_view** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


