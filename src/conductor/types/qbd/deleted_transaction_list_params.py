# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeletedTransactionListParams"]


class DeletedTransactionListParams(TypedDict, total=False):
    transaction_types: Required[
        Annotated[
            List[
                Literal[
                    "ar_refund_credit_card",
                    "bill",
                    "bill_payment_check",
                    "bill_payment_credit_card",
                    "build_assembly",
                    "charge",
                    "check",
                    "credit_card_charge",
                    "credit_card_credit",
                    "credit_memo",
                    "deposit",
                    "estimate",
                    "inventory_adjustment",
                    "invoice",
                    "item_receipt",
                    "journal_entry",
                    "purchase_order",
                    "receive_payment",
                    "sales_order",
                    "sales_receipt",
                    "sales_tax_payment_check",
                    "time_tracking",
                    "transfer_inventory",
                    "vehicle_mileage",
                    "vendor_credit",
                ]
            ],
            PropertyInfo(alias="transactionTypes"),
        ]
    ]
    """Filter for deleted transactions by their transaction type(s)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    deleted_after: Annotated[str, PropertyInfo(alias="deletedAfter")]
    """
    Filter for deleted transactions deleted on or after this date/time, within the
    last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets this as midnight in
      the host machine’s local timezone.
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop uses
      the host machine’s local timezone to interpret the timestamp.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      uses this timezone to interpret the timestamp.
    """

    deleted_before: Annotated[str, PropertyInfo(alias="deletedBefore")]
    """
    Filter for deleted transactions deleted on or before this date/time, within the
    last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets this as midnight in
      the host machine’s local timezone.
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop uses
      the host machine’s local timezone to interpret the timestamp.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      uses this timezone to interpret the timestamp.
    """
