# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredSendEmailResponse(TypedDict):
    pass

class OptionalSendEmailResponse(TypedDict, total=False):
    # The ID of the sent email.
    id: str

class SendEmailResponse(RequiredSendEmailResponse, OptionalSendEmailResponse):
    pass
