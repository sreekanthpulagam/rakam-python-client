# rakam_client.FunnelApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_funnel**](FunnelApi.md#analyze_funnel) | **POST** /funnel/analyze | Execute query


# **analyze_funnel**
> QueryResult analyze_funnel(funnel_query)

Execute query



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
api_instance = rakam_client.FunnelApi()
funnel_query = rakam_client.FunnelQuery() # FunnelQuery | 

try: 
    # Execute query
    api_response = api_instance.analyze_funnel(funnel_query)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FunnelApi->analyze_funnel: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funnel_query** | [**FunnelQuery**](FunnelQuery.md)|  | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

