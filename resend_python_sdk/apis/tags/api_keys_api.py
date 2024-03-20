# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from resend_python_sdk.paths.api_keys.post import CreateNewKey
from resend_python_sdk.paths.api_keys.get import GetList
from resend_python_sdk.paths.api_keys_api_key_id.delete import RemoveExistingKey
from resend_python_sdk.apis.tags.api_keys_api_raw import APIKeysApiRaw


class APIKeysApi(
    CreateNewKey,
    GetList,
    RemoveExistingKey,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: APIKeysApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = APIKeysApiRaw(api_client)