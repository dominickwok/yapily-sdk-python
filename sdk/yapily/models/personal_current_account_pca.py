# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.165
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.personal_current_account_pca_marketing_state import PersonalCurrentAccountPCAMarketingState  # noqa: F401,E501


class PersonalCurrentAccountPCA(object):
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
        'identification': 'str',
        'name': 'str',
        'pca_marketing_state': 'list[PersonalCurrentAccountPCAMarketingState]',
        'segment': 'list[str]'
    }

    attribute_map = {
        'identification': 'Identification',
        'name': 'Name',
        'pca_marketing_state': 'PCAMarketingState',
        'segment': 'Segment'
    }

    def __init__(self, identification=None, name=None, pca_marketing_state=None, segment=None):  # noqa: E501
        """PersonalCurrentAccountPCA - a model defined in Swagger"""  # noqa: E501

        self._identification = None
        self._name = None
        self._pca_marketing_state = None
        self._segment = None
        self.discriminator = None

        if identification is not None:
            self.identification = identification
        if name is not None:
            self.name = name
        if pca_marketing_state is not None:
            self.pca_marketing_state = pca_marketing_state
        if segment is not None:
            self.segment = segment

    @property
    def identification(self):
        """Gets the identification of this PersonalCurrentAccountPCA.  # noqa: E501


        :return: The identification of this PersonalCurrentAccountPCA.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PersonalCurrentAccountPCA.


        :param identification: The identification of this PersonalCurrentAccountPCA.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def name(self):
        """Gets the name of this PersonalCurrentAccountPCA.  # noqa: E501


        :return: The name of this PersonalCurrentAccountPCA.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalCurrentAccountPCA.


        :param name: The name of this PersonalCurrentAccountPCA.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pca_marketing_state(self):
        """Gets the pca_marketing_state of this PersonalCurrentAccountPCA.  # noqa: E501


        :return: The pca_marketing_state of this PersonalCurrentAccountPCA.  # noqa: E501
        :rtype: list[PersonalCurrentAccountPCAMarketingState]
        """
        return self._pca_marketing_state

    @pca_marketing_state.setter
    def pca_marketing_state(self, pca_marketing_state):
        """Sets the pca_marketing_state of this PersonalCurrentAccountPCA.


        :param pca_marketing_state: The pca_marketing_state of this PersonalCurrentAccountPCA.  # noqa: E501
        :type: list[PersonalCurrentAccountPCAMarketingState]
        """

        self._pca_marketing_state = pca_marketing_state

    @property
    def segment(self):
        """Gets the segment of this PersonalCurrentAccountPCA.  # noqa: E501


        :return: The segment of this PersonalCurrentAccountPCA.  # noqa: E501
        :rtype: list[str]
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this PersonalCurrentAccountPCA.


        :param segment: The segment of this PersonalCurrentAccountPCA.  # noqa: E501
        :type: list[str]
        """

        self._segment = segment

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
        if not isinstance(other, PersonalCurrentAccountPCA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
