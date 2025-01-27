# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from resend_python_sdk import schemas  # noqa: F401


class ListContactsResponseSuccessData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Array containing contact information.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ListContactsResponseSuccessDataItem']:
            return ListContactsResponseSuccessDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ListContactsResponseSuccessDataItem'], typing.List['ListContactsResponseSuccessDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ListContactsResponseSuccessData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ListContactsResponseSuccessDataItem':
        return super().__getitem__(i)

from resend_python_sdk.model.list_contacts_response_success_data_item import ListContactsResponseSuccessDataItem
