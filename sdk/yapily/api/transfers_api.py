# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.170
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class TransfersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transfer_using_put(self, consent, account_id, **kwargs):  # noqa: E501
        """Transfer money from one account to another account accessible with the same consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.transfer_using_put(consent, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param TransferRequest transfer_request: transferRequest
        :return: ApiResponseOfTransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.transfer_using_put_with_http_info(consent, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_using_put_with_http_info(consent, account_id, **kwargs)  # noqa: E501
            return data

    def transfer_using_put_with_http_info(self, consent, account_id, **kwargs):  # noqa: E501
        """Transfer money from one account to another account accessible with the same consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.transfer_using_put_with_http_info(consent, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param TransferRequest transfer_request: transferRequest
        :return: ApiResponseOfTransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent', 'account_id', 'transfer_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `transfer_using_put`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `transfer_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transfer_request' in params:
            body_params = params['transfer_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/transfer', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfTransferResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
