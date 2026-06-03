# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillCheckPaymentCreateParams", "ApplyToTransaction", "ApplyToTransactionApplyCredit"]


class BillCheckPaymentCreateParams(TypedDict, total=False):
    apply_to_transactions: Required[Annotated[Iterable[ApplyToTransaction], PropertyInfo(alias="applyToTransactions")]]
    """The bills to be paid by this bill check payment.

    This will create a link between this bill check payment and the specified bills.

    **IMPORTANT**: In each `applyToTransactions` object, you must specify either
    `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
    if none of these are specified, you will receive an error for an empty
    transaction.

    **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
    will report this object as "cannot be found".
    """

    bank_account_id: Required[Annotated[str, PropertyInfo(alias="bankAccountId")]]
    """
    The bank account from which the funds are being drawn for this bill check
    payment; e.g., Checking or Savings. This bill check payment will decrease the
    balance of this account.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this bill check payment, in ISO 8601 format (YYYY-MM-DD)."""

    vendor_id: Required[Annotated[str, PropertyInfo(alias="vendorId")]]
    """
    The vendor who sent the bill(s) that this bill check payment is paying and who
    will receive this payment.

    **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
    `applyToTransactions`; otherwise, QuickBooks will say the `transactionId` in
    `applyToTransactions` "does not exist".
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this bill check payment's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this bill check payment is included in the queue of documents
    for QuickBooks to print.
    """

    memo: str
    """A memo or note for this bill check payment."""

    payables_account_id: Annotated[str, PropertyInfo(alias="payablesAccountId")]
    """
    The Accounts-Payable (A/P) account to which this bill check payment is assigned,
    used for accounts-payable tracking. If omitted, QuickBooks Desktop uses the
    default A/P account configured in the company file.

    **IMPORTANT**: If this bill check payment is linked to other transactions, this
    A/P account must match the `payablesAccount` used in those other transactions.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this bill check payment,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).

    **IMPORTANT**: For checks, this field is the check number.

    Maximum length: 11 characters.
    """


class ApplyToTransactionApplyCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """
    The amount of the selected credit transaction to apply to this transaction,
    represented as a decimal string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """

    credit_transaction_id: Required[Annotated[str, PropertyInfo(alias="creditTransactionId")]]
    """
    The unique identifier of the credit transaction to apply to this transaction,
    such as a credit memo, vendor credit, or journal-entry credit.
    """

    override_credit_application: Annotated[bool, PropertyInfo(alias="overrideCreditApplication")]
    """Indicates whether to override the credit."""


class ApplyToTransaction(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the target transaction to which this payment is applied."""

    apply_credits: Annotated[Iterable[ApplyToTransactionApplyCredit], PropertyInfo(alias="applyCredits")]
    """Credits to apply to this target transaction, reducing its balance.

    This creates a link between this target transaction and the specified credit
    transactions.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transactions in this endpoint's response even when this request is
    successful. To see the transactions linked via this field, refetch the target
    transaction and check the `linkedTransactions` response field. If fetching a
    list of target transactions, you must also specify the parameter
    `includeLinkedTransactions=true` to see the `linkedTransactions` response field.
    """

    discount_account_id: Annotated[str, PropertyInfo(alias="discountAccountId")]
    """The financial account used to track this target transaction's discount."""

    discount_amount: Annotated[str, PropertyInfo(alias="discountAmount")]
    """
    The monetary amount by which to reduce this target transaction's balance,
    represented as a decimal string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """

    discount_class_id: Annotated[str, PropertyInfo(alias="discountClassId")]
    """The class used to track this target transaction's discount."""

    payment_amount: Annotated[str, PropertyInfo(alias="paymentAmount")]
    """
    The monetary amount to apply to the target transaction, represented as a decimal
    string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """
