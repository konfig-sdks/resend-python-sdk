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

from resend_python_sdk.pydantic.list_contacts_response_success_data_item import ListContactsResponseSuccessDataItem

ListContactsResponseSuccessData = typing.List[ListContactsResponseSuccessDataItem]
