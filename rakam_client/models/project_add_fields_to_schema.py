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


class ProjectAddFieldsToSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, collection=None, fields=None):
        """
        ProjectAddFieldsToSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'collection': 'str',
            'fields': 'list[SchemaField]'
        }

        self.attribute_map = {
            'collection': 'collection',
            'fields': 'fields'
        }

        self._collection = collection
        self._fields = fields

    @property
    def collection(self):
        """
        Gets the collection of this ProjectAddFieldsToSchema.


        :return: The collection of this ProjectAddFieldsToSchema.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """
        Sets the collection of this ProjectAddFieldsToSchema.


        :param collection: The collection of this ProjectAddFieldsToSchema.
        :type: str
        """

        self._collection = collection

    @property
    def fields(self):
        """
        Gets the fields of this ProjectAddFieldsToSchema.


        :return: The fields of this ProjectAddFieldsToSchema.
        :rtype: list[SchemaField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this ProjectAddFieldsToSchema.


        :param fields: The fields of this ProjectAddFieldsToSchema.
        :type: list[SchemaField]
        """

        self._fields = fields

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
