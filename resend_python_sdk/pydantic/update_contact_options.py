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
from pydantic import BaseModel, Field, RootModel


class UpdateContactOptions(BaseModel):
    # Email address of the contact.
    email: typing.Optional[str] = Field(None, alias='email')

    # First name of the contact.
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # Last name of the contact.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # Indicates the subscription status of the contact.
    unsubscribed: typing.Optional[bool] = Field(None, alias='unsubscribed')
    class Config:
        arbitrary_types_allowed = True