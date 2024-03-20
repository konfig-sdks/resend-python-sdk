<div align="center">

[![Visit Resend](./header.png)](https://resend.com)

# Resend<a id="resend"></a>

Resend is the email platform for developers.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`resend.api_keys.create_new_key`](#resendapi_keyscreate_new_key)
  * [`resend.api_keys.get_list`](#resendapi_keysget_list)
  * [`resend.api_keys.remove_existing_key`](#resendapi_keysremove_existing_key)
  * [`resend.audiences.create_contact_list`](#resendaudiencescreate_contact_list)
  * [`resend.audiences.get_list`](#resendaudiencesget_list)
  * [`resend.audiences.get_single_audience`](#resendaudiencesget_single_audience)
  * [`resend.audiences.remove_existing_audience`](#resendaudiencesremove_existing_audience)
  * [`resend.contacts.create_new_contact`](#resendcontactscreate_new_contact)
  * [`resend.contacts.get_list`](#resendcontactsget_list)
  * [`resend.contacts.get_single`](#resendcontactsget_single)
  * [`resend.contacts.remove_by_email`](#resendcontactsremove_by_email)
  * [`resend.contacts.remove_by_id`](#resendcontactsremove_by_id)
  * [`resend.contacts.update_single_contact`](#resendcontactsupdate_single_contact)
  * [`resend.domains.create_new_domain`](#resenddomainscreate_new_domain)
  * [`resend.domains.get_list`](#resenddomainsget_list)
  * [`resend.domains.get_single_domain`](#resenddomainsget_single_domain)
  * [`resend.domains.remove_domain`](#resenddomainsremove_domain)
  * [`resend.domains.update_existing_domain`](#resenddomainsupdate_existing_domain)
  * [`resend.domains.verify_domain`](#resenddomainsverify_domain)
  * [`resend.emails.get_single_email`](#resendemailsget_single_email)
  * [`resend.emails.send_email`](#resendemailssend_email)
  * [`resend.emails.trigger_batch_emails`](#resendemailstrigger_batch_emails)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Resend&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from resend_python_sdk import Resend, ApiException

resend = Resend(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Create a new API key
    create_new_key_response = resend.api_keys.create_new_key(
        name="string_example",
        permission="full_access",
        domain_id="string_example",
    )
    print(create_new_key_response)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_new_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from resend_python_sdk import Resend, ApiException

resend = Resend(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Create a new API key
        create_new_key_response = await resend.api_keys.acreate_new_key(
            name="string_example",
            permission="full_access",
            domain_id="string_example",
        )
        print(create_new_key_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi.create_new_key: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from resend_python_sdk import Resend, ApiException

resend = Resend(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Create a new API key
    create_new_key_response = resend.api_keys.raw.create_new_key(
        name="string_example",
        permission="full_access",
        domain_id="string_example",
    )
    pprint(create_new_key_response.body)
    pprint(create_new_key_response.body["id"])
    pprint(create_new_key_response.body["token"])
    pprint(create_new_key_response.headers)
    pprint(create_new_key_response.status)
    pprint(create_new_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeysApi.create_new_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `resend.api_keys.create_new_key`<a id="resendapi_keyscreate_new_key"></a>

Create a new API key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_key_response = resend.api_keys.create_new_key(
    name="string_example",
    permission="full_access",
    domain_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The API key name.

##### permission: `str`<a id="permission-str"></a>

The API key can have full access to Resend’s API or be only restricted to send emails. * full_access - Can create, delete, get, and update any resource. * sending_access - Can only send emails.

##### domain_id: `str`<a id="domain_id-str"></a>

Restrict an API key to send emails only from a specific domain. Only used when the permission is sending_acces.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApiKeyRequest`](./resend_python_sdk/type/create_api_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateApiKeyResponse`](./resend_python_sdk/pydantic/create_api_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.api_keys.get_list`<a id="resendapi_keysget_list"></a>

Retrieve a list of API keys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = resend.api_keys.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListApiKeysResponse`](./resend_python_sdk/pydantic/list_api_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.api_keys.remove_existing_key`<a id="resendapi_keysremove_existing_key"></a>

Remove an existing API key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resend.api_keys.remove_existing_key(
    api_key_id="api_key_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key_id: `str`<a id="api_key_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-keys/{api_key_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.audiences.create_contact_list`<a id="resendaudiencescreate_contact_list"></a>

Create a list of contacts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_contact_list_response = resend.audiences.create_contact_list(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the audience you want to create.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAudienceOptions`](./resend_python_sdk/type/create_audience_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateAudienceResponseSuccess`](./resend_python_sdk/pydantic/create_audience_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.audiences.get_list`<a id="resendaudiencesget_list"></a>

Retrieve a list of audiences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = resend.audiences.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListAudiencesResponseSuccess`](./resend_python_sdk/pydantic/list_audiences_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.audiences.get_single_audience`<a id="resendaudiencesget_single_audience"></a>

Retrieve a single audience

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_audience_response = resend.audiences.get_single_audience(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetAudienceResponseSuccess`](./resend_python_sdk/pydantic/get_audience_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.audiences.remove_existing_audience`<a id="resendaudiencesremove_existing_audience"></a>

Remove an existing audience

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_existing_audience_response = resend.audiences.remove_existing_audience(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RemoveAudienceResponseSuccess`](./resend_python_sdk/pydantic/remove_audience_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.create_new_contact`<a id="resendcontactscreate_new_contact"></a>

Create a new contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_contact_response = resend.contacts.create_new_contact(
    email="steve.wozniak@gmail.com",
    audience_id="audience_id_example",
    first_name="Steve",
    last_name="Wozniak",
    unsubscribed=False,
    audience_id="78261eea-8f8b-4381-83c6-79fa7120f1cf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

##### requestBody: [`CreateContactOptions`](./resend_python_sdk/type/create_contact_options.py)<a id="requestbody-createcontactoptionsresend_python_sdktypecreate_contact_optionspy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CreateContactResponseSuccess`](./resend_python_sdk/pydantic/create_contact_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.get_list`<a id="resendcontactsget_list"></a>

Retrieve a list of contacts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = resend.contacts.get_list(
    audience_id="audience_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ListContactsResponseSuccess`](./resend_python_sdk/pydantic/list_contacts_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.get_single`<a id="resendcontactsget_single"></a>

Retrieve a single contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = resend.contacts.get_single(
    id="id_example",
    audience_id="audience_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetContactResponseSuccess`](./resend_python_sdk/pydantic/get_contact_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.remove_by_email`<a id="resendcontactsremove_by_email"></a>

Remove an existing contact by email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_by_email_response = resend.contacts.remove_by_email(
    email="email_example",
    audience_id="audience_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RemoveContactResponseSuccess`](./resend_python_sdk/pydantic/remove_contact_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts/{email}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.remove_by_id`<a id="resendcontactsremove_by_id"></a>

Remove an existing contact by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_by_id_response = resend.contacts.remove_by_id(
    id="id_example",
    audience_id="audience_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RemoveContactResponseSuccess`](./resend_python_sdk/pydantic/remove_contact_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.contacts.update_single_contact`<a id="resendcontactsupdate_single_contact"></a>

Update a single contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_single_contact_response = resend.contacts.update_single_contact(
    id="id_example",
    audience_id="audience_id_example",
    email="steve.wozniak@gmail.com",
    first_name="Steve",
    last_name="Wozniak",
    unsubscribed=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### audience_id: `str`<a id="audience_id-str"></a>

##### email: `str`<a id="email-str"></a>

Email address of the contact.

##### first_name: `str`<a id="first_name-str"></a>

First name of the contact.

##### last_name: `str`<a id="last_name-str"></a>

Last name of the contact.

##### unsubscribed: `bool`<a id="unsubscribed-bool"></a>

Indicates the subscription status of the contact.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateContactOptions`](./resend_python_sdk/type/update_contact_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UpdateContactResponseSuccess`](./resend_python_sdk/pydantic/update_contact_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/audiences/{audience_id}/contacts/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.create_new_domain`<a id="resenddomainscreate_new_domain"></a>

Create a new domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_domain_response = resend.domains.create_new_domain(
    name="string_example",
    region="us-east-1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the domain you want to create.

##### region: `str`<a id="region-str"></a>

The region where emails will be sent from. Possible values are us-east-1' | 'eu-west-1' | 'sa-east-1

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDomainRequest`](./resend_python_sdk/type/create_domain_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateDomainResponse`](./resend_python_sdk/pydantic/create_domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.get_list`<a id="resenddomainsget_list"></a>

Retrieve a list of domains

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = resend.domains.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListDomainsResponse`](./resend_python_sdk/pydantic/list_domains_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.get_single_domain`<a id="resenddomainsget_single_domain"></a>

Retrieve a single domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_domain_response = resend.domains.get_single_domain(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Domain`](./resend_python_sdk/pydantic/domain.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.remove_domain`<a id="resenddomainsremove_domain"></a>

Remove an existing domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_domain_response = resend.domains.remove_domain(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteDomainResponse`](./resend_python_sdk/pydantic/delete_domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.update_existing_domain`<a id="resenddomainsupdate_existing_domain"></a>

Update an existing domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_domain_response = resend.domains.update_existing_domain(
    domain_id="domain_id_example",
    click_tracking=True,
    open_tracking=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

##### click_tracking: `bool`<a id="click_tracking-bool"></a>

Enable or disable click tracking for the domain.

##### open_tracking: `bool`<a id="open_tracking-bool"></a>

Enable or disable open tracking for the domain.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateDomainOptions`](./resend_python_sdk/type/update_domain_options.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UpdateDomainResponseSuccess`](./resend_python_sdk/pydantic/update_domain_response_success.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.domains.verify_domain`<a id="resenddomainsverify_domain"></a>

Verify an existing domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_domain_response = resend.domains.verify_domain(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VerifyDomainResponse`](./resend_python_sdk/pydantic/verify_domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.emails.get_single_email`<a id="resendemailsget_single_email"></a>

Retrieve a single email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_email_response = resend.emails.get_single_email(
    email_id="email_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_id: `str`<a id="email_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Email`](./resend_python_sdk/pydantic/email.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/emails/{email_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.emails.send_email`<a id="resendemailssend_email"></a>

Send an email

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_email_response = resend.emails.send_email(
    _from="string_example",
    to=[
        "string_example"
    ],
    subject="string_example",
    tags=[
        {
        }
    ],
    bcc="string_example",
    cc="string_example",
    reply_to="string_example",
    html="string_example",
    text="string_example",
    headers={},
    attachments=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

Sender email address. To include a friendly name, use the format \\\"Your Name <sender@domain.com>\\\".

##### to: [`SendEmailRequestTo`](./resend_python_sdk/type/send_email_request_to.py)<a id="to-sendemailrequesttoresend_python_sdktypesend_email_request_topy"></a>

##### subject: `str`<a id="subject-str"></a>

Email subject.

##### tags: List[`Tag`]<a id="tags-listtag"></a>

##### bcc: `str`<a id="bcc-str"></a>

Bcc recipient email address. For multiple addresses, send as an array of strings.

##### cc: `str`<a id="cc-str"></a>

Cc recipient email address. For multiple addresses, send as an array of strings.

##### reply_to: `str`<a id="reply_to-str"></a>

Reply-to email address. For multiple addresses, send as an array of strings.

##### html: `str`<a id="html-str"></a>

The HTML version of the message.

##### text: `str`<a id="text-str"></a>

The plain text version of the message.

##### headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Custom headers to add to the email.

##### attachments: List[`Attachment`]<a id="attachments-listattachment"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SendEmailRequest`](./resend_python_sdk/type/send_email_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SendEmailResponse`](./resend_python_sdk/pydantic/send_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/emails` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `resend.emails.trigger_batch_emails`<a id="resendemailstrigger_batch_emails"></a>

Trigger up to 100 batch emails at once.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_batch_emails_response = resend.emails.trigger_batch_emails(
    body=[
        {
            "_from": "_from_example",
            "to": [
                "to_example"
            ],
            "subject": "subject_example",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailsTriggerBatchEmailsRequest`](./resend_python_sdk/type/emails_trigger_batch_emails_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateBatchEmailsResponse`](./resend_python_sdk/pydantic/create_batch_emails_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/emails/batch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
