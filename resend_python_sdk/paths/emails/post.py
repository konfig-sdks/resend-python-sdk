# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.

    The version of the OpenAPI document: 1.1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from resend_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from resend_python_sdk.api_response import AsyncGeneratorResponse
from resend_python_sdk import api_client, exceptions
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

from resend_python_sdk.model.send_email_request import SendEmailRequest as SendEmailRequestSchema
from resend_python_sdk.model.attachment import Attachment as AttachmentSchema
from resend_python_sdk.model.tag import Tag as TagSchema
from resend_python_sdk.model.send_email_response import SendEmailResponse as SendEmailResponseSchema
from resend_python_sdk.model.send_email_request_to import SendEmailRequestTo as SendEmailRequestToSchema

from resend_python_sdk.type.send_email_request_to import SendEmailRequestTo
from resend_python_sdk.type.attachment import Attachment
from resend_python_sdk.type.tag import Tag
from resend_python_sdk.type.send_email_request import SendEmailRequest
from resend_python_sdk.type.send_email_response import SendEmailResponse

from ...api_client import Dictionary
from resend_python_sdk.pydantic.send_email_request_to import SendEmailRequestTo as SendEmailRequestToPydantic
from resend_python_sdk.pydantic.send_email_request import SendEmailRequest as SendEmailRequestPydantic
from resend_python_sdk.pydantic.send_email_response import SendEmailResponse as SendEmailResponsePydantic
from resend_python_sdk.pydantic.tag import Tag as TagPydantic
from resend_python_sdk.pydantic.attachment import Attachment as AttachmentPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SendEmailRequestSchema


request_body_send_email_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = SendEmailResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SendEmailResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SendEmailResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _send_email_mapped_args(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if _from is not None:
            _body["from"] = _from
        if to is not None:
            _body["to"] = to
        if subject is not None:
            _body["subject"] = subject
        if bcc is not None:
            _body["bcc"] = bcc
        if cc is not None:
            _body["cc"] = cc
        if reply_to is not None:
            _body["reply_to"] = reply_to
        if html is not None:
            _body["html"] = html
        if text is not None:
            _body["text"] = text
        if headers is not None:
            _body["headers"] = headers
        if attachments is not None:
            _body["attachments"] = attachments
        args.body = _body
        return args

    async def _asend_email_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Send an email
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/emails',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_send_email_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _send_email_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Send an email
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/emails',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_send_email_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class SendEmailRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asend_email(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_email_mapped_args(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
        )
        return await self._asend_email_oapg(
            body=args.body,
            **kwargs,
        )
    
    def send_email(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_email_mapped_args(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
        )
        return self._send_email_oapg(
            body=args.body,
        )

class SendEmail(BaseApi):

    async def asend_email(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
        validate: bool = False,
        **kwargs,
    ) -> SendEmailResponsePydantic:
        raw_response = await self.raw.asend_email(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
            **kwargs,
        )
        if validate:
            return SendEmailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SendEmailResponsePydantic, raw_response.body)
    
    
    def send_email(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
        validate: bool = False,
    ) -> SendEmailResponsePydantic:
        raw_response = self.raw.send_email(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
        )
        if validate:
            return SendEmailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SendEmailResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_email_mapped_args(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
        )
        return await self._asend_email_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        _from: str,
        to: SendEmailRequestTo,
        subject: str,
        tags: typing.Optional[typing.List[Tag]] = None,
        bcc: typing.Optional[str] = None,
        cc: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        html: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        attachments: typing.Optional[typing.List[Attachment]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_email_mapped_args(
            _from=_from,
            to=to,
            subject=subject,
            tags=tags,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
            html=html,
            text=text,
            headers=headers,
            attachments=attachments,
        )
        return self._send_email_oapg(
            body=args.body,
        )

