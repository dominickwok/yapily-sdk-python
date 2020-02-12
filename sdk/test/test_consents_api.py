# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.168-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.consents_api import ConsentsApi  # noqa: E501
from yapily.rest import ApiException


class TestConsentsApi(unittest.TestCase):
    """ConsentsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.consents_api.ConsentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_consent_using_post(self):
        """Test case for add_consent_using_post

        Post consent  # noqa: E501
        """
        pass

    def test_create_consent_with_code_using_post(self):
        """Test case for create_consent_with_code_using_post

        Post auth-code and auth-state  # noqa: E501
        """
        pass

    def test_delete_using_delete(self):
        """Test case for delete_using_delete

        Delete consent  # noqa: E501
        """
        pass

    def test_get_consent_by_id_using_get(self):
        """Test case for get_consent_by_id_using_get

        Get consent  # noqa: E501
        """
        pass

    def test_get_consent_by_single_access_consent_using_post(self):
        """Test case for get_consent_by_single_access_consent_using_post

        Post one time token  # noqa: E501
        """
        pass

    def test_get_consents_using_get(self):
        """Test case for get_consents_using_get

        Get consents sorted by creation date  # noqa: E501
        """
        pass

    def test_get_user_consents_using_get(self):
        """Test case for get_user_consents_using_get

        Get latest user consents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
