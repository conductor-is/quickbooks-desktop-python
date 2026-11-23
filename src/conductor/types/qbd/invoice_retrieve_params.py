# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["InvoiceRetrieveParams"]


class InvoiceRetrieveParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    custom_field_owner_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="customFieldOwnerIds")]
    """The owners whose custom fields to return on invoices.

    Defaults to `["0"]`, the public custom fields people create and see in
    QuickBooks. For an application's private custom fields, list its owner ID, a
    GUID in braces. Only listed owners are returned, so keep `"0"` for the public
    ones. QuickBooks rejects the whole request if a listed private owner has no
    custom fields for invoices.
    """
