# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.196
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.international_payment_request import InternationalPaymentRequest  # noqa: E501
from yapily.rest import ApiException

class TestInternationalPaymentRequest(unittest.TestCase):
    """InternationalPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InternationalPaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.international_payment_request.InternationalPaymentRequest()  # noqa: E501
        if include_optional :
            return InternationalPaymentRequest(
                currency_of_transfer = '0', 
                exchange_rate_information = yapily.models.exchange_rate_information.ExchangeRateInformation(
                    foreign_exchange_contract_reference = '0', 
                    rate = 1.337, 
                    rate_type = 'ACTUAL', 
                    unit_currency = '0', ), 
                purpose = '0', 
                priority = 'NORMAL', 
                charge_bearer = 'DEBT'
            )
        else :
            return InternationalPaymentRequest(
                currency_of_transfer = '0',
        )

    def testInternationalPaymentRequest(self):
        """Test InternationalPaymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
