# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TimeTrackingActivityListParams"]


class TimeTrackingActivityListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    entity_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="entityIds")]
    """
    Filter for time tracking activities tracking the time of these employees,
    vendors, or persons on QuickBooks's "Other Names" list.
    """

    ids: SequenceNotStr[str]
    """
    Filter for specific time tracking activities by their QuickBooks-assigned unique
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

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for time tracking activities whose `date` field is on or after this date,
    in ISO 8601 format (YYYY-MM-DD).

    **NOTE:** QuickBooks Desktop interprets this date as the **start of the
    specified day** in the local timezone of the end-user's computer (e.g.,
    `2025-01-01` → `2025-01-01T00:00:00`).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for time tracking activities whose `date` field is on or before this
    date, in ISO 8601 format (YYYY-MM-DD).

    **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
    day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
    `2025-01-01T23:59:59`).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for time tracking activities updated on or after this date/time.

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
    """Filter for time tracking activities updated on or before this date/time.

    Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **end of the specified day** in the local timezone of the end-user's computer
      (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """
