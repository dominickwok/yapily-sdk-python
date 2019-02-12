# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.79
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.application_users_api import ApplicationUsersApi  # noqa: E501
from yapily.rest import ApiException


class TestApplicationUsersApi(unittest.TestCase):
    """ApplicationUsersApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.application_users_api.ApplicationUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_using_post(self):
        """Test case for add_user_using_post

        Add an application user  # noqa: E501
        """
        pass

    def test_delete_user_using_delete(self):
        """Test case for delete_user_using_delete

        Delete an application user  # noqa: E501
        """
        pass

    def test_get_user_using_get(self):
        """Test case for get_user_using_get

        Get an application user  # noqa: E501
        """
        pass

    def test_get_users_using_get(self):
        """Test case for get_users_using_get

        Get application users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
