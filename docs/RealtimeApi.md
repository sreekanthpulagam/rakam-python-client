# rakam_client.RealtimeApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_table**](RealtimeApi.md#create_table) | **POST** /realtime/create | Create report
[**delete_table**](RealtimeApi.md#delete_table) | **POST** /realtime/delete | Delete report
[**list_tables**](RealtimeApi.md#list_tables) | **POST** /realtime/list | List queries
[**query_table**](RealtimeApi.md#query_table) | **POST** /realtime/get | Get report


# **create_table**
> SuccessMessage create_table(real_time_report)

Create report



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
api_instance = rakam_client.RealtimeApi()
real_time_report = rakam_client.RealTimeReport() # RealTimeReport | 

try: 
    # Create report
    api_response = api_instance.create_table(real_time_report)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RealtimeApi->create_table: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **real_time_report** | [**RealTimeReport**](RealTimeReport.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table**
> SuccessMessage delete_table(realtime_delete_table)

Delete report



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
api_instance = rakam_client.RealtimeApi()
realtime_delete_table = rakam_client.RealtimeDeleteTable() # RealtimeDeleteTable | 

try: 
    # Delete report
    api_response = api_instance.delete_table(realtime_delete_table)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RealtimeApi->delete_table: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_delete_table** | [**RealtimeDeleteTable**](RealtimeDeleteTable.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tables**
> list[ContinuousQuery] list_tables()

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
api_instance = rakam_client.RealtimeApi()

try: 
    # List queries
    api_response = api_instance.list_tables()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RealtimeApi->list_tables: %s\n" % e
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

# **query_table**
> RealTimeQueryResult query_table(realtime_query_table)

Get report



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
api_instance = rakam_client.RealtimeApi()
realtime_query_table = rakam_client.RealtimeQueryTable() # RealtimeQueryTable | 

try: 
    # Get report
    api_response = api_instance.query_table(realtime_query_table)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RealtimeApi->query_table: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realtime_query_table** | [**RealtimeQueryTable**](RealtimeQueryTable.md)|  | 

### Return type

[**RealTimeQueryResult**](RealTimeQueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

