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
from rakam_client.apis.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """ AdminApi unit test stubs """

    def setUp(self):
        self.api = rakam_client.apis.admin_api.AdminApi()

    def tearDown(self):
        pass

    def test_add_custom_fields_to_schema(self):
        """
        Test case for add_custom_fields_to_schema

        Add fields to collections by transforming other schemas
        """
        pass

    def test_add_fields_to_schema(self):
        """
        Test case for add_fields_to_schema

        Add fields to collections
        """
        pass

    def test_check_api_keys(self):
        """
        Test case for check_api_keys

        Create API Keys
        """
        pass

    def test_check_lock_key(self):
        """
        Test case for check_lock_key

        Check lock key
        """
        pass

    def test_collections(self):
        """
        Test case for collections

        Get collection names
        """
        pass

    def test_create_api_keys(self):
        """
        Test case for create_api_keys

        Create API Keys
        """
        pass

    def test_create_project(self):
        """
        Test case for create_project

        Create project
        """
        pass

    def test_delete_project(self):
        """
        Test case for delete_project

        Delete project
        """
        pass

    def test_get_configurations(self):
        """
        Test case for get_configurations

        List installed modules
        """
        pass

    def test_get_projects(self):
        """
        Test case for get_projects

        List created projects
        """
        pass

    def test_get_stats(self):
        """
        Test case for get_stats

        Get project stats
        """
        pass

    def test_get_types(self):
        """
        Test case for get_types

        Get types
        """
        pass

    def test_revoke_api_keys(self):
        """
        Test case for revoke_api_keys

        Revoke API Keys
        """
        pass

    def test_schema(self):
        """
        Test case for schema

        Get collection schema
        """
        pass


if __name__ == '__main__':
    unittest.main()
