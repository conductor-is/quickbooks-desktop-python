# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimeTrackingActivityListParams"]


class TimeTrackingActivityListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Do not include this parameter on the first call. Use the
    `nextCursor` value returned in the previous response to request subsequent
    results.
    """

    entity_ids: Annotated[List[str], PropertyInfo(alias="entityIds")]
    """
    Filter for time tracking activities tracking the time of these employees,
    vendors, or persons on QuickBooks's "Other Names" list.
    """

    ids: List[str]
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
    in ISO 8601 format (YYYY-MM-DD). **NOTE**: QuickBooks Desktop interprets
    date-only values in the QuickBooks Desktop host machine’s local timezone (i.e.,
    midnight in that timezone).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for time tracking activities whose `date` field is on or before this
    date, in ISO 8601 format (YYYY-MM-DD). **NOTE**: QuickBooks Desktop interprets
    date-only values in the QuickBooks Desktop host machine’s local timezone (i.e.,
    midnight in that timezone).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for time tracking activities updated on or after this date/time.

    Format: ISO 8601. Accepts date-only (YYYY-MM-DD), datetime without timezone
    (YYYY-MM-DDTHH:mm:ss), or datetime with timezone (YYYY-MM-DDTHH:mm:ss±HH:mm).
    **NOTE**: Date-only and timezone-less datetimes are passed through for
    QuickBooks Desktop to interpret in the QuickBooks Desktop host machine’s local
    timezone. If the datetime includes a timezone (e.g., `+05:30` or `Z`),
    QuickBooks Desktop uses that timezone to interpret the timestamp.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """Filter for time tracking activities updated on or before this date/time.

    Format: ISO 8601. Accepts date-only (YYYY-MM-DD), datetime without timezone
    (YYYY-MM-DDTHH:mm:ss), or datetime with timezone (YYYY-MM-DDTHH:mm:ss±HH:mm).
    **NOTE**: Date-only and timezone-less datetimes are passed through for
    QuickBooks Desktop to interpret in the QuickBooks Desktop host machine’s local
    timezone. If the datetime includes a timezone (e.g., `+05:30` or `Z`),
    QuickBooks Desktop uses that timezone to interpret the timestamp.
    """
