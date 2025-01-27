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


class GetAudienceResponseSuccess(BaseModel):
    # The ID of the audience.
    id: typing.Optional[str] = Field(None, alias='id')

    # The object of the audience.
    object: typing.Optional[str] = Field(None, alias='object')

    # The name of the audience.
    name: typing.Optional[str] = Field(None, alias='name')

    # The date that the object was created.
    created_at: typing.Optional[str] = Field(None, alias='created_at')
    class Config:
        arbitrary_types_allowed = True
