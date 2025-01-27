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


class Attachment(BaseModel):
    # Content of an attached file.
    content: typing.Optional[typing.IO] = Field(None, alias='content')

    # Name of attached file.
    filename: typing.Optional[str] = Field(None, alias='filename')

    # Path where the attachment file is hosted
    path: typing.Optional[str] = Field(None, alias='path')
    class Config:
        arbitrary_types_allowed = True
