# rakam_client.MaterializedviewApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](MaterializedviewApi.md#create_view) | **POST** /materialized-view/create | Create view
[**delete_view**](MaterializedviewApi.md#delete_view) | **POST** /materialized-view/delete | Delete materialized view
[**get_schema_of_view**](MaterializedviewApi.md#get_schema_of_view) | **POST** /materialized-view/schema | Get schemas
[**get_view**](MaterializedviewApi.md#get_view) | **POST** /materialized-view/get | Get view
[**list_views**](MaterializedviewApi.md#list_views) | **POST** /materialized-view/list | List views


# **create_view**
> SuccessMessage create_view(materialized_view)

Create view



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
api_instance = rakam_client.MaterializedviewApi()
materialized_view = rakam_client.MaterializedView() # MaterializedView | 

try: 
    # Create view
    api_response = api_instance.create_view(materialized_view)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaterializedviewApi->create_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **materialized_view** | [**MaterializedView**](MaterializedView.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view**
> SuccessMessage delete_view(materialized_view_delete_view)

Delete materialized view



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
api_instance = rakam_client.MaterializedviewApi()
materialized_view_delete_view = rakam_client.MaterializedViewDeleteView() # MaterializedViewDeleteView | 

try: 
    # Delete materialized view
    api_response = api_instance.delete_view(materialized_view_delete_view)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaterializedviewApi->delete_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **materialized_view_delete_view** | [**MaterializedViewDeleteView**](MaterializedViewDeleteView.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_of_view**
> list[MaterializedViewSchema] get_schema_of_view(materialized_view_get_schema_of_view)

Get schemas



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
api_instance = rakam_client.MaterializedviewApi()
materialized_view_get_schema_of_view = rakam_client.MaterializedViewGetSchemaOfView() # MaterializedViewGetSchemaOfView | 

try: 
    # Get schemas
    api_response = api_instance.get_schema_of_view(materialized_view_get_schema_of_view)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaterializedviewApi->get_schema_of_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **materialized_view_get_schema_of_view** | [**MaterializedViewGetSchemaOfView**](MaterializedViewGetSchemaOfView.md)|  | 

### Return type

[**list[MaterializedViewSchema]**](MaterializedViewSchema.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> MaterializedView get_view(materialized_view_get_view)

Get view



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
api_instance = rakam_client.MaterializedviewApi()
materialized_view_get_view = rakam_client.MaterializedViewGetView() # MaterializedViewGetView | 

try: 
    # Get view
    api_response = api_instance.get_view(materialized_view_get_view)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaterializedviewApi->get_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **materialized_view_get_view** | [**MaterializedViewGetView**](MaterializedViewGetView.md)|  | 

### Return type

[**MaterializedView**](MaterializedView.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_views**
> list[MaterializedView] list_views()

List views



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
api_instance = rakam_client.MaterializedviewApi()

try: 
    # List views
    api_response = api_instance.list_views()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaterializedviewApi->list_views: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaterializedView]**](MaterializedView.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

