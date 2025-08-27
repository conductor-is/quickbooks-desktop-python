# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StandardTerm"]


class StandardTerm(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this standard term.

    This ID is unique across all standard terms but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this standard term was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    discount_days: Optional[float] = FieldInfo(alias="discountDays", default=None)
    """
    The number of days within which payment must be received to qualify for the
    discount specified by `discountPercentage`.
    """

    discount_percentage: Optional[str] = FieldInfo(alias="discountPercentage", default=None)
    """
    The discount percentage applied to the payment if received within the number of
    days specified by `discountDays`. The value is between 0 and 100.
    """

    due_days: Optional[float] = FieldInfo(alias="dueDays", default=None)
    """The number of days until payment is due."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this standard term is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this standard term, unique across all
    standard terms.

    **NOTE**: Standard terms do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_standard_term"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_standard_term"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this standard term object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this standard term was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
