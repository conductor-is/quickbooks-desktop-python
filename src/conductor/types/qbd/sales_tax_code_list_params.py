# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxCodeListParams"]


class SalesTaxCodeListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    ids: List[str]
    """
    Filter for specific sales-tax codes by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    limit: int
    """The maximum number of objects to return.

    **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
    sales-tax codes. This parameter will limit the response size, but you cannot
    fetch subsequent results using a cursor. For pagination, use the name-range
    parameters instead (e.g., `nameFrom=A&nameTo=B`).

    When this parameter is omitted, the endpoint returns all sales-tax codes without
    limit, unlike paginated endpoints which default to 150 records. This is
    acceptable because sales-tax codes typically have low record counts.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """
    Filter for sales-tax codes whose `name` contains this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for sales-tax codes whose `name` ends with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for sales-tax codes whose `name` is alphabetically greater than or equal
    to this value.
    """

    names: List[str]
    """Filter for specific sales-tax codes by their name(s), case-insensitive.

    Like `id`, `name` is a unique identifier for a sales-tax code.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for sales-tax codes whose `name` starts with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for sales-tax codes whose `name` is alphabetically less than or equal to
    this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for sales-tax codes that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for sales-tax codes updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for sales-tax codes updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.
    """
