# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.172
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class AccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_account_direct_debits_using_get(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account direct debits  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_direct_debits_using_get(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's direct debit results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_account_direct_debits_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_direct_debits_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
            return data

    def get_account_direct_debits_using_get_with_http_info(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account direct debits  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_direct_debits_using_get_with_http_info(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's direct debit results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'consent', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_direct_debits_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_direct_debits_using_get`")  # noqa: E501
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_account_direct_debits_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/direct-debits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfPaymentResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_periodic_payments_using_get(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account payments detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_periodic_payments_using_get(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's periodic payment order results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_account_periodic_payments_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_periodic_payments_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
            return data

    def get_account_periodic_payments_using_get_with_http_info(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account payments detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_periodic_payments_using_get_with_http_info(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's periodic payment order results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'consent', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_periodic_payments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_periodic_payments_using_get`")  # noqa: E501
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_account_periodic_payments_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/periodic-payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfPaymentResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_scheduled_payments_using_get(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account scheduled payments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_scheduled_payments_using_get(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's scheduled payment results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_account_scheduled_payments_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_scheduled_payments_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501
            return data

    def get_account_scheduled_payments_using_get_with_http_info(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account scheduled payments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_scheduled_payments_using_get_with_http_info(account_id, consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: accountId (required)
        :param str consent: Consent Token (required)
        :param int limit: Use this parameter to limit account's scheduled payment results
        :return: ApiListResponseOfPaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'consent', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_scheduled_payments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_scheduled_payments_using_get`")  # noqa: E501
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_account_scheduled_payments_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/scheduled-payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfPaymentResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_account_using_get(self, consent, account_id, **kwargs):  # noqa: E501
        """Get account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_using_get(consent, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :return: ApiResponseOfAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_account_using_get_with_http_info(consent, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_using_get_with_http_info(consent, account_id, **kwargs)  # noqa: E501
            return data

    def get_account_using_get_with_http_info(self, consent, account_id, **kwargs):  # noqa: E501
        """Get account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_using_get_with_http_info(consent, account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :return: ApiResponseOfAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent', 'account_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_account_using_get`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_using_get`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAccount',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_accounts_using_get(self, consent, **kwargs):  # noqa: E501
        """Get accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_accounts_using_get(consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :return: ApiListResponseOfAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_accounts_using_get_with_http_info(consent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_accounts_using_get_with_http_info(consent, **kwargs)  # noqa: E501
            return data

    def get_accounts_using_get_with_http_info(self, consent, **kwargs):  # noqa: E501
        """Get accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_accounts_using_get_with_http_info(consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :return: ApiListResponseOfAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accounts_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `get_accounts_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfAccount',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def initiate_account_request_using_post(self, account_auth_request, **kwargs):  # noqa: E501
        """Initiate a new account request for user to authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.initiate_account_request_using_post(account_auth_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param AccountAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.initiate_account_request_using_post_with_http_info(account_auth_request, **kwargs)  # noqa: E501
        else:
            (data) = self.initiate_account_request_using_post_with_http_info(account_auth_request, **kwargs)  # noqa: E501
            return data

    def initiate_account_request_using_post_with_http_info(self, account_auth_request, **kwargs):  # noqa: E501
        """Initiate a new account request for user to authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.initiate_account_request_using_post_with_http_info(account_auth_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param AccountAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_auth_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_account_request_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_auth_request' is set
        if ('account_auth_request' not in params or
                params['account_auth_request'] is None):
            raise ValueError("Missing the required parameter `account_auth_request` when calling `initiate_account_request_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_auth_request' in params:
            body_params = params['account_auth_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account-auth-requests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAuthorisationRequestResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def re_authorise_account_using_patch(self, consent, **kwargs):  # noqa: E501
        """Re-authorize account request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.re_authorise_account_using_patch(consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.re_authorise_account_using_patch_with_http_info(consent, **kwargs)  # noqa: E501
        else:
            (data) = self.re_authorise_account_using_patch_with_http_info(consent, **kwargs)  # noqa: E501
            return data

    def re_authorise_account_using_patch_with_http_info(self, consent, **kwargs):  # noqa: E501
        """Re-authorize account request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.re_authorise_account_using_patch_with_http_info(consent, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent: Consent Token (required)
        :return: ApiResponseOfAuthorisationRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method re_authorise_account_using_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent' is set
        if ('consent' not in params or
                params['consent'] is None):
            raise ValueError("Missing the required parameter `consent` when calling `re_authorise_account_using_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consent' in params:
            header_params['consent'] = params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account-auth-requests', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAuthorisationRequestResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
