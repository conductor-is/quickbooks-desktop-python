# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_ids: Annotated[List[str], PropertyInfo(alias="classIds")]
    """Filter for customers of these classes.

    A class is a way end-users can categorize customers in QuickBooks.
    """

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for customers in these currencies."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    full_names: Annotated[List[str], PropertyInfo(alias="fullNames")]
    """Filter for specific customers by their full-name(s), case-insensitive.

    Like `id`, `fullName` is a unique identifier for a customer, formed by by
    combining the names of its parent objects with its own `name`, separated by
    colons. For example, if a customer is under "ABC Corporation" and has the `name`
    "Website Redesign Project", its `fullName` would be "ABC Corporation:Website
    Redesign Project".

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    ids: List[str]
    """Filter for specific customers by their QuickBooks-assigned unique identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
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
    """Filter for customers whose `name` contains this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for customers whose `name` ends with this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for customers whose `name` is alphabetically greater than or equal to
    this value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """Filter for customers whose `name` starts with this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for customers whose `name` is alphabetically less than or equal to this
    value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for customers that are active, inactive, or both."""

    total_balance: Annotated[str, PropertyInfo(alias="totalBalance")]
    """
    Filter for customers whose `totalBalance` equals this amount, represented as a
    decimal string. You can only use one total-balance filter at a time.
    """

    total_balance_greater_than: Annotated[str, PropertyInfo(alias="totalBalanceGreaterThan")]
    """
    Filter for customers whose `totalBalance` is greater than this amount,
    represented as a decimal string. You can only use one total-balance filter at a
    time.
    """

    total_balance_greater_than_or_equal_to: Annotated[str, PropertyInfo(alias="totalBalanceGreaterThanOrEqualTo")]
    """
    Filter for customers whose `totalBalance` is greater than or equal to this
    amount, represented as a decimal string. You can only use one total-balance
    filter at a time.
    """

    total_balance_less_than: Annotated[str, PropertyInfo(alias="totalBalanceLessThan")]
    """
    Filter for customers whose `totalBalance` is less than this amount, represented
    as a decimal string. You can only use one total-balance filter at a time.
    """

    total_balance_less_than_or_equal_to: Annotated[str, PropertyInfo(alias="totalBalanceLessThanOrEqualTo")]
    """
    Filter for customers whose `totalBalance` is less than or equal to this amount,
    represented as a decimal string. You can only use one total-balance filter at a
    time.
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for customers updated on or after this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for customers updated on or before this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 23:59:59 of that day.
    """
