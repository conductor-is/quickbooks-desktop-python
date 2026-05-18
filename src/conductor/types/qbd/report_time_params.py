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

    columns_to_return: Annotated[Literal["active_only", "non_zero", "all"], PropertyInfo(alias="columnsToReturn")]
    """Filters which report columns QuickBooks returns.

    Use `active_only` for active columns, `non_zero` for columns with non-zero
    values, or `all` for all columns.
    """

    entity_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityFullNames")]
    """Filter for report data by entity `fullName` values, case-insensitive.

    A `fullName` is a fully-qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Repeat this query parameter
    to include multiple entities. Use only one entity filter per request.
    """

    entity_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityIds")]
    """Filter for report data by QuickBooks-assigned entity IDs.

    Repeat this query parameter to include multiple entities. Use only one entity
    filter per request.
    """

    entity_type: Annotated[Literal["customer", "employee", "other_name", "vendor"], PropertyInfo(alias="entityType")]
    """
    Filter for report data by entity type, such as customer, vendor, employee, or
    other name. Use only one entity filter per request.
    """

    include_subcolumns: Annotated[bool, PropertyInfo(alias="includeSubcolumns")]
    """Whether to include subcolumns in the report.

    QuickBooks Desktop may still omit subcolumns that it can easily compute from
    other returned values.
    """

    item_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="itemFullNames")]
    """Filter for report data by item `fullName` values, case-insensitive.

    A `fullName` is a fully-qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Repeat this query parameter
    to include multiple items. Use only one item filter per request.
    """

    item_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="itemIds")]
    """Filter for report data by QuickBooks-assigned item IDs.

    Repeat this query parameter to include multiple items. Use only one item filter
    per request.
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
    """Filter for report data by item type. Use only one item filter per request."""

    report_calendar: Annotated[
        Literal["calendar_year", "fiscal_year", "tax_year"], PropertyInfo(alias="reportCalendar")
    ]
    """The type of year to use for the report."""

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
