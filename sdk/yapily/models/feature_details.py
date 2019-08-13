# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.133
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureDetails(object):
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
        'feature': 'str',
        'endpoint': 'str',
        'documentation_url': 'str'
    }

    attribute_map = {
        'feature': 'feature',
        'endpoint': 'endpoint',
        'documentation_url': 'documentationUrl'
    }

    def __init__(self, feature=None, endpoint=None, documentation_url=None):  # noqa: E501
        """FeatureDetails - a model defined in Swagger"""  # noqa: E501

        self._feature = None
        self._endpoint = None
        self._documentation_url = None
        self.discriminator = None

        if feature is not None:
            self.feature = feature
        if endpoint is not None:
            self.endpoint = endpoint
        if documentation_url is not None:
            self.documentation_url = documentation_url

    @property
    def feature(self):
        """Gets the feature of this FeatureDetails.  # noqa: E501


        :return: The feature of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeatureDetails.


        :param feature: The feature of this FeatureDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIATE_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_STATEMENTS", "ACCOUNT_STATEMENT", "ACCOUNT_STATEMENT_FILE", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "INITIATE_PAYMENT", "CREATE_PAYMENT", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS"]  # noqa: E501
        if feature not in allowed_values:
            raise ValueError(
                "Invalid value for `feature` ({0}), must be one of {1}"  # noqa: E501
                .format(feature, allowed_values)
            )

        self._feature = feature

    @property
    def endpoint(self):
        """Gets the endpoint of this FeatureDetails.  # noqa: E501


        :return: The endpoint of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this FeatureDetails.


        :param endpoint: The endpoint of this FeatureDetails.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def documentation_url(self):
        """Gets the documentation_url of this FeatureDetails.  # noqa: E501


        :return: The documentation_url of this FeatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this FeatureDetails.


        :param documentation_url: The documentation_url of this FeatureDetails.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

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
        if not isinstance(other, FeatureDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
