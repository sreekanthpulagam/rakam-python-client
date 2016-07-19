# rakam_client.RecipeApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_recipe**](RecipeApi.md#export_recipe) | **GET** /recipe/export | Export recipe
[**install_recipe**](RecipeApi.md#install_recipe) | **POST** /recipe/install | Install recipe


# **export_recipe**
> Recipe export_recipe(accept)

Export recipe



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
api_instance = rakam_client.RecipeApi()
accept = 'accept_example' # str | 

try: 
    # Export recipe
    api_response = api_instance.export_recipe(accept)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecipeApi->export_recipe: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | 

### Return type

[**Recipe**](Recipe.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_recipe**
> SuccessMessage install_recipe()

Install recipe



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
api_instance = rakam_client.RecipeApi()

try: 
    # Install recipe
    api_response = api_instance.install_recipe()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RecipeApi->install_recipe: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

