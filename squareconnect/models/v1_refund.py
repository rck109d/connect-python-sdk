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


class V1Refund(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, reason=None, refunded_money=None, created_at=None, processed_at=None, payment_id=None, merchant_id=None):
        """
        V1Refund - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'reason': 'str',
            'refunded_money': 'V1Money',
            'created_at': 'str',
            'processed_at': 'str',
            'payment_id': 'str',
            'merchant_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'reason': 'reason',
            'refunded_money': 'refunded_money',
            'created_at': 'created_at',
            'processed_at': 'processed_at',
            'payment_id': 'payment_id',
            'merchant_id': 'merchant_id'
        }

        self._type = type
        self._reason = reason
        self._refunded_money = refunded_money
        self._created_at = created_at
        self._processed_at = processed_at
        self._payment_id = payment_id
        self._merchant_id = merchant_id

    @property
    def type(self):
        """
        Gets the type of this V1Refund.
        The type of refund 

        :return: The type of this V1Refund.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Refund.
        The type of refund 

        :param type: The type of this V1Refund.
        :type: str
        """

        self._type = type

    @property
    def reason(self):
        """
        Gets the reason of this V1Refund.
        The merchant-specified reason for the refund.

        :return: The reason of this V1Refund.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1Refund.
        The merchant-specified reason for the refund.

        :param reason: The reason of this V1Refund.
        :type: str
        """

        self._reason = reason

    @property
    def refunded_money(self):
        """
        Gets the refunded_money of this V1Refund.
        The amount of money refunded. This amount is always negative.

        :return: The refunded_money of this V1Refund.
        :rtype: V1Money
        """
        return self._refunded_money

    @refunded_money.setter
    def refunded_money(self, refunded_money):
        """
        Sets the refunded_money of this V1Refund.
        The amount of money refunded. This amount is always negative.

        :param refunded_money: The refunded_money of this V1Refund.
        :type: V1Money
        """

        self._refunded_money = refunded_money

    @property
    def created_at(self):
        """
        Gets the created_at of this V1Refund.
        The time when the merchant initiated the refund for Square to process, in ISO 8601 format..

        :return: The created_at of this V1Refund.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this V1Refund.
        The time when the merchant initiated the refund for Square to process, in ISO 8601 format..

        :param created_at: The created_at of this V1Refund.
        :type: str
        """

        self._created_at = created_at

    @property
    def processed_at(self):
        """
        Gets the processed_at of this V1Refund.
        The time when Square processed the refund on behalf of the merchant, in ISO 8601 format.

        :return: The processed_at of this V1Refund.
        :rtype: str
        """
        return self._processed_at

    @processed_at.setter
    def processed_at(self, processed_at):
        """
        Sets the processed_at of this V1Refund.
        The time when Square processed the refund on behalf of the merchant, in ISO 8601 format.

        :param processed_at: The processed_at of this V1Refund.
        :type: str
        """

        self._processed_at = processed_at

    @property
    def payment_id(self):
        """
        Gets the payment_id of this V1Refund.
        The Square-issued ID of the payment the refund is applied to.

        :return: The payment_id of this V1Refund.
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this V1Refund.
        The Square-issued ID of the payment the refund is applied to.

        :param payment_id: The payment_id of this V1Refund.
        :type: str
        """

        self._payment_id = payment_id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this V1Refund.
        

        :return: The merchant_id of this V1Refund.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this V1Refund.
        

        :param merchant_id: The merchant_id of this V1Refund.
        :type: str
        """

        self._merchant_id = merchant_id

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