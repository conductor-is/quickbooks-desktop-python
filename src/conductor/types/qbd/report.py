# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Report",
    "Column",
    "ColumnTitle",
    "Row",
    "RowQbdReportTextRow",
    "RowQbdReportDataRow",
    "RowQbdReportDataRowCell",
    "RowQbdReportDataRowRowDescriptor",
    "RowQbdReportSubtotalRow",
    "RowQbdReportSubtotalRowCell",
    "RowQbdReportSubtotalRowRowDescriptor",
    "RowQbdReportTotalRow",
    "RowQbdReportTotalRowCell",
    "RowQbdReportTotalRowRowDescriptor",
]


class ColumnTitle(BaseModel):
    row_number: float = FieldInfo(alias="rowNumber")
    """The one-based title row number. Reports can have multiple title rows."""

    value: Optional[str] = None
    """The title text for this column title row.

    This is `null` if QuickBooks Desktop does not provide one.
    """


class Column(BaseModel):
    column_id: str = FieldInfo(alias="columnId")
    """The report column identifier.

    QuickBooks Desktop numbers columns from left to right, starting at 1. Use this
    value to match row cells to columns.
    """

    column_type: str = FieldInfo(alias="columnType")
    """
    The report column type, describing the business meaning of the column, such as
    `date`, `amount`, or `transaction_type`.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """The raw value data type for this column, such as `string`, `amount`, or `date`.

    This is `null` if QuickBooks Desktop does not provide a data type.
    """

    titles: List[ColumnTitle]
    """The column title cells. Reports can use multiple title rows."""


class RowQbdReportTextRow(BaseModel):
    kind: Literal["text"]
    """The row kind. This value is always `"text"`."""

    row_number: float = FieldInfo(alias="rowNumber")
    """The one-based row number from the report."""

    text: Optional[str] = None
    """The text row value.

    Text rows are mainly used for headings. This is `null` if QuickBooks Desktop
    does not provide one.
    """


class RowQbdReportDataRowCell(BaseModel):
    column_id: str = FieldInfo(alias="columnId")
    """The column identifier for this cell.

    This matches a column's `columnId` and refers to the column's left-to-right
    position in the report.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """The value data type for this cell.

    If QuickBooks Desktop omits the cell data type, this uses the matching column's
    `dataType` when available.
    """

    value: Optional[str] = None
    """The cell value as a QuickBooks Desktop-formatted string.

    This is `null` if QuickBooks Desktop does not provide a value for the cell.
    """


class RowQbdReportDataRowRowDescriptor(BaseModel):
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when QuickBooks Desktop does not provide one.
    """

    type: Optional[str] = None
    """The kind of row-level descriptor, such as `account`, `customer`, or `vendor`.

    This is `null` if QuickBooks Desktop does not provide one.
    """

    value: Optional[str] = None
    """The row-level descriptor value.

    This can differ from the first cell value and is `null` if QuickBooks Desktop
    does not provide one.
    """


class RowQbdReportDataRow(BaseModel):
    cells: List[RowQbdReportDataRowCell]
    """The cells in this report row.

    Report rows are sparse, so cells appear only for columns where QuickBooks
    Desktop returned a value.
    """

    kind: Literal["data"]
    """The row kind. This value is always `"data"`."""

    row_descriptor: Optional[RowQbdReportDataRowRowDescriptor] = FieldInfo(alias="rowDescriptor", default=None)
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when
    QuickBooks Desktop does not provide one.
    """

    row_number: float = FieldInfo(alias="rowNumber")
    """The one-based row number from the report."""


class RowQbdReportSubtotalRowCell(BaseModel):
    column_id: str = FieldInfo(alias="columnId")
    """The column identifier for this cell.

    This matches a column's `columnId` and refers to the column's left-to-right
    position in the report.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """The value data type for this cell.

    If QuickBooks Desktop omits the cell data type, this uses the matching column's
    `dataType` when available.
    """

    value: Optional[str] = None
    """The cell value as a QuickBooks Desktop-formatted string.

    This is `null` if QuickBooks Desktop does not provide a value for the cell.
    """


class RowQbdReportSubtotalRowRowDescriptor(BaseModel):
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when QuickBooks Desktop does not provide one.
    """

    type: Optional[str] = None
    """The kind of row-level descriptor, such as `account`, `customer`, or `vendor`.

    This is `null` if QuickBooks Desktop does not provide one.
    """

    value: Optional[str] = None
    """The row-level descriptor value.

    This can differ from the first cell value and is `null` if QuickBooks Desktop
    does not provide one.
    """


class RowQbdReportSubtotalRow(BaseModel):
    cells: List[RowQbdReportSubtotalRowCell]
    """The cells in this report row.

    Report rows are sparse, so cells appear only for columns where QuickBooks
    Desktop returned a value.
    """

    kind: Literal["subtotal"]
    """The row kind. This value is always `"subtotal"`."""

    row_descriptor: Optional[RowQbdReportSubtotalRowRowDescriptor] = FieldInfo(alias="rowDescriptor", default=None)
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when
    QuickBooks Desktop does not provide one.
    """

    row_number: float = FieldInfo(alias="rowNumber")
    """The one-based row number from the report."""


class RowQbdReportTotalRowCell(BaseModel):
    column_id: str = FieldInfo(alias="columnId")
    """The column identifier for this cell.

    This matches a column's `columnId` and refers to the column's left-to-right
    position in the report.
    """

    data_type: Optional[str] = FieldInfo(alias="dataType", default=None)
    """The value data type for this cell.

    If QuickBooks Desktop omits the cell data type, this uses the matching column's
    `dataType` when available.
    """

    value: Optional[str] = None
    """The cell value as a QuickBooks Desktop-formatted string.

    This is `null` if QuickBooks Desktop does not provide a value for the cell.
    """


class RowQbdReportTotalRowRowDescriptor(BaseModel):
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when QuickBooks Desktop does not provide one.
    """

    type: Optional[str] = None
    """The kind of row-level descriptor, such as `account`, `customer`, or `vendor`.

    This is `null` if QuickBooks Desktop does not provide one.
    """

    value: Optional[str] = None
    """The row-level descriptor value.

    This can differ from the first cell value and is `null` if QuickBooks Desktop
    does not provide one.
    """


class RowQbdReportTotalRow(BaseModel):
    cells: List[RowQbdReportTotalRowCell]
    """The cells in this report row.

    Report rows are sparse, so cells appear only for columns where QuickBooks
    Desktop returned a value.
    """

    kind: Literal["total"]
    """The row kind. This value is always `"total"`."""

    row_descriptor: Optional[RowQbdReportTotalRowRowDescriptor] = FieldInfo(alias="rowDescriptor", default=None)
    """The row-level descriptor provided by QuickBooks Desktop.

    This is separate from the row's table values in `cells` and is `null` when
    QuickBooks Desktop does not provide one.
    """

    row_number: float = FieldInfo(alias="rowNumber")
    """The one-based row number from the report."""


Row: TypeAlias = Annotated[
    Union[RowQbdReportTextRow, RowQbdReportDataRow, RowQbdReportSubtotalRow, RowQbdReportTotalRow],
    PropertyInfo(discriminator="kind"),
]


class Report(BaseModel):
    basis: Optional[Literal["accrual", "cash", "none"]] = None
    """The accounting basis."""

    category: Literal[
        "general_summary",
        "general_detail",
        "aging",
        "budget_summary",
        "job",
        "time",
        "custom_detail",
        "custom_summary",
        "payroll_detail",
        "payroll_summary",
    ]
    """The report category."""

    column_count: Optional[float] = FieldInfo(alias="columnCount", default=None)
    """The number of columns in the report."""

    columns: List[Column]
    """The report columns, in display order.

    Use each column's `columnId` to match row cells to columns.
    """

    column_title_row_count: Optional[float] = FieldInfo(alias="columnTitleRowCount", default=None)
    """The number of title rows for the report columns."""

    object_type: Literal["qbd_report"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_report"`."""

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
        "ap_aging_detail",
        "ap_aging_summary",
        "ar_aging_detail",
        "ar_aging_summary",
        "collections_report",
        "balance_sheet_budget_overview",
        "balance_sheet_budget_vs_actual",
        "profit_and_loss_budget_overview",
        "profit_and_loss_budget_performance",
        "profit_and_loss_budget_vs_actual",
        "item_estimates_vs_actuals",
        "item_profitability",
        "job_estimates_vs_actuals_detail",
        "job_estimates_vs_actuals_summary",
        "job_profitability_detail",
        "job_profitability_summary",
        "time_by_item",
        "time_by_job_detail",
        "time_by_job_summary",
        "time_by_name",
        "custom_transaction_detail",
        "custom_summary",
        "employee_state_taxes_detail",
        "payroll_item_detail",
        "payroll_review_detail",
        "payroll_transaction_detail",
        "payroll_transactions_by_payee",
        "employee_earnings_summary",
        "payroll_liability_balances",
        "payroll_summary",
    ] = FieldInfo(alias="reportType")
    """The report type."""

    row_count: Optional[float] = FieldInfo(alias="rowCount", default=None)
    """The number of rows in the report."""

    rows: List[Row]
    """The report rows, in display order.

    Rows can be text rows, detail data rows, subtotal rows, or total rows.
    """

    subtitle: Optional[str] = None
    """The report subtitle."""

    title: Optional[str] = None
    """The report title."""
