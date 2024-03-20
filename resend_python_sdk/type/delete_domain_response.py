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


class RequiredDeleteDomainResponse(TypedDict):
    pass

class OptionalDeleteDomainResponse(TypedDict, total=False):
    # The type of object.
    object: str

    # The ID of the domain.
    id: str

    # Indicates whether the domain was deleted successfully.
    deleted: bool

class DeleteDomainResponse(RequiredDeleteDomainResponse, OptionalDeleteDomainResponse):
    pass
