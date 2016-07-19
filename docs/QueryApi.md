# rakam_client.QueryApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute**](QueryApi.md#execute) | **POST** /query/execute | Execute query on event data-set
[**explain**](QueryApi.md#explain) | **POST** /query/explain | Explain query
[**metadata**](QueryApi.md#metadata) | **POST** /query/metadata | Test query


# **execute**
> QueryResult execute(execute)

Execute query on event data-set



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
api_instance = rakam_client.QueryApi()
execute = rakam_client.Execute() # Execute | 

try: 
    # Execute query on event data-set
    api_response = api_instance.execute(execute)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->execute: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute** | [**Execute**](Execute.md)|  | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain**
> ResponseQuery explain(explain)

Explain query



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
api_instance = rakam_client.QueryApi()
explain = rakam_client.Explain() # Explain | 

try: 
    # Explain query
    api_response = api_instance.explain(explain)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->explain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explain** | [**Explain**](Explain.md)|  | 

### Return type

[**ResponseQuery**](ResponseQuery.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata**
> list[SchemaField] metadata(query_metadata)

Test query



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
api_instance = rakam_client.QueryApi()
query_metadata = rakam_client.QueryMetadata() # QueryMetadata | 

try: 
    # Test query
    api_response = api_instance.metadata(query_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->metadata: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_metadata** | [**QueryMetadata**](QueryMetadata.md)|  | 

### Return type

[**list[SchemaField]**](SchemaField.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

