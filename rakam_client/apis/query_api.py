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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class QueryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def execute(self, **kwargs):
        """
        Execute query on event data-set
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.execute(execute=execute_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Execute execute:  (required)
        :return: QueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.execute_with_http_info(**kwargs)
        else:
            (data) = self.execute_with_http_info(**kwargs)
            return data

    def execute_with_http_info(self, **kwargs):
        """
        Execute query on event data-set
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.execute_with_http_info(execute=execute_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Execute execute:  (required)
        :return: QueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execute']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'execute' is set
        if ('execute' not in params) or (params['execute'] is None):
            raise ValueError("Missing the required parameter `execute` when calling `execute`")

        resource_path = '/query/execute'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'execute' in params:
            body_params = params['execute']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['read_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='QueryResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def explain(self, **kwargs):
        """
        Explain query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.explain(explain=explain_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Explain explain:  (required)
        :return: ResponseQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.explain_with_http_info(**kwargs)
        else:
            (data) = self.explain_with_http_info(**kwargs)
            return data

    def explain_with_http_info(self, **kwargs):
        """
        Explain query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.explain_with_http_info(explain=explain_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Explain explain:  (required)
        :return: ResponseQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['explain']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method explain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'explain' is set
        if ('explain' not in params) or (params['explain'] is None):
            raise ValueError("Missing the required parameter `explain` when calling `explain`")

        resource_path = '/query/explain'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'explain' in params:
            body_params = params['explain']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['read_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseQuery',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def metadata(self, **kwargs):
        """
        Test query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.metadata(query_metadata=query_metadata_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param QueryMetadata query_metadata:  (required)
        :return: list[SchemaField]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.metadata_with_http_info(**kwargs)
        else:
            (data) = self.metadata_with_http_info(**kwargs)
            return data

    def metadata_with_http_info(self, **kwargs):
        """
        Test query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.metadata_with_http_info(query_metadata=query_metadata_value, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param QueryMetadata query_metadata:  (required)
        :return: list[SchemaField]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_metadata']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_metadata' is set
        if ('query_metadata' not in params) or (params['query_metadata'] is None):
            raise ValueError("Missing the required parameter `query_metadata` when calling `metadata`")

        resource_path = '/query/metadata'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_metadata' in params:
            body_params = params['query_metadata']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['read_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[SchemaField]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
