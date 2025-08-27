# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferListParams"]


class TransferListParams(TypedDict, total=False):
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

    ids: List[str]
    """Filter for specific transfers by their QuickBooks-assigned unique identifier(s).

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
    Filter for transfers whose `date` field is on or after this date, in ISO 8601
    format (YYYY-MM-DD). QuickBooks Desktop interprets this date-only value in the
    host machine’s local timezone; i.e., midnight in the timezone of the end-user's
    computer running QuickBooks Desktop.
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for transfers whose `date` field is on or before this date, in ISO 8601
    format (YYYY-MM-DD). QuickBooks Desktop interprets this date-only value in the
    host machine’s local timezone; i.e., midnight in the timezone of the end-user's
    computer running QuickBooks Desktop.
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """Filter for transfers updated on or after this date/time.

    Format: ISO 8601. Accepts date-only (YYYY-MM-DD), datetime without timezone
    (YYYY-MM-DDTHH:mm:ss), or datetime with timezone (YYYY-MM-DDTHH:mm:ss±HH:mm).
    Date-only and timezone-less datetimes are passed through for QuickBooks Desktop
    to interpret in the host machine’s local timezone. If the datetime includes a
    timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
    interpret the timestamp.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """Filter for transfers updated on or before this date/time.

    Format: ISO 8601. Accepts date-only (YYYY-MM-DD), datetime without timezone
    (YYYY-MM-DDTHH:mm:ss), or datetime with timezone (YYYY-MM-DDTHH:mm:ss±HH:mm).
    Date-only and timezone-less datetimes are passed through for QuickBooks Desktop
    to interpret in the host machine’s local timezone. If the datetime includes a
    timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
    interpret the timestamp.
    """
