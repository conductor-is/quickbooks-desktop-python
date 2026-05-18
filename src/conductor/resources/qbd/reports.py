# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import (
    report_job_params,
    report_time_params,
    report_aging_params,
    report_custom_detail_params,
    report_budget_summary_params,
    report_custom_summary_params,
    report_general_detail_params,
    report_payroll_detail_params,
    report_general_summary_params,
    report_payroll_summary_params,
)
from ..._base_client import make_request_options
from ...types.qbd.report import Report

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def aging(
        self,
        *,
        report_type: Literal[
            "ap_aging_detail", "ap_aging_summary", "ar_aging_detail", "ar_aging_summary", "collections_report"
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        aging_as_of: Literal["report_end_date", "today"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves an accounts receivable, accounts payable, or collections aging report
        showing unpaid invoices and bills by aging criteria. This report is useful for
        analyzing receivables, payables, and collection work across summary or detail
        aging views.

        Args:
          report_type: The aging report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          aging_as_of: The date through which QuickBooks Desktop calculates aging information.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/aging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "aging_as_of": aging_as_of,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_aging_params.ReportAgingParams,
                ),
            ),
            cast_to=Report,
        )

    def budget_summary(
        self,
        *,
        fiscal_year: float,
        report_type: Literal[
            "balance_sheet_budget_overview",
            "balance_sheet_budget_vs_actual",
            "profit_and_loss_budget_overview",
            "profit_and_loss_budget_performance",
            "profit_and_loss_budget_vs_actual",
        ],
        conductor_end_user_id: str,
        budget_criterion: Literal["accounts", "accounts_and_classes", "accounts_and_customers"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_columns_by: Literal["class", "customer", "date"] | Omit = omit,
        summarize_rows_by: Literal["account", "class", "customer"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop budget summary report for Balance Sheet or Profit
        and Loss budgets, including budget overview, budget versus actual, and
        performance views. This report compares budgeted amounts against actual activity
        for a fiscal year and budget criterion; the target budget must already exist in
        QuickBooks Desktop.

        Args:
          fiscal_year: The fiscal year of the QuickBooks budget. QuickBooks Desktop returns the full
              fiscal year for prior years and year-to-date data for the current fiscal year.

          report_type: The budget summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          budget_criterion: What the budget covers, such as accounts, accounts and classes, or accounts and
              customers.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_columns_by: How QuickBooks Desktop calculates budget report columns and labels column
              headers.

          summarize_rows_by: How QuickBooks Desktop labels budget report rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/budget-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "report_type": report_type,
                        "budget_criterion": budget_criterion,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_columns_by": summarize_columns_by,
                        "summarize_rows_by": summarize_rows_by,
                    },
                    report_budget_summary_params.ReportBudgetSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    def custom_detail(
        self,
        *,
        include_columns: List[
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
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        report_type: Literal["custom_transaction_detail"] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a custom transaction detail report built from the row grouping,
        included columns, date period, and filters you request. This report is useful
        when no preset detail report exposes the transaction rows or report-only columns
        you need; QuickBooks Desktop does not choose default columns for this report.

        Args:
          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          report_type: The custom detail report type to retrieve. This endpoint supports only
              `custom_transaction_detail`, so this parameter is optional and defaults to
              `custom_transaction_detail`.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/custom-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_columns": include_columns,
                        "summarize_rows_by": summarize_rows_by,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "report_type": report_type,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_custom_detail_params.ReportCustomDetailParams,
                ),
            ),
            cast_to=Report,
        )

    def custom_summary(
        self,
        *,
        summarize_columns_by: Literal[
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
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        report_type: Literal["custom_summary"] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a custom summary report built from the row and column axes, filters,
        date period, calendar, and basis options you request. This report is useful when
        preset summary reports do not match the dimensions you need; QuickBooks Desktop
        does not assume a default layout.

        Args:
          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          report_type: The custom summary report type to retrieve. This endpoint supports only
              `custom_summary`, so this parameter is optional and defaults to
              `custom_summary`.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/custom-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "summarize_columns_by": summarize_columns_by,
                        "summarize_rows_by": summarize_rows_by,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "report_type": report_type,
                        "rows_to_return": rows_to_return,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_custom_summary_params.ReportCustomSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    def general_detail(
        self,
        *,
        report_type: Literal[
            "1099_detail",
            "audit_trail",
            "balance_sheet_detail",
            "check_detail",
            "customer_balance_detail",
            "deposit_detail",
            "estimates_by_job",
            "expense_by_vendor_detail",
            "general_ledger",
            "income_by_customer_detail",
            "income_tax_detail",
            "inventory_valuation_detail",
            "job_progress_invoices_vs_estimates",
            "journal",
            "missing_checks",
            "open_invoices",
            "open_purchase_orders",
            "open_purchase_orders_by_job",
            "open_sales_order_by_customer",
            "open_sales_order_by_item",
            "pending_sales",
            "profit_and_loss_detail",
            "purchase_by_item_detail",
            "purchase_by_vendor_detail",
            "sales_by_customer_detail",
            "sales_by_item_detail",
            "sales_by_sales_representative_detail",
            "transaction_detail_by_account",
            "transaction_list_by_customer",
            "transaction_list_by_date",
            "transaction_list_by_vendor",
            "unpaid_bills_detail",
            "unbilled_costs_by_job",
            "vendor_balance_detail",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop general detail report with transaction-level
        rows, such as General Ledger, Journal, Open Invoices, unpaid bills, sales
        detail, purchase detail, audit trail, and transaction lists. This report is
        useful for inspecting the transactions behind balances, receivables, payables,
        sales, purchases, inventory valuation, and audit activity, including report-only
        columns that may not be available from standard object queries.

        Args:
          report_type: The general detail report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/general-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_rows_by": summarize_rows_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_general_detail_params.ReportGeneralDetailParams,
                ),
            ),
            cast_to=Report,
        )

    def general_summary(
        self,
        *,
        report_type: Literal[
            "balance_sheet_by_class",
            "balance_sheet_previous_year_comparison",
            "balance_sheet_standard",
            "balance_sheet_summary",
            "customer_balance_summary",
            "expense_by_vendor_summary",
            "income_by_customer_summary",
            "inventory_stock_status_by_item",
            "inventory_stock_status_by_vendor",
            "income_tax_summary",
            "inventory_valuation_summary",
            "inventory_valuation_summary_by_site",
            "lot_number_in_stock_by_site",
            "physical_inventory_worksheet",
            "profit_and_loss_by_class",
            "profit_and_loss_by_job",
            "profit_and_loss_previous_year_comparison",
            "profit_and_loss_standard",
            "profit_and_loss_ytd_comparison",
            "purchase_by_item_summary",
            "purchase_by_vendor_summary",
            "sales_by_customer_summary",
            "sales_by_item_summary",
            "sales_by_sales_representative_summary",
            "sales_tax_liability",
            "sales_tax_revenue_summary",
            "serial_number_in_stock_by_site",
            "trial_balance",
            "vendor_balance_summary",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop general summary report, such as a balance sheet,
        profit and loss, trial balance, sales, purchase, inventory, customer balance,
        vendor balance, sales tax, or income tax summary. This report is useful for
        aggregated financial or operational totals with optional date periods, filters,
        calendar settings, and column summarization.

        Args:
          report_type: The general summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/general-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_general_summary_params.ReportGeneralSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    def job(
        self,
        *,
        report_type: Literal[
            "item_estimates_vs_actuals",
            "item_profitability",
            "job_estimates_vs_actuals_detail",
            "job_estimates_vs_actuals_summary",
            "job_profitability_detail",
            "job_profitability_summary",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop job report for estimates versus actuals, item
        profitability, or job profitability. This report is useful for project costing,
        margin analysis, and estimate tracking by customer or job; job profitability
        detail and estimates-versus-actuals detail report types require a customer or
        job filter.

        Args:
          report_type: The job report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_columns_by": summarize_columns_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_job_params.ReportJobParams,
                ),
            ),
            cast_to=Report,
        )

    def payroll_detail(
        self,
        *,
        report_type: Literal[
            "employee_state_taxes_detail",
            "payroll_item_detail",
            "payroll_review_detail",
            "payroll_transaction_detail",
            "payroll_transactions_by_payee",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop payroll detail report, including employee state
        tax detail, payroll item detail, payroll review detail, payroll transaction
        detail, and payroll transactions by payee. This report is useful for auditing
        paycheck line items, payroll item usage, tax calculations, and payee-level
        payroll activity.

        Args:
          report_type: The payroll detail report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/payroll-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_rows_by": summarize_rows_by,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_payroll_detail_params.ReportPayrollDetailParams,
                ),
            ),
            cast_to=Report,
        )

    def payroll_summary(
        self,
        *,
        report_type: Literal["employee_earnings_summary", "payroll_liability_balances", "payroll_summary"],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop payroll summary report, including payroll totals
        by employee, employee earnings by payroll item, and payroll liability balances.
        This report is useful for wage, tax, deduction, addition, employer contribution,
        and unpaid payroll liability reporting.

        Args:
          report_type: The payroll summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/payroll-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_payroll_summary_params.ReportPayrollSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    def time(
        self,
        *,
        report_type: Literal["time_by_item", "time_by_job_detail", "time_by_job_summary", "time_by_name"],
        conductor_end_user_id: str,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop time report by item, job, or name, with summary
        or detail rows depending on the selected report type. This report is useful for
        analyzing tracked time for billing, costing, staffing, or project review.

        Args:
          report_type: The time report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/reports/time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "report_type": report_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                    },
                    report_time_params.ReportTimeParams,
                ),
            ),
            cast_to=Report,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def aging(
        self,
        *,
        report_type: Literal[
            "ap_aging_detail", "ap_aging_summary", "ar_aging_detail", "ar_aging_summary", "collections_report"
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        aging_as_of: Literal["report_end_date", "today"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves an accounts receivable, accounts payable, or collections aging report
        showing unpaid invoices and bills by aging criteria. This report is useful for
        analyzing receivables, payables, and collection work across summary or detail
        aging views.

        Args:
          report_type: The aging report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          aging_as_of: The date through which QuickBooks Desktop calculates aging information.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/aging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "aging_as_of": aging_as_of,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_aging_params.ReportAgingParams,
                ),
            ),
            cast_to=Report,
        )

    async def budget_summary(
        self,
        *,
        fiscal_year: float,
        report_type: Literal[
            "balance_sheet_budget_overview",
            "balance_sheet_budget_vs_actual",
            "profit_and_loss_budget_overview",
            "profit_and_loss_budget_performance",
            "profit_and_loss_budget_vs_actual",
        ],
        conductor_end_user_id: str,
        budget_criterion: Literal["accounts", "accounts_and_classes", "accounts_and_customers"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_columns_by: Literal["class", "customer", "date"] | Omit = omit,
        summarize_rows_by: Literal["account", "class", "customer"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop budget summary report for Balance Sheet or Profit
        and Loss budgets, including budget overview, budget versus actual, and
        performance views. This report compares budgeted amounts against actual activity
        for a fiscal year and budget criterion; the target budget must already exist in
        QuickBooks Desktop.

        Args:
          fiscal_year: The fiscal year of the QuickBooks budget. QuickBooks Desktop returns the full
              fiscal year for prior years and year-to-date data for the current fiscal year.

          report_type: The budget summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          budget_criterion: What the budget covers, such as accounts, accounts and classes, or accounts and
              customers.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_columns_by: How QuickBooks Desktop calculates budget report columns and labels column
              headers.

          summarize_rows_by: How QuickBooks Desktop labels budget report rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/budget-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fiscal_year": fiscal_year,
                        "report_type": report_type,
                        "budget_criterion": budget_criterion,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_columns_by": summarize_columns_by,
                        "summarize_rows_by": summarize_rows_by,
                    },
                    report_budget_summary_params.ReportBudgetSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    async def custom_detail(
        self,
        *,
        include_columns: List[
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
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        report_type: Literal["custom_transaction_detail"] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a custom transaction detail report built from the row grouping,
        included columns, date period, and filters you request. This report is useful
        when no preset detail report exposes the transaction rows or report-only columns
        you need; QuickBooks Desktop does not choose default columns for this report.

        Args:
          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          report_type: The custom detail report type to retrieve. This endpoint supports only
              `custom_transaction_detail`, so this parameter is optional and defaults to
              `custom_transaction_detail`.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/custom-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_columns": include_columns,
                        "summarize_rows_by": summarize_rows_by,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "report_type": report_type,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_custom_detail_params.ReportCustomDetailParams,
                ),
            ),
            cast_to=Report,
        )

    async def custom_summary(
        self,
        *,
        summarize_columns_by: Literal[
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
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        report_type: Literal["custom_summary"] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a custom summary report built from the row and column axes, filters,
        date period, calendar, and basis options you request. This report is useful when
        preset summary reports do not match the dimensions you need; QuickBooks Desktop
        does not assume a default layout.

        Args:
          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          report_type: The custom summary report type to retrieve. This endpoint supports only
              `custom_summary`, so this parameter is optional and defaults to
              `custom_summary`.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/custom-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "summarize_columns_by": summarize_columns_by,
                        "summarize_rows_by": summarize_rows_by,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "report_type": report_type,
                        "rows_to_return": rows_to_return,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_custom_summary_params.ReportCustomSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    async def general_detail(
        self,
        *,
        report_type: Literal[
            "1099_detail",
            "audit_trail",
            "balance_sheet_detail",
            "check_detail",
            "customer_balance_detail",
            "deposit_detail",
            "estimates_by_job",
            "expense_by_vendor_detail",
            "general_ledger",
            "income_by_customer_detail",
            "income_tax_detail",
            "inventory_valuation_detail",
            "job_progress_invoices_vs_estimates",
            "journal",
            "missing_checks",
            "open_invoices",
            "open_purchase_orders",
            "open_purchase_orders_by_job",
            "open_sales_order_by_customer",
            "open_sales_order_by_item",
            "pending_sales",
            "profit_and_loss_detail",
            "purchase_by_item_detail",
            "purchase_by_vendor_detail",
            "sales_by_customer_detail",
            "sales_by_item_detail",
            "sales_by_sales_representative_detail",
            "transaction_detail_by_account",
            "transaction_list_by_customer",
            "transaction_list_by_date",
            "transaction_list_by_vendor",
            "unpaid_bills_detail",
            "unbilled_costs_by_job",
            "vendor_balance_detail",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop general detail report with transaction-level
        rows, such as General Ledger, Journal, Open Invoices, unpaid bills, sales
        detail, purchase detail, audit trail, and transaction lists. This report is
        useful for inspecting the transactions behind balances, receivables, payables,
        sales, purchases, inventory valuation, and audit activity, including report-only
        columns that may not be available from standard object queries.

        Args:
          report_type: The general detail report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/general-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_rows_by": summarize_rows_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_general_detail_params.ReportGeneralDetailParams,
                ),
            ),
            cast_to=Report,
        )

    async def general_summary(
        self,
        *,
        report_type: Literal[
            "balance_sheet_by_class",
            "balance_sheet_previous_year_comparison",
            "balance_sheet_standard",
            "balance_sheet_summary",
            "customer_balance_summary",
            "expense_by_vendor_summary",
            "income_by_customer_summary",
            "inventory_stock_status_by_item",
            "inventory_stock_status_by_vendor",
            "income_tax_summary",
            "inventory_valuation_summary",
            "inventory_valuation_summary_by_site",
            "lot_number_in_stock_by_site",
            "physical_inventory_worksheet",
            "profit_and_loss_by_class",
            "profit_and_loss_by_job",
            "profit_and_loss_previous_year_comparison",
            "profit_and_loss_standard",
            "profit_and_loss_ytd_comparison",
            "purchase_by_item_summary",
            "purchase_by_vendor_summary",
            "sales_by_customer_summary",
            "sales_by_item_summary",
            "sales_by_sales_representative_summary",
            "sales_tax_liability",
            "sales_tax_revenue_summary",
            "serial_number_in_stock_by_site",
            "trial_balance",
            "vendor_balance_summary",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        basis: Literal["accrual", "cash", "none"] | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop general summary report, such as a balance sheet,
        profit and loss, trial balance, sales, purchase, inventory, customer balance,
        vendor balance, sales tax, or income tax summary. This report is useful for
        aggregated financial or operational totals with optional date periods, filters,
        calendar settings, and column summarization.

        Args:
          report_type: The general summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          basis: The accounting basis to use for the report. Use `cash` to base income and
              expenses on when money changes hands, `accrual` to base them on invoice and bill
              dates, or `none` to use the QuickBooks Desktop default for the report.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/general-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "basis": basis,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_general_summary_params.ReportGeneralSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    async def job(
        self,
        *,
        report_type: Literal[
            "item_estimates_vs_actuals",
            "item_profitability",
            "job_estimates_vs_actuals_detail",
            "job_estimates_vs_actuals_summary",
            "job_profitability_detail",
            "job_profitability_summary",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        transaction_types: List[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop job report for estimates versus actuals, item
        profitability, or job profitability. This report is useful for project costing,
        margin analysis, and estimate tracking by customer or job; job profitability
        detail and estimates-versus-actuals detail report types require a customer or
        job filter.

        Args:
          report_type: The job report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          transaction_types: Filter report rows by transaction type. Accepts one or more transaction types.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/job",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_columns_by": summarize_columns_by,
                        "transaction_types": transaction_types,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_job_params.ReportJobParams,
                ),
            ),
            cast_to=Report,
        )

    async def payroll_detail(
        self,
        *,
        report_type: Literal[
            "employee_state_taxes_detail",
            "payroll_item_detail",
            "payroll_review_detail",
            "payroll_transaction_detail",
            "payroll_transactions_by_payee",
        ],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        accounts_to_include: Literal["all", "in_use"] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_columns: List[
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
        ]
        | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        open_balance_as_of: Literal["report_end_date", "today"] | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        summarize_rows_by: Literal[
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
            "tax_line",
            "terms",
            "total_only",
            "two_week",
            "vendor",
            "vendor_type",
            "week",
            "year",
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop payroll detail report, including employee state
        tax detail, payroll item detail, payroll review detail, payroll transaction
        detail, and payroll transactions by payee. This report is useful for auditing
        paycheck line items, payroll item usage, tax calculations, and payee-level
        payroll activity.

        Args:
          report_type: The payroll detail report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          accounts_to_include: Whether to include all accounts or only accounts in use.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_columns: The report columns to include, by column type. Accepts one or more columns.

              **IMPORTANT**: When this parameter is present, QuickBooks Desktop omits its
              default report columns unless you include them here.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          open_balance_as_of: The date through which QuickBooks Desktop calculates open balance information.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          summarize_rows_by: How QuickBooks Desktop calculates report data and labels report rows.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/payroll-detail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "accounts_to_include": accounts_to_include,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_columns": include_columns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "open_balance_as_of": open_balance_as_of,
                        "posting_status": posting_status,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "summarize_rows_by": summarize_rows_by,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_payroll_detail_params.ReportPayrollDetailParams,
                ),
            ),
            cast_to=Report,
        )

    async def payroll_summary(
        self,
        *,
        report_type: Literal["employee_earnings_summary", "payroll_liability_balances", "payroll_summary"],
        conductor_end_user_id: str,
        account_full_names: SequenceNotStr[str] | Omit = omit,
        account_ids: SequenceNotStr[str] | Omit = omit,
        account_type: Literal[
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
        ]
        | Omit = omit,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        detail_level: Literal["all", "all_except_summary", "summary_only"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        posting_status: Literal["either", "non_posting", "posting"] | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        updated_after: Union[str, date] | Omit = omit,
        updated_before: Union[str, date] | Omit = omit,
        updated_date_macro: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop payroll summary report, including payroll totals
        by employee, employee earnings by payroll item, and payroll liability balances.
        This report is useful for wage, tax, deduction, addition, employer contribution,
        and unpaid payroll liability reporting.

        Args:
          report_type: The payroll summary report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_full_names: Filter report rows by account `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more account full names. Choose
              only one account filter per request: `accountType`, `accountIds`, or
              `accountFullNames`.

          account_ids: Filter report rows by QuickBooks-assigned account IDs. Accepts one or more
              account IDs. Choose only one account filter per request: `accountType`,
              `accountIds`, or `accountFullNames`.

          account_type:
              Filter report rows by account type. Choose only one account filter per request:
              `accountType`, `accountIds`, or `accountFullNames`.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          detail_level: The report detail level to include. Use `all` for all rows, `all_except_summary`
              to omit summary rows, or `summary_only` to return only summary rows.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          posting_status: Filter report rows that are posting, non-posting, or either. Posting status
              refers to whether QuickBooks records the transaction in an account register.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          updated_after: Filter report rows updated on or after this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_before: Filter report rows updated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `updatedDateMacro` or
              `updatedAfter`/`updatedBefore`.

          updated_date_macro: A QuickBooks Desktop relative updated-date macro. Choose either
              `updatedDateMacro` or `updatedAfter`/`updatedBefore`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/payroll-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "account_full_names": account_full_names,
                        "account_ids": account_ids,
                        "account_type": account_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "detail_level": detail_level,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "posting_status": posting_status,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "updated_date_macro": updated_date_macro,
                    },
                    report_payroll_summary_params.ReportPayrollSummaryParams,
                ),
            ),
            cast_to=Report,
        )

    async def time(
        self,
        *,
        report_type: Literal["time_by_item", "time_by_job_detail", "time_by_job_summary", "time_by_name"],
        conductor_end_user_id: str,
        class_full_names: SequenceNotStr[str] | Omit = omit,
        class_ids: SequenceNotStr[str] | Omit = omit,
        columns_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        entity_full_names: SequenceNotStr[str] | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        entity_type: Literal["customer", "employee", "other_name", "vendor"] | Omit = omit,
        include_subcolumns: bool | Omit = omit,
        item_full_names: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
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
        ]
        | Omit = omit,
        report_calendar: Literal["calendar_year", "fiscal_year", "tax_year"] | Omit = omit,
        report_date_from: Union[str, date] | Omit = omit,
        report_date_macro: Literal[
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
        ]
        | Omit = omit,
        report_date_to: Union[str, date] | Omit = omit,
        rows_to_return: Literal["active_only", "non_zero", "all"] | Omit = omit,
        summarize_columns_by: Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieves a QuickBooks Desktop time report by item, job, or name, with summary
        or detail rows depending on the selected report type. This report is useful for
        analyzing tracked time for billing, costing, staffing, or project review.

        Args:
          report_type: The time report type to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          class_full_names: Filter report rows by class `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more class full names. Choose only
              one class filter per request: `classIds` or `classFullNames`.

          class_ids: Filter report rows by QuickBooks-assigned class IDs. Accepts one or more class
              IDs. Choose only one class filter per request: `classIds` or `classFullNames`.

          columns_to_return: Filters which report columns QuickBooks returns. Use `active_only` for active
              columns, `non_zero` for columns with non-zero values, or `all` for all columns.

          entity_full_names: Filter report rows by entity `fullName` values, case-insensitive. A `fullName`
              is a fully qualified QuickBooks name formed by joining parent object names with
              the object's `name` using colons. Accepts one or more entity full names. Choose
              only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_ids: Filter report rows by QuickBooks-assigned entity IDs. Accepts one or more entity
              IDs. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          entity_type: Filter report rows by entity type, such as customer, vendor, employee, or other
              name. Choose only one entity filter per request: `entityType`, `entityIds`, or
              `entityFullNames`.

          include_subcolumns: Whether to include subcolumns in the report.

              **NOTE**: QuickBooks Desktop may still omit subcolumns that it can easily
              compute from other returned values.

          item_full_names: Filter report rows by item `fullName` values, case-insensitive. A `fullName` is
              a fully qualified QuickBooks name formed by joining parent object names with the
              object's `name` using colons. Accepts one or more item full names. Choose only
              one item filter per request: `itemType`, `itemIds`, or `itemFullNames`.

          item_ids: Filter report rows by QuickBooks-assigned item IDs. Accepts one or more item
              IDs. Choose only one item filter per request: `itemType`, `itemIds`, or
              `itemFullNames`.

          item_type:
              Filter report rows by item type. Choose only one item filter per request:
              `itemType`, `itemIds`, or `itemFullNames`.

          report_calendar: The type of year to use for the report.

          report_date_from: Filter report rows dated on or after this date, in ISO 8601 format (YYYY-MM-DD).
              Choose either `reportDateMacro` or `reportDateFrom`/`reportDateTo`. If you omit
              `reportDateFrom`, `reportDateTo`, and `reportDateMacro`, QuickBooks Desktop uses
              the current fiscal year to date.

          report_date_macro: A QuickBooks Desktop relative date macro for the report period. Choose either
              `reportDateMacro` or `reportDateFrom`/`reportDateTo`.

          report_date_to: Filter report rows dated on or before this date, in ISO 8601 format
              (YYYY-MM-DD). Choose either `reportDateMacro` or
              `reportDateFrom`/`reportDateTo`. If you omit `reportDateFrom`, `reportDateTo`,
              and `reportDateMacro`, QuickBooks Desktop uses the current fiscal year to date.

          rows_to_return: Filters which report rows QuickBooks returns. Use `active_only` for active rows,
              `non_zero` for rows with non-zero values, or `all` for all rows.

          summarize_columns_by: How QuickBooks Desktop calculates report data and labels report column headers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/reports/time",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "report_type": report_type,
                        "class_full_names": class_full_names,
                        "class_ids": class_ids,
                        "columns_to_return": columns_to_return,
                        "entity_full_names": entity_full_names,
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "include_subcolumns": include_subcolumns,
                        "item_full_names": item_full_names,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "report_calendar": report_calendar,
                        "report_date_from": report_date_from,
                        "report_date_macro": report_date_macro,
                        "report_date_to": report_date_to,
                        "rows_to_return": rows_to_return,
                        "summarize_columns_by": summarize_columns_by,
                    },
                    report_time_params.ReportTimeParams,
                ),
            ),
            cast_to=Report,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.aging = to_raw_response_wrapper(
            reports.aging,
        )
        self.budget_summary = to_raw_response_wrapper(
            reports.budget_summary,
        )
        self.custom_detail = to_raw_response_wrapper(
            reports.custom_detail,
        )
        self.custom_summary = to_raw_response_wrapper(
            reports.custom_summary,
        )
        self.general_detail = to_raw_response_wrapper(
            reports.general_detail,
        )
        self.general_summary = to_raw_response_wrapper(
            reports.general_summary,
        )
        self.job = to_raw_response_wrapper(
            reports.job,
        )
        self.payroll_detail = to_raw_response_wrapper(
            reports.payroll_detail,
        )
        self.payroll_summary = to_raw_response_wrapper(
            reports.payroll_summary,
        )
        self.time = to_raw_response_wrapper(
            reports.time,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.aging = async_to_raw_response_wrapper(
            reports.aging,
        )
        self.budget_summary = async_to_raw_response_wrapper(
            reports.budget_summary,
        )
        self.custom_detail = async_to_raw_response_wrapper(
            reports.custom_detail,
        )
        self.custom_summary = async_to_raw_response_wrapper(
            reports.custom_summary,
        )
        self.general_detail = async_to_raw_response_wrapper(
            reports.general_detail,
        )
        self.general_summary = async_to_raw_response_wrapper(
            reports.general_summary,
        )
        self.job = async_to_raw_response_wrapper(
            reports.job,
        )
        self.payroll_detail = async_to_raw_response_wrapper(
            reports.payroll_detail,
        )
        self.payroll_summary = async_to_raw_response_wrapper(
            reports.payroll_summary,
        )
        self.time = async_to_raw_response_wrapper(
            reports.time,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.aging = to_streamed_response_wrapper(
            reports.aging,
        )
        self.budget_summary = to_streamed_response_wrapper(
            reports.budget_summary,
        )
        self.custom_detail = to_streamed_response_wrapper(
            reports.custom_detail,
        )
        self.custom_summary = to_streamed_response_wrapper(
            reports.custom_summary,
        )
        self.general_detail = to_streamed_response_wrapper(
            reports.general_detail,
        )
        self.general_summary = to_streamed_response_wrapper(
            reports.general_summary,
        )
        self.job = to_streamed_response_wrapper(
            reports.job,
        )
        self.payroll_detail = to_streamed_response_wrapper(
            reports.payroll_detail,
        )
        self.payroll_summary = to_streamed_response_wrapper(
            reports.payroll_summary,
        )
        self.time = to_streamed_response_wrapper(
            reports.time,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.aging = async_to_streamed_response_wrapper(
            reports.aging,
        )
        self.budget_summary = async_to_streamed_response_wrapper(
            reports.budget_summary,
        )
        self.custom_detail = async_to_streamed_response_wrapper(
            reports.custom_detail,
        )
        self.custom_summary = async_to_streamed_response_wrapper(
            reports.custom_summary,
        )
        self.general_detail = async_to_streamed_response_wrapper(
            reports.general_detail,
        )
        self.general_summary = async_to_streamed_response_wrapper(
            reports.general_summary,
        )
        self.job = async_to_streamed_response_wrapper(
            reports.job,
        )
        self.payroll_detail = async_to_streamed_response_wrapper(
            reports.payroll_detail,
        )
        self.payroll_summary = async_to_streamed_response_wrapper(
            reports.payroll_summary,
        )
        self.time = async_to_streamed_response_wrapper(
            reports.time,
        )
