# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.71
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Address(object):
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
        'address_lines': 'list[str]',
        'street_name': 'str',
        'building_number': 'str',
        'post_code': 'str',
        'town_name': 'str',
        'county': 'list[str]',
        'country': 'str'
    }

    attribute_map = {
        'address_lines': 'addressLines',
        'street_name': 'streetName',
        'building_number': 'buildingNumber',
        'post_code': 'postCode',
        'town_name': 'townName',
        'county': 'county',
        'country': 'country'
    }

    def __init__(self, address_lines=None, street_name=None, building_number=None, post_code=None, town_name=None, county=None, country=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501

        self._address_lines = None
        self._street_name = None
        self._building_number = None
        self._post_code = None
        self._town_name = None
        self._county = None
        self._country = None
        self.discriminator = None

        self.address_lines = address_lines
        self.street_name = street_name
        self.building_number = building_number
        self.post_code = post_code
        self.town_name = town_name
        self.county = county
        self.country = country

    @property
    def address_lines(self):
        """Gets the address_lines of this Address.  # noqa: E501


        :return: The address_lines of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_lines

    @address_lines.setter
    def address_lines(self, address_lines):
        """Sets the address_lines of this Address.


        :param address_lines: The address_lines of this Address.  # noqa: E501
        :type: list[str]
        """
        if address_lines is None:
            raise ValueError("Invalid value for `address_lines`, must not be `None`")  # noqa: E501

        self._address_lines = address_lines

    @property
    def street_name(self):
        """Gets the street_name of this Address.  # noqa: E501


        :return: The street_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Address.


        :param street_name: The street_name of this Address.  # noqa: E501
        :type: str
        """
        if street_name is None:
            raise ValueError("Invalid value for `street_name`, must not be `None`")  # noqa: E501

        self._street_name = street_name

    @property
    def building_number(self):
        """Gets the building_number of this Address.  # noqa: E501


        :return: The building_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this Address.


        :param building_number: The building_number of this Address.  # noqa: E501
        :type: str
        """
        if building_number is None:
            raise ValueError("Invalid value for `building_number`, must not be `None`")  # noqa: E501

        self._building_number = building_number

    @property
    def post_code(self):
        """Gets the post_code of this Address.  # noqa: E501


        :return: The post_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Address.


        :param post_code: The post_code of this Address.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")  # noqa: E501

        self._post_code = post_code

    @property
    def town_name(self):
        """Gets the town_name of this Address.  # noqa: E501


        :return: The town_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._town_name

    @town_name.setter
    def town_name(self, town_name):
        """Sets the town_name of this Address.


        :param town_name: The town_name of this Address.  # noqa: E501
        :type: str
        """
        if town_name is None:
            raise ValueError("Invalid value for `town_name`, must not be `None`")  # noqa: E501

        self._town_name = town_name

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501


        :return: The county of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.


        :param county: The county of this Address.  # noqa: E501
        :type: list[str]
        """
        if county is None:
            raise ValueError("Invalid value for `county`, must not be `None`")  # noqa: E501

        self._county = county

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
