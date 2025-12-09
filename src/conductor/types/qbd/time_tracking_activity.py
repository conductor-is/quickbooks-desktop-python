# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimeTrackingActivity", "Class", "Customer", "Entity", "PayrollWageItem", "ServiceItem"]


class Class(BaseModel):
    """The time tracking activity's class.

    Classes can be used to categorize objects into meaningful segments, such as department, location, or type of work. In QuickBooks, class tracking is off by default.
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


class Customer(BaseModel):
    """
    The customer or customer-job to which this time tracking activity could be billed. If `billingStatus` is set to "billable", this field is required.
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


class Entity(BaseModel):
    """
    The employee, vendor, or person on QuickBooks's "Other Names" list whose time is being tracked in this time tracking activity. This cannot refer to a customer - use the `customer` field to associate a customer or customer-job with this time tracking activity.
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


class PayrollWageItem(BaseModel):
    """
    The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time tracking activity. This field can only be used for time tracking if: (1) the person specified in `entity` is an employee in QuickBooks, and (2) the "Use time data to create paychecks" preference is enabled in their payroll settings.
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


class ServiceItem(BaseModel):
    """
    The type of service performed during this time tracking activity, referring to billable or purchasable services such as specialized labor, consulting hours, and professional fees.

    **NOTE**: This field is not required if no `customer` is specified. However, if `billingStatus` is set to "billable", both this field and `customer` are required.
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


class TimeTrackingActivity(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this time tracking activity.

    This ID is unique across all transaction types.
    """

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this time tracking activity.

    **IMPORTANT**: When this field is set to "billable" for time tracking
    activities, both `customer` and `serviceItem` are required so that an invoice
    can be created.
    """

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The time tracking activity's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this time tracking activity was created, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """

    customer: Optional[Customer] = None
    """
    The customer or customer-job to which this time tracking activity could be
    billed. If `billingStatus` is set to "billable", this field is required.
    """

    duration: str
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

    entity: Entity
    """
    The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
    being tracked in this time tracking activity. This cannot refer to a customer -
    use the `customer` field to associate a customer or customer-job with this time
    tracking activity.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_billed: Optional[bool] = FieldInfo(alias="isBilled", default=None)
    """Indicates whether this time tracking activity has been billed."""

    note: Optional[str] = None
    """A note or comment about this time tracking activity."""

    object_type: Literal["qbd_time_tracking_activity"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_time_tracking_activity"`."""

    payroll_wage_item: Optional[PayrollWageItem] = FieldInfo(alias="payrollWageItem", default=None)
    """
    The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
    tracking activity. This field can only be used for time tracking if: (1) the
    person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
    data to create paychecks" preference is enabled in their payroll settings.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this time tracking activity
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    service_item: Optional[ServiceItem] = FieldInfo(alias="serviceItem", default=None)
    """
    The type of service performed during this time tracking activity, referring to
    billable or purchasable services such as specialized labor, consulting hours,
    and professional fees.

    **NOTE**: This field is not required if no `customer` is specified. However, if
    `billingStatus` is set to "billable", both this field and `customer` are
    required.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this time tracking activity was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """
