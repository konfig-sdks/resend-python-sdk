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


class ListAudiencesResponseSuccessData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Array containing audience information.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ListAudiencesResponseSuccessDataItem']:
            return ListAudiencesResponseSuccessDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ListAudiencesResponseSuccessDataItem'], typing.List['ListAudiencesResponseSuccessDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ListAudiencesResponseSuccessData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ListAudiencesResponseSuccessDataItem':
        return super().__getitem__(i)

from resend_python_sdk.model.list_audiences_response_success_data_item import ListAudiencesResponseSuccessDataItem