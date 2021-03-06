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


class PredictionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clf_file_predict_proba_post(self, **kwargs):  # noqa: E501
        """Creates predictions for texts in supplied csv file with ',' delimiters and the column header 'text'  # noqa: E501

        Predictions are created async in can be fetched via GET /file/predictions/<id>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_file_predict_proba_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The file to upload.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_file_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_file_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_file_predict_proba_post_with_http_info(self, **kwargs):  # noqa: E501
        """Creates predictions for texts in supplied csv file with ',' delimiters and the column header 'text'  # noqa: E501

        Predictions are created async in can be fetched via GET /file/predictions/<id>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_file_predict_proba_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: The file to upload.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_file_predict_proba_post" % key
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

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/file/predict_proba', 'POST',
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

    def clf_m_predict_proba_post(self, **kwargs):  # noqa: E501
        """Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_m_predict_proba_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_m_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_m_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_m_predict_proba_post_with_http_info(self, **kwargs):  # noqa: E501
        """Predict probabilities for top n class labels for all supplied texts. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_m_predict_proba_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_m_predict_proba_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/m/predict_proba', 'POST',
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

    def clf_predict_post(self, **kwargs):  # noqa: E501
        """Predict the class label of one input text. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_predict_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_predict_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_predict_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_predict_post_with_http_info(self, **kwargs):  # noqa: E501
        """Predict the class label of one input text. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_predict_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_predict_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/predict', 'POST',
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

    def clf_predict_proba_post(self, **kwargs):  # noqa: E501
        """Predict probabilities for top n class labels. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_predict_proba_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clf_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clf_predict_proba_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def clf_predict_proba_post_with_http_info(self, **kwargs):  # noqa: E501
        """Predict probabilities for top n class labels. Requires a previous train-call  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clf_predict_proba_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clf_predict_proba_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/clf/predict_proba', 'POST',
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
