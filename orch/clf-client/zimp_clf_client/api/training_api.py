# coding: utf-8

"""
    Text Classification Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zimp_clf_client.api_client import ApiClient


class TrainingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clf_train_post(self, **kwargs):  # noqa: E501
        """Trains a model using a csv file with ',' delimiters and the column headers 'text', 'target'  # noqa: E501

        May take several minutes, depending on used model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_train_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The file to upload.
        :param str model_type: Type of model to be trained
        :param int seed: random seed required for reproducibility
        :param bool asynchronous: do not wait for training to complete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_train_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_train_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_train_post_with_http_info(self, **kwargs):  # noqa: E501
        """Trains a model using a csv file with ',' delimiters and the column headers 'text', 'target'  # noqa: E501

        May take several minutes, depending on used model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_train_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The file to upload.
        :param str model_type: Type of model to be trained
        :param int seed: random seed required for reproducibility
        :param bool asynchronous: do not wait for training to complete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'model_type', 'seed', 'asynchronous']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_train_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501
        if 'model_type' in params:
            form_params.append(('modelType', params['model_type']))  # noqa: E501
        if 'seed' in params:
            form_params.append(('seed', params['seed']))  # noqa: E501
        if 'asynchronous' in params:
            form_params.append(('asynchronous', params['asynchronous']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/train', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def clf_training_status_get(self, **kwargs):  # noqa: E501
        """Checks if a trained model is available (and fully trained)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_training_status_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_training_status_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_training_status_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_training_status_get_with_http_info(self, **kwargs):  # noqa: E501
        """Checks if a trained model is available (and fully trained)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_training_status_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_training_status_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/training/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)