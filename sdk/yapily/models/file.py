# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.196
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class File(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'absolute': 'bool',
        'absolute_file': 'file',
        'absolute_path': 'str',
        'canonical_file': 'file',
        'canonical_path': 'str',
        'directory': 'bool',
        'file': 'bool',
        'free_space': 'int',
        'hidden': 'bool',
        'name': 'str',
        'parent': 'str',
        'parent_file': 'file',
        'path': 'str',
        'total_space': 'int',
        'usable_space': 'int'
    }

    attribute_map = {
        'absolute': 'absolute',
        'absolute_file': 'absoluteFile',
        'absolute_path': 'absolutePath',
        'canonical_file': 'canonicalFile',
        'canonical_path': 'canonicalPath',
        'directory': 'directory',
        'file': 'file',
        'free_space': 'freeSpace',
        'hidden': 'hidden',
        'name': 'name',
        'parent': 'parent',
        'parent_file': 'parentFile',
        'path': 'path',
        'total_space': 'totalSpace',
        'usable_space': 'usableSpace'
    }

    def __init__(self, absolute=None, absolute_file=None, absolute_path=None, canonical_file=None, canonical_path=None, directory=None, file=None, free_space=None, hidden=None, name=None, parent=None, parent_file=None, path=None, total_space=None, usable_space=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._absolute = None
        self._absolute_file = None
        self._absolute_path = None
        self._canonical_file = None
        self._canonical_path = None
        self._directory = None
        self._file = None
        self._free_space = None
        self._hidden = None
        self._name = None
        self._parent = None
        self._parent_file = None
        self._path = None
        self._total_space = None
        self._usable_space = None
        self.discriminator = None

        if absolute is not None:
            self.absolute = absolute
        if absolute_file is not None:
            self.absolute_file = absolute_file
        if absolute_path is not None:
            self.absolute_path = absolute_path
        if canonical_file is not None:
            self.canonical_file = canonical_file
        if canonical_path is not None:
            self.canonical_path = canonical_path
        if directory is not None:
            self.directory = directory
        if file is not None:
            self.file = file
        if free_space is not None:
            self.free_space = free_space
        if hidden is not None:
            self.hidden = hidden
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if parent_file is not None:
            self.parent_file = parent_file
        if path is not None:
            self.path = path
        if total_space is not None:
            self.total_space = total_space
        if usable_space is not None:
            self.usable_space = usable_space

    @property
    def absolute(self):
        """Gets the absolute of this File.  # noqa: E501


        :return: The absolute of this File.  # noqa: E501
        :rtype: bool
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        """Sets the absolute of this File.


        :param absolute: The absolute of this File.  # noqa: E501
        :type: bool
        """

        self._absolute = absolute

    @property
    def absolute_file(self):
        """Gets the absolute_file of this File.  # noqa: E501


        :return: The absolute_file of this File.  # noqa: E501
        :rtype: file
        """
        return self._absolute_file

    @absolute_file.setter
    def absolute_file(self, absolute_file):
        """Sets the absolute_file of this File.


        :param absolute_file: The absolute_file of this File.  # noqa: E501
        :type: file
        """

        self._absolute_file = absolute_file

    @property
    def absolute_path(self):
        """Gets the absolute_path of this File.  # noqa: E501


        :return: The absolute_path of this File.  # noqa: E501
        :rtype: str
        """
        return self._absolute_path

    @absolute_path.setter
    def absolute_path(self, absolute_path):
        """Sets the absolute_path of this File.


        :param absolute_path: The absolute_path of this File.  # noqa: E501
        :type: str
        """

        self._absolute_path = absolute_path

    @property
    def canonical_file(self):
        """Gets the canonical_file of this File.  # noqa: E501


        :return: The canonical_file of this File.  # noqa: E501
        :rtype: file
        """
        return self._canonical_file

    @canonical_file.setter
    def canonical_file(self, canonical_file):
        """Sets the canonical_file of this File.


        :param canonical_file: The canonical_file of this File.  # noqa: E501
        :type: file
        """

        self._canonical_file = canonical_file

    @property
    def canonical_path(self):
        """Gets the canonical_path of this File.  # noqa: E501


        :return: The canonical_path of this File.  # noqa: E501
        :rtype: str
        """
        return self._canonical_path

    @canonical_path.setter
    def canonical_path(self, canonical_path):
        """Sets the canonical_path of this File.


        :param canonical_path: The canonical_path of this File.  # noqa: E501
        :type: str
        """

        self._canonical_path = canonical_path

    @property
    def directory(self):
        """Gets the directory of this File.  # noqa: E501


        :return: The directory of this File.  # noqa: E501
        :rtype: bool
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this File.


        :param directory: The directory of this File.  # noqa: E501
        :type: bool
        """

        self._directory = directory

    @property
    def file(self):
        """Gets the file of this File.  # noqa: E501


        :return: The file of this File.  # noqa: E501
        :rtype: bool
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this File.


        :param file: The file of this File.  # noqa: E501
        :type: bool
        """

        self._file = file

    @property
    def free_space(self):
        """Gets the free_space of this File.  # noqa: E501


        :return: The free_space of this File.  # noqa: E501
        :rtype: int
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """Sets the free_space of this File.


        :param free_space: The free_space of this File.  # noqa: E501
        :type: int
        """

        self._free_space = free_space

    @property
    def hidden(self):
        """Gets the hidden of this File.  # noqa: E501


        :return: The hidden of this File.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this File.


        :param hidden: The hidden of this File.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501


        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.


        :param name: The name of this File.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this File.  # noqa: E501


        :return: The parent of this File.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this File.


        :param parent: The parent of this File.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def parent_file(self):
        """Gets the parent_file of this File.  # noqa: E501


        :return: The parent_file of this File.  # noqa: E501
        :rtype: file
        """
        return self._parent_file

    @parent_file.setter
    def parent_file(self, parent_file):
        """Sets the parent_file of this File.


        :param parent_file: The parent_file of this File.  # noqa: E501
        :type: file
        """

        self._parent_file = parent_file

    @property
    def path(self):
        """Gets the path of this File.  # noqa: E501


        :return: The path of this File.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this File.


        :param path: The path of this File.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def total_space(self):
        """Gets the total_space of this File.  # noqa: E501


        :return: The total_space of this File.  # noqa: E501
        :rtype: int
        """
        return self._total_space

    @total_space.setter
    def total_space(self, total_space):
        """Sets the total_space of this File.


        :param total_space: The total_space of this File.  # noqa: E501
        :type: int
        """

        self._total_space = total_space

    @property
    def usable_space(self):
        """Gets the usable_space of this File.  # noqa: E501


        :return: The usable_space of this File.  # noqa: E501
        :rtype: int
        """
        return self._usable_space

    @usable_space.setter
    def usable_space(self, usable_space):
        """Sets the usable_space of this File.


        :param usable_space: The usable_space of this File.  # noqa: E501
        :type: int
        """

        self._usable_space = usable_space

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
