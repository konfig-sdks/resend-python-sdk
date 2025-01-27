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

from resend_python_sdk.type.list_domains_item import ListDomainsItem

class RequiredListDomainsResponse(TypedDict):
    pass

class OptionalListDomainsResponse(TypedDict, total=False):
    data: typing.List[ListDomainsItem]

class ListDomainsResponse(RequiredListDomainsResponse, OptionalListDomainsResponse):
    pass
