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


class BulkEventRemote(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, collection=None, urls=None, type=None, compression=None, options=None):
        """
        BulkEventRemote - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'collection': 'str',
            'urls': 'list[str]',
            'type': 'str',
            'compression': 'str',
            'options': 'dict(str, str)'
        }

        self.attribute_map = {
            'collection': 'collection',
            'urls': 'urls',
            'type': 'type',
            'compression': 'compression',
            'options': 'options'
        }

        self._collection = collection
        self._urls = urls
        self._type = type
        self._compression = compression
        self._options = options

    @property
    def collection(self):
        """
        Gets the collection of this BulkEventRemote.


        :return: The collection of this BulkEventRemote.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """
        Sets the collection of this BulkEventRemote.


        :param collection: The collection of this BulkEventRemote.
        :type: str
        """

        self._collection = collection

    @property
    def urls(self):
        """
        Gets the urls of this BulkEventRemote.


        :return: The urls of this BulkEventRemote.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        Sets the urls of this BulkEventRemote.


        :param urls: The urls of this BulkEventRemote.
        :type: list[str]
        """

        self._urls = urls

    @property
    def type(self):
        """
        Gets the type of this BulkEventRemote.


        :return: The type of this BulkEventRemote.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BulkEventRemote.


        :param type: The type of this BulkEventRemote.
        :type: str
        """
        allowed_values = ["AVRO", "CSV", "JSON"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def compression(self):
        """
        Gets the compression of this BulkEventRemote.


        :return: The compression of this BulkEventRemote.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """
        Sets the compression of this BulkEventRemote.


        :param compression: The compression of this BulkEventRemote.
        :type: str
        """
        allowed_values = ["GZIP"]
        if compression not in allowed_values:
            raise ValueError(
                "Invalid value for `compression` ({0}), must be one of {1}"
                .format(compression, allowed_values)
            )

        self._compression = compression

    @property
    def options(self):
        """
        Gets the options of this BulkEventRemote.


        :return: The options of this BulkEventRemote.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this BulkEventRemote.


        :param options: The options of this BulkEventRemote.
        :type: dict(str, str)
        """

        self._options = options

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
