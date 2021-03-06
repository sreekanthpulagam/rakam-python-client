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


class RealTimeReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, measures=None, table_name=None, collections=None, filter=None, dimensions=None):
        """
        RealTimeReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'measures': 'list[Measure]',
            'table_name': 'str',
            'collections': 'list[str]',
            'filter': 'str',
            'dimensions': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'measures': 'measures',
            'table_name': 'table_name',
            'collections': 'collections',
            'filter': 'filter',
            'dimensions': 'dimensions'
        }

        self._name = name
        self._measures = measures
        self._table_name = table_name
        self._collections = collections
        self._filter = filter
        self._dimensions = dimensions

    @property
    def name(self):
        """
        Gets the name of this RealTimeReport.


        :return: The name of this RealTimeReport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RealTimeReport.


        :param name: The name of this RealTimeReport.
        :type: str
        """

        self._name = name

    @property
    def measures(self):
        """
        Gets the measures of this RealTimeReport.


        :return: The measures of this RealTimeReport.
        :rtype: list[Measure]
        """
        return self._measures

    @measures.setter
    def measures(self, measures):
        """
        Sets the measures of this RealTimeReport.


        :param measures: The measures of this RealTimeReport.
        :type: list[Measure]
        """

        self._measures = measures

    @property
    def table_name(self):
        """
        Gets the table_name of this RealTimeReport.


        :return: The table_name of this RealTimeReport.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this RealTimeReport.


        :param table_name: The table_name of this RealTimeReport.
        :type: str
        """

        self._table_name = table_name

    @property
    def collections(self):
        """
        Gets the collections of this RealTimeReport.


        :return: The collections of this RealTimeReport.
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """
        Sets the collections of this RealTimeReport.


        :param collections: The collections of this RealTimeReport.
        :type: list[str]
        """

        self._collections = collections

    @property
    def filter(self):
        """
        Gets the filter of this RealTimeReport.


        :return: The filter of this RealTimeReport.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this RealTimeReport.


        :param filter: The filter of this RealTimeReport.
        :type: str
        """

        self._filter = filter

    @property
    def dimensions(self):
        """
        Gets the dimensions of this RealTimeReport.


        :return: The dimensions of this RealTimeReport.
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this RealTimeReport.


        :param dimensions: The dimensions of this RealTimeReport.
        :type: list[str]
        """

        self._dimensions = dimensions

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
