# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from resend_python_sdk.paths.audiences.post import CreateContactList
from resend_python_sdk.paths.audiences.get import GetList
from resend_python_sdk.paths.audiences_id.get import GetSingleAudience
from resend_python_sdk.paths.audiences_id.delete import RemoveExistingAudience
from resend_python_sdk.apis.tags.audiences_api_raw import AudiencesApiRaw


class AudiencesApi(
    CreateContactList,
    GetList,
    GetSingleAudience,
    RemoveExistingAudience,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AudiencesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AudiencesApiRaw(api_client)
