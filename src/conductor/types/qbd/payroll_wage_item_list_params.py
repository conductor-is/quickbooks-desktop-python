# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PayrollWageItemListParams"]


class PayrollWageItemListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.

    **IMPORTANT**: The cursor is the same value for every page, and requests that
    send it are not idempotent: each one returns the next page. Send each request
    within 10 seconds of the previous response. If you miss that window or a request
    fails, start over without a cursor. To make a run resumable, see
    [Paging by name](https://docs.conductor.is/api-ref/pagination#paging-by-name).
    """

    ids: SequenceNotStr[str]
    """
    Filter for specific payroll wage items by their QuickBooks-assigned unique
    identifier(s).

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
    """
    Filter for payroll wage items whose `name` contains this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for payroll wage items whose `name` ends with this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for payroll wage items whose `name` sorts at or after this value
    (inclusive), compared case-insensitively in QuickBooks' sort order: punctuation
    first, then digits, then letters.

    When you set `nameFrom` or `nameTo`, QuickBooks returns payroll wage items
    sorted by `name` in that order; without either, the order is not guaranteed. To
    page through payroll wage items by name, see
    [Paging by name](https://docs.conductor.is/api-ref/pagination#paging-by-name).

    **NOTE**: If you use this parameter, you cannot also use `nameContains`,
    `nameStartsWith`, or `nameEndsWith`.
    """

    names: SequenceNotStr[str]
    """Filter for specific payroll wage items by their name(s), case-insensitive.

    Like `id`, `name` is a unique identifier for a payroll wage item.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for payroll wage items whose `name` starts with this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for payroll wage items whose `name` sorts at or before this value
    (inclusive), compared case-insensitively in QuickBooks' sort order: punctuation
    first, then digits, then letters. If you also set `nameFrom`, it must not sort
    after this value, or QuickBooks returns an error.

    When you set `nameFrom` or `nameTo`, QuickBooks returns payroll wage items
    sorted by `name` in that order; without either, the order is not guaranteed.

    **NOTE**: If you use this parameter, you cannot also use `nameContains`,
    `nameStartsWith`, or `nameEndsWith`.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for payroll wage items that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for payroll wage items updated on or after this date/time.

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
    """Filter for payroll wage items updated on or before this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **end of the specified day** in the local timezone of the end-user's computer
      (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """
