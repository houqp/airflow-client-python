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


class ExtraLink(object):
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
        'class_ref': 'ClassReference',
        'name': 'str',
        'href': 'str'
    }

    attribute_map = {
        'class_ref': 'class_ref',
        'name': 'name',
        'href': 'href'
    }

    def __init__(self, class_ref=None, name=None, href=None, local_vars_configuration=None):  # noqa: E501
        """ExtraLink - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._class_ref = None
        self._name = None
        self._href = None
        self.discriminator = None

        if class_ref is not None:
            self.class_ref = class_ref
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href

    @property
    def class_ref(self):
        """Gets the class_ref of this ExtraLink.  # noqa: E501


        :return: The class_ref of this ExtraLink.  # noqa: E501
        :rtype: ClassReference
        """
        return self._class_ref

    @class_ref.setter
    def class_ref(self, class_ref):
        """Sets the class_ref of this ExtraLink.


        :param class_ref: The class_ref of this ExtraLink.  # noqa: E501
        :type: ClassReference
        """

        self._class_ref = class_ref

    @property
    def name(self):
        """Gets the name of this ExtraLink.  # noqa: E501


        :return: The name of this ExtraLink.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtraLink.


        :param name: The name of this ExtraLink.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this ExtraLink.  # noqa: E501


        :return: The href of this ExtraLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ExtraLink.


        :param href: The href of this ExtraLink.  # noqa: E501
        :type: str
        """

        self._href = href

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
        if not isinstance(other, ExtraLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtraLink):
            return True

        return self.to_dict() != other.to_dict()