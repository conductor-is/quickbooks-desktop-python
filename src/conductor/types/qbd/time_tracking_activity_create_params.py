# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimeTrackingActivityCreateParams"]


class TimeTrackingActivityCreateParams(TypedDict, total=False):
    duration: Required[str]
    """
    The time spent performing the service during this time tracking activity, in ISO
    8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
    represented as PT1H30M.

    **NOTE**: Although seconds can be specified when creating a time tracking
    activity, they are not returned in responses since QuickBooks Desktop's UI does
    not display seconds.

    **IMPORTANT**: This field is required for updating time tracking activities,
    even if the field is not being modified, because of a bug in QuickBooks itself.
    """

    entity_id: Required[Annotated[str, PropertyInfo(alias="entityId")]]
    """
    The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
    being tracked in this time tracking activity. This cannot refer to a customer -
    use the `customer` field to associate a customer or customer-job with this time
    tracking activity.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this time tracking activity.

    **IMPORTANT**: When this field is set to "billable" for time tracking
    activities, both `customer` and `serviceItem` are required so that an invoice
    can be created.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The time tracking activity's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """
    The customer or customer-job to which this time tracking activity could be
    billed. If `billingStatus` is set to "billable", this field is required.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    note: str
    """A note or comment about this time tracking activity."""

    payroll_wage_item_id: Annotated[str, PropertyInfo(alias="payrollWageItemId")]
    """
    The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
    tracking activity. This field can only be used for time tracking if: (1) the
    person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
    data to create paychecks" preference is enabled in their payroll settings.
    """

    service_item_id: Annotated[str, PropertyInfo(alias="serviceItemId")]
    """
    The type of service performed during this time tracking activity, referring to
    billable or purchasable services such as specialized labor, consulting hours,
    and professional fees.

    **NOTE**: This field is not required if no `customer` is specified. However, if
    `billingStatus` is set to "billable", both this field and `customer` are
    required.
    """
