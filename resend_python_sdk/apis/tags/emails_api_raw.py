# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from resend_python_sdk.paths.emails_email_id.get import GetSingleEmailRaw
from resend_python_sdk.paths.emails.post import SendEmailRaw
from resend_python_sdk.paths.emails_batch.post import TriggerBatchEmailsRaw


class EmailsApiRaw(
    GetSingleEmailRaw,
    SendEmailRaw,
    TriggerBatchEmailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
