# zimp_clf_client.PredictionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clf_file_predict_proba_post**](PredictionApi.md#clf_file_predict_proba_post) | **POST** /clf/file/predict_proba | Creates predictions for texts in supplied csv file with &#39;,&#39; delimiters and the column header &#39;text&#39;
[**clf_m_predict_proba_post**](PredictionApi.md#clf_m_predict_proba_post) | **POST** /clf/m/predict_proba | Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call
[**clf_predict_post**](PredictionApi.md#clf_predict_post) | **POST** /clf/predict | Predict the class label of one input text. Requires a previous train-call
[**clf_predict_proba_post**](PredictionApi.md#clf_predict_proba_post) | **POST** /clf/predict_proba | Predict probabilities for top n class labels. Requires a previous train-call


# **clf_file_predict_proba_post**
> object clf_file_predict_proba_post(file=file)

Creates predictions for texts in supplied csv file with ',' delimiters and the column header 'text'

Predictions are created async in can be fetched via GET /file/predictions/<id>

### Example
```python
from __future__ import print_function
import time
import zimp_clf_client
from zimp_clf_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zimp_clf_client.PredictionApi()
file = '/path/to/file.txt' # file | The file to upload. (optional)

try:
    # Creates predictions for texts in supplied csv file with ',' delimiters and the column header 'text'
    api_response = api_instance.clf_file_predict_proba_post(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionApi->clf_file_predict_proba_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to upload. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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
api_instance = zimp_clf_client.PredictionApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call
    api_response = api_instance.clf_m_predict_proba_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionApi->clf_m_predict_proba_post: %s\n" % e)
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
api_instance = zimp_clf_client.PredictionApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict the class label of one input text. Requires a previous train-call
    api_response = api_instance.clf_predict_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionApi->clf_predict_post: %s\n" % e)
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
api_instance = zimp_clf_client.PredictionApi()
body = zimp_clf_client.Body() # Body |  (optional)

try:
    # Predict probabilities for top n class labels. Requires a previous train-call
    api_response = api_instance.clf_predict_proba_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionApi->clf_predict_proba_post: %s\n" % e)
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

