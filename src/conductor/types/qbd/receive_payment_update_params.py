# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ReceivePaymentUpdateParams",
    "ApplyToTransaction",
    "ApplyToTransactionApplyCredit",
    "CreditCardTransaction",
    "CreditCardTransactionRequest",
    "CreditCardTransactionResponse",
]


class ReceivePaymentUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the receive-payment object
    you are updating, which you can get by fetching the object first. Provide the
    most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    apply_to_transactions: Annotated[Iterable[ApplyToTransaction], PropertyInfo(alias="applyToTransactions")]
    """The invoices to be paid by this receive-payment.

    This will create a link between this receive-payment and the specified invoices.

    **IMPORTANT**: In each `applyToTransactions` object, you must specify either
    `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
    if none of these are specified, you will receive an error for an empty
    transaction.

    **IMPORTANT**: The target invoice must have `isPaid=false`, otherwise,
    QuickBooks will report this object as "cannot be found".
    """

    credit_card_transaction: Annotated[CreditCardTransaction, PropertyInfo(alias="creditCardTransaction")]
    """
    The credit card transaction data for this receive-payment's payment when using
    QuickBooks Merchant Services (QBMS). If specifying this field, you must also
    specify the `paymentMethod` field.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """
    The customer or customer-job to which the payment for this receive-payment is
    credited.
    """

    deposit_to_account_id: Annotated[str, PropertyInfo(alias="depositToAccountId")]
    """
    The account where the funds for this receive-payment will be or have been
    deposited.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this receive-payment's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    memo: str
    """
    A memo or note for this receive-payment that will be displayed at the beginning
    of reports containing details about this receive-payment.
    """

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """The receive-payment's payment method (e.g., cash, check, credit card)."""

    receivables_account_id: Annotated[str, PropertyInfo(alias="receivablesAccountId")]
    """
    The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
    used to track the amount owed. If not specified, QuickBooks Desktop will use its
    default A/R account.

    **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
    account must match the `receivablesAccount` used in all linked transactions. For
    example, when refunding a credit card payment, the A/R account must match the
    one used in the original credit transactions being refunded.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this receive-payment, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    total_amount: Annotated[str, PropertyInfo(alias="totalAmount")]
    """
    The total monetary amount of this receive-payment, represented as a decimal
    string.

    **NOTE**: The sum of the `paymentAmount` amounts in the `applyToTransactions`
    array cannot exceed the `totalAmount`, or you will receive an error.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD)."""


class ApplyToTransactionApplyCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """The amount of credit applied to this transaction.

    This could include customer deposits, payments, or credits. Represented as a
    decimal string.
    """

    credit_transaction_id: Required[Annotated[str, PropertyInfo(alias="creditTransactionId")]]
    """
    The unique identifier of the credit transaction (credit memo or vendor credit)
    to apply to this transaction.
    """

    override_credit_application: Annotated[bool, PropertyInfo(alias="overrideCreditApplication")]
    """Indicates whether to override the credit."""


class ApplyToTransaction(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the receivable transaction to which this payment is applied."""

    apply_credits: Annotated[Iterable[ApplyToTransactionApplyCredit], PropertyInfo(alias="applyCredits")]
    """Credit memos to apply to this receivable transaction, reducing its balance.

    This creates a link between this receivable transaction and the specified credit
    memos.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transactions in this endpoint's response even when this request is
    successful. To see the transactions linked via this field, refetch the
    receivable transaction and check the `linkedTransactions` response field. If
    fetching a list of receivable transactions, you must also specify the parameter
    `includeLinkedTransactions=true` to see the `linkedTransactions` response field.
    """

    discount_account_id: Annotated[str, PropertyInfo(alias="discountAccountId")]
    """The financial account used to track this receivable transaction's discount."""

    discount_amount: Annotated[str, PropertyInfo(alias="discountAmount")]
    """
    The monetary amount by which to reduce the receivable transaction's receivable
    amount, represented as a decimal string.
    """

    discount_class_id: Annotated[str, PropertyInfo(alias="discountClassId")]
    """The class used to track this receivable transaction's discount."""

    payment_amount: Annotated[str, PropertyInfo(alias="paymentAmount")]
    """
    The monetary amount to apply to the receivable transaction, represented as a
    decimal string.
    """


class CreditCardTransactionRequest(TypedDict, total=False):
    address: str
    """The card's billing address."""

    commercial_card_code: Annotated[str, PropertyInfo(alias="commercialCardCode")]
    """
    The commercial card code identifies the type of business credit card being used
    (purchase, corporate, or business) for Visa and Mastercard transactions only.
    When provided, this code may qualify the transaction for lower processing fees
    compared to the standard rates that apply when no code is specified.
    """

    expiration_month: Annotated[float, PropertyInfo(alias="expirationMonth")]
    """The month when the credit card expires."""

    expiration_year: Annotated[float, PropertyInfo(alias="expirationYear")]
    """The year when the credit card expires."""

    name: str
    """The cardholder's name on the card."""

    number: str
    """The credit card number. Must be masked with lower case "x" and no dashes."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The card's billing address ZIP or postal code."""

    transaction_mode: Annotated[Literal["card_not_present", "card_present"], PropertyInfo(alias="transactionMode")]
    """
    Indicates whether this credit card transaction came from a card swipe
    (`card_present`) or not (`card_not_present`).
    """

    transaction_type: Annotated[
        Literal["authorization", "capture", "charge", "refund", "voice_authorization"],
        PropertyInfo(alias="transactionType"),
    ]
    """The QBMS transaction type from which the current transaction data originated."""


class CreditCardTransactionResponse(TypedDict, total=False):
    authorization_code: Annotated[str, PropertyInfo(alias="authorizationCode")]
    """
    The authorization code returned from the credit card processor to indicate that
    this charge will be paid by the card issuer.
    """

    avs_street_status: Annotated[Literal["fail", "not_available", "pass"], PropertyInfo(alias="avsStreetStatus")]
    """
    Indicates whether the street address supplied in the transaction request matches
    the customer's address on file at the card issuer.
    """

    avs_zip_status: Annotated[Literal["fail", "not_available", "pass"], PropertyInfo(alias="avsZipStatus")]
    """
    Indicates whether the customer postal ZIP code supplied in the transaction
    request matches the customer's postal code recognized at the card issuer.
    """

    card_security_code_match: Annotated[
        Literal["fail", "not_available", "pass"], PropertyInfo(alias="cardSecurityCodeMatch")
    ]
    """
    Indicates whether the card security code supplied in the transaction request
    matches the card security code recognized for that credit card number at the
    card issuer.
    """

    client_transaction_id: Annotated[str, PropertyInfo(alias="clientTransactionId")]
    """
    A value returned from QBMS transactions for future use by the QuickBooks
    Reconciliation feature.
    """

    credit_card_transaction_id: Annotated[str, PropertyInfo(alias="creditCardTransactionId")]
    """
    The ID returned from the credit card processor for this credit card transaction.
    """

    merchant_account_number: Annotated[str, PropertyInfo(alias="merchantAccountNumber")]
    """
    The QBMS account number of the merchant who is running this transaction using
    the customer's credit card.
    """

    payment_grouping_code: Annotated[float, PropertyInfo(alias="paymentGroupingCode")]
    """
    An internal code returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    payment_status: Annotated[Literal["completed", "unknown"], PropertyInfo(alias="paymentStatus")]
    """
    Indicates whether this credit card transaction is known to have been
    successfully processed by the card issuer.
    """

    recon_batch_id: Annotated[str, PropertyInfo(alias="reconBatchId")]
    """
    An internal ID returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    status_code: Annotated[float, PropertyInfo(alias="statusCode")]
    """
    The status code returned in the original QBMS transaction response for this
    credit card transaction.
    """

    status_message: Annotated[str, PropertyInfo(alias="statusMessage")]
    """
    The status message returned in the original QBMS transaction response for this
    credit card transaction.
    """

    transaction_authorization_stamp: Annotated[float, PropertyInfo(alias="transactionAuthorizationStamp")]
    """
    An internal value for this credit card transaction, needed for the QuickBooks
    reconciliation feature.
    """

    transaction_authorized_at: Annotated[str, PropertyInfo(alias="transactionAuthorizedAt")]
    """
    The date and time when the credit card processor authorized this credit card
    transaction.
    """


class CreditCardTransaction(TypedDict, total=False):
    request: CreditCardTransactionRequest
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: CreditCardTransactionResponse
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """
