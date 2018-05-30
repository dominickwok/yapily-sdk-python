# yapily
To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.5
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import yapily 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import yapily
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import yapily
from yapily.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
yapily.configuration.username = 'YOUR_USERNAME'
yapily.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = yapily.AccountsApi()
account_id = 'account_id_example' # str | accountId
consent = 'consent_example' # str | Consent Token (optional)

try:
    # Get account
    api_response = api_instance.get_account_using_get(account_id, consent=consent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_using_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.yapily.com:443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_account_using_get**](docs/AccountsApi.md#get_account_using_get) | **GET** /accounts/{accountId} | Get account
*AccountsApi* | [**get_accounts_using_get**](docs/AccountsApi.md#get_accounts_using_get) | **GET** /accounts | Get accounts
*ApplicationUsersApi* | [**add_user_using_post**](docs/ApplicationUsersApi.md#add_user_using_post) | **POST** /users | Add an application user
*ApplicationUsersApi* | [**get_user_using_get**](docs/ApplicationUsersApi.md#get_user_using_get) | **GET** /users/{uuid} | Get an application user
*ApplicationUsersApi* | [**get_users_using_get**](docs/ApplicationUsersApi.md#get_users_using_get) | **GET** /users | Get application users
*ApplicationUsersApi* | [**update_user_using_put**](docs/ApplicationUsersApi.md#update_user_using_put) | **PUT** /users/{uuid} | Update an application user
*ConsentsApi* | [**add_consent_using_post**](docs/ConsentsApi.md#add_consent_using_post) | **POST** /users/{userUuid}/consents | Post consent
*ConsentsApi* | [**delete_using_delete**](docs/ConsentsApi.md#delete_using_delete) | **DELETE** /users/{userUuid}/consents/{consentToken} | Delete consent
*ConsentsApi* | [**get_user_consents_using_get**](docs/ConsentsApi.md#get_user_consents_using_get) | **GET** /users/{userUuid}/consents | Get consent
*IdentityApi* | [**identity_using_get**](docs/IdentityApi.md#identity_using_get) | **GET** /identity | Get identity
*InstitutionsApi* | [**get_institution_using_get**](docs/InstitutionsApi.md#get_institution_using_get) | **GET** /institutions/{institutionId} | Retrieves details of a specific institution available in Yapily
*InstitutionsApi* | [**get_institutions_using_get**](docs/InstitutionsApi.md#get_institutions_using_get) | **GET** /institutions | Retrieves the list of institutions available in Yapily
*TransactionsApi* | [**get_transactions_using_get**](docs/TransactionsApi.md#get_transactions_using_get) | **GET** /accounts/{accountId}/transactions | Get account transactions


## Documentation For Models

 - [Account](docs/Account.md)
 - [ApplicationUser](docs/ApplicationUser.md)
 - [Consent](docs/Consent.md)
 - [Country](docs/Country.md)
 - [CreateConsentApiKey](docs/CreateConsentApiKey.md)
 - [Identity](docs/Identity.md)
 - [IdentityAddress](docs/IdentityAddress.md)
 - [Institution](docs/Institution.md)
 - [InstitutionConsent](docs/InstitutionConsent.md)
 - [Media](docs/Media.md)
 - [ResponseEntity](docs/ResponseEntity.md)
 - [Transaction](docs/Transaction.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author


