# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["VendorListParams"]


class VendorListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    class_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="classIds")]
    """Filter for vendors of these classes.

    A class is a way end-users can categorize vendors in QuickBooks.
    """

    currency_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="currencyIds")]
    """Filter for vendors in these currencies."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    ids: SequenceNotStr[str]
    """Filter for specific vendors by their QuickBooks-assigned unique identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    limit: int
    """The maximum number of objects to return.

    Accepts values ranging from 1 to 150, defaults to 150. When used with
    cursor-based pagination, this parameter controls how many results are returned
    per page. To paginate through results, combine this with the `cursor` parameter.
    Each response will include a `nextCursor` value that can be passed to subsequent
    requests to retrieve the next page of results.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """Filter for vendors whose `name` contains this substring, case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for vendors whose `name` ends with this substring, case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for vendors whose `name` is alphabetically greater than or equal to this
    value.
    """

    names: SequenceNotStr[str]
    """Filter for specific vendors by their name(s), case-insensitive.

    Like `id`, `name` is a unique identifier for a vendor.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """Filter for vendors whose `name` starts with this substring, case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for vendors whose `name` is alphabetically less than or equal to this
    value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for vendors that are active, inactive, or both."""

    total_balance: Annotated[str, PropertyInfo(alias="totalBalance")]
    """
    Filter for vendors whose `totalBalance` equals this amount, represented as a
    decimal string. You can only use one total-balance filter at a time.
    """

    total_balance_greater_than: Annotated[str, PropertyInfo(alias="totalBalanceGreaterThan")]
    """
    Filter for vendors whose `totalBalance` is greater than this amount, represented
    as a decimal string. You can only use one total-balance filter at a time.
    """

    total_balance_greater_than_or_equal_to: Annotated[str, PropertyInfo(alias="totalBalanceGreaterThanOrEqualTo")]
    """
    Filter for vendors whose `totalBalance` is greater than or equal to this amount,
    represented as a decimal string. You can only use one total-balance filter at a
    time.
    """

    total_balance_less_than: Annotated[str, PropertyInfo(alias="totalBalanceLessThan")]
    """
    Filter for vendors whose `totalBalance` is less than this amount, represented as
    a decimal string. You can only use one total-balance filter at a time.
    """

    total_balance_less_than_or_equal_to: Annotated[str, PropertyInfo(alias="totalBalanceLessThanOrEqualTo")]
    """
    Filter for vendors whose `totalBalance` is less than or equal to this amount,
    represented as a decimal string. You can only use one total-balance filter at a
    time.
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for vendors updated on or after this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **start of the specified day** in the local timezone of the end-user's
      computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """Filter for vendors updated on or before this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **end of the specified day** in the local timezone of the end-user's computer
      (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """
