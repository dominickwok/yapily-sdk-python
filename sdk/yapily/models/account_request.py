# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.176
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountRequest(object):
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
        'transaction_from': 'datetime',
        'transaction_to': 'datetime',
        'expires_at': 'datetime',
        'feature_scope': 'list[str]'
    }

    attribute_map = {
        'transaction_from': 'transactionFrom',
        'transaction_to': 'transactionTo',
        'expires_at': 'expiresAt',
        'feature_scope': 'featureScope'
    }

    def __init__(self, transaction_from=None, transaction_to=None, expires_at=None, feature_scope=None):  # noqa: E501
        """AccountRequest - a model defined in Swagger"""  # noqa: E501

        self._transaction_from = None
        self._transaction_to = None
        self._expires_at = None
        self._feature_scope = None
        self.discriminator = None

        if transaction_from is not None:
            self.transaction_from = transaction_from
        if transaction_to is not None:
            self.transaction_to = transaction_to
        if expires_at is not None:
            self.expires_at = expires_at
        if feature_scope is not None:
            self.feature_scope = feature_scope

    @property
    def transaction_from(self):
        """Gets the transaction_from of this AccountRequest.  # noqa: E501


        :return: The transaction_from of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_from

    @transaction_from.setter
    def transaction_from(self, transaction_from):
        """Sets the transaction_from of this AccountRequest.


        :param transaction_from: The transaction_from of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._transaction_from = transaction_from

    @property
    def transaction_to(self):
        """Gets the transaction_to of this AccountRequest.  # noqa: E501


        :return: The transaction_to of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_to

    @transaction_to.setter
    def transaction_to(self, transaction_to):
        """Sets the transaction_to of this AccountRequest.


        :param transaction_to: The transaction_to of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._transaction_to = transaction_to

    @property
    def expires_at(self):
        """Gets the expires_at of this AccountRequest.  # noqa: E501


        :return: The expires_at of this AccountRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AccountRequest.


        :param expires_at: The expires_at of this AccountRequest.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def feature_scope(self):
        """Gets the feature_scope of this AccountRequest.  # noqa: E501


        :return: The feature_scope of this AccountRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_scope

    @feature_scope.setter
    def feature_scope(self, feature_scope):
        """Sets the feature_scope of this AccountRequest.


        :param feature_scope: The feature_scope of this AccountRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["INITIATE_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_STATEMENTS", "ACCOUNT_STATEMENT", "ACCOUNT_STATEMENT_FILE", "ACCOUNT_SCHEDULED_PAYMENTS", "ACCOUNT_DIRECT_DEBITS", "ACCOUNT_PERIODIC_PAYMENTS", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "INITIATE_DOMESTIC_SINGLE_PAYMENT", "CREATE_DOMESTIC_SINGLE_PAYMENT", "INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "INITIATE_DOMESTIC_SCHEDULED_PAYMENT", "CREATE_DOMESTIC_SCHEDULED_PAYMENT", "INITIATE_DOMESTIC_PERIODIC_PAYMENT", "CREATE_DOMESTIC_PERIODIC_PAYMENT", "PERIODIC_PAYMENT_FREQUENCY_EXTENDED", "INITIATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "CREATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT", "CREATE_INTERNATIONAL_SCHEDULED_PAYMENT", "INITIATE_INTERNATIONAL_PERIODIC_PAYMENT", "CREATE_INTERNATIONAL_PERIODIC_PAYMENT", "INITIATE_INTERNATIONAL_SINGLE_PAYMENT", "CREATE_INTERNATIONAL_SINGLE_PAYMENT", "INITIATE_BULK_PAYMENT", "CREATE_BULK_PAYMENT", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS"]  # noqa: E501
        if not set(feature_scope).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `feature_scope` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(feature_scope) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._feature_scope = feature_scope

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
        if not isinstance(other, AccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
