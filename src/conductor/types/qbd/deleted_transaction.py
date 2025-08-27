# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeletedTransaction"]


class DeletedTransaction(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this deleted transaction.

    This ID is unique across all transaction types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this deleted transaction was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    deleted_at: str = FieldInfo(alias="deletedAt")
    """
    The date and time when this deleted transaction was deleted, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    object_type: Literal["qbd_deleted_transaction"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deleted_transaction"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this deleted transaction,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_type: Literal[
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
    ] = FieldInfo(alias="transactionType")
    """The type of deleted transaction."""
