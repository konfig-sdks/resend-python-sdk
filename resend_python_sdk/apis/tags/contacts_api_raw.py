# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from resend_python_sdk.paths.audiences_audience_id_contacts.post import CreateNewContactRaw
from resend_python_sdk.paths.audiences_audience_id_contacts.get import GetListRaw
from resend_python_sdk.paths.audiences_audience_id_contacts_id.get import GetSingleRaw
from resend_python_sdk.paths.audiences_audience_id_contacts_email.delete import RemoveByEmailRaw
from resend_python_sdk.paths.audiences_audience_id_contacts_id.delete import RemoveByIdRaw
from resend_python_sdk.paths.audiences_audience_id_contacts_id.patch import UpdateSingleContactRaw


class ContactsApiRaw(
    CreateNewContactRaw,
    GetListRaw,
    GetSingleRaw,
    RemoveByEmailRaw,
    RemoveByIdRaw,
    UpdateSingleContactRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass