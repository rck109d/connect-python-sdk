# coding: utf-8

"""
Copyright 2017 Square, Inc.

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


class ModifierOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, price_money=None, name=None, ordinal=None, modifier_list_id=None):
        """
        ModifierOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'price_money': 'Money',
            'name': 'str',
            'ordinal': 'int',
            'modifier_list_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'price_money': 'price_money',
            'name': 'name',
            'ordinal': 'ordinal',
            'modifier_list_id': 'modifier_list_id'
        }

        self._id = id
        self._price_money = price_money
        self._name = name
        self._ordinal = ordinal
        self._modifier_list_id = modifier_list_id

    @property
    def id(self):
        """
        Gets the id of this ModifierOption.
        

        :return: The id of this ModifierOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModifierOption.
        

        :param id: The id of this ModifierOption.
        :type: str
        """

        self._id = id

    @property
    def price_money(self):
        """
        Gets the price_money of this ModifierOption.
        

        :return: The price_money of this ModifierOption.
        :rtype: Money
        """
        return self._price_money

    @price_money.setter
    def price_money(self, price_money):
        """
        Sets the price_money of this ModifierOption.
        

        :param price_money: The price_money of this ModifierOption.
        :type: Money
        """

        self._price_money = price_money

    @property
    def name(self):
        """
        Gets the name of this ModifierOption.
        

        :return: The name of this ModifierOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModifierOption.
        

        :param name: The name of this ModifierOption.
        :type: str
        """

        self._name = name

    @property
    def ordinal(self):
        """
        Gets the ordinal of this ModifierOption.
        

        :return: The ordinal of this ModifierOption.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """
        Sets the ordinal of this ModifierOption.
        

        :param ordinal: The ordinal of this ModifierOption.
        :type: int
        """

        self._ordinal = ordinal

    @property
    def modifier_list_id(self):
        """
        Gets the modifier_list_id of this ModifierOption.
        

        :return: The modifier_list_id of this ModifierOption.
        :rtype: str
        """
        return self._modifier_list_id

    @modifier_list_id.setter
    def modifier_list_id(self, modifier_list_id):
        """
        Sets the modifier_list_id of this ModifierOption.
        

        :param modifier_list_id: The modifier_list_id of this ModifierOption.
        :type: str
        """

        self._modifier_list_id = modifier_list_id

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