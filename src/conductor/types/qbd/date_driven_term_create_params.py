# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DateDrivenTermCreateParams"]


class DateDrivenTermCreateParams(TypedDict, total=False):
    due_day_of_month: Required[Annotated[float, PropertyInfo(alias="dueDayOfMonth")]]
    """The day of the month when full payment is due without discount."""

    name: Required[str]
    """
    The case-insensitive unique name of this date-driven term, unique across all
    date-driven terms.

    **NOTE**: Date-driven terms do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    discount_day_of_month: Annotated[float, PropertyInfo(alias="discountDayOfMonth")]
    """
    The day of the month within which payment must be received to qualify for the
    discount specified by `discountPercentage`.
    """

    discount_percentage: Annotated[str, PropertyInfo(alias="discountPercentage")]
    """
    The discount percentage applied to the payment if received on or before the
    specified `discountDayOfMonth`. The value is between 0 and 100.
    """

    grace_period_days: Annotated[float, PropertyInfo(alias="gracePeriodDays")]
    """
    The number of days before `dueDayOfMonth` when an invoice or bill issued within
    this threshold is considered due the following month. For example, with
    `dueDayOfMonth` set to 15 and `gracePeriodDays` set to 2, an invoice issued on
    the 13th would be due on the 15th of the next month, while an invoice issued on
    the 12th would be due on the 15th of the current month.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this date-driven term is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """
