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
import datetime

import airflow_client
from airflow_client.models.task import Task  # noqa: E501
from airflow_client.rest import ApiException

class TestTask(unittest.TestCase):
    """Task unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Task
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = airflow_client.models.task.Task()  # noqa: E501
        if include_optional :
            return Task(
                class_ref = airflow_client.models.class_reference.ClassReference(
                    module_path = '0', 
                    class_name = '0', ), 
                task_id = '0', 
                owner = '0', 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                trigger_rule = 'all_success', 
                extra_links = [
                    airflow_client.models.task_extra_links.Task_extra_links(
                        class_ref = airflow_client.models.class_reference.ClassReference(
                            module_path = '0', 
                            class_name = '0', ), )
                    ], 
                depends_on_past = True, 
                wait_for_downstream = True, 
                retries = 1.337, 
                queue = '0', 
                pool = '0', 
                pool_slots = 1.337, 
                execution_timeout = airflow_client.models.time_delta.TimeDelta(
                    __type = '0', 
                    days = 56, 
                    seconds = 56, 
                    microseconds = 56, ), 
                retry_delay = airflow_client.models.time_delta.TimeDelta(
                    __type = '0', 
                    days = 56, 
                    seconds = 56, 
                    microseconds = 56, ), 
                retry_exponential_backoff = True, 
                priority_weight = 1.337, 
                weight_rule = 'downstream', 
                ui_color = 'a', 
                ui_fgcolor = 'a', 
                template_fields = [
                    '0'
                    ], 
                sub_dag = airflow_client.models.dag.DAG(
                    dag_id = '0', 
                    root_dag_id = '0', 
                    is_paused = True, 
                    is_subdag = True, 
                    fileloc = '0', 
                    file_token = '0', 
                    owners = [
                        '0'
                        ], 
                    description = '0', 
                    schedule_interval = null, 
                    tags = [
                        airflow_client.models.tag.Tag(
                            name = '0', )
                        ], ), 
                downstream_task_ids = [
                    '0'
                    ]
            )
        else :
            return Task(
        )

    def testTask(self):
        """Test Task"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
