# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BillsToPayListParams"]


class BillsToPayListParams(TypedDict, total=False):
    vendor_id: Required[Annotated[str, PropertyInfo(alias="vendorId")]]
    """The vendor whose open bills and available credits should be returned."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    currency_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="currencyIds")]
    """Filter for open bills and available credits in these currencies."""

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """
    Filter the bill branch to open bills due on or before this date, in ISO 8601
    format (YYYY-MM-DD). If omitted, QuickBooks Desktop returns open bills from all
    due dates. Available credits can still be returned because credits do not have a
    due date.
    """

    payables_account_id: Annotated[str, PropertyInfo(alias="payablesAccountId")]
    """
    Filter for open bills and available credits assigned to this Accounts-Payable
    account. If omitted, QuickBooks Desktop uses the default A/P account configured
    in the company file.
    """
