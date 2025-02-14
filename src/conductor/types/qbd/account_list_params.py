# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_type: Annotated[
        Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ],
        PropertyInfo(alias="accountType"),
    ]
    """Filter for accounts of this type."""

    currency_ids: Annotated[List[str], PropertyInfo(alias="currencyIds")]
    """Filter for accounts in these currencies."""

    full_names: Annotated[List[str], PropertyInfo(alias="fullNames")]
    """Filter for specific accounts by their full-name(s), case-insensitive.

    Like `id`, `fullName` is a unique identifier for an account, formed by by
    combining the names of its parent objects with its own `name`, separated by
    colons. For example, if an account is under "Corporate" and has the `name`
    "Accounts-Payable", its `fullName` would be "Corporate:Accounts-Payable".

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    ids: List[str]
    """Filter for specific accounts by their QuickBooks-assigned unique identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.

    **NOTE**: If any of the values you specify in this parameter are not found, the
    request will fail.
    """

    limit: int
    """The maximum number of objects to return.

    **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
    accounts. This parameter will limit the response size, but you cannot fetch
    subsequent results using a cursor. For pagination, use the name-range parameters
    instead (e.g., `nameFrom=A&nameTo=B`).

    When this parameter is omitted, the endpoint returns all accounts without limit,
    unlike paginated endpoints which default to 150 records. This is acceptable
    because accounts typically have low record counts.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """Filter for accounts whose `name` contains this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
    `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for accounts whose `name` ends with this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameContains` or
    `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for accounts whose `name` is alphabetically greater than or equal to this
    value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """Filter for accounts whose `name` starts with this substring, case-insensitive.

    NOTE: If you use this parameter, you cannot also use `nameContains` or
    `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for accounts whose `name` is alphabetically less than or equal to this
    value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for accounts that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for accounts updated on or after this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for accounts updated on or before this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 23:59:59 of that day.
    """
