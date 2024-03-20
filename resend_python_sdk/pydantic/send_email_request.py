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

from resend_python_sdk.pydantic.attachment import Attachment
from resend_python_sdk.pydantic.send_email_request_to import SendEmailRequestTo
from resend_python_sdk.pydantic.tag import Tag

class SendEmailRequest(BaseModel):
    # Sender email address. To include a friendly name, use the format \"Your Name <sender@domain.com>\".
    from_: str = Field(alias='from')

    to: SendEmailRequestTo = Field(alias='to')

    # Email subject.
    subject: str = Field(alias='subject')

    tags: typing.Optional[typing.List[Tag]] = Field(None, alias='tags')

    # Bcc recipient email address. For multiple addresses, send as an array of strings.
    bcc: typing.Optional[str] = Field(None, alias='bcc')

    # Cc recipient email address. For multiple addresses, send as an array of strings.
    cc: typing.Optional[str] = Field(None, alias='cc')

    # Reply-to email address. For multiple addresses, send as an array of strings.
    reply_to: typing.Optional[str] = Field(None, alias='reply_to')

    # The HTML version of the message.
    html: typing.Optional[str] = Field(None, alias='html')

    # The plain text version of the message.
    text: typing.Optional[str] = Field(None, alias='text')

    # Custom headers to add to the email.
    headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='headers')

    attachments: typing.Optional[typing.List[Attachment]] = Field(None, alias='attachments')
    class Config:
        arbitrary_types_allowed = True