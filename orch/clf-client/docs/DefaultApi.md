# zimp_clf_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clf_download_get**](DefaultApi.md#clf_download_get) | **GET** /clf/download | Retrieves an implementation-specific model dump (e.g. joblib for sklearn)
[**clf_m_predict_proba_post**](DefaultApi.md#clf_m_predict_proba_post) | **POST** /clf/m/predict_proba | Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call
[**clf_predict_post**](DefaultApi.md#clf_predict_post) | **POST** /clf/predict | Predict the class label of one input text. Requires a previous train-call
[**clf_predict_proba_post**](DefaultApi.md#clf_predict_proba_post) | **POST** /clf/predict_proba | Predict probabilities for top n class labels. Requires a previous train-call
[**clf_train_post**](DefaultApi.md#clf_train_post) | **POST** /clf/train | Trains a model using a csv file with &#39;,&#39; delimiters and the column headers &#39;text&#39;, &#39;target&#39;
[**clf_training_status_get**](DefaultApi.md#clf_training_status_get) | **GET** /clf/training/status | Checks if a trained model is available (and fully trained)


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
api_instance = zimp_clf_client.DefaultApi()

try:
    # Retrieves an implementation-specific model dump (e.g. joblib for sklearn)
    api_instance.clf_download_get()
except ApiException as e:
    print("Exception when calling DefaultApi->clf_download_get: %s\n" % e)
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

# **clf_m_predict_proba_post**
> object clf_m_predict_proba_post(body=body)

Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DefaultApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call
    api_response = api_instance.clf_m_predict_proba_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clf_m_predict_proba_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clf_predict_post**
> object clf_predict_post(body=body)

Predict the class label of one input text. Requires a previous train-call



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DefaultApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict the class label of one input text. Requires a previous train-call
    api_response = api_instance.clf_predict_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clf_predict_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clf_predict_proba_post**
> object clf_predict_proba_post(body=body)

Predict probabilities for top n class labels. Requires a previous train-call



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DefaultApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict probabilities for top n class labels. Requires a previous train-call
    api_response = api_instance.clf_predict_proba_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clf_predict_proba_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clf_train_post**
> clf_train_post(file=file, model_type=model_type, seed=seed, asynchronous=asynchronous)

Trains a model using a csv file with ',' delimiters and the column headers 'text', 'target'

May take several minutes, depending on used model

### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DefaultApi()
file = '/path/to/file.txt' # file | The file to upload. (optional)
model_type = 'model_type_example' # str | Type of model to be trained (optional)
seed = 56 # int | random seed required for reproducibility (optional)
asynchronous = True # bool | do not wait for training to complete (optional)

try:
    # Trains a model using a csv file with ',' delimiters and the column headers 'text', 'target'
    api_instance.clf_train_post(file=file, model_type=model_type, seed=seed, asynchronous=asynchronous)
except ApiException as e:
    print("Exception when calling DefaultApi->clf_train_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to upload. | [optional] 
 **model_type** | **str**| Type of model to be trained | [optional] 
 **seed** | **int**| random seed required for reproducibility | [optional] 
 **asynchronous** | **bool**| do not wait for training to complete | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clf_training_status_get**
> object clf_training_status_get()

Checks if a trained model is available (and fully trained)



### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.DefaultApi()

try:
    # Checks if a trained model is available (and fully trained)
    api_response = api_instance.clf_training_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clf_training_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

