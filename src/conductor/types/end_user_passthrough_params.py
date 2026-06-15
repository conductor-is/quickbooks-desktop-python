# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["EndUserPassthroughParams"]


class EndUserPassthroughParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the end-user who owns the integration connection."""

    qbd_payload: Required[Dict[str, object]]
    """The raw qbXML request object to send to the integration connection.

    For QuickBooks Desktop, use a qbXML request wrapper such as `InvoiceQueryRq` or
    `CustomerQueryRq`. This body is forwarded directly and does not use Conductor
    field names.
    """
