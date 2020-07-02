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


class ClearTaskInstance(object):
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
        'dry_run': 'bool',
        'start_date': 'str',
        'end_date': 'str',
        'only_failed': 'str',
        'only_running': 'str',
        'include_subdags': 'bool',
        'include_parentdag': 'bool',
        'reset_dag_runs': 'bool'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'only_failed': 'only_failed',
        'only_running': 'only_running',
        'include_subdags': 'include_subdags',
        'include_parentdag': 'include_parentdag',
        'reset_dag_runs': 'reset_dag_runs'
    }

    def __init__(self, dry_run=True, start_date=None, end_date=None, only_failed=None, only_running=None, include_subdags=None, include_parentdag=None, reset_dag_runs=None, local_vars_configuration=None):  # noqa: E501
        """ClearTaskInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dry_run = None
        self._start_date = None
        self._end_date = None
        self._only_failed = None
        self._only_running = None
        self._include_subdags = None
        self._include_parentdag = None
        self._reset_dag_runs = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if only_failed is not None:
            self.only_failed = only_failed
        if only_running is not None:
            self.only_running = only_running
        if include_subdags is not None:
            self.include_subdags = include_subdags
        if include_parentdag is not None:
            self.include_parentdag = include_parentdag
        if reset_dag_runs is not None:
            self.reset_dag_runs = reset_dag_runs

    @property
    def dry_run(self):
        """Gets the dry_run of this ClearTaskInstance.  # noqa: E501

        If set, don't actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.   # noqa: E501

        :return: The dry_run of this ClearTaskInstance.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ClearTaskInstance.

        If set, don't actually run this operation. The response will contain a list of task instances planned to be cleaned, but not modified in any way.   # noqa: E501

        :param dry_run: The dry_run of this ClearTaskInstance.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def start_date(self):
        """Gets the start_date of this ClearTaskInstance.  # noqa: E501

        The minimum execution date to clear.  # noqa: E501

        :return: The start_date of this ClearTaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ClearTaskInstance.

        The minimum execution date to clear.  # noqa: E501

        :param start_date: The start_date of this ClearTaskInstance.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ClearTaskInstance.  # noqa: E501

        The maximum execution date to clear.  # noqa: E501

        :return: The end_date of this ClearTaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ClearTaskInstance.

        The maximum execution date to clear.  # noqa: E501

        :param end_date: The end_date of this ClearTaskInstance.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def only_failed(self):
        """Gets the only_failed of this ClearTaskInstance.  # noqa: E501

        Only clear failed tasks.  # noqa: E501

        :return: The only_failed of this ClearTaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._only_failed

    @only_failed.setter
    def only_failed(self, only_failed):
        """Sets the only_failed of this ClearTaskInstance.

        Only clear failed tasks.  # noqa: E501

        :param only_failed: The only_failed of this ClearTaskInstance.  # noqa: E501
        :type: str
        """

        self._only_failed = only_failed

    @property
    def only_running(self):
        """Gets the only_running of this ClearTaskInstance.  # noqa: E501

        Only clear running tasks.  # noqa: E501

        :return: The only_running of this ClearTaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._only_running

    @only_running.setter
    def only_running(self, only_running):
        """Sets the only_running of this ClearTaskInstance.

        Only clear running tasks.  # noqa: E501

        :param only_running: The only_running of this ClearTaskInstance.  # noqa: E501
        :type: str
        """

        self._only_running = only_running

    @property
    def include_subdags(self):
        """Gets the include_subdags of this ClearTaskInstance.  # noqa: E501

        Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker.  # noqa: E501

        :return: The include_subdags of this ClearTaskInstance.  # noqa: E501
        :rtype: bool
        """
        return self._include_subdags

    @include_subdags.setter
    def include_subdags(self, include_subdags):
        """Sets the include_subdags of this ClearTaskInstance.

        Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker.  # noqa: E501

        :param include_subdags: The include_subdags of this ClearTaskInstance.  # noqa: E501
        :type: bool
        """

        self._include_subdags = include_subdags

    @property
    def include_parentdag(self):
        """Gets the include_parentdag of this ClearTaskInstance.  # noqa: E501

        Clear tasks in the parent dag of the subdag.  # noqa: E501

        :return: The include_parentdag of this ClearTaskInstance.  # noqa: E501
        :rtype: bool
        """
        return self._include_parentdag

    @include_parentdag.setter
    def include_parentdag(self, include_parentdag):
        """Sets the include_parentdag of this ClearTaskInstance.

        Clear tasks in the parent dag of the subdag.  # noqa: E501

        :param include_parentdag: The include_parentdag of this ClearTaskInstance.  # noqa: E501
        :type: bool
        """

        self._include_parentdag = include_parentdag

    @property
    def reset_dag_runs(self):
        """Gets the reset_dag_runs of this ClearTaskInstance.  # noqa: E501

        Set state of DAG Runs to RUNNING.  # noqa: E501

        :return: The reset_dag_runs of this ClearTaskInstance.  # noqa: E501
        :rtype: bool
        """
        return self._reset_dag_runs

    @reset_dag_runs.setter
    def reset_dag_runs(self, reset_dag_runs):
        """Sets the reset_dag_runs of this ClearTaskInstance.

        Set state of DAG Runs to RUNNING.  # noqa: E501

        :param reset_dag_runs: The reset_dag_runs of this ClearTaskInstance.  # noqa: E501
        :type: bool
        """

        self._reset_dag_runs = reset_dag_runs

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
        if not isinstance(other, ClearTaskInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClearTaskInstance):
            return True

        return self.to_dict() != other.to_dict()
