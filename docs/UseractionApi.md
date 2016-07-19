# rakam_client.UseractionApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch**](UseractionApi.md#batch) | **POST** /user/action/email/batch | Apply batch operation
[**send**](UseractionApi.md#send) | **POST** /user/action/email/single | Perform action for single user


# **batch**
> int batch(user_email_action_batch)

Apply batch operation



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
api_instance = rakam_client.UseractionApi()
user_email_action_batch = rakam_client.UserEmailActionBatch() # UserEmailActionBatch | 

try: 
    # Apply batch operation
    api_response = api_instance.batch(user_email_action_batch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UseractionApi->batch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email_action_batch** | [**UserEmailActionBatch**](UserEmailActionBatch.md)|  | 

### Return type

**int**

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> bool send(user_email_action_send)

Perform action for single user



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
api_instance = rakam_client.UseractionApi()
user_email_action_send = rakam_client.UserEmailActionSend() # UserEmailActionSend | 

try: 
    # Perform action for single user
    api_response = api_instance.send(user_email_action_send)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UseractionApi->send: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email_action_send** | [**UserEmailActionSend**](UserEmailActionSend.md)|  | 

### Return type

**bool**

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

