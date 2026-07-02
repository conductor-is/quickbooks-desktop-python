# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BillToPay",
    "Bill",
    "BillCurrency",
    "BillPayablesAccount",
    "Credit",
    "CreditCurrency",
    "CreditPayablesAccount",
]


class BillCurrency(BaseModel):
    """The payable bill's currency.

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


class BillPayablesAccount(BaseModel):
    """
    The Accounts-Payable (A/P) account to which this payable bill is assigned, used for accounts-payable tracking.

    **IMPORTANT**: If this payable bill is linked to other transactions, this A/P account must match the `payablesAccount` used in those other transactions.
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


class Bill(BaseModel):
    """
    The open bill with a positive amount due that can be paid for the requested vendor. In each bills-to-pay result, either `bill` is an object and `credit` is `null`, or `credit` is an object and `bill` is `null`.
    """

    amount_due: str = FieldInfo(alias="amountDue")
    """
    The amount QuickBooks Desktop reports as due and available to pay for this open
    bill, represented as a decimal string. Use this value as the candidate
    `applyToTransactions[].paymentAmount` when creating a bill payment; reduce the
    payment by any credits you apply.
    """

    amount_due_in_home_currency: Optional[str] = FieldInfo(alias="amountDueInHomeCurrency", default=None)
    """
    The monetary amount due for this payable bill converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    bill_id: str = FieldInfo(alias="billId")
    """The ID of the open bill available to pay.

    Pass this value as `transactionId` in a bill-payment `applyToTransactions`
    entry.
    """

    currency: Optional[BillCurrency] = None
    """The payable bill's currency.

    For built-in currencies, the name and code are standard ISO 4217 international
    values. For user-defined currencies, all values are editable.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """
    The date by which this payable bill must be paid, in ISO 8601 format
    (YYYY-MM-DD).
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this payable bill's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    payables_account: BillPayablesAccount = FieldInfo(alias="payablesAccount")
    """
    The Accounts-Payable (A/P) account to which this payable bill is assigned, used
    for accounts-payable tracking.

    **IMPORTANT**: If this payable bill is linked to other transactions, this A/P
    account must match the `payablesAccount` used in those other transactions.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this payable bill, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this payable bill, in ISO 8601 format (YYYY-MM-DD)."""

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
        "unknown",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this payable bill."""


class CreditCurrency(BaseModel):
    """The applicable credit's currency.

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


class CreditPayablesAccount(BaseModel):
    """
    The Accounts-Payable (A/P) account to which this applicable credit is assigned, used for accounts-payable tracking.

    **IMPORTANT**: If this applicable credit is linked to other transactions, this A/P account must match the `payablesAccount` used in those other transactions.
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


class Credit(BaseModel):
    """
    The vendor credit linked to the requested vendor that can be applied to open bills. In each bills-to-pay result, either `credit` is an object and `bill` is `null`, or `bill` is an object and `credit` is `null`.
    """

    credit_remaining: str = FieldInfo(alias="creditRemaining")
    """
    The remaining vendor credit available to apply to open bills, represented as a
    decimal string. When applying this credit to a bill-payment request, choose an
    `applyToTransactions[].applyCredits[].appliedAmount` that does not exceed this
    value or the target bill's remaining amount due.
    """

    credit_remaining_in_home_currency: Optional[str] = FieldInfo(alias="creditRemainingInHomeCurrency", default=None)
    """
    The remaining balance of this applicable credit converted to the home currency
    of the QuickBooks company file. Represented as a decimal string.
    """

    credit_transaction_id: str = FieldInfo(alias="creditTransactionId")
    """The ID of the credit transaction available to apply to the vendor's open bills.

    To apply this credit in a bill-payment request, place it under the target bill's
    `applyToTransactions[].applyCredits[]` entry and pass this value as
    `creditTransactionId`.
    """

    currency: Optional[CreditCurrency] = None
    """The applicable credit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international
    values. For user-defined currencies, all values are editable.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this applicable credit's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    payables_account: CreditPayablesAccount = FieldInfo(alias="payablesAccount")
    """
    The Accounts-Payable (A/P) account to which this applicable credit is assigned,
    used for accounts-payable tracking.

    **IMPORTANT**: If this applicable credit is linked to other transactions, this
    A/P account must match the `payablesAccount` used in those other transactions.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this applicable credit,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this applicable credit, in ISO 8601 format (YYYY-MM-DD)."""

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
        "unknown",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this applicable credit."""


class BillToPay(BaseModel):
    bill: Optional[Bill] = None
    """
    The open bill with a positive amount due that can be paid for the requested
    vendor. In each bills-to-pay result, either `bill` is an object and `credit` is
    `null`, or `credit` is an object and `bill` is `null`.
    """

    credit: Optional[Credit] = None
    """
    The vendor credit linked to the requested vendor that can be applied to open
    bills. In each bills-to-pay result, either `credit` is an object and `bill` is
    `null`, or `bill` is an object and `credit` is `null`.
    """
