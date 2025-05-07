# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PayrollWageItem", "ExpenseAccount"]


class ExpenseAccount(BaseModel):
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
    id: str
    """The unique identifier assigned by QuickBooks to this payroll wage item.

    This ID is unique across all payroll wage items but not across different
    QuickBooks object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this payroll wage item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    expense_account: Optional[ExpenseAccount] = FieldInfo(alias="expenseAccount", default=None)
    """
    The expense account used to track wage expenses paid through this payroll wage
    item.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this payroll wage item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this payroll wage item, unique across all
    payroll wage items.

    **NOTE**: Payroll wage items do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_payroll_wage_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_payroll_wage_item"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this payroll wage item
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this payroll wage item was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """

    wage_type: Literal[
        "bonus",
        "commission",
        "hourly_overtime",
        "hourly_regular",
        "hourly_sick",
        "hourly_vacation",
        "salary_regular",
        "salary_sick",
        "salary_vacation",
    ] = FieldInfo(alias="wageType")
    """
    Categorizes how this payroll wage item calculates pay - can be hourly (regular,
    overtime, sick, or vacation), salary (regular, sick, or vacation), bonus, or
    commission based.
    """
