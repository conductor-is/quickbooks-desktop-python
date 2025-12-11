# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaymentMethodCreateParams"]


class PaymentMethodCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this payment method, unique across all
    payment methods.

    **NOTE**: Payment methods do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    payment_method_type: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="paymentMethodType"),
        ]
    ]
    """This payment method's type."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this payment method is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """
