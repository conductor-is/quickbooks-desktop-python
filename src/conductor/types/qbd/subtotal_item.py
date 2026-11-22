# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubtotalItem", "CustomField"]


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The owner of this custom field: `"0"` for a public custom field, which
    QuickBooks users define and see, or an application's GUID in braces for a
    private custom field, which appears only in requests that name that owner.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    QuickBooks keeps at most 30 characters of a public custom field's value: it
    refuses a longer one on a customer or item, and on a transaction or line it
    stores only the first 30 without an error. A private custom field's limit
    depends on its type.
    """


class SubtotalItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this subtotal item.

    This ID is unique across all subtotal items but not across different QuickBooks
    object types.
    """

    barcode: Optional[str] = None
    """The subtotal item's barcode."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this subtotal item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields that have a value on this subtotal item, for the owners named
    in the request's `customFieldOwnerIds` (by default, the public custom fields).

    **NOTE**: To set or clear custom field values, use the set-custom-fields
    endpoint. An update cannot change them, and its response returns this as an
    empty array even when values exist; retrieve the record to see them.
    """

    description: Optional[str] = None
    """
    The subtotal item's description that will appear on sales forms that include
    this item.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this subtotal item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this subtotal item, unique across all
    subtotal items.

    **NOTE**: Subtotal items do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_subtotal_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_subtotal_item"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this subtotal item object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    special_item_type: Optional[
        Literal["finance_charge", "reimbursable_expense_group", "reimbursable_expense_subtotal"]
    ] = FieldInfo(alias="specialItemType", default=None)
    """The type of special item for this subtotal item."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this subtotal item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
