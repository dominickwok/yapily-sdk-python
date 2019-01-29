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

from yapily.models.atm_branch import ATMBranch  # noqa: F401,E501
from yapily.models.atm_location import ATMLocation  # noqa: F401,E501
from yapily.models.atm_open_data_other_accessibility import ATMOpenDataOtherAccessibility  # noqa: F401,E501
from yapily.models.atm_open_data_other_atm_services import ATMOpenDataOtherATMServices  # noqa: F401,E501


class ATMOpenDataATM(object):
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
        'access24_hours_indicator': 'bool',
        'accessibility': 'list[str]',
        'branch': 'ATMBranch',
        'identification': 'str',
        'location': 'ATMLocation',
        'minimum_possible_amount': 'str',
        'note': 'str',
        'other_atm_services': 'list[ATMOpenDataOtherATMServices]',
        'other_accessibility': 'list[ATMOpenDataOtherAccessibility]',
        'services': 'list[str]',
        'supported_currencies': 'list[str]',
        'supported_languages': 'list[str]'
    }

    attribute_map = {
        'access24_hours_indicator': 'Access24HoursIndicator',
        'accessibility': 'Accessibility',
        'branch': 'Branch',
        'identification': 'Identification',
        'location': 'Location',
        'minimum_possible_amount': 'MinimumPossibleAmount',
        'note': 'Note',
        'other_atm_services': 'OtherATMServices',
        'other_accessibility': 'OtherAccessibility',
        'services': 'Services',
        'supported_currencies': 'SupportedCurrencies',
        'supported_languages': 'SupportedLanguages'
    }

    def __init__(self, access24_hours_indicator=None, accessibility=None, branch=None, identification=None, location=None, minimum_possible_amount=None, note=None, other_atm_services=None, other_accessibility=None, services=None, supported_currencies=None, supported_languages=None):  # noqa: E501
        """ATMOpenDataATM - a model defined in Swagger"""  # noqa: E501

        self._access24_hours_indicator = None
        self._accessibility = None
        self._branch = None
        self._identification = None
        self._location = None
        self._minimum_possible_amount = None
        self._note = None
        self._other_atm_services = None
        self._other_accessibility = None
        self._services = None
        self._supported_currencies = None
        self._supported_languages = None
        self.discriminator = None

        if access24_hours_indicator is not None:
            self.access24_hours_indicator = access24_hours_indicator
        if accessibility is not None:
            self.accessibility = accessibility
        if branch is not None:
            self.branch = branch
        if identification is not None:
            self.identification = identification
        if location is not None:
            self.location = location
        if minimum_possible_amount is not None:
            self.minimum_possible_amount = minimum_possible_amount
        if note is not None:
            self.note = note
        if other_atm_services is not None:
            self.other_atm_services = other_atm_services
        if other_accessibility is not None:
            self.other_accessibility = other_accessibility
        if services is not None:
            self.services = services
        if supported_currencies is not None:
            self.supported_currencies = supported_currencies
        if supported_languages is not None:
            self.supported_languages = supported_languages

    @property
    def access24_hours_indicator(self):
        """Gets the access24_hours_indicator of this ATMOpenDataATM.  # noqa: E501


        :return: The access24_hours_indicator of this ATMOpenDataATM.  # noqa: E501
        :rtype: bool
        """
        return self._access24_hours_indicator

    @access24_hours_indicator.setter
    def access24_hours_indicator(self, access24_hours_indicator):
        """Sets the access24_hours_indicator of this ATMOpenDataATM.


        :param access24_hours_indicator: The access24_hours_indicator of this ATMOpenDataATM.  # noqa: E501
        :type: bool
        """

        self._access24_hours_indicator = access24_hours_indicator

    @property
    def accessibility(self):
        """Gets the accessibility of this ATMOpenDataATM.  # noqa: E501


        :return: The accessibility of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this ATMOpenDataATM.


        :param accessibility: The accessibility of this ATMOpenDataATM.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AudioCashMachine", "AutomaticDoors", "ExternalRamp", "InductionLoop", "InternalRamp", "LevelAccess", "LowerLevelCounter", "Other", "WheelchairAccess"]  # noqa: E501
        if not set(accessibility).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `accessibility` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(accessibility) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._accessibility = accessibility

    @property
    def branch(self):
        """Gets the branch of this ATMOpenDataATM.  # noqa: E501


        :return: The branch of this ATMOpenDataATM.  # noqa: E501
        :rtype: ATMBranch
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ATMOpenDataATM.


        :param branch: The branch of this ATMOpenDataATM.  # noqa: E501
        :type: ATMBranch
        """

        self._branch = branch

    @property
    def identification(self):
        """Gets the identification of this ATMOpenDataATM.  # noqa: E501


        :return: The identification of this ATMOpenDataATM.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this ATMOpenDataATM.


        :param identification: The identification of this ATMOpenDataATM.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def location(self):
        """Gets the location of this ATMOpenDataATM.  # noqa: E501


        :return: The location of this ATMOpenDataATM.  # noqa: E501
        :rtype: ATMLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ATMOpenDataATM.


        :param location: The location of this ATMOpenDataATM.  # noqa: E501
        :type: ATMLocation
        """

        self._location = location

    @property
    def minimum_possible_amount(self):
        """Gets the minimum_possible_amount of this ATMOpenDataATM.  # noqa: E501


        :return: The minimum_possible_amount of this ATMOpenDataATM.  # noqa: E501
        :rtype: str
        """
        return self._minimum_possible_amount

    @minimum_possible_amount.setter
    def minimum_possible_amount(self, minimum_possible_amount):
        """Sets the minimum_possible_amount of this ATMOpenDataATM.


        :param minimum_possible_amount: The minimum_possible_amount of this ATMOpenDataATM.  # noqa: E501
        :type: str
        """

        self._minimum_possible_amount = minimum_possible_amount

    @property
    def note(self):
        """Gets the note of this ATMOpenDataATM.  # noqa: E501


        :return: The note of this ATMOpenDataATM.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ATMOpenDataATM.


        :param note: The note of this ATMOpenDataATM.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def other_atm_services(self):
        """Gets the other_atm_services of this ATMOpenDataATM.  # noqa: E501


        :return: The other_atm_services of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[ATMOpenDataOtherATMServices]
        """
        return self._other_atm_services

    @other_atm_services.setter
    def other_atm_services(self, other_atm_services):
        """Sets the other_atm_services of this ATMOpenDataATM.


        :param other_atm_services: The other_atm_services of this ATMOpenDataATM.  # noqa: E501
        :type: list[ATMOpenDataOtherATMServices]
        """

        self._other_atm_services = other_atm_services

    @property
    def other_accessibility(self):
        """Gets the other_accessibility of this ATMOpenDataATM.  # noqa: E501


        :return: The other_accessibility of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[ATMOpenDataOtherAccessibility]
        """
        return self._other_accessibility

    @other_accessibility.setter
    def other_accessibility(self, other_accessibility):
        """Sets the other_accessibility of this ATMOpenDataATM.


        :param other_accessibility: The other_accessibility of this ATMOpenDataATM.  # noqa: E501
        :type: list[ATMOpenDataOtherAccessibility]
        """

        self._other_accessibility = other_accessibility

    @property
    def services(self):
        """Gets the services of this ATMOpenDataATM.  # noqa: E501


        :return: The services of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ATMOpenDataATM.


        :param services: The services of this ATMOpenDataATM.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Balance", "BillPayments", "CashDeposits", "CharityDonation", "ChequeDeposits", "CashWithdrawal", "EnvelopeDeposit", "FastCash", "MobileBankingRegistration", "MobilePaymentRegistration", "MobilePhoneTopUp", "OrderStatement", "Other", "PINActivation", "PINChange", "PINUnblock", "MiniStatement"]  # noqa: E501
        if not set(services).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `services` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(services) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._services = services

    @property
    def supported_currencies(self):
        """Gets the supported_currencies of this ATMOpenDataATM.  # noqa: E501


        :return: The supported_currencies of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
        """Sets the supported_currencies of this ATMOpenDataATM.


        :param supported_currencies: The supported_currencies of this ATMOpenDataATM.  # noqa: E501
        :type: list[str]
        """

        self._supported_currencies = supported_currencies

    @property
    def supported_languages(self):
        """Gets the supported_languages of this ATMOpenDataATM.  # noqa: E501


        :return: The supported_languages of this ATMOpenDataATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_languages

    @supported_languages.setter
    def supported_languages(self, supported_languages):
        """Sets the supported_languages of this ATMOpenDataATM.


        :param supported_languages: The supported_languages of this ATMOpenDataATM.  # noqa: E501
        :type: list[str]
        """

        self._supported_languages = supported_languages

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
        if not isinstance(other, ATMOpenDataATM):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
