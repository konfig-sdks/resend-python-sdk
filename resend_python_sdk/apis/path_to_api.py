import typing_extensions

from resend_python_sdk.paths import PathValues
from resend_python_sdk.apis.paths.emails import Emails
from resend_python_sdk.apis.paths.emails_email_id import EmailsEmailId
from resend_python_sdk.apis.paths.emails_batch import EmailsBatch
from resend_python_sdk.apis.paths.domains import Domains
from resend_python_sdk.apis.paths.domains_domain_id import DomainsDomainId
from resend_python_sdk.apis.paths.domains_domain_id_verify import DomainsDomainIdVerify
from resend_python_sdk.apis.paths.api_keys import ApiKeys
from resend_python_sdk.apis.paths.api_keys_api_key_id import ApiKeysApiKeyId
from resend_python_sdk.apis.paths.audiences import Audiences
from resend_python_sdk.apis.paths.audiences_id import AudiencesId
from resend_python_sdk.apis.paths.audiences_audience_id_contacts import AudiencesAudienceIdContacts
from resend_python_sdk.apis.paths.audiences_audience_id_contacts_email import AudiencesAudienceIdContactsEmail
from resend_python_sdk.apis.paths.audiences_audience_id_contacts_id import AudiencesAudienceIdContactsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_EMAIL_ID: EmailsEmailId,
        PathValues.EMAILS_BATCH: EmailsBatch,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DOMAIN_ID: DomainsDomainId,
        PathValues.DOMAINS_DOMAIN_ID_VERIFY: DomainsDomainIdVerify,
        PathValues.APIKEYS: ApiKeys,
        PathValues.APIKEYS_API_KEY_ID: ApiKeysApiKeyId,
        PathValues.AUDIENCES: Audiences,
        PathValues.AUDIENCES_ID: AudiencesId,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS: AudiencesAudienceIdContacts,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS_EMAIL: AudiencesAudienceIdContactsEmail,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS_ID: AudiencesAudienceIdContactsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EMAILS: Emails,
        PathValues.EMAILS_EMAIL_ID: EmailsEmailId,
        PathValues.EMAILS_BATCH: EmailsBatch,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DOMAIN_ID: DomainsDomainId,
        PathValues.DOMAINS_DOMAIN_ID_VERIFY: DomainsDomainIdVerify,
        PathValues.APIKEYS: ApiKeys,
        PathValues.APIKEYS_API_KEY_ID: ApiKeysApiKeyId,
        PathValues.AUDIENCES: Audiences,
        PathValues.AUDIENCES_ID: AudiencesId,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS: AudiencesAudienceIdContacts,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS_EMAIL: AudiencesAudienceIdContactsEmail,
        PathValues.AUDIENCES_AUDIENCE_ID_CONTACTS_ID: AudiencesAudienceIdContactsId,
    }
)
