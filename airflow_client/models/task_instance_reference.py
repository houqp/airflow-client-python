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


import pprint
import re  # noqa: F401

import six

from airflow_client.configuration import Configuration


class TaskInstanceReference(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'task_id': 'str',
        'dag_id': 'str',
        'execution_date': 'str',
        'dag_run_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'dag_id': 'dag_id',
        'execution_date': 'execution_date',
        'dag_run_id': 'dag_run_id'
    }

    def __init__(self, task_id=None, dag_id=None, execution_date=None, dag_run_id=None, local_vars_configuration=None):  # noqa: E501
        """TaskInstanceReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._task_id = None
        self._dag_id = None
        self._execution_date = None
        self._dag_run_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if dag_id is not None:
            self.dag_id = dag_id
        if execution_date is not None:
            self.execution_date = execution_date
        if dag_run_id is not None:
            self.dag_run_id = dag_run_id

    @property
    def task_id(self):
        """Gets the task_id of this TaskInstanceReference.  # noqa: E501


        :return: The task_id of this TaskInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskInstanceReference.


        :param task_id: The task_id of this TaskInstanceReference.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def dag_id(self):
        """Gets the dag_id of this TaskInstanceReference.  # noqa: E501


        :return: The dag_id of this TaskInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._dag_id

    @dag_id.setter
    def dag_id(self, dag_id):
        """Sets the dag_id of this TaskInstanceReference.


        :param dag_id: The dag_id of this TaskInstanceReference.  # noqa: E501
        :type: str
        """

        self._dag_id = dag_id

    @property
    def execution_date(self):
        """Gets the execution_date of this TaskInstanceReference.  # noqa: E501


        :return: The execution_date of this TaskInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this TaskInstanceReference.


        :param execution_date: The execution_date of this TaskInstanceReference.  # noqa: E501
        :type: str
        """

        self._execution_date = execution_date

    @property
    def dag_run_id(self):
        """Gets the dag_run_id of this TaskInstanceReference.  # noqa: E501


        :return: The dag_run_id of this TaskInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._dag_run_id

    @dag_run_id.setter
    def dag_run_id(self, dag_run_id):
        """Sets the dag_run_id of this TaskInstanceReference.


        :param dag_run_id: The dag_run_id of this TaskInstanceReference.  # noqa: E501
        :type: str
        """

        self._dag_run_id = dag_run_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskInstanceReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskInstanceReference):
            return True

        return self.to_dict() != other.to_dict()
