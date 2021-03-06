# coding: utf-8

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

import unittest

import airflow_client
from airflow_client.api.x_com_api import XComApi  # noqa: E501
from airflow_client.rest import ApiException


class TestXComApi(unittest.TestCase):
    """XComApi unit test stubs"""

    def setUp(self):
        self.api = airflow_client.api.x_com_api.XComApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_xcom_entry(self):
        """Test case for delete_xcom_entry

        Delete an XCom entry  # noqa: E501
        """
        pass

    def test_get_xcom_entries(self):
        """Test case for get_xcom_entries

        Get all XCom entries  # noqa: E501
        """
        pass

    def test_get_xcom_entry(self):
        """Test case for get_xcom_entry

        Get an XCom entry  # noqa: E501
        """
        pass

    def test_patch_xcom_entry(self):
        """Test case for patch_xcom_entry

        Update an XCom entry  # noqa: E501
        """
        pass

    def test_post_xcom_entries(self):
        """Test case for post_xcom_entries

        Create an XCom entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
