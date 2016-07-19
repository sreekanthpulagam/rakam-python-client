# rakam_client.UserApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](UserApi.md#create_segment) | **POST** /user/create_segment | Get events of the user
[**create_user**](UserApi.md#create_user) | **POST** /user/create | Create new user
[**create_users**](UserApi.md#create_users) | **POST** /user/batch/create | Create multiple new users
[**get_events**](UserApi.md#get_events) | **POST** /user/get_events | Get events of the user
[**get_metadata**](UserApi.md#get_metadata) | **GET** /user/metadata | Get user storage metadata
[**get_user**](UserApi.md#get_user) | **POST** /user/get | Get user
[**increment_property**](UserApi.md#increment_property) | **POST** /user/increment_property | Set user property
[**search_users**](UserApi.md#search_users) | **POST** /user/search | Search users
[**set_properties**](UserApi.md#set_properties) | **POST** /user/set_properties | Set user properties
[**set_properties_once**](UserApi.md#set_properties_once) | **POST** /user/set_properties_once | Set user properties once
[**unset_property**](UserApi.md#unset_property) | **POST** /user/unset_properties | Unset user property


# **create_segment**
> SuccessMessage create_segment(user_create_segment)

Get events of the user



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: read_key
rakam_client.configuration.api_key['read_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['read_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_create_segment = rakam_client.UserCreateSegment() # UserCreateSegment | 

try: 
    # Get events of the user
    api_response = api_instance.create_segment(user_create_segment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_segment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_segment** | [**UserCreateSegment**](UserCreateSegment.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> int create_user(user)

Create new user



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.UserApi()
user = rakam_client.User() # User | 

try: 
    # Create new user
    api_response = api_instance.create_user(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_users**
> list[object] create_users(user_create_users)

Create multiple new users

Returns user ids. User id may be string or numeric.

### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: write_key
rakam_client.configuration.api_key['write_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['write_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_create_users = rakam_client.UserCreateUsers() # UserCreateUsers | 

try: 
    # Create multiple new users
    api_response = api_instance.create_users(user_create_users)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_users** | [**UserCreateUsers**](UserCreateUsers.md)|  | 

### Return type

**list[object]**

### Authorization

[write_key](../README.md#write_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> list[CollectionEvent] get_events(user_get_events)

Get events of the user



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: read_key
rakam_client.configuration.api_key['read_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['read_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_get_events = rakam_client.UserGetEvents() # UserGetEvents | 

try: 
    # Get events of the user
    api_response = api_instance.get_events(user_get_events)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_get_events** | [**UserGetEvents**](UserGetEvents.md)|  | 

### Return type

[**list[CollectionEvent]**](CollectionEvent.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> MetadataResponse get_metadata()

Get user storage metadata



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: read_key
rakam_client.configuration.api_key['read_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['read_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()

try: 
    # Get user storage metadata
    api_response = api_instance.get_metadata()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_metadata: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_get_user)

Get user



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: read_key
rakam_client.configuration.api_key['read_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['read_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_get_user = rakam_client.UserGetUser() # UserGetUser | 

try: 
    # Get user
    api_response = api_instance.get_user(user_get_user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_get_user** | [**UserGetUser**](UserGetUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increment_property**
> SuccessMessage increment_property(user_increment_property)

Set user property



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: master_key
rakam_client.configuration.api_key['master_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['master_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_increment_property = rakam_client.UserIncrementProperty() # UserIncrementProperty | 

try: 
    # Set user property
    api_response = api_instance.increment_property(user_increment_property)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->increment_property: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_increment_property** | [**UserIncrementProperty**](UserIncrementProperty.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> QueryResult search_users(user_search_users)

Search users



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: read_key
rakam_client.configuration.api_key['read_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# rakam_client.configuration.api_key_prefix['read_key'] = 'Bearer'

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_search_users = rakam_client.UserSearchUsers() # UserSearchUsers | 

try: 
    # Search users
    api_response = api_instance.search_users(user_search_users)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->search_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_search_users** | [**UserSearchUsers**](UserSearchUsers.md)|  | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_properties**
> int set_properties(user)

Set user properties



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.UserApi()
user = rakam_client.User() # User | 

try: 
    # Set user properties
    api_response = api_instance.set_properties(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->set_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_properties_once**
> int set_properties_once(user)

Set user properties once



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.UserApi()
user = rakam_client.User() # User | 

try: 
    # Set user properties once
    api_response = api_instance.set_properties_once(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->set_properties_once: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_property**
> SuccessMessage unset_property(user_unset_property)

Unset user property



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.UserApi()
user_unset_property = rakam_client.UserUnsetProperty() # UserUnsetProperty | 

try: 
    # Unset user property
    api_response = api_instance.unset_property(user_unset_property)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->unset_property: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_unset_property** | [**UserUnsetProperty**](UserUnsetProperty.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

