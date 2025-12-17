# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PayrollWageItemCreateParams"]


class PayrollWageItemCreateParams(TypedDict, total=False):
    expense_account_id: Required[Annotated[str, PropertyInfo(alias="expenseAccountId")]]
    """
    The expense account used to track wage expenses paid through this payroll wage
    item.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this payroll wage item, unique across all
    payroll wage items.

    **NOTE**: Payroll wage items do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    wage_type: Required[
        Annotated[
            Literal[
                "bonus",
                "commission",
                "hourly_overtime",
                "hourly_regular",
                "hourly_sick",
                "hourly_vacation",
                "salary_regular",
                "salary_sick",
                "salary_vacation",
            ],
            PropertyInfo(alias="wageType"),
        ]
    ]
    """
    Categorizes how this payroll wage item calculates pay - can be hourly (regular,
    overtime, sick, or vacation), salary (regular, sick, or vacation), bonus, or
    commission based.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this payroll wage item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    overtime_multiplier: Annotated[str, PropertyInfo(alias="overtimeMultiplier")]
    """
    The overtime pay multiplier for this payroll wage item, represented as a decimal
    string. For example, `"1.5"` represents time-and-a-half pay.
    """

    rate: str
    """The default rate for this payroll wage item, represented as a decimal string.

    Only one of `rate` and `ratePercent` can be set.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The default rate for this payroll wage item expressed as a percentage.

    Only one of `rate` and `ratePercent` can be set.
    """
