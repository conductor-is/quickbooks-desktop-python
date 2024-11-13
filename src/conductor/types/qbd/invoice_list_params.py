# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_ids: Annotated[List[str], PropertyInfo(alias="accountIds")]
    """Filter for invoices from this account or accounts."""

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for invoices in this currency or currencies."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Retrieve this value from the `nextCursor` field in the
    previous response. If omitted, the API returns the first page of results.
    """

    customer_ids: Annotated[List[str], PropertyInfo(alias="customerIds")]
    """Filter for invoices from this customer or customers."""

    ids: List[str]
    """Filter for specific invoices by their QuickBooks-assigned unique identifier(s).

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    include_line_items: Annotated[bool, PropertyInfo(alias="includeLineItems")]
    """Whether to include line items in the response."""

    include_linked_transactions: Annotated[bool, PropertyInfo(alias="includeLinkedTransactions")]
    """Whether to include linked transactions in the response.

    For example, a payment linked to the corresponding invoice.
    """

    limit: int
    """The maximum number of objects to return.

    Ranging from 1 to 150, defaults to 150. Use this parameter in conjunction with
    the `cursor` parameter to paginate through results. The response will include a
    `nextCursor` field, which can be used as the `cursor` parameter value in
    subsequent requests to fetch the next set of results.
    """

    payment_status: Annotated[Literal["all", "paid", "not_paid"], PropertyInfo(alias="paymentStatus")]
    """Filter for invoices that are paid, not paid, or both."""

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for invoices whose `refNumber` contains this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberStartsWith` or
    `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for invoices whose `refNumber` ends with this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """Filter for invoices whose `refNumber` is greater than or equal to this value.

    If omitted, the range will begin with the first number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    ref_numbers: Annotated[List[str], PropertyInfo(alias="refNumbers")]
    """Filter for specific invoices by their ref-number(s), case-sensitive.

    In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
    changed by the QuickBooks user.

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for invoices whose `refNumber` starts with this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """Filter for invoices whose `refNumber` is less than or equal to this value.

    If omitted, the range will end with the last number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for invoices created on or after this date, in ISO 8601 format
    (YYYY-MM-DD).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for invoices created on or before this date, in ISO 8601 format
    (YYYY-MM-DD).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for invoices updated on or after this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for invoices updated on or before this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 23:59:59 of that day.
    """
