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


class ConnectionCollectionItem(object):
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
        'connection_id': 'str',
        'conn_type': 'str',
        'host': 'str',
        'login': 'str',
        'schema': 'str',
        'port': 'int'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'conn_type': 'conn_type',
        'host': 'host',
        'login': 'login',
        'schema': 'schema',
        'port': 'port'
    }

    def __init__(self, connection_id=None, conn_type=None, host=None, login=None, schema=None, port=None, local_vars_configuration=None):  # noqa: E501
        """ConnectionCollectionItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_id = None
        self._conn_type = None
        self._host = None
        self._login = None
        self._schema = None
        self._port = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if conn_type is not None:
            self.conn_type = conn_type
        self.host = host
        self.login = login
        self.schema = schema
        self.port = port

    @property
    def connection_id(self):
        """Gets the connection_id of this ConnectionCollectionItem.  # noqa: E501


        :return: The connection_id of this ConnectionCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ConnectionCollectionItem.


        :param connection_id: The connection_id of this ConnectionCollectionItem.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def conn_type(self):
        """Gets the conn_type of this ConnectionCollectionItem.  # noqa: E501


        :return: The conn_type of this ConnectionCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._conn_type

    @conn_type.setter
    def conn_type(self, conn_type):
        """Sets the conn_type of this ConnectionCollectionItem.


        :param conn_type: The conn_type of this ConnectionCollectionItem.  # noqa: E501
        :type: str
        """

        self._conn_type = conn_type

    @property
    def host(self):
        """Gets the host of this ConnectionCollectionItem.  # noqa: E501


        :return: The host of this ConnectionCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ConnectionCollectionItem.


        :param host: The host of this ConnectionCollectionItem.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def login(self):
        """Gets the login of this ConnectionCollectionItem.  # noqa: E501


        :return: The login of this ConnectionCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ConnectionCollectionItem.


        :param login: The login of this ConnectionCollectionItem.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def schema(self):
        """Gets the schema of this ConnectionCollectionItem.  # noqa: E501


        :return: The schema of this ConnectionCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ConnectionCollectionItem.


        :param schema: The schema of this ConnectionCollectionItem.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def port(self):
        """Gets the port of this ConnectionCollectionItem.  # noqa: E501


        :return: The port of this ConnectionCollectionItem.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ConnectionCollectionItem.


        :param port: The port of this ConnectionCollectionItem.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, ConnectionCollectionItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionCollectionItem):
            return True

        return self.to_dict() != other.to_dict()
