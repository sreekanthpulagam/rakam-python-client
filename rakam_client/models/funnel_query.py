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


class FunnelQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, steps=None, dimension=None, start_date=None, window=None, end_date=None):
        """
        FunnelQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'steps': 'list[FunnelStep]',
            'dimension': 'str',
            'start_date': 'date',
            'window': 'FunnelWindow',
            'end_date': 'date'
        }

        self.attribute_map = {
            'steps': 'steps',
            'dimension': 'dimension',
            'start_date': 'startDate',
            'window': 'window',
            'end_date': 'endDate'
        }

        self._steps = steps
        self._dimension = dimension
        self._start_date = start_date
        self._window = window
        self._end_date = end_date

    @property
    def steps(self):
        """
        Gets the steps of this FunnelQuery.


        :return: The steps of this FunnelQuery.
        :rtype: list[FunnelStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this FunnelQuery.


        :param steps: The steps of this FunnelQuery.
        :type: list[FunnelStep]
        """

        self._steps = steps

    @property
    def dimension(self):
        """
        Gets the dimension of this FunnelQuery.


        :return: The dimension of this FunnelQuery.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """
        Sets the dimension of this FunnelQuery.


        :param dimension: The dimension of this FunnelQuery.
        :type: str
        """

        self._dimension = dimension

    @property
    def start_date(self):
        """
        Gets the start_date of this FunnelQuery.


        :return: The start_date of this FunnelQuery.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this FunnelQuery.


        :param start_date: The start_date of this FunnelQuery.
        :type: date
        """

        self._start_date = start_date

    @property
    def window(self):
        """
        Gets the window of this FunnelQuery.


        :return: The window of this FunnelQuery.
        :rtype: FunnelWindow
        """
        return self._window

    @window.setter
    def window(self, window):
        """
        Sets the window of this FunnelQuery.


        :param window: The window of this FunnelQuery.
        :type: FunnelWindow
        """

        self._window = window

    @property
    def end_date(self):
        """
        Gets the end_date of this FunnelQuery.


        :return: The end_date of this FunnelQuery.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this FunnelQuery.


        :param end_date: The end_date of this FunnelQuery.
        :type: date
        """

        self._end_date = end_date

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