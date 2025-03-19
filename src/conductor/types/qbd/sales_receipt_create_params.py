# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "SalesReceiptCreateParams",
    "BillingAddress",
    "CreditCardTransaction",
    "CreditCardTransactionRequest",
    "CreditCardTransactionResponse",
    "LineGroup",
    "LineGroupCustomField",
    "Line",
    "LineCreditCardTransaction",
    "LineCreditCardTransactionRequest",
    "LineCreditCardTransactionResponse",
    "LineCustomField",
    "ShippingAddress",
]


class SalesReceiptCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """
    The customer or customer-job to which the payment for this sales receipt is
    credited.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The sales receipt's billing address."""

    check_number: Annotated[str, PropertyInfo(alias="checkNumber")]
    """The check number of a check received for this sales receipt."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales receipt's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this sales receipt's line
    items unless overridden at the line item level.
    """

    credit_card_transaction: Annotated[CreditCardTransaction, PropertyInfo(alias="creditCardTransaction")]
    """
    The credit card transaction data for this sales receipt's payment when using
    QuickBooks Merchant Services (QBMS). If specifying this field, you must also
    specify the `paymentMethod` field.
    """

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the sales receipt."""

    deposit_to_account_id: Annotated[str, PropertyInfo(alias="depositToAccountId")]
    """
    The account where the funds for this sales receipt will be or have been
    deposited.
    """

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this sales receipt when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """
    The date by which this sales receipt must be paid, in ISO 8601 format
    (YYYY-MM-DD).

    **NOTE**: For sales receipts, this field is often `null` because sales receipts
    are generally used for point-of-sale payments, where full payment is received at
    the time of purchase.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this sales receipt's currency and the home
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

    is_pending: Annotated[bool, PropertyInfo(alias="isPending")]
    """Indicates whether this sales receipt has not been completed."""

    is_queued_for_email: Annotated[bool, PropertyInfo(alias="isQueuedForEmail")]
    """
    Indicates whether this sales receipt is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this sales receipt is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: Annotated[Iterable[LineGroup], PropertyInfo(alias="lineGroups")]
    """
    The sales receipt's line item groups, each representing a predefined set of
    related items.

    **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
    sales receipt.
    """

    lines: Iterable[Line]
    """
    The sales receipt's line items, each representing a single product or service
    sold.

    **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
    sales receipt.
    """

    memo: str
    """
    A memo or note for this sales receipt that appears in reports, but not on the
    sales receipt.
    """

    other_custom_field: Annotated[str, PropertyInfo(alias="otherCustomField")]
    """
    A built-in custom field for additional information specific to this sales
    receipt. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales receipts for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Unlike `otherCustomField1` and
    `otherCustomField2`, which are line item fields, this exists at the transaction
    level. Hidden by default in the QuickBooks UI.
    """

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """The sales receipt's payment method (e.g., cash, check, credit card).

    **NOTE**: If this sales receipt contains credit card transaction data supplied
    from QuickBooks Merchant Services (QBMS) transaction responses, you must specify
    a credit card payment method (e.g., "Visa", "MasterCard", etc.).
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this sales receipt, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The sales receipt's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this sales receipt, determining whether it is taxable or
    non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this sales
    receipt's transactions by applying a specific tax rate collected for a single
    tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.

    For sales receipts, while using this field to specify a single tax item/group
    that applies uniformly is recommended, complex tax scenarios may require
    alternative approaches. In such cases, you can set this field to a 0% tax item
    (conventionally named "Tax Calculated On Invoice") and handle tax calculations
    through line items instead. When using line items for taxes, note that only
    individual tax items (not tax groups) can be used, subtotals can help apply a
    tax to multiple items but only the first tax line after a subtotal is calculated
    automatically (subsequent tax lines require manual amounts), and the rate column
    will always display the actual tax amount rather than the rate percentage.
    """

    shipment_origin: Annotated[str, PropertyInfo(alias="shipmentOrigin")]
    """
    The origin location from where the product associated with this sales receipt is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The sales receipt's shipping address."""

    shipping_date: Annotated[Union[str, date], PropertyInfo(alias="shippingDate", format="iso8601")]
    """
    The date when the products or services for this sales receipt were shipped or
    are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]
    """
    The shipping method used for this sales receipt, such as standard mail or
    overnight delivery.
    """


class BillingAddress(TypedDict, total=False):
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


class LineGroupCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class LineGroup(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]
    """
    The sales receipt line group's item group, representing a predefined set of
    items bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    custom_fields: Annotated[Iterable[LineGroupCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the sales receipt line group object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item group associated with this sales
    receipt line group is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item group associated with this sales receipt line group is stored.
    """

    quantity: float
    """The quantity of the item group associated with this sales receipt line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this sales receipt line group.

    Must be a valid unit within the item's available units of measure.
    """


class LineCreditCardTransactionRequest(TypedDict, total=False):
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


class LineCreditCardTransactionResponse(TypedDict, total=False):
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


class LineCreditCardTransaction(TypedDict, total=False):
    request: LineCreditCardTransactionRequest
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: LineCreditCardTransactionResponse
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """


class LineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class Line(TypedDict, total=False):
    amount: str
    """The monetary amount of this sales receipt line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales receipt line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales receipt lines unless overridden here, at the
    transaction line level.
    """

    credit_card_transaction: Annotated[LineCreditCardTransaction, PropertyInfo(alias="creditCardTransaction")]
    """
    The credit card transaction data for this sales receipt line's payment when
    using QuickBooks Merchant Services (QBMS). If specifying this field, you must
    also specify the `paymentMethod` field.
    """

    custom_fields: Annotated[Iterable[LineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the sales receipt line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: str
    """A description of this sales receipt line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this sales
    receipt line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales receipt line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this sales receipt line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this sales receipt line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this sales receipt line, overriding the default account
    associated with the item.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this sales receipt line.

    This overrides any price level set on the corresponding customer. The resulting
    sales receipt line will not show this price level, only the final `rate`
    calculated from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    sales receipt line.
    """

    quantity: float
    """The quantity of the item associated with this sales receipt line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: str
    """The price per unit for this sales receipt line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this sales receipt line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this sales receipt line, determining whether it is
    taxable or non-taxable. If set, this overrides any sales-tax codes defined on
    the parent transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this sales receipt line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Annotated[Union[str, date], PropertyInfo(alias="serviceDate", format="iso8601")]
    """
    The date on which the service for this sales receipt line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this sales receipt line.

    Must be a valid unit within the item's available units of measure.
    """


class ShippingAddress(TypedDict, total=False):
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
