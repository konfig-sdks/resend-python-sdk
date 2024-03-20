import typing_extensions

from resend_python_sdk.apis.tags import TagValues
from resend_python_sdk.apis.tags.domains_api import DomainsApi
from resend_python_sdk.apis.tags.contacts_api import ContactsApi
from resend_python_sdk.apis.tags.audiences_api import AudiencesApi
from resend_python_sdk.apis.tags.emails_api import EmailsApi
from resend_python_sdk.apis.tags.api_keys_api import APIKeysApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOMAINS: DomainsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.AUDIENCES: AudiencesApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.API_KEYS: APIKeysApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOMAINS: DomainsApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.AUDIENCES: AudiencesApi,
        TagValues.EMAILS: EmailsApi,
        TagValues.API_KEYS: APIKeysApi,
    }
)
