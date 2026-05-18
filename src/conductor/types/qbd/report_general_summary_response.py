# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .report import Report

__all__ = ["ReportGeneralSummaryResponse"]


class ReportGeneralSummaryResponse(Report):
    category: Literal["general_summary"]  # type: ignore

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
