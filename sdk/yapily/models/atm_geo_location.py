# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.atm_geographic_coordinates import ATMGeographicCoordinates  # noqa: F401,E501


class ATMGeoLocation(object):
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
        'geographic_coordinates': 'ATMGeographicCoordinates'
    }

    attribute_map = {
        'geographic_coordinates': 'GeographicCoordinates'
    }

    def __init__(self, geographic_coordinates=None):  # noqa: E501
        """ATMGeoLocation - a model defined in Swagger"""  # noqa: E501

        self._geographic_coordinates = None
        self.discriminator = None

        if geographic_coordinates is not None:
            self.geographic_coordinates = geographic_coordinates

    @property
    def geographic_coordinates(self):
        """Gets the geographic_coordinates of this ATMGeoLocation.  # noqa: E501


        :return: The geographic_coordinates of this ATMGeoLocation.  # noqa: E501
        :rtype: ATMGeographicCoordinates
        """
        return self._geographic_coordinates

    @geographic_coordinates.setter
    def geographic_coordinates(self, geographic_coordinates):
        """Sets the geographic_coordinates of this ATMGeoLocation.


        :param geographic_coordinates: The geographic_coordinates of this ATMGeoLocation.  # noqa: E501
        :type: ATMGeographicCoordinates
        """

        self._geographic_coordinates = geographic_coordinates

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
        if not isinstance(other, ATMGeoLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other