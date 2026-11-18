# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CreditCardCreditRetrieveParams"]


class CreditCardCreditRetrieveParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    custom_field_owner_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="customFieldOwnerIds")]
    """The owners whose custom fields to return on credit card credits.

    Defaults to `["0"]`, the owner of public custom fields, which QuickBooks users
    define and see. To get an application's private custom fields, add its owner ID,
    a GUID in braces. Only the owners you list are returned, so keep `"0"` in the
    list to also get the public ones.
    """
