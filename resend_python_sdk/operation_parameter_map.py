operation_parameter_map = {
    '/api-keys-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'domain_id'
            },
        ]
    },
    '/api-keys-GET': {
        'parameters': [
        ]
    },
    '/api-keys/{api_key_id}-DELETE': {
        'parameters': [
            {
                'name': 'api_key_id'
            },
        ]
    },
    '/audiences-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/audiences-GET': {
        'parameters': [
        ]
    },
    '/audiences/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/audiences/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'audience_id'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'unsubscribed'
            },
            {
                'name': 'audience_id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts-GET': {
        'parameters': [
            {
                'name': 'audience_id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'audience_id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts/{email}-DELETE': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'audience_id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'audience_id'
            },
        ]
    },
    '/audiences/{audience_id}/contacts/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'audience_id'
            },
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'unsubscribed'
            },
        ]
    },
    '/domains-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'region'
            },
        ]
    },
    '/domains-GET': {
        'parameters': [
        ]
    },
    '/domains/{domain_id}-GET': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/domains/{domain_id}-DELETE': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/domains/{domain_id}-PATCH': {
        'parameters': [
            {
                'name': 'domain_id'
            },
            {
                'name': 'click_tracking'
            },
            {
                'name': 'open_tracking'
            },
        ]
    },
    '/domains/{domain_id}/verify-POST': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/emails/{email_id}-GET': {
        'parameters': [
            {
                'name': 'email_id'
            },
        ]
    },
    '/emails-POST': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'reply_to'
            },
            {
                'name': 'html'
            },
            {
                'name': 'text'
            },
            {
                'name': 'headers'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/emails/batch-POST': {
        'parameters': [
        ]
    },
};