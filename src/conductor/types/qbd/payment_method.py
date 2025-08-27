# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaymentMethod"]


class PaymentMethod(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this payment method.

    This ID is unique across all payment methods but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this payment method was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this payment method is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this payment method, unique across all
    payment methods.

    **NOTE**: Payment methods do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_payment_method"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_payment_method"`."""

    payment_method_type: Literal[
        "american_express",
        "cash",
        "check",
        "debit_card",
        "discover",
        "e_check",
        "gift_card",
        "master_card",
        "other",
        "other_credit_card",
        "visa",
    ] = FieldInfo(alias="paymentMethodType")
    """This payment method's type."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this payment method object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this payment method was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
