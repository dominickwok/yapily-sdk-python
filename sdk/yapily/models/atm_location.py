# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.79
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.atm_location_other_location_category import ATMLocationOtherLocationCategory  # noqa: F401,E501
from yapily.models.atm_map_service_links import ATMMapServiceLinks  # noqa: F401,E501
from yapily.models.atm_postal_address import ATMPostalAddress  # noqa: F401,E501
from yapily.models.atm_site import ATMSite  # noqa: F401,E501


class ATMLocation(object):
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
        'location_category': 'list[str]',
        'other_location_category': 'list[ATMLocationOtherLocationCategory]',
        'postal_address': 'ATMPostalAddress',
        'site': 'ATMSite',
        'map_service_links': 'ATMMapServiceLinks'
    }

    attribute_map = {
        'location_category': 'LocationCategory',
        'other_location_category': 'OtherLocationCategory',
        'postal_address': 'PostalAddress',
        'site': 'Site',
        'map_service_links': 'mapServiceLinks'
    }

    def __init__(self, location_category=None, other_location_category=None, postal_address=None, site=None, map_service_links=None):  # noqa: E501
        """ATMLocation - a model defined in Swagger"""  # noqa: E501

        self._location_category = None
        self._other_location_category = None
        self._postal_address = None
        self._site = None
        self._map_service_links = None
        self.discriminator = None

        if location_category is not None:
            self.location_category = location_category
        if other_location_category is not None:
            self.other_location_category = other_location_category
        if postal_address is not None:
            self.postal_address = postal_address
        if site is not None:
            self.site = site
        if map_service_links is not None:
            self.map_service_links = map_service_links

    @property
    def location_category(self):
        """Gets the location_category of this ATMLocation.  # noqa: E501


        :return: The location_category of this ATMLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._location_category

    @location_category.setter
    def location_category(self, location_category):
        """Sets the location_category of this ATMLocation.


        :param location_category: The location_category of this ATMLocation.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["BranchExternal", "BranchInternal", "BranchLobby", "Other", "RetailerOutlet", "RemoteUnit"]  # noqa: E501
        if not set(location_category).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `location_category` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(location_category) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._location_category = location_category

    @property
    def other_location_category(self):
        """Gets the other_location_category of this ATMLocation.  # noqa: E501


        :return: The other_location_category of this ATMLocation.  # noqa: E501
        :rtype: list[ATMLocationOtherLocationCategory]
        """
        return self._other_location_category

    @other_location_category.setter
    def other_location_category(self, other_location_category):
        """Sets the other_location_category of this ATMLocation.


        :param other_location_category: The other_location_category of this ATMLocation.  # noqa: E501
        :type: list[ATMLocationOtherLocationCategory]
        """

        self._other_location_category = other_location_category

    @property
    def postal_address(self):
        """Gets the postal_address of this ATMLocation.  # noqa: E501


        :return: The postal_address of this ATMLocation.  # noqa: E501
        :rtype: ATMPostalAddress
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this ATMLocation.


        :param postal_address: The postal_address of this ATMLocation.  # noqa: E501
        :type: ATMPostalAddress
        """

        self._postal_address = postal_address

    @property
    def site(self):
        """Gets the site of this ATMLocation.  # noqa: E501


        :return: The site of this ATMLocation.  # noqa: E501
        :rtype: ATMSite
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this ATMLocation.


        :param site: The site of this ATMLocation.  # noqa: E501
        :type: ATMSite
        """

        self._site = site

    @property
    def map_service_links(self):
        """Gets the map_service_links of this ATMLocation.  # noqa: E501


        :return: The map_service_links of this ATMLocation.  # noqa: E501
        :rtype: ATMMapServiceLinks
        """
        return self._map_service_links

    @map_service_links.setter
    def map_service_links(self, map_service_links):
        """Sets the map_service_links of this ATMLocation.


        :param map_service_links: The map_service_links of this ATMLocation.  # noqa: E501
        :type: ATMMapServiceLinks
        """

        self._map_service_links = map_service_links

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
        if not isinstance(other, ATMLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
