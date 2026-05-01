# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaymentToDeposit", "Currency", "Customer"]


class Currency(BaseModel):
    """The payment to deposit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international values. For user-defined currencies, all values are editable.
    """

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class Customer(BaseModel):
    """The customer or customer-job associated with this payment to deposit."""

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class PaymentToDeposit(BaseModel):
    amount: str
    """
    The monetary amount of this received payment that is currently available to
    deposit, represented as a decimal string.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The monetary amount of this payment to deposit converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    currency: Optional[Currency] = None
    """The payment to deposit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international
    values. For user-defined currencies, all values are editable.
    """

    customer: Optional[Customer] = None
    """The customer or customer-job associated with this payment to deposit."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this payment to deposit's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    payment_transaction_id: str = FieldInfo(alias="paymentTransactionId")
    """The ID of the received payment that is available to deposit.

    Pass this value as `paymentTransactionId` when creating a deposit line.
    """

    payment_transaction_line_id: Optional[str] = FieldInfo(alias="paymentTransactionLineId", default=None)
    """The ID of the specific received-payment line that is available to deposit.

    If this value is not `null`, pass it as `paymentTransactionLineId` with
    `paymentTransactionId` when creating a deposit line.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this payment to deposit,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this payment to deposit, in ISO 8601 format (YYYY-MM-DD)."""

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
        "liability_adjustment",
        "paycheck",
        "payroll_liability_check",
        "purchase_order",
        "receive_payment",
        "sales_order",
        "sales_receipt",
        "sales_tax_payment_check",
        "transfer",
        "vendor_credit",
        "ytd_adjustment",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this payment to deposit."""
