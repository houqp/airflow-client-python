# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding: utf-8

"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from airflow_client.api_client import ApiClient
from airflow_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class XComApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_xcom_entries(self, dag_id, dag_run_id, task_id, **kwargs):  # noqa: E501
        """Get all XCom entries  # noqa: E501

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG Runs and task instances.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xcom_entries(dag_id, dag_run_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG Run ID. (required)
        :param str task_id: The Task ID. (required)
        :param int limit: The numbers of items to return.
        :param int offset: The number of items to skip before starting to collect the result set.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XComCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_xcom_entries_with_http_info(dag_id, dag_run_id, task_id, **kwargs)  # noqa: E501

    def get_xcom_entries_with_http_info(self, dag_id, dag_run_id, task_id, **kwargs):  # noqa: E501
        """Get all XCom entries  # noqa: E501

        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG Runs and task instances.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xcom_entries_with_http_info(dag_id, dag_run_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG Run ID. (required)
        :param str task_id: The Task ID. (required)
        :param int limit: The numbers of items to return.
        :param int offset: The number of items to skip before starting to collect the result set.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XComCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'dag_run_id',
            'task_id',
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_xcom_entries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `get_xcom_entries`")  # noqa: E501
        # verify the required parameter 'dag_run_id' is set
        if self.api_client.client_side_validation and ('dag_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_run_id` when calling `get_xcom_entries`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `get_xcom_entries`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_xcom_entries`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501
        if 'dag_run_id' in local_var_params:
            path_params['dag_run_id'] = local_var_params['dag_run_id']  # noqa: E501
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XComCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_xcom_entry(self, dag_id, dag_run_id, task_id, xcom_key, **kwargs):  # noqa: E501
        """Get an XCom entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG Run ID. (required)
        :param str task_id: The Task ID. (required)
        :param str xcom_key: The XCom Key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: XCom
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_xcom_entry_with_http_info(dag_id, dag_run_id, task_id, xcom_key, **kwargs)  # noqa: E501

    def get_xcom_entry_with_http_info(self, dag_id, dag_run_id, task_id, xcom_key, **kwargs):  # noqa: E501
        """Get an XCom entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_xcom_entry_with_http_info(dag_id, dag_run_id, task_id, xcom_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG Run ID. (required)
        :param str task_id: The Task ID. (required)
        :param str xcom_key: The XCom Key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(XCom, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'dag_run_id',
            'task_id',
            'xcom_key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_xcom_entry" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `get_xcom_entry`")  # noqa: E501
        # verify the required parameter 'dag_run_id' is set
        if self.api_client.client_side_validation and ('dag_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_run_id` when calling `get_xcom_entry`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `get_xcom_entry`")  # noqa: E501
        # verify the required parameter 'xcom_key' is set
        if self.api_client.client_side_validation and ('xcom_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['xcom_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `xcom_key` when calling `get_xcom_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501
        if 'dag_run_id' in local_var_params:
            path_params['dag_run_id'] = local_var_params['dag_run_id']  # noqa: E501
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'xcom_key' in local_var_params:
            path_params['xcom_key'] = local_var_params['xcom_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XCom',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
