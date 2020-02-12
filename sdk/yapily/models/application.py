# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.168-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.institution import Institution  # noqa: F401,E501
from yapily.models.media import Media  # noqa: F401,E501


class Application(object):
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
        'uuid': 'str',
        'name': 'str',
        'active': 'bool',
        'auth_callbacks': 'list[str]',
        'institutions': 'list[Institution]',
        'media': 'list[Media]',
        'created': 'datetime',
        'updated': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'active': 'active',
        'auth_callbacks': 'authCallbacks',
        'institutions': 'institutions',
        'media': 'media',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, uuid=None, name=None, active=None, auth_callbacks=None, institutions=None, media=None, created=None, updated=None):  # noqa: E501
        """Application - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._name = None
        self._active = None
        self._auth_callbacks = None
        self._institutions = None
        self._media = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if auth_callbacks is not None:
            self.auth_callbacks = auth_callbacks
        if institutions is not None:
            self.institutions = institutions
        if media is not None:
            self.media = media
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def uuid(self):
        """Gets the uuid of this Application.  # noqa: E501

        Application UUID  # noqa: E501

        :return: The uuid of this Application.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Application.

        Application UUID  # noqa: E501

        :param uuid: The uuid of this Application.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501


        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.


        :param name: The name of this Application.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this Application.  # noqa: E501


        :return: The active of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Application.


        :param active: The active of this Application.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def auth_callbacks(self):
        """Gets the auth_callbacks of this Application.  # noqa: E501


        :return: The auth_callbacks of this Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._auth_callbacks

    @auth_callbacks.setter
    def auth_callbacks(self, auth_callbacks):
        """Sets the auth_callbacks of this Application.


        :param auth_callbacks: The auth_callbacks of this Application.  # noqa: E501
        :type: list[str]
        """

        self._auth_callbacks = auth_callbacks

    @property
    def institutions(self):
        """Gets the institutions of this Application.  # noqa: E501


        :return: The institutions of this Application.  # noqa: E501
        :rtype: list[Institution]
        """
        return self._institutions

    @institutions.setter
    def institutions(self, institutions):
        """Sets the institutions of this Application.


        :param institutions: The institutions of this Application.  # noqa: E501
        :type: list[Institution]
        """

        self._institutions = institutions

    @property
    def media(self):
        """Gets the media of this Application.  # noqa: E501


        :return: The media of this Application.  # noqa: E501
        :rtype: list[Media]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this Application.


        :param media: The media of this Application.  # noqa: E501
        :type: list[Media]
        """

        self._media = media

    @property
    def created(self):
        """Gets the created of this Application.  # noqa: E501


        :return: The created of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Application.


        :param created: The created of this Application.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Application.  # noqa: E501


        :return: The updated of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Application.


        :param updated: The updated of this Application.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
