# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from resend_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EMAILS = "/emails"
    EMAILS_EMAIL_ID = "/emails/{email_id}"
    EMAILS_BATCH = "/emails/batch"
    DOMAINS = "/domains"
    DOMAINS_DOMAIN_ID = "/domains/{domain_id}"
    DOMAINS_DOMAIN_ID_VERIFY = "/domains/{domain_id}/verify"
    APIKEYS = "/api-keys"
    APIKEYS_API_KEY_ID = "/api-keys/{api_key_id}"
    AUDIENCES = "/audiences"
    AUDIENCES_ID = "/audiences/{id}"
    AUDIENCES_AUDIENCE_ID_CONTACTS = "/audiences/{audience_id}/contacts"
    AUDIENCES_AUDIENCE_ID_CONTACTS_EMAIL = "/audiences/{audience_id}/contacts/{email}"
    AUDIENCES_AUDIENCE_ID_CONTACTS_ID = "/audiences/{audience_id}/contacts/{id}"
