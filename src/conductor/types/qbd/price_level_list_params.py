# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PriceLevelListParams"]


class PriceLevelListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for price levels in these currencies."""

    ids: List[str]
    """
    Filter for specific price levels by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    item_ids: Annotated[List[str], PropertyInfo(alias="itemIds")]
    """Filter for price levels containing these items."""

    limit: int
    """The maximum number of objects to return.

    **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
    price levels. This parameter will limit the response size, but you cannot fetch
    subsequent results using a cursor. For pagination, use the name-range parameters
    instead (e.g., `nameFrom=A&nameTo=B`).

    When this parameter is omitted, the endpoint returns all price levels without
    limit, unlike paginated endpoints which default to 150 records. This is
    acceptable because price levels typically have low record counts.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """Filter for price levels whose `name` contains this substring, case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for price levels whose `name` ends with this substring, case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for price levels whose `name` is alphabetically greater than or equal to
    this value.
    """

    names: List[str]
    """Filter for specific price levels by their name(s), case-insensitive.

    Like `id`, `name` is a unique identifier for a price level.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will return an error.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for price levels whose `name` starts with this substring,
    case-insensitive.

    **NOTE**: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for price levels whose `name` is alphabetically less than or equal to
    this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for price levels that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for price levels updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for price levels updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.
    """
