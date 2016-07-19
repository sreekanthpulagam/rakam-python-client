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

from pprint import pformat
from six import iteritems
import re


class Execute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, query='', export_type='', limit=None):
        """
        Execute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'str',
            'export_type': 'str',
            'limit': 'int'
        }

        self.attribute_map = {
            'query': 'query',
            'export_type': 'export_type',
            'limit': 'limit'
        }

        self._query = query
        self._export_type = export_type
        self._limit = limit

    @property
    def query(self):
        """
        Gets the query of this Execute.
        

        :return: The query of this Execute.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this Execute.
        

        :param query: The query of this Execute.
        :type: str
        """

        self._query = query

    @property
    def export_type(self):
        """
        Gets the export_type of this Execute.
        

        :return: The export_type of this Execute.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """
        Sets the export_type of this Execute.
        

        :param export_type: The export_type of this Execute.
        :type: str
        """
        allowed_values = ["AVRO", "CSV", "JSON"]
        if export_type not in allowed_values:
            raise ValueError(
                "Invalid value for `export_type` ({0}), must be one of {1}"
                .format(export_type, allowed_values)
            )

        self._export_type = export_type

    @property
    def limit(self):
        """
        Gets the limit of this Execute.
        

        :return: The limit of this Execute.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this Execute.
        

        :param limit: The limit of this Execute.
        :type: int
        """

        self._limit = limit

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
