# rakam_client.ContinuousqueryApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query**](ContinuousqueryApi.md#create_query) | **POST** /continuous-query/create | Create stream
[**delete_query**](ContinuousqueryApi.md#delete_query) | **POST** /continuous-query/delete | Delete stream
[**get_query**](ContinuousqueryApi.md#get_query) | **POST** /continuous-query/get | Get continuous query
[**get_schema_of_query**](ContinuousqueryApi.md#get_schema_of_query) | **POST** /continuous-query/schema | Get query schema
[**list_queries**](ContinuousqueryApi.md#list_queries) | **POST** /continuous-query/list | List queries
[**test_query**](ContinuousqueryApi.md#test_query) | **POST** /continuous-query/test | Test continuous query


# **create_query**
> SuccessMessage create_query(continuous_query)

Create stream

Creates a new continuous query for specified SQL query. Rakam will process data in batches keep the result of query in-memory all the time. Compared to reports, continuous queries continuously aggregate the data on the fly and the result is always available either in-memory or disk.

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
api_instance = rakam_client.ContinuousqueryApi()
continuous_query = rakam_client.ContinuousQuery() # ContinuousQuery | 

try: 
    # Create stream
    api_response = api_instance.create_query(continuous_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->create_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuous_query** | [**ContinuousQuery**](ContinuousQuery.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query**
> SuccessMessage delete_query(continuous_query_delete_query)

Delete stream



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
api_instance = rakam_client.ContinuousqueryApi()
continuous_query_delete_query = rakam_client.ContinuousQueryDeleteQuery() # ContinuousQueryDeleteQuery | 

try: 
    # Delete stream
    api_response = api_instance.delete_query(continuous_query_delete_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->delete_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuous_query_delete_query** | [**ContinuousQueryDeleteQuery**](ContinuousQueryDeleteQuery.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query**
> ContinuousQuery get_query(continuous_query_get_query)

Get continuous query



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
api_instance = rakam_client.ContinuousqueryApi()
continuous_query_get_query = rakam_client.ContinuousQueryGetQuery() # ContinuousQueryGetQuery | 

try: 
    # Get continuous query
    api_response = api_instance.get_query(continuous_query_get_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->get_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuous_query_get_query** | [**ContinuousQueryGetQuery**](ContinuousQueryGetQuery.md)|  | 

### Return type

[**ContinuousQuery**](ContinuousQuery.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_of_query**
> list[Collection] get_schema_of_query(continuous_query_get_schema_of_query)

Get query schema



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
api_instance = rakam_client.ContinuousqueryApi()
continuous_query_get_schema_of_query = rakam_client.ContinuousQueryGetSchemaOfQuery() # ContinuousQueryGetSchemaOfQuery | 

try: 
    # Get query schema
    api_response = api_instance.get_schema_of_query(continuous_query_get_schema_of_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->get_schema_of_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuous_query_get_schema_of_query** | [**ContinuousQueryGetSchemaOfQuery**](ContinuousQueryGetSchemaOfQuery.md)|  | 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queries**
> list[ContinuousQuery] list_queries()

List queries



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
api_instance = rakam_client.ContinuousqueryApi()

try: 
    # List queries
    api_response = api_instance.list_queries()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->list_queries: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ContinuousQuery]**](ContinuousQuery.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_query**
> bool test_query(continuous_query_test_query)

Test continuous query



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
api_instance = rakam_client.ContinuousqueryApi()
continuous_query_test_query = rakam_client.ContinuousQueryTestQuery() # ContinuousQueryTestQuery | 

try: 
    # Test continuous query
    api_response = api_instance.test_query(continuous_query_test_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContinuousqueryApi->test_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuous_query_test_query** | [**ContinuousQueryTestQuery**](ContinuousQueryTestQuery.md)|  | 

### Return type

**bool**

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

