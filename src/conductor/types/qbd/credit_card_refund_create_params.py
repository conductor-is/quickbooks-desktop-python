# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CreditCardRefundCreateParams",
    "RefundAppliedToTransaction",
    "Address",
    "CreditCardTransaction",
    "CreditCardTransactionRequest",
    "CreditCardTransactionResponse",
]


class CreditCardRefundCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer or customer-job associated with this credit card refund."""

    refund_applied_to_transactions: Required[
        Annotated[Iterable[RefundAppliedToTransaction], PropertyInfo(alias="refundAppliedToTransactions")]
    ]
    """The credit transactions to refund in this credit card refund.

    Each entry links this credit card refund to an existing credit (for example, a
    credit memo or unused receive-payment credit).

    **IMPORTANT**: The `refundAmount` for each linked credit cannot exceed that
    credit's remaining balance, and the combined `refundAmount` across all links
    cannot exceed this credit card refund's `totalAmount`.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this credit card refund, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    address: Address
    """The address that is printed on the credit card refund."""

    credit_card_transaction: Annotated[CreditCardTransaction, PropertyInfo(alias="creditCardTransaction")]
    """
    The credit card transaction data for this credit card refund's payment when
    using QuickBooks Merchant Services (QBMS). If specifying this field, you must
    also specify the `paymentMethod` field.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this credit card refund's currency and the home
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

    memo: str
    """A memo or note for this credit card refund."""

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """The credit card refund's payment method (e.g., cash, check, credit card).

    **NOTE**: If this credit card refund contains credit card transaction data
    supplied from QuickBooks Merchant Services (QBMS) transaction responses, you
    must specify a credit card payment method (e.g., "Visa", "MasterCard", etc.).
    """

    receivables_account_id: Annotated[str, PropertyInfo(alias="receivablesAccountId")]
    """
    The Accounts-Receivable (A/R) account to which this credit card refund is
    assigned, used to track the amount owed. If not specified, QuickBooks Desktop
    will use its default A/R account.

    **IMPORTANT**: If this credit card refund is linked to other transactions, this
    A/R account must match the `receivablesAccount` used in all linked transactions.
    For example, when refunding a credit card payment, the A/R account must match
    the one used in each linked credit transaction being refunded.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this credit card refund,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).
    """

    refund_from_account_id: Annotated[str, PropertyInfo(alias="refundFromAccountId")]
    """The account providing funds for this credit card refund.

    This is typically the Undeposited Funds account used to hold customer payments.
    If omitted, QuickBooks Desktop will use the default Undeposited Funds account.
    """


class RefundAppliedToTransaction(TypedDict, total=False):
    refund_amount: Required[Annotated[str, PropertyInfo(alias="refundAmount")]]
    """
    The monetary amount to refund from the linked credit transaction within this
    credit transaction, represented as a decimal string.
    """

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the credit transaction being refunded by this credit card refund."""


class Address(TypedDict, total=False):
    """The address that is printed on the credit card refund."""

    city: str
    """The city, district, suburb, town, or village name of the address.

    Maximum length: 31 characters.
    """

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name).

    Maximum length: 41 characters.
    """

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).

    Maximum length: 41 characters.
    """

    line3: str
    """The third line of the address, if needed.

    Maximum length: 41 characters.
    """

    line4: str
    """The fourth line of the address, if needed.

    Maximum length: 41 characters.
    """

    line5: str
    """The fifth line of the address, if needed.

    Maximum length: 41 characters.
    """

    note: str
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address.

    Maximum length: 13 characters.
    """

    state: str
    """The state, county, province, or region name of the address.

    Maximum length: 21 characters.
    """


class CreditCardTransactionRequest(TypedDict, total=False):
    """
    The transaction request data originally supplied for this credit card transaction when using QuickBooks Merchant Services (QBMS).
    """

    expiration_month: Required[Annotated[float, PropertyInfo(alias="expirationMonth")]]
    """The month when the credit card expires."""

    expiration_year: Required[Annotated[float, PropertyInfo(alias="expirationYear")]]
    """The year when the credit card expires."""

    name: Required[str]
    """The cardholder's name on the card."""

    number: Required[str]
    """The credit card number. Must be masked with lower case "x" and no dashes."""

    address: str
    """The card's billing address."""

    commercial_card_code: Annotated[str, PropertyInfo(alias="commercialCardCode")]
    """
    The commercial card code identifies the type of business credit card being used
    (purchase, corporate, or business) for Visa and Mastercard transactions only.
    When provided, this code may qualify the transaction for lower processing fees
    compared to the standard rates that apply when no code is specified.
    """

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
    """
    The transaction response data for this credit card transaction when using QuickBooks Merchant Services (QBMS).
    """

    credit_card_transaction_id: Required[Annotated[str, PropertyInfo(alias="creditCardTransactionId")]]
    """
    The ID returned from the credit card processor for this credit card transaction.
    """

    merchant_account_number: Required[Annotated[str, PropertyInfo(alias="merchantAccountNumber")]]
    """
    The QBMS account number of the merchant who is running this transaction using
    the customer's credit card.
    """

    payment_status: Required[Annotated[Literal["completed", "unknown"], PropertyInfo(alias="paymentStatus")]]
    """
    Indicates whether this credit card transaction is known to have been
    successfully processed by the card issuer.
    """

    status_code: Required[Annotated[float, PropertyInfo(alias="statusCode")]]
    """
    The status code returned in the original QBMS transaction response for this
    credit card transaction.
    """

    status_message: Required[Annotated[str, PropertyInfo(alias="statusMessage")]]
    """
    The status message returned in the original QBMS transaction response for this
    credit card transaction.
    """

    transaction_authorized_at: Required[Annotated[str, PropertyInfo(alias="transactionAuthorizedAt")]]
    """
    The date and time when the credit card processor authorized this credit card
    transaction.
    """

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

    payment_grouping_code: Annotated[float, PropertyInfo(alias="paymentGroupingCode")]
    """
    An internal code returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    recon_batch_id: Annotated[str, PropertyInfo(alias="reconBatchId")]
    """
    An internal ID returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    transaction_authorization_stamp: Annotated[float, PropertyInfo(alias="transactionAuthorizationStamp")]
    """
    An internal value for this credit card transaction, needed for the QuickBooks
    reconciliation feature.
    """


class CreditCardTransaction(TypedDict, total=False):
    """
    The credit card transaction data for this credit card refund's payment when using QuickBooks Merchant Services (QBMS). If specifying this field, you must also specify the `paymentMethod` field.
    """

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
