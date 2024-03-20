from resend_python_sdk.paths.domains_domain_id.get import ApiForget
from resend_python_sdk.paths.domains_domain_id.delete import ApiFordelete
from resend_python_sdk.paths.domains_domain_id.patch import ApiForpatch


class DomainsDomainId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
