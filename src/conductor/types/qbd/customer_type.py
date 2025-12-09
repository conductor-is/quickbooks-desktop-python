# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerType", "Parent"]


class Parent(BaseModel):
    """The parent customer type one level above this one in the hierarchy.

    For example, if this customer type has a `fullName` of "Industry:Healthcare", its parent has a `fullName` of "Industry". If this customer type is at the top level, this field will be `null`.
    """

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class CustomerType(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this customer type.

    This ID is unique across all customer types but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this customer type was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this customer type, formed
    by combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if a customer type is under "Industry" and has
    the `name` "Healthcare", its `fullName` would be "Industry:Healthcare".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    customer type objects. However, `fullName` can still be arbitrarily changed by
    the QuickBooks user when they modify the underlying `name` field.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this customer type is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """The case-insensitive name of this customer type.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two customer
    types could both have the `name` "Healthcare", but they could have unique
    `fullName` values, such as "Industry:Healthcare" and "Region:Healthcare".
    """

    object_type: Literal["qbd_customer_type"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_customer_type"`."""

    parent: Optional[Parent] = None
    """The parent customer type one level above this one in the hierarchy.

    For example, if this customer type has a `fullName` of "Industry:Healthcare",
    its parent has a `fullName` of "Industry". If this customer type is at the top
    level, this field will be `null`.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this customer type object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sublevel: float
    """The depth level of this customer type in the hierarchy.

    A top-level customer type has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, a customer type with a `fullName` of
    "Industry:Healthcare" would have a `sublevel` of 1.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this customer type was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
