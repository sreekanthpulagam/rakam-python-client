# rakam_client.EventexplorerApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_events**](EventexplorerApi.md#analyze_events) | **POST** /event-explorer/analyze | Perform simple query on event data
[**create_precomputed_table**](EventexplorerApi.md#create_precomputed_table) | **POST** /event-explorer/pre_calculate | Create Pre-computed table
[**get_event_statistics**](EventexplorerApi.md#get_event_statistics) | **POST** /event-explorer/statistics | Event statistics
[**get_extra_dimensions**](EventexplorerApi.md#get_extra_dimensions) | **GET** /event-explorer/extra_dimensions | Event statistics


# **analyze_events**
> QueryResult analyze_events(analyze_request)

Perform simple query on event data



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
api_instance = rakam_client.EventexplorerApi()
analyze_request = rakam_client.AnalyzeRequest() # AnalyzeRequest | 

try: 
    # Perform simple query on event data
    api_response = api_instance.analyze_events(analyze_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventexplorerApi->analyze_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyze_request** | [**AnalyzeRequest**](AnalyzeRequest.md)|  | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_precomputed_table**
> PrecalculatedTable create_precomputed_table(create_precomputed_table)

Create Pre-computed table



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
api_instance = rakam_client.EventexplorerApi()
create_precomputed_table = rakam_client.CreatePrecomputedTable() # CreatePrecomputedTable | 

try: 
    # Create Pre-computed table
    api_response = api_instance.create_precomputed_table(create_precomputed_table)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventexplorerApi->create_precomputed_table: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_precomputed_table** | [**CreatePrecomputedTable**](CreatePrecomputedTable.md)|  | 

### Return type

[**PrecalculatedTable**](PrecalculatedTable.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_statistics**
> QueryResult get_event_statistics(event_explorer_get_event_statistics)

Event statistics



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
api_instance = rakam_client.EventexplorerApi()
event_explorer_get_event_statistics = rakam_client.EventExplorerGetEventStatistics() # EventExplorerGetEventStatistics | 

try: 
    # Event statistics
    api_response = api_instance.get_event_statistics(event_explorer_get_event_statistics)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventexplorerApi->get_event_statistics: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_explorer_get_event_statistics** | [**EventExplorerGetEventStatistics**](EventExplorerGetEventStatistics.md)|  | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extra_dimensions**
> dict(str, list[str]) get_extra_dimensions()

Event statistics



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
api_instance = rakam_client.EventexplorerApi()

try: 
    # Event statistics
    api_response = api_instance.get_extra_dimensions()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventexplorerApi->get_extra_dimensions: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, list[str])**](dict.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

