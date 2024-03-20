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


class RequiredCreateDomainRequest(TypedDict):
    # The name of the domain you want to create.
    name: str

class OptionalCreateDomainRequest(TypedDict, total=False):
    # The region where emails will be sent from. Possible values are us-east-1' | 'eu-west-1' | 'sa-east-1
    region: str

class CreateDomainRequest(RequiredCreateDomainRequest, OptionalCreateDomainRequest):
    pass
