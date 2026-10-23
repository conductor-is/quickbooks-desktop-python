# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CustomerTypeListParams"]


class CustomerTypeListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    full_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="fullNames")]
    """Filter for specific customer types by their full-name(s), case-insensitive.

    Like `id`, `fullName` is a unique identifier for a customer type, formed by by
    combining the names of its parent objects with its own `name`, separated by
    colons. For example, if a customer type is under "Industry" and has the `name`
    "Healthcare", its `fullName` would be "Industry:Healthcare".

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    ids: SequenceNotStr[str]
    """
    Filter for specific customer types by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    limit: int
    """The maximum number of objects to return.

    **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
    customer types, so this parameter only limits the response size. To page through
    customer types by name, see
    [Paging by name](https://docs.conductor.is/api-ref/pagination#paging-by-name).

    When this parameter is omitted, the endpoint returns all customer types without
    limit, unlike paginated endpoints which default to 150 records.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """
    Filter for customer types whose `name` contains this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for customer types whose `name` ends with this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for customer types whose `fullName` sorts at or after this value
    (inclusive), compared case-insensitively in QuickBooks' sort order: punctuation
    first, then digits, then letters.

    When you set `nameFrom` or `nameTo`, QuickBooks returns customer types sorted by
    `fullName` in that order; without either, the order is not guaranteed. To page
    through customer types by name, see
    [Paging by name](https://docs.conductor.is/api-ref/pagination#paging-by-name).

    **NOTE**: If you use this parameter, you cannot also use `nameContains`,
    `nameStartsWith`, or `nameEndsWith`.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for customer types whose `name` starts with this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for customer types whose `fullName` sorts at or before this value
    (inclusive), compared case-insensitively in QuickBooks' sort order: punctuation
    first, then digits, then letters. If you also set `nameFrom`, it must not sort
    after this value, or QuickBooks returns an error.

    When you set `nameFrom` or `nameTo`, QuickBooks returns customer types sorted by
    `fullName` in that order; without either, the order is not guaranteed.

    **NOTE**: If you use this parameter, you cannot also use `nameContains`,
    `nameStartsWith`, or `nameEndsWith`.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for customer types that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for customer types updated on or after this date/time.

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
    """Filter for customer types updated on or before this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **end of the specified day** in the local timezone of the end-user's computer
      (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """
