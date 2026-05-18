# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ReportTimeParams"]


class ReportTimeParams(TypedDict, total=False):
    report_type: Required[
        Annotated[
            Literal["time_by_item", "time_by_job_detail", "time_by_job_summary", "time_by_name"],
            PropertyInfo(alias="reportType"),
        ]
    ]
    """The time report type to retrieve."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    class_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="classFullNames")]
    """Filter report rows by class `fullName` values, case-insensitive.

    A `fullName` is a fully qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Accepts one or more class
    full names. Choose only one class filter per request: `classIds` or
    `classFullNames`.
    """

    class_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="classIds")]
    """Filter report rows by QuickBooks-assigned class IDs.

    Accepts one or more class IDs. Choose only one class filter per request:
    `classIds` or `classFullNames`.
    """

    columns_to_return: Annotated[Literal["active_only", "non_zero", "all"], PropertyInfo(alias="columnsToReturn")]
    """Filters which report columns QuickBooks returns.

    Use `active_only` for active columns, `non_zero` for columns with non-zero
    values, or `all` for all columns.
    """

    entity_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityFullNames")]
    """Filter report rows by entity `fullName` values, case-insensitive.

    A `fullName` is a fully qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Accepts one or more entity
    full names. Choose only one entity filter per request: `entityType`,
    `entityIds`, or `entityFullNames`.
    """

    entity_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityIds")]
    """Filter report rows by QuickBooks-assigned entity IDs.

    Accepts one or more entity IDs. Choose only one entity filter per request:
    `entityType`, `entityIds`, or `entityFullNames`.
    """

    entity_type: Annotated[Literal["customer", "employee", "other_name", "vendor"], PropertyInfo(alias="entityType")]
    """
    Filter report rows by entity type, such as customer, vendor, employee, or other
    name. Choose only one entity filter per request: `entityType`, `entityIds`, or
    `entityFullNames`.
    """

    include_subcolumns: Annotated[bool, PropertyInfo(alias="includeSubcolumns")]
    """Whether to include subcolumns in the report.

    **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
    compute from other returned values.
    """

    item_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="itemFullNames")]
    """Filter report rows by item `fullName` values, case-insensitive.

    A `fullName` is a fully qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Accepts one or more item
    full names. Choose only one item filter per request: `itemType`, `itemIds`, or
    `itemFullNames`.
    """

    item_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="itemIds")]
    """Filter report rows by QuickBooks-assigned item IDs.

    Accepts one or more item IDs. Choose only one item filter per request:
    `itemType`, `itemIds`, or `itemFullNames`.
    """

    item_type: Annotated[
        Literal[
            "all_except_fixed_asset",
            "assembly",
            "discount",
            "fixed_asset",
            "inventory",
            "inventory_and_assembly",
            "non_inventory",
            "other_charge",
            "payment",
            "sales",
            "sales_tax",
            "service",
        ],
        PropertyInfo(alias="itemType"),
    ]
    """Filter report rows by item type.

    Choose only one item filter per request: `itemType`, `itemIds`, or
    `itemFullNames`.
    """

    report_calendar: Annotated[
        Literal["calendar_year", "fiscal_year", "tax_year"], PropertyInfo(alias="reportCalendar")
    ]
    """The type of year to use for the report."""

    report_date_from: Annotated[Union[str, date], PropertyInfo(alias="reportDateFrom", format="iso8601")]
    """Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).

    Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
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
    """A QuickBooks Desktop relative date macro for the report period.

    Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`.
    """

    report_date_to: Annotated[Union[str, date], PropertyInfo(alias="reportDateTo", format="iso8601")]
    """Filter report rows dated on or before this date, in ISO 8601 format
    (YYYY-MM-DD).

    Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
    `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
    the current fiscal year to date.
    """

    rows_to_return: Annotated[Literal["active_only", "non_zero", "all"], PropertyInfo(alias="rowsToReturn")]
    """Filters which report rows QuickBooks returns.

    Use `active_only` for active rows, `non_zero` for rows with non-zero values, or
    `all` for all rows.
    """

    summarize_columns_by: Annotated[
        Literal[
            "account",
            "balance_sheet",
            "class",
            "customer",
            "customer_type",
            "day",
            "employee",
            "four_week",
            "half_month",
            "income_statement",
            "item_detail",
            "item_type",
            "month",
            "payee",
            "payment_method",
            "payroll_item_detail",
            "payroll_ytd_detail",
            "quarter",
            "sales_representative",
            "sales_tax_code",
            "shipping_method",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ],
        PropertyInfo(alias="summarizeColumnsBy"),
    ]
    """How QuickBooks Desktop calculates report data and labels report column headers."""
