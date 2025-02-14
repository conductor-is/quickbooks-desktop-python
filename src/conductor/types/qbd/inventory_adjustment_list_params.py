# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryAdjustmentListParams"]


class InventoryAdjustmentListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_ids: Annotated[List[str], PropertyInfo(alias="accountIds")]
    """Filter for inventory adjustments associated with these accounts."""

    customer_ids: Annotated[List[str], PropertyInfo(alias="customerIds")]
    """Filter for inventory adjustments associated with these customers."""

    ids: List[str]
    """
    Filter for specific inventory adjustments by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    include_line_items: Annotated[bool, PropertyInfo(alias="includeLineItems")]
    """Whether to include line items in the response. Defaults to `true`."""

    item_ids: Annotated[List[str], PropertyInfo(alias="itemIds")]
    """Filter for inventory adjustments containing these inventory items."""

    limit: int
    """The maximum number of objects to return.

    **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
    inventory adjustments. This parameter will limit the response size, but you
    cannot fetch subsequent results using a cursor. For pagination, use the
    name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

    When this parameter is omitted, the endpoint returns all inventory adjustments
    without limit, unlike paginated endpoints which default to 150 records. This is
    acceptable because inventory adjustments typically have low record counts.
    """

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for inventory adjustments whose `refNumber` contains this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberStartsWith` or
    `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for inventory adjustments whose `refNumber` ends with this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """
    Filter for inventory adjustments whose `refNumber` is greater than or equal to
    this value. If omitted, the range will begin with the first number of the list.
    Uses a numerical comparison for values that contain only digits; otherwise, uses
    a lexicographical comparison.
    """

    ref_numbers: Annotated[List[str], PropertyInfo(alias="refNumbers")]
    """Filter for specific inventory adjustments by their ref-number(s),
    case-sensitive.

    In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
    changed by the QuickBooks user.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for inventory adjustments whose `refNumber` starts with this substring.

    NOTE: If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """
    Filter for inventory adjustments whose `refNumber` is less than or equal to this
    value. If omitted, the range will end with the last number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for inventory adjustments created on or after this date, in ISO 8601
    format (YYYY-MM-DD).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for inventory adjustments created on or before this date, in ISO 8601
    format (YYYY-MM-DD).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for inventory adjustments updated on or after this date and time, in ISO
    8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
    time is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for inventory adjustments updated on or before this date and time, in ISO
    8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
    time is assumed to be 23:59:59 of that day.
    """
