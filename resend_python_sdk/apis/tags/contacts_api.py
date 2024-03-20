# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from resend_python_sdk.paths.audiences_audience_id_contacts.post import CreateNewContact
from resend_python_sdk.paths.audiences_audience_id_contacts.get import GetList
from resend_python_sdk.paths.audiences_audience_id_contacts_id.get import GetSingle
from resend_python_sdk.paths.audiences_audience_id_contacts_email.delete import RemoveByEmail
from resend_python_sdk.paths.audiences_audience_id_contacts_id.delete import RemoveById
from resend_python_sdk.paths.audiences_audience_id_contacts_id.patch import UpdateSingleContact
from resend_python_sdk.apis.tags.contacts_api_raw import ContactsApiRaw


class ContactsApi(
    CreateNewContact,
    GetList,
    GetSingle,
    RemoveByEmail,
    RemoveById,
    UpdateSingleContact,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContactsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContactsApiRaw(api_client)
