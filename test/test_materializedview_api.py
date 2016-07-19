# coding: utf-8

"""
    Rakam API Documentation

    An analytics platform API that lets you create your own analytics services.

    OpenAPI spec version: 0.5
    Contact: contact@rakam.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import rakam_client
from rakam_client.rest import ApiException
from rakam_client.apis.materializedview_api import MaterializedviewApi


class TestMaterializedviewApi(unittest.TestCase):
    """ MaterializedviewApi unit test stubs """

    def setUp(self):
        self.api = rakam_client.apis.materializedview_api.MaterializedviewApi()

    def tearDown(self):
        pass

    def test_create_view(self):
        """
        Test case for create_view

        Create view
        """
        pass

    def test_delete_view(self):
        """
        Test case for delete_view

        Delete materialized view
        """
        pass

    def test_get_schema_of_view(self):
        """
        Test case for get_schema_of_view

        Get schemas
        """
        pass

    def test_get_view(self):
        """
        Test case for get_view

        Get view
        """
        pass

    def test_list_views(self):
        """
        Test case for list_views

        List views
        """
        pass


if __name__ == '__main__':
    unittest.main()
