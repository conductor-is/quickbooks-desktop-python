# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeletedTransactionListParams"]


class DeletedTransactionListParams(TypedDict, total=False):
    transaction_type: Required[
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
            PropertyInfo(alias="transactionType"),
        ]
    ]
    """Filter for deleted transactions by their transaction type.

    You can specify one or more types.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    deleted_after: Annotated[str, PropertyInfo(alias="deletedAfter")]
    """
    Filter for deleted transactions deleted on or after this date and time, within
    the last 90 days (QuickBooks limit), in ISO 8601 format (YYYY-MM-DDTHH:mm:ss).
    If you only provide a date (YYYY-MM-DD), the time is assumed to be 00:00:00 of
    that day.
    """

    deleted_before: Annotated[str, PropertyInfo(alias="deletedBefore")]
    """
    Filter for deleted transactions deleted on or before this date and time, within
    the last 90 days (QuickBooks limit), in ISO 8601 format (YYYY-MM-DDTHH:mm:ss).
    If you only provide a date (YYYY-MM-DD), the time is assumed to be 23:59:59 of
    that day.
    """
