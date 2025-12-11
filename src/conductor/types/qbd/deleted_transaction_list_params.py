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
    """The ID of the End-User to receive this request."""

    deleted_after: Annotated[str, PropertyInfo(alias="deletedAfter")]
    """
    Filter for deleted transactions deleted on or after this date/time, within the
    last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **start of the specified day** in the local timezone of the end-user's
      computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """

    deleted_before: Annotated[str, PropertyInfo(alias="deletedBefore")]
    """
    Filter for deleted transactions deleted on or before this date/time, within the
    last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

    - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
      **end of the specified day** in the local timezone of the end-user's computer
      (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
    - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
      interprets the timestamp in the local timezone of the end-user's computer.
    - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
      interprets the timestamp using the specified timezone.
    """
