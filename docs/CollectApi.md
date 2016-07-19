# rakam_client.CollectApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_events**](CollectApi.md#batch_events) | **POST** /event/batch | Collect multiple events
[**bulk_events**](CollectApi.md#bulk_events) | **POST** /event/bulk | Collect Bulk events
[**bulk_events_remote**](CollectApi.md#bulk_events_remote) | **POST** /event/bulk/remote | Collect bulk events from remote
[**collect_event**](CollectApi.md#collect_event) | **POST** /event/collect | Collect event
[**commit_bulk_events**](CollectApi.md#commit_bulk_events) | **POST** /event/bulk/commit | Commit Bulk events


# **batch_events**
> int batch_events(event_list)

Collect multiple events

Returns 1 if the events are collected.

### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.CollectApi()
event_list = rakam_client.EventList() # EventList | 

try: 
    # Collect multiple events
    api_response = api_instance.batch_events(event_list)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CollectApi->batch_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_list** | [**EventList**](EventList.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_events**
> SuccessMessage bulk_events(event_list)

Collect Bulk events

Bulk API requires master_key as api key and designed to handle large value of data. The endpoint also accepts application/avro and text/csv formats. You need need to set 'collection' and 'master_key' query parameters if the content-type is not application/json.

### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.CollectApi()
event_list = rakam_client.EventList() # EventList | 

try: 
    # Collect Bulk events
    api_response = api_instance.bulk_events(event_list)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CollectApi->bulk_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_list** | [**EventList**](EventList.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_events_remote**
> int bulk_events_remote(bulk_event_remote)

Collect bulk events from remote



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.CollectApi()
bulk_event_remote = rakam_client.BulkEventRemote() # BulkEventRemote | 

try: 
    # Collect bulk events from remote
    api_response = api_instance.bulk_events_remote(bulk_event_remote)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CollectApi->bulk_events_remote: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_event_remote** | [**BulkEventRemote**](BulkEventRemote.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_event**
> int collect_event(event)

Collect event



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.CollectApi()
event = rakam_client.Event() # Event | 

try: 
    # Collect event
    api_response = api_instance.collect_event(event)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CollectApi->collect_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**Event**](Event.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_bulk_events**
> SuccessMessage commit_bulk_events(commit_bulk_events)

Commit Bulk events



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
api_instance = rakam_client.CollectApi()
commit_bulk_events = rakam_client.CommitBulkEvents() # CommitBulkEvents | 

try: 
    # Commit Bulk events
    api_response = api_instance.commit_bulk_events(commit_bulk_events)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CollectApi->commit_bulk_events: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commit_bulk_events** | [**CommitBulkEvents**](CommitBulkEvents.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

