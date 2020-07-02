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


class RelativeDelta(object):
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
        'type': 'str',
        'years': 'int',
        'months': 'int',
        'days': 'int',
        'leapdays': 'int',
        'hours': 'int',
        'minutes': 'int',
        'seconds': 'int',
        'microseconds': 'int',
        'year': 'int',
        'month': 'int',
        'day': 'int',
        'hour': 'int',
        'minute': 'int',
        'second': 'int',
        'microsecond': 'int'
    }

    attribute_map = {
        'type': '__type',
        'years': 'years',
        'months': 'months',
        'days': 'days',
        'leapdays': 'leapdays',
        'hours': 'hours',
        'minutes': 'minutes',
        'seconds': 'seconds',
        'microseconds': 'microseconds',
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'hour': 'hour',
        'minute': 'minute',
        'second': 'second',
        'microsecond': 'microsecond'
    }

    def __init__(self, type=None, years=None, months=None, days=None, leapdays=None, hours=None, minutes=None, seconds=None, microseconds=None, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, local_vars_configuration=None):  # noqa: E501
        """RelativeDelta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._years = None
        self._months = None
        self._days = None
        self._leapdays = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._microseconds = None
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._second = None
        self._microsecond = None
        self.discriminator = None

        self.type = type
        self.years = years
        self.months = months
        self.days = days
        self.leapdays = leapdays
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond

    @property
    def type(self):
        """Gets the type of this RelativeDelta.  # noqa: E501


        :return: The type of this RelativeDelta.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RelativeDelta.


        :param type: The type of this RelativeDelta.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def years(self):
        """Gets the years of this RelativeDelta.  # noqa: E501


        :return: The years of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this RelativeDelta.


        :param years: The years of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and years is None:  # noqa: E501
            raise ValueError("Invalid value for `years`, must not be `None`")  # noqa: E501

        self._years = years

    @property
    def months(self):
        """Gets the months of this RelativeDelta.  # noqa: E501


        :return: The months of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this RelativeDelta.


        :param months: The months of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and months is None:  # noqa: E501
            raise ValueError("Invalid value for `months`, must not be `None`")  # noqa: E501

        self._months = months

    @property
    def days(self):
        """Gets the days of this RelativeDelta.  # noqa: E501


        :return: The days of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this RelativeDelta.


        :param days: The days of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and days is None:  # noqa: E501
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def leapdays(self):
        """Gets the leapdays of this RelativeDelta.  # noqa: E501


        :return: The leapdays of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._leapdays

    @leapdays.setter
    def leapdays(self, leapdays):
        """Sets the leapdays of this RelativeDelta.


        :param leapdays: The leapdays of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and leapdays is None:  # noqa: E501
            raise ValueError("Invalid value for `leapdays`, must not be `None`")  # noqa: E501

        self._leapdays = leapdays

    @property
    def hours(self):
        """Gets the hours of this RelativeDelta.  # noqa: E501


        :return: The hours of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this RelativeDelta.


        :param hours: The hours of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hours is None:  # noqa: E501
            raise ValueError("Invalid value for `hours`, must not be `None`")  # noqa: E501

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this RelativeDelta.  # noqa: E501


        :return: The minutes of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this RelativeDelta.


        :param minutes: The minutes of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minutes is None:  # noqa: E501
            raise ValueError("Invalid value for `minutes`, must not be `None`")  # noqa: E501

        self._minutes = minutes

    @property
    def seconds(self):
        """Gets the seconds of this RelativeDelta.  # noqa: E501


        :return: The seconds of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this RelativeDelta.


        :param seconds: The seconds of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds

    @property
    def microseconds(self):
        """Gets the microseconds of this RelativeDelta.  # noqa: E501


        :return: The microseconds of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._microseconds

    @microseconds.setter
    def microseconds(self, microseconds):
        """Sets the microseconds of this RelativeDelta.


        :param microseconds: The microseconds of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and microseconds is None:  # noqa: E501
            raise ValueError("Invalid value for `microseconds`, must not be `None`")  # noqa: E501

        self._microseconds = microseconds

    @property
    def year(self):
        """Gets the year of this RelativeDelta.  # noqa: E501


        :return: The year of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this RelativeDelta.


        :param year: The year of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this RelativeDelta.  # noqa: E501


        :return: The month of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this RelativeDelta.


        :param month: The month of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def day(self):
        """Gets the day of this RelativeDelta.  # noqa: E501


        :return: The day of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this RelativeDelta.


        :param day: The day of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and day is None:  # noqa: E501
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def hour(self):
        """Gets the hour of this RelativeDelta.  # noqa: E501


        :return: The hour of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this RelativeDelta.


        :param hour: The hour of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hour is None:  # noqa: E501
            raise ValueError("Invalid value for `hour`, must not be `None`")  # noqa: E501

        self._hour = hour

    @property
    def minute(self):
        """Gets the minute of this RelativeDelta.  # noqa: E501


        :return: The minute of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this RelativeDelta.


        :param minute: The minute of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minute is None:  # noqa: E501
            raise ValueError("Invalid value for `minute`, must not be `None`")  # noqa: E501

        self._minute = minute

    @property
    def second(self):
        """Gets the second of this RelativeDelta.  # noqa: E501


        :return: The second of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this RelativeDelta.


        :param second: The second of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and second is None:  # noqa: E501
            raise ValueError("Invalid value for `second`, must not be `None`")  # noqa: E501

        self._second = second

    @property
    def microsecond(self):
        """Gets the microsecond of this RelativeDelta.  # noqa: E501


        :return: The microsecond of this RelativeDelta.  # noqa: E501
        :rtype: int
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, microsecond):
        """Sets the microsecond of this RelativeDelta.


        :param microsecond: The microsecond of this RelativeDelta.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and microsecond is None:  # noqa: E501
            raise ValueError("Invalid value for `microsecond`, must not be `None`")  # noqa: E501

        self._microsecond = microsecond

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
        if not isinstance(other, RelativeDelta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelativeDelta):
            return True

        return self.to_dict() != other.to_dict()
