# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_ids: Annotated[List[str], PropertyInfo(alias="accountIds")]
    """Filter for transactions associated with these accounts.

    **NOTE**: To filter on transaction lines, you must specify the
    `transactionDetailLevel` parameter as `all` or `transaction_lines_only`.
    """

    class_ids: Annotated[List[str], PropertyInfo(alias="classIds")]
    """Filter for transactions of these classes.

    A class is a way end-users can categorize transactions in QuickBooks.

    **NOTE**: To filter on transaction lines, you must specify the
    `transactionDetailLevel` parameter as `all` or `transaction_lines_only`.
    """

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for transactions in these currencies."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    detail_level: Annotated[
        Literal["all", "transaction_lines_only", "transactions_without_lines"], PropertyInfo(alias="detailLevel")
    ]
    """
    Specify whether to return all matching transaction and transaction-line objects
    (`all`), only transaction objects (`transactions_without_lines`, the default),
    or only transaction-line objects (`transaction_lines_only`.
    """

    entity_ids: Annotated[List[str], PropertyInfo(alias="entityIds")]
    """
    Filter for transactions associated with these entities (customers, vendors,
    employees, etc.).

    **NOTE**: To filter on transaction lines, you must specify the
    `transactionDetailLevel` parameter as `all` or `transaction_lines_only`.
    """

    ids: List[str]
    """
    Filter for specific transactions by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.

    **NOTE**: You cannot supply the ID of a time tracking activity to this request.
    If you do, you get an error stating that no such record could be found, even
    though the transaction is in QuickBooks. This limitation is enforced by
    QuickBooks.
    """

    item_ids: Annotated[List[str], PropertyInfo(alias="itemIds")]
    """Filter for transactions associated with these items.

    **NOTE**: To filter on transaction lines, you must specify the
    `transactionDetailLevel` parameter as `all` or `transaction_lines_only`.
    """

    limit: int
    """The maximum number of objects to return.

    Accepts values ranging from 1 to 150, defaults to 150. When used with
    cursor-based pagination, this parameter controls how many results are returned
    per page. To paginate through results, combine this with the `cursor` parameter.
    Each response will include a `nextCursor` value that can be passed to subsequent
    requests to retrieve the next page of results.
    """

    payment_status: Annotated[Literal["closed", "either", "open"], PropertyInfo(alias="paymentStatus")]
    """Filter for transactions that are open, closed, or either.

    Open transactions have a remaining balance, such as credits not fully applied or
    invoices not fully paid.
    """

    posting_status: Annotated[Literal["either", "non_posting", "posting"], PropertyInfo(alias="postingStatus")]
    """Filter for transactions that are posting, non-posting, or either.

    Posting status refers to whether QuickBooks records the transaction in an
    account register.
    """

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for transactions whose `refNumber` contains this substring.

    **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
    or `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for transactions whose `refNumber` ends with this substring.

    **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """Filter for transactions whose `refNumber` is greater than or equal to this
    value.

    If omitted, the range will begin with the first number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    ref_numbers: Annotated[List[str], PropertyInfo(alias="refNumbers")]
    """Filter for specific transactions by their ref-number(s), case-sensitive.

    In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
    changed by the QuickBooks user.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for transactions whose `refNumber` starts with this substring.

    **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """Filter for transactions whose `refNumber` is less than or equal to this value.

    If omitted, the range will end with the last number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for transactions whose `date` field is on or after this date, in ISO 8601
    format (YYYY-MM-DD).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for transactions whose `date` field is on or before this date, in ISO
    8601 format (YYYY-MM-DD).
    """

    transaction_type: Annotated[
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
        PropertyInfo(alias="transactionType"),
    ]
    """Filter for transactions by their type.

    You can specify one or more transaction types.

    **NOTE**: Filtering for time tracking activities is not supported by QuickBooks
    for this endpoint.
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for transactions updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for transactions updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.
    """
