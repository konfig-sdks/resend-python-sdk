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


class RequiredListContactsResponseSuccessDataItem(TypedDict):
    pass

class OptionalListContactsResponseSuccessDataItem(TypedDict, total=False):
    # Unique identifier for the contact.
    id: str

    # Email address of the contact.
    email: str

    # First name of the contact.
    first_name: str

    # Last name of the contact.
    last_name: str

    # Timestamp indicating when the contact was created.
    created_at: datetime

    # Indicates if the contact is unsubscribed.
    unsubscribed: bool

class ListContactsResponseSuccessDataItem(RequiredListContactsResponseSuccessDataItem, OptionalListContactsResponseSuccessDataItem):
    pass