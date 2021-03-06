# coding: utf-8

"""
    Text Classification Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import zimp_clf_client
from zimp_clf_client.api.download_api import DownloadApi  # noqa: E501
from zimp_clf_client.rest import ApiException


class TestDownloadApi(unittest.TestCase):
    """DownloadApi unit test stubs"""

    def setUp(self):
        self.api = zimp_clf_client.api.download_api.DownloadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clf_download_get(self):
        """Test case for clf_download_get

        Retrieves an implementation-specific model dump (e.g. joblib for sklearn)  # noqa: E501
        """
        pass

    def test_clf_file_predictions_id_get(self):
        """Test case for clf_file_predictions_id_get

        Retrieve async predictions for given result id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
