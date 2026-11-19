# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesRepresentative", "Entity"]


class Entity(BaseModel):
    """
    The sales representative's corresponding person entity in QuickBooks, stored as either an employee, vendor, or other-name entry.
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


class SalesRepresentative(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales representative.

    This ID is unique across all sales representatives but not across different
    QuickBooks object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales representative was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    entity: Entity
    """
    The sales representative's corresponding person entity in QuickBooks, stored as
    either an employee, vendor, or other-name entry.
    """

    initial: str
    """The initials of this sales representative's name."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this sales representative is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    object_type: Literal["qbd_sales_representative"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_representative"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this sales representative
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales representative was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """
