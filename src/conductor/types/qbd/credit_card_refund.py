# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CreditCardRefund",
    "Address",
    "CreditCardTransaction",
    "CreditCardTransactionRequest",
    "CreditCardTransactionResponse",
    "Currency",
    "Customer",
    "CustomField",
    "PaymentMethod",
    "ReceivablesAccount",
    "RefundAppliedToTransaction",
    "RefundFromAccount",
]


class Address(BaseModel):
    """The address that is printed on the credit card refund."""

    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class CreditCardTransactionRequest(BaseModel):
    """
    The transaction request data originally supplied for this credit card transaction when using QuickBooks Merchant Services (QBMS).
    """

    address: Optional[str] = None
    """The card's billing address."""

    commercial_card_code: Optional[str] = FieldInfo(alias="commercialCardCode", default=None)
    """
    The commercial card code identifies the type of business credit card being used
    (purchase, corporate, or business) for Visa and Mastercard transactions only.
    When provided, this code may qualify the transaction for lower processing fees
    compared to the standard rates that apply when no code is specified.
    """

    expiration_month: float = FieldInfo(alias="expirationMonth")
    """The month when the credit card expires."""

    expiration_year: float = FieldInfo(alias="expirationYear")
    """The year when the credit card expires."""

    name: Optional[str] = None
    """The cardholder's name on the card."""

    number: str
    """The credit card number. Must be masked with lower case "x" and no dashes."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The card's billing address ZIP or postal code."""

    transaction_mode: Optional[Literal["card_not_present", "card_present"]] = FieldInfo(
        alias="transactionMode", default=None
    )
    """
    Indicates whether this credit card transaction came from a card swipe
    (`card_present`) or not (`card_not_present`).
    """

    transaction_type: Optional[Literal["authorization", "capture", "charge", "refund", "voice_authorization"]] = (
        FieldInfo(alias="transactionType", default=None)
    )
    """The QBMS transaction type from which the current transaction data originated."""


class CreditCardTransactionResponse(BaseModel):
    """
    The transaction response data for this credit card transaction when using QuickBooks Merchant Services (QBMS).
    """

    authorization_code: Optional[str] = FieldInfo(alias="authorizationCode", default=None)
    """
    The authorization code returned from the credit card processor to indicate that
    this charge will be paid by the card issuer.
    """

    avs_street_status: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(
        alias="avsStreetStatus", default=None
    )
    """
    Indicates whether the street address supplied in the transaction request matches
    the customer's address on file at the card issuer.
    """

    avs_zip_status: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(alias="avsZipStatus", default=None)
    """
    Indicates whether the customer postal ZIP code supplied in the transaction
    request matches the customer's postal code recognized at the card issuer.
    """

    card_security_code_match: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(
        alias="cardSecurityCodeMatch", default=None
    )
    """
    Indicates whether the card security code supplied in the transaction request
    matches the card security code recognized for that credit card number at the
    card issuer.
    """

    client_transaction_id: Optional[str] = FieldInfo(alias="clientTransactionId", default=None)
    """
    A value returned from QBMS transactions for future use by the QuickBooks
    Reconciliation feature.
    """

    credit_card_transaction_id: str = FieldInfo(alias="creditCardTransactionId")
    """
    The ID returned from the credit card processor for this credit card transaction.
    """

    merchant_account_number: str = FieldInfo(alias="merchantAccountNumber")
    """
    The QBMS account number of the merchant who is running this transaction using
    the customer's credit card.
    """

    payment_grouping_code: Optional[float] = FieldInfo(alias="paymentGroupingCode", default=None)
    """
    An internal code returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    payment_status: Literal["completed", "unknown"] = FieldInfo(alias="paymentStatus")
    """
    Indicates whether this credit card transaction is known to have been
    successfully processed by the card issuer.
    """

    recon_batch_id: Optional[str] = FieldInfo(alias="reconBatchId", default=None)
    """
    An internal ID returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    status_code: float = FieldInfo(alias="statusCode")
    """
    The status code returned in the original QBMS transaction response for this
    credit card transaction.
    """

    status_message: str = FieldInfo(alias="statusMessage")
    """
    The status message returned in the original QBMS transaction response for this
    credit card transaction.
    """

    transaction_authorization_stamp: Optional[float] = FieldInfo(alias="transactionAuthorizationStamp", default=None)
    """
    An internal value for this credit card transaction, needed for the QuickBooks
    reconciliation feature.
    """

    transaction_authorized_at: str = FieldInfo(alias="transactionAuthorizedAt")
    """
    The date and time when the credit card processor authorized this credit card
    transaction.
    """


class CreditCardTransaction(BaseModel):
    """
    The credit card transaction data for this credit card refund's payment when using QuickBooks Merchant Services (QBMS).
    """

    request: Optional[CreditCardTransactionRequest] = None
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: Optional[CreditCardTransactionResponse] = None
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """


class Currency(BaseModel):
    """The credit card refund's currency.

    For built-in currencies, the name and code are standard international values. For user-defined currencies, all values are editable.
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
    """The customer or customer-job associated with this credit card refund."""

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


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class PaymentMethod(BaseModel):
    """The credit card refund's payment method (e.g., cash, check, credit card)."""

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


class ReceivablesAccount(BaseModel):
    """
    The Accounts-Receivable (A/R) account to which this credit card refund is assigned, used to track the amount owed. If not specified, QuickBooks Desktop will use its default A/R account.

    **IMPORTANT**: If this credit card refund is linked to other transactions, this A/R account must match the `receivablesAccount` used in all linked transactions. For example, when refunding a credit card payment, the A/R account must match the one used in each linked credit transaction being refunded.
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


class RefundAppliedToTransaction(BaseModel):
    credit_remaining: Optional[str] = FieldInfo(alias="creditRemaining", default=None)
    """
    The remaining balance of this credit transaction that has not yet been applied
    to other transactions or refunded to the customer. Represented as a decimal
    string.
    """

    credit_remaining_in_home_currency: Optional[str] = FieldInfo(alias="creditRemainingInHomeCurrency", default=None)
    """
    The remaining balance of this credit transaction converted to the home currency
    of the QuickBooks company file. Represented as a decimal string.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this credit transaction,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    refund_amount: str = FieldInfo(alias="refundAmount")
    """
    The monetary amount to refund from the linked credit transaction within this
    credit transaction, represented as a decimal string.
    """

    refund_amount_in_home_currency: Optional[str] = FieldInfo(alias="refundAmountInHomeCurrency", default=None)
    """
    The monetary amount to refund from the linked credit transaction in this credit
    transaction, converted to the home currency of the QuickBooks company file.
    Represented as a decimal string.
    """

    transaction_date: Optional[date] = FieldInfo(alias="transactionDate", default=None)
    """The date of this credit transaction, in ISO 8601 format (YYYY-MM-DD)."""

    transaction_id: str = FieldInfo(alias="transactionId")
    """The ID of the credit transaction being refunded by this credit card refund."""

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
    """The type of transaction for this credit transaction."""


class RefundFromAccount(BaseModel):
    """The account providing funds for this credit card refund.

    This is typically the Undeposited Funds account used to hold customer payments.
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


class CreditCardRefund(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this credit card refund.

    This ID is unique across all transaction types.
    """

    address: Optional[Address] = None
    """The address that is printed on the credit card refund."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this credit card refund was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    credit_card_transaction: Optional[CreditCardTransaction] = FieldInfo(alias="creditCardTransaction", default=None)
    """
    The credit card transaction data for this credit card refund's payment when
    using QuickBooks Merchant Services (QBMS).
    """

    currency: Optional[Currency] = None
    """The credit card refund's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """The customer or customer-job associated with this credit card refund."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the credit card refund object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this credit card refund's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    memo: Optional[str] = None
    """A memo or note for this credit card refund."""

    object_type: Literal["qbd_credit_card_refund"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_credit_card_refund"`."""

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)
    """The credit card refund's payment method (e.g., cash, check, credit card)."""

    receivables_account: Optional[ReceivablesAccount] = FieldInfo(alias="receivablesAccount", default=None)
    """
    The Accounts-Receivable (A/R) account to which this credit card refund is
    assigned, used to track the amount owed. If not specified, QuickBooks Desktop
    will use its default A/R account.

    **IMPORTANT**: If this credit card refund is linked to other transactions, this
    A/R account must match the `receivablesAccount` used in all linked transactions.
    For example, when refunding a credit card payment, the A/R account must match
    the one used in each linked credit transaction being refunded.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this credit card refund,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    refund_applied_to_transactions: List[RefundAppliedToTransaction] = FieldInfo(alias="refundAppliedToTransactions")
    """The credit transactions refunded by this credit card refund."""

    refund_from_account: Optional[RefundFromAccount] = FieldInfo(alias="refundFromAccount", default=None)
    """The account providing funds for this credit card refund.

    This is typically the Undeposited Funds account used to hold customer payments.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this credit card refund
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this credit card refund, represented as a decimal
    string.
    """

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount of this credit card refund converted to the home
    currency of the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this credit card refund, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this credit card refund was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """
