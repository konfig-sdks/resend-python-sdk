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


class RequiredRemoveAudienceResponseSuccess(TypedDict):
    pass

class OptionalRemoveAudienceResponseSuccess(TypedDict, total=False):
    # The ID of the audience.
    id: str

    # The object of the audience.
    object: str

    # The deleted attribute indicates that the corresponding audience has been deleted.
    deleted: bool

class RemoveAudienceResponseSuccess(RequiredRemoveAudienceResponseSuccess, OptionalRemoveAudienceResponseSuccess):
    pass
