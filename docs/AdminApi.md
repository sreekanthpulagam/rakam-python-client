# rakam_client.AdminApi

All URIs are relative to *https://app.rakam.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_fields_to_schema**](AdminApi.md#add_custom_fields_to_schema) | **POST** /project/schema/add/custom | Add fields to collections by transforming other schemas
[**add_fields_to_schema**](AdminApi.md#add_fields_to_schema) | **POST** /project/schema/add | Add fields to collections
[**check_api_keys**](AdminApi.md#check_api_keys) | **POST** /project/check-api-keys | Create API Keys
[**check_lock_key**](AdminApi.md#check_lock_key) | **POST** /admin/lock_key | Check lock key
[**collections**](AdminApi.md#collections) | **POST** /project/collection | Get collection names
[**create_api_keys**](AdminApi.md#create_api_keys) | **POST** /project/create-api-keys | Create API Keys
[**create_project**](AdminApi.md#create_project) | **POST** /project/create | Create project
[**delete_project**](AdminApi.md#delete_project) | **DELETE** /project/delete | Delete project
[**get_configurations**](AdminApi.md#get_configurations) | **GET** /admin/configurations | List installed modules
[**get_projects**](AdminApi.md#get_projects) | **GET** /project/list | List created projects
[**get_stats**](AdminApi.md#get_stats) | **POST** /project/stats | Get project stats
[**get_types**](AdminApi.md#get_types) | **GET** /admin/types | Get types
[**revoke_api_keys**](AdminApi.md#revoke_api_keys) | **DELETE** /project/revoke-api-keys | Revoke API Keys
[**schema**](AdminApi.md#schema) | **POST** /project/schema | Get collection schema


# **add_custom_fields_to_schema**
> list[SchemaField] add_custom_fields_to_schema(project_add_custom_fields_to_schema)

Add fields to collections by transforming other schemas



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
api_instance = rakam_client.AdminApi()
project_add_custom_fields_to_schema = rakam_client.ProjectAddCustomFieldsToSchema() # ProjectAddCustomFieldsToSchema | 

try: 
    # Add fields to collections by transforming other schemas
    api_response = api_instance.add_custom_fields_to_schema(project_add_custom_fields_to_schema)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->add_custom_fields_to_schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_add_custom_fields_to_schema** | [**ProjectAddCustomFieldsToSchema**](ProjectAddCustomFieldsToSchema.md)|  | 

### Return type

[**list[SchemaField]**](SchemaField.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fields_to_schema**
> list[SchemaField] add_fields_to_schema(project_add_fields_to_schema)

Add fields to collections



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
api_instance = rakam_client.AdminApi()
project_add_fields_to_schema = rakam_client.ProjectAddFieldsToSchema() # ProjectAddFieldsToSchema | 

try: 
    # Add fields to collections
    api_response = api_instance.add_fields_to_schema(project_add_fields_to_schema)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->add_fields_to_schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_add_fields_to_schema** | [**ProjectAddFieldsToSchema**](ProjectAddFieldsToSchema.md)|  | 

### Return type

[**list[SchemaField]**](SchemaField.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_api_keys**
> list[bool] check_api_keys(project_check_api_keys)

Create API Keys



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.AdminApi()
project_check_api_keys = rakam_client.ProjectCheckApiKeys() # ProjectCheckApiKeys | 

try: 
    # Create API Keys
    api_response = api_instance.check_api_keys(project_check_api_keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->check_api_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_check_api_keys** | [**ProjectCheckApiKeys**](ProjectCheckApiKeys.md)|  | 

### Return type

**list[bool]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_lock_key**
> bool check_lock_key(check_lock_key)

Check lock key



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
api_instance = rakam_client.AdminApi()
check_lock_key = rakam_client.CheckLockKey() # CheckLockKey | 

try: 
    # Check lock key
    api_response = api_instance.check_lock_key(check_lock_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->check_lock_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_lock_key** | [**CheckLockKey**](CheckLockKey.md)|  | 

### Return type

**bool**

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections**
> list[str] collections()

Get collection names



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
api_instance = rakam_client.AdminApi()

try: 
    # Get collection names
    api_response = api_instance.collections()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->collections: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_keys**
> ProjectApiKeys create_api_keys()

Create API Keys



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
api_instance = rakam_client.AdminApi()

try: 
    # Create API Keys
    api_response = api_instance.create_api_keys()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->create_api_keys: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectApiKeys**](ProjectApiKeys.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectApiKeys create_project(create_project)

Create project



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.AdminApi()
create_project = rakam_client.CreateProject() # CreateProject | 

try: 
    # Create project
    api_response = api_instance.create_project(create_project)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->create_project: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project** | [**CreateProject**](CreateProject.md)|  | 

### Return type

[**ProjectApiKeys**](ProjectApiKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> SuccessMessage delete_project()

Delete project



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
api_instance = rakam_client.AdminApi()

try: 
    # Delete project
    api_response = api_instance.delete_project()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->delete_project: %s\n" % e
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

# **get_configurations**
> list[ModuleDescriptor] get_configurations()

List installed modules



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
api_instance = rakam_client.AdminApi()

try: 
    # List installed modules
    api_response = api_instance.get_configurations()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->get_configurations: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ModuleDescriptor]**](ModuleDescriptor.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[str] get_projects()

List created projects



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
api_instance = rakam_client.AdminApi()

try: 
    # List created projects
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->get_projects: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> dict(str, Stats) get_stats(project_get_stats)

Get project stats



### Example 
```python
import time
import rakam_client
from rakam_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rakam_client.AdminApi()
project_get_stats = rakam_client.ProjectGetStats() # ProjectGetStats | 

try: 
    # Get project stats
    api_response = api_instance.get_stats(project_get_stats)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->get_stats: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_get_stats** | [**ProjectGetStats**](ProjectGetStats.md)|  | 

### Return type

[**dict(str, Stats)**](Stats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> dict(str, str) get_types()

Get types



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
api_instance = rakam_client.AdminApi()

try: 
    # Get types
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->get_types: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, str)**](dict.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_keys**
> SuccessMessage revoke_api_keys(master_key)

Revoke API Keys



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
api_instance = rakam_client.AdminApi()
master_key = 'master_key_example' # str | 

try: 
    # Revoke API Keys
    api_response = api_instance.revoke_api_keys(master_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->revoke_api_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_key** | **str**|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[master_key](../README.md#master_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema**
> list[Collection] schema(project_schema)

Get collection schema



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
api_instance = rakam_client.AdminApi()
project_schema = rakam_client.ProjectSchema() # ProjectSchema | 

try: 
    # Get collection schema
    api_response = api_instance.schema(project_schema)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdminApi->schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_schema** | [**ProjectSchema**](ProjectSchema.md)|  | 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

[read_key](../README.md#read_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

