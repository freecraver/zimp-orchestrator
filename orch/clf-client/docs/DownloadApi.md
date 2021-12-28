# zimp_clf_client.DownloadApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clf_download_get**](DownloadApi.md#clf_download_get) | **GET** /clf/download | Retrieves an implementation-specific model dump (e.g. joblib for sklearn)
[**clf_file_predictions_id_get**](DownloadApi.md#clf_file_predictions_id_get) | **GET** /clf/file/predictions/{id} | Retrieve async predictions for given result id


# **clf_download_get**
> clf_download_get()

Retrieves an implementation-specific model dump (e.g. joblib for sklearn)



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DownloadApi()

try:
    # Retrieves an implementation-specific model dump (e.g. joblib for sklearn)
    api_instance.clf_download_get()
except ApiException as e:
    print("Exception when calling DownloadApi->clf_download_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clf_file_predictions_id_get**
> clf_file_predictions_id_get(id)

Retrieve async predictions for given result id



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DownloadApi()
id = NULL # object | result-id retrieved from async file prediction

try:
    # Retrieve async predictions for given result id
    api_instance.clf_file_predictions_id_get(id)
except ApiException as e:
    print("Exception when calling DownloadApi->clf_file_predictions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| result-id retrieved from async file prediction | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

