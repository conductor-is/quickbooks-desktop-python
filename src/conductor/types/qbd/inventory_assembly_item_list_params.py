# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryAssemblyItemListParams"]


class InventoryAssemblyItemListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_ids: Annotated[List[str], PropertyInfo(alias="classIds")]
    """Filter for inventory assembly items of these classes.

    A class is a way end-users can categorize inventory assembly items in
    QuickBooks.
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    full_names: Annotated[List[str], PropertyInfo(alias="fullNames")]
    """
    Filter for specific inventory assembly items by their full-name(s),
    case-insensitive. Like `id`, `fullName` is a unique identifier for an inventory
    assembly item, formed by by combining the names of its parent objects with its
    own `name`, separated by colons. For example, if an inventory assembly item is
    under "Assemblies" and has the `name` "Deluxe Kit", its `fullName` would be
    "Assemblies:Deluxe Kit".

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    ids: List[str]
    """
    Filter for specific inventory assembly items by their QuickBooks-assigned unique
    identifier(s).

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
    """
    Filter for inventory assembly items whose `name` contains this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for inventory assembly items whose `name` ends with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for inventory assembly items whose `name` is alphabetically greater than
    or equal to this value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for inventory assembly items whose `name` starts with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for inventory assembly items whose `name` is alphabetically less than or
    equal to this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for inventory assembly items that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for inventory assembly items updated on or after this date and time, in
    ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
    the time is assumed to be 00:00:00 of that day.

    **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedAfter`
    parameter may not correctly filter inventory assembly items by their updated
    dates. To accurately retrieve the desired inventory assembly items, we recommend
    avoiding this parameter and instead fetching a broader dataset, then filtering
    the results locally using the `updatedAt` property.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for inventory assembly items updated on or before this date and time, in
    ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
    the time is assumed to be 23:59:59 of that day.

    **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedBefore`
    parameter may not correctly filter inventory assembly items by their updated
    dates. To accurately retrieve the desired inventory assembly items, we recommend
    avoiding this parameter and instead fetching a broader dataset, then filtering
    the results locally using the `updatedAt` property.
    """
