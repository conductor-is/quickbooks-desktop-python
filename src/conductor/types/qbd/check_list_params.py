# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CheckListParams"]


class CheckListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_ids: Annotated[List[str], PropertyInfo(alias="accountIds")]
    """Filter for checks associated with these accounts."""

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for checks in these currencies."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    ids: List[str]
    """Filter for specific checks by their QuickBooks-assigned unique identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    include_line_items: Annotated[bool, PropertyInfo(alias="includeLineItems")]
    """Whether to include line items in the response. Defaults to `true`."""

    include_linked_transactions: Annotated[bool, PropertyInfo(alias="includeLinkedTransactions")]
    """Whether to include linked transactions in the response.

    Defaults to `false`. For example, a payment linked to the corresponding check.
    """

    limit: int
    """The maximum number of objects to return.

    Accepts values ranging from 1 to 150, defaults to 150. When used with
    cursor-based pagination, this parameter controls how many results are returned
    per page. To paginate through results, combine this with the `cursor` parameter.
    Each response will include a `nextCursor` value that can be passed to subsequent
    requests to retrieve the next page of results.
    """

    payee_ids: Annotated[List[str], PropertyInfo(alias="payeeIds")]
    """Filter for checks addressed to these payees.

    These are the people or companies who will receive these checks.
    """

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for checks whose `refNumber` contains this substring.

    (For checks, this field is the check number.)

    **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
    or `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for checks whose `refNumber` ends with this substring.

    (For checks, this field is the check number.)

    **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """Filter for checks whose `refNumber` is greater than or equal to this value.

    (For checks, this field is the check number.) If omitted, the range will begin
    with the first number of the list. Uses a numerical comparison for values that
    contain only digits; otherwise, uses a lexicographical comparison.
    """

    ref_numbers: Annotated[List[str], PropertyInfo(alias="refNumbers")]
    """Filter for specific checks by their ref-number(s), case-sensitive.

    In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
    changed by the QuickBooks user.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for checks whose `refNumber` starts with this substring.

    (For checks, this field is the check number.)

    **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """Filter for checks whose `refNumber` is less than or equal to this value.

    (For checks, this field is the check number.) If omitted, the range will end
    with the last number of the list. Uses a numerical comparison for values that
    contain only digits; otherwise, uses a lexicographical comparison.
    """

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for checks whose `date` field is on or after this date, in ISO 8601
    format (YYYY-MM-DD).

    **NOTE**: QuickBooks Desktop interprets date-only values in the local timezone
    of the end-user's computer (i.e., midnight in that timezone).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for checks whose `date` field is on or before this date, in ISO 8601
    format (YYYY-MM-DD).

    **NOTE**: QuickBooks Desktop interprets date-only values in the local timezone
    of the end-user's computer (i.e., midnight in that timezone).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for checks updated on or after this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets this as midnight in
      the local timezone of the end-user's computer.
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop uses
      the local timezone of the end-user's computer to interpret the timestamp.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      uses this timezone to interpret the timestamp.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """Filter for checks updated on or before this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets this as midnight in
      the local timezone of the end-user's computer.
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop uses
      the local timezone of the end-user's computer to interpret the timestamp.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      uses this timezone to interpret the timestamp.
    """
