# yapily.AccountsApi

All URIs are relative to *https://api.yapily.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_using_get**](AccountsApi.md#get_account_using_get) | **GET** /accounts/{accountId} | Get account
[**get_accounts_using_get**](AccountsApi.md#get_accounts_using_get) | **GET** /accounts | Get accounts


# **get_account_using_get**
> Account get_account_using_get(account_id, consent=consent)

Get account

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
consent = 'consent_example' # str | Consent Token (optional)

try:
    # Get account
    api_response = api_instance.get_account_using_get(account_id, consent=consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **consent** | **str**| Consent Token | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_using_get**
> list[Account] get_accounts_using_get(consent=consent)

Get accounts

### Example
```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = yapily.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = yapily.AccountsApi(yapily.ApiClient(configuration))
consent = 'consent_example' # str | Consent Token (optional)

try:
    # Get accounts
    api_response = api_instance.get_accounts_using_get(consent=consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent** | **str**| Consent Token | [optional] 

### Return type

[**list[Account]**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
