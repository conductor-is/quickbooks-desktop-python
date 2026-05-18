# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ReportBudgetSummaryParams"]


class ReportBudgetSummaryParams(TypedDict, total=False):
    fiscal_year: Required[Annotated[float, PropertyInfo(alias="fiscalYear")]]
    """The fiscal year of the QuickBooks budget.

    QuickBooks Desktop returns the full fiscal year for prior years and year-to-date
    data for the current fiscal year.
    """

    report_type: Required[
        Annotated[
            Literal[
                "balance_sheet_budget_overview",
                "balance_sheet_budget_vs_actual",
                "profit_and_loss_budget_overview",
                "profit_and_loss_budget_performance",
                "profit_and_loss_budget_vs_actual",
            ],
            PropertyInfo(alias="reportType"),
        ]
    ]
    """The budget summary report type to retrieve."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    budget_criterion: Annotated[
        Literal["accounts", "accounts_and_classes", "accounts_and_customers"], PropertyInfo(alias="budgetCriterion")
    ]
    """
    What the budget covers, such as accounts, accounts and classes, or accounts and
    customers.
    """

    class_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="classFullNames")]
    """Filter for report data by class `fullName` values, case-insensitive.

    A `fullName` is a fully-qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Repeat this query parameter
    to include multiple classes. Use only one class filter per request.
    """

    class_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="classIds")]
    """Filter for report data by QuickBooks-assigned class IDs.

    Repeat this query parameter to include multiple classes. Use only one class
    filter per request.
    """

    report_date_from: Annotated[Union[str, date], PropertyInfo(alias="reportDateFrom", format="iso8601")]
    """
    Filter for report data dated on or after this date, in ISO 8601 format
    (YYYY-MM-DD). This cannot be combined with `reportDateMacro`. If you omit
    `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
    the current fiscal year to date.
    """

    report_date_macro: Annotated[
        Literal[
            "all",
            "today",
            "this_week",
            "this_week_to_date",
            "this_month",
            "this_month_to_date",
            "this_quarter",
            "this_quarter_to_date",
            "this_year",
            "this_year_to_date",
            "yesterday",
            "last_week",
            "last_week_to_date",
            "last_month",
            "last_month_to_date",
            "last_quarter",
            "last_quarter_to_date",
            "last_year",
            "last_year_to_date",
            "next_week",
            "next_four_weeks",
            "next_month",
            "next_quarter",
            "next_year",
        ],
        PropertyInfo(alias="reportDateMacro"),
    ]
    """A QuickBooks Desktop relative date macro.

    This cannot be combined with `reportDateFrom` or `reportDateTo`.
    """

    report_date_to: Annotated[Union[str, date], PropertyInfo(alias="reportDateTo", format="iso8601")]
    """
    Filter for report data dated on or before this date, in ISO 8601 format
    (YYYY-MM-DD). This cannot be combined with `reportDateMacro`. If you omit
    `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
    the current fiscal year to date.
    """

    summarize_columns_by: Annotated[Literal["class", "customer", "date"], PropertyInfo(alias="summarizeColumnsBy")]
    """
    How QuickBooks Desktop calculates budget report columns and labels column
    headers.
    """

    summarize_rows_by: Annotated[Literal["account", "class", "customer"], PropertyInfo(alias="summarizeRowsBy")]
    """How QuickBooks Desktop labels budget report rows."""
