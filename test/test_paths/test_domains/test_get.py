# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import resend_python_sdk
from resend_python_sdk.paths.domains import get
from resend_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDomains(ApiTestMixin, unittest.TestCase):
    """
    Domains unit test stubs
        Retrieve a list of domains
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
