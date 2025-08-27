# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this template.

    This ID is unique across all templates but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this template was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this template is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """The case-insensitive unique name of this template, unique across all templates.

    **NOTE**: Templates do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_template"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_template"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this template object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    template_type: Literal[
        "bill_payment",
        "build_assembly",
        "credit_memo",
        "estimate",
        "invoice",
        "payment_receipt",
        "purchase_order",
        "sales_order",
        "sales_receipt",
    ] = FieldInfo(alias="templateType")
    """The type of transaction that this template is used for."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this template was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
