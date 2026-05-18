# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ReportAgingParams"]


class ReportAgingParams(TypedDict, total=False):
    report_type: Required[
        Annotated[
            Literal["ap_aging_detail", "ap_aging_summary", "ar_aging_detail", "ar_aging_summary", "collections_report"],
            PropertyInfo(alias="reportType"),
        ]
    ]
    """The aging report type to retrieve."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    account_full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountFullNames")]
    """Filter for report data by account `fullName` values, case-insensitive.

    A `fullName` is a fully-qualified QuickBooks name formed by joining parent
    object names with the object's `name` using colons. Repeat this query parameter
    to include multiple accounts. Use only one account filter per request.
    """

    account_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountIds")]
    """Filter for report data by QuickBooks-assigned account IDs.

    Repeat this query parameter to include multiple accounts. Use only one account
    filter per request.
    """

    accounts_to_include: Annotated[Literal["all", "in_use"], PropertyInfo(alias="accountsToInclude")]
    """Whether to include all accounts or only accounts in use."""

    account_type: Annotated[
        Literal[
            "accounts_payable",
            "accounts_receivable",
            "allowed_for_1099",
            "ap_and_sales_tax",
            "ap_or_credit_card",
            "ar_and_ap",
            "asset",
            "balance_sheet",
            "bank",
            "bank_and_ar_and_ap_and_uf",
            "bank_and_uf",
            "cost_of_sales",
            "credit_card",
            "current_asset",
            "current_asset_and_expense",
            "current_liability",
            "equity",
            "equity_and_income_and_expense",
            "expense_and_other_expense",
            "fixed_asset",
            "income_and_expense",
            "income_and_other_income",
            "liability",
            "liability_and_equity",
            "long_term_liability",
            "non_posting",
            "ordinary_expense",
            "ordinary_income",
            "ordinary_income_and_cogs",
            "ordinary_income_and_expense",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
            "other_income_or_expense",
        ],
        PropertyInfo(alias="accountType"),
    ]
    """Filter for report data by account type.

    Use only one account filter per request.
    """

    aging_as_of: Annotated[Literal["report_end_date", "today"], PropertyInfo(alias="agingAsOf")]
    """The date through which QuickBooks Desktop calculates aging information."""

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

    detail_level: Annotated[Literal["all", "all_except_summary", "summary_only"], PropertyInfo(alias="detailLevel")]
    """The report detail level to include.

    Use `all` for all rows, `all_except_summary` to omit summary rows, or
    `summary_only` to return only summary rows.
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

    include_columns: Annotated[
        List[
            Literal[
                "account",
                "aging",
                "amount",
                "amount_difference",
                "average_cost",
                "billed_date",
                "billing_status",
                "calculated_amount",
                "class",
                "cleared_status",
                "cost_price",
                "credit",
                "currency",
                "date",
                "debit",
                "delivery_date",
                "due_date",
                "estimate_active",
                "exchange_rate",
                "shipment_origin",
                "income_subject_to_tax",
                "invoiced",
                "item",
                "description",
                "last_modified_by",
                "latest_or_prior_state",
                "memo",
                "updated_at",
                "name",
                "name_account_number",
                "name_address",
                "name_city",
                "name_contact",
                "name_email",
                "name_fax",
                "name_phone",
                "name_state",
                "name_postal_code",
                "open_balance",
                "original_amount",
                "paid_amount",
                "paid_status",
                "paid_through_date",
                "payment_method",
                "payroll_item",
                "purchase_order_number",
                "print_status",
                "progress_amount",
                "progress_percent",
                "quantity",
                "quantity_available",
                "quantity_on_hand",
                "quantity_on_sales_order",
                "received_quantity",
                "ref_number",
                "running_balance",
                "sales_representative",
                "sales_tax_code",
                "serial_or_lot_number",
                "shipping_date",
                "shipping_method",
                "source_name",
                "split_account",
                "ssn_or_tax_identification_number",
                "tax_line",
                "tax_table_version",
                "terms",
                "transaction_id",
                "transaction_number",
                "transaction_type",
                "unit_price",
                "user_edit",
                "value_on_hand",
                "wage_base",
                "wage_base_tips",
            ]
        ],
        PropertyInfo(alias="includeColumns"),
    ]
    """The specific report columns to include, by column type.

    Repeat this query parameter to request multiple columns. When this parameter is
    present, QuickBooks Desktop omits its default report columns unless you include
    them here.
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

    posting_status: Annotated[Literal["either", "non_posting", "posting"], PropertyInfo(alias="postingStatus")]
    """Filter for report data that is posting, non-posting, or either.

    Posting status refers to whether QuickBooks records the transaction in an
    account register.
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

    transaction_types: Annotated[
        List[
            Literal[
                "all",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "deposit",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item_receipt",
                "journal_entry",
                "liability_adjustment",
                "paycheck",
                "payroll_liability_check",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "transfer",
                "vendor_credit",
                "ytd_adjustment",
            ]
        ],
        PropertyInfo(alias="transactionTypes"),
    ]
    """Filter for report data by transaction type(s).

    Repeat this query parameter to include multiple transaction types.
    """

    updated_after: Annotated[Union[str, date], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """
    Filter for report data updated on or after this date, in ISO 8601 format
    (YYYY-MM-DD). This cannot be combined with `updatedDateMacro`.
    """

    updated_before: Annotated[Union[str, date], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """
    Filter for report data updated on or before this date, in ISO 8601 format
    (YYYY-MM-DD). This cannot be combined with `updatedDateMacro`.
    """

    updated_date_macro: Annotated[
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
        PropertyInfo(alias="updatedDateMacro"),
    ]
    """A QuickBooks Desktop relative updated-date macro.

    This cannot be combined with `updatedAfter` or `updatedBefore`.
    """
