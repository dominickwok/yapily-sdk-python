# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.89-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.atm_open_data_atm import ATMOpenDataATM  # noqa: F401,E501


class ATMOpenDataBrand(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'atm': 'list[ATMOpenDataATM]',
        'brand_name': 'str'
    }

    attribute_map = {
        'atm': 'ATM',
        'brand_name': 'BrandName'
    }

    def __init__(self, atm=None, brand_name=None):  # noqa: E501
        """ATMOpenDataBrand - a model defined in Swagger"""  # noqa: E501

        self._atm = None
        self._brand_name = None
        self.discriminator = None

        if atm is not None:
            self.atm = atm
        if brand_name is not None:
            self.brand_name = brand_name

    @property
    def atm(self):
        """Gets the atm of this ATMOpenDataBrand.  # noqa: E501


        :return: The atm of this ATMOpenDataBrand.  # noqa: E501
        :rtype: list[ATMOpenDataATM]
        """
        return self._atm

    @atm.setter
    def atm(self, atm):
        """Sets the atm of this ATMOpenDataBrand.


        :param atm: The atm of this ATMOpenDataBrand.  # noqa: E501
        :type: list[ATMOpenDataATM]
        """

        self._atm = atm

    @property
    def brand_name(self):
        """Gets the brand_name of this ATMOpenDataBrand.  # noqa: E501


        :return: The brand_name of this ATMOpenDataBrand.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this ATMOpenDataBrand.


        :param brand_name: The brand_name of this ATMOpenDataBrand.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ATMOpenDataBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
