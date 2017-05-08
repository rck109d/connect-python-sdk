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


class CatalogTax(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, calculation_phase=None, inclusion_type=None, percentage=None, applies_to_custom_amounts=None, enabled=None):
        """
        CatalogTax - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'calculation_phase': 'str',
            'inclusion_type': 'str',
            'percentage': 'str',
            'applies_to_custom_amounts': 'bool',
            'enabled': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'calculation_phase': 'calculation_phase',
            'inclusion_type': 'inclusion_type',
            'percentage': 'percentage',
            'applies_to_custom_amounts': 'applies_to_custom_amounts',
            'enabled': 'enabled'
        }

        self._name = name
        self._calculation_phase = calculation_phase
        self._inclusion_type = inclusion_type
        self._percentage = percentage
        self._applies_to_custom_amounts = applies_to_custom_amounts
        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this CatalogTax.
        The tax's name. Searchable.

        :return: The name of this CatalogTax.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogTax.
        The tax's name. Searchable.

        :param name: The name of this CatalogTax.
        :type: str
        """

        if not name:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def calculation_phase(self):
        """
        Gets the calculation_phase of this CatalogTax.
        Whether the tax is calculated based on a payment's subtotal or total. See [TaxCalculationPhase](#type-taxcalculationphase) for all possible values.

        :return: The calculation_phase of this CatalogTax.
        :rtype: str
        """
        return self._calculation_phase

    @calculation_phase.setter
    def calculation_phase(self, calculation_phase):
        """
        Sets the calculation_phase of this CatalogTax.
        Whether the tax is calculated based on a payment's subtotal or total. See [TaxCalculationPhase](#type-taxcalculationphase) for all possible values.

        :param calculation_phase: The calculation_phase of this CatalogTax.
        :type: str
        """

        self._calculation_phase = calculation_phase

    @property
    def inclusion_type(self):
        """
        Gets the inclusion_type of this CatalogTax.
        Whether the tax is `ADDITIVE` or `INCLUSIVE`. See [TaxInclusionType](#type-taxinclusiontype) for all possible values.

        :return: The inclusion_type of this CatalogTax.
        :rtype: str
        """
        return self._inclusion_type

    @inclusion_type.setter
    def inclusion_type(self, inclusion_type):
        """
        Sets the inclusion_type of this CatalogTax.
        Whether the tax is `ADDITIVE` or `INCLUSIVE`. See [TaxInclusionType](#type-taxinclusiontype) for all possible values.

        :param inclusion_type: The inclusion_type of this CatalogTax.
        :type: str
        """

        self._inclusion_type = inclusion_type

    @property
    def percentage(self):
        """
        Gets the percentage of this CatalogTax.
        The percentage of the tax in decimal form, using a '.' as the decimal separator and without a '%' sign. A value of `7.5` corresponds to 7.5%.

        :return: The percentage of this CatalogTax.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this CatalogTax.
        The percentage of the tax in decimal form, using a '.' as the decimal separator and without a '%' sign. A value of `7.5` corresponds to 7.5%.

        :param percentage: The percentage of this CatalogTax.
        :type: str
        """

        self._percentage = percentage

    @property
    def applies_to_custom_amounts(self):
        """
        Gets the applies_to_custom_amounts of this CatalogTax.
        If `true`, the fee applies to custom amounts entered into the Square Point of Sale app that are not associated with a particular [CatalogItem](#type-catalogitem).

        :return: The applies_to_custom_amounts of this CatalogTax.
        :rtype: bool
        """
        return self._applies_to_custom_amounts

    @applies_to_custom_amounts.setter
    def applies_to_custom_amounts(self, applies_to_custom_amounts):
        """
        Sets the applies_to_custom_amounts of this CatalogTax.
        If `true`, the fee applies to custom amounts entered into the Square Point of Sale app that are not associated with a particular [CatalogItem](#type-catalogitem).

        :param applies_to_custom_amounts: The applies_to_custom_amounts of this CatalogTax.
        :type: bool
        """

        self._applies_to_custom_amounts = applies_to_custom_amounts

    @property
    def enabled(self):
        """
        Gets the enabled of this CatalogTax.
        If `true`, the tax will be shown as enabled in the Square Point of Sale app.

        :return: The enabled of this CatalogTax.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CatalogTax.
        If `true`, the tax will be shown as enabled in the Square Point of Sale app.

        :param enabled: The enabled of this CatalogTax.
        :type: bool
        """

        self._enabled = enabled

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
