# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .report import Report

__all__ = ["ReportGeneralDetailResponse"]


class ReportGeneralDetailResponse(Report):
    category: Literal["general_detail"]  # type: ignore

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
    ] = FieldInfo(alias="reportType")  # type: ignore

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
