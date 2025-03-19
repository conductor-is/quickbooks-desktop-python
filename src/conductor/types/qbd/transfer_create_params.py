# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateParams"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[str]
    """The monetary amount of this transfer, represented as a decimal string."""

    source_account_id: Required[Annotated[str, PropertyInfo(alias="sourceAccountId")]]
    """The account from which money will be transferred."""

    target_account_id: Required[Annotated[str, PropertyInfo(alias="targetAccountId")]]
    """The account to which money will be transferred."""

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this transfer, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The transfer's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    memo: str
    """A memo or note for this transfer."""
