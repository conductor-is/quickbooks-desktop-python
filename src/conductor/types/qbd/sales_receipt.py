# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SalesReceipt",
    "BillingAddress",
    "Class",
    "CreditCardTransaction",
    "CreditCardTransactionRequest",
    "CreditCardTransactionResponse",
    "Currency",
    "Customer",
    "CustomerMessage",
    "CustomField",
    "DepositToAccount",
    "DocumentTemplate",
    "LineGroup",
    "LineGroupCustomField",
    "LineGroupItemGroup",
    "LineGroupLine",
    "LineGroupLineClass",
    "LineGroupLineCreditCardTransaction",
    "LineGroupLineCreditCardTransactionRequest",
    "LineGroupLineCreditCardTransactionResponse",
    "LineGroupLineCustomField",
    "LineGroupLineInventorySite",
    "LineGroupLineInventorySiteLocation",
    "LineGroupLineItem",
    "LineGroupLineOverrideUnitOfMeasureSet",
    "LineGroupLineSalesTaxCode",
    "LineGroupOverrideUnitOfMeasureSet",
    "Line",
    "LineClass",
    "LineCreditCardTransaction",
    "LineCreditCardTransactionRequest",
    "LineCreditCardTransactionResponse",
    "LineCustomField",
    "LineInventorySite",
    "LineInventorySiteLocation",
    "LineItem",
    "LineOverrideUnitOfMeasureSet",
    "LineSalesTaxCode",
    "PaymentMethod",
    "SalesRepresentative",
    "SalesTaxCode",
    "SalesTaxItem",
    "ShippingAddress",
    "ShippingMethod",
]


class BillingAddress(BaseModel):
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


class Class(BaseModel):
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


class CreditCardTransactionRequest(BaseModel):
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

    name: str
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


class CustomerMessage(BaseModel):
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


class DepositToAccount(BaseModel):
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


class DocumentTemplate(BaseModel):
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


class LineGroupCustomField(BaseModel):
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


class LineGroupItemGroup(BaseModel):
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


class LineGroupLineClass(BaseModel):
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


class LineGroupLineCreditCardTransactionRequest(BaseModel):
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

    name: str
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


class LineGroupLineCreditCardTransactionResponse(BaseModel):
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


class LineGroupLineCreditCardTransaction(BaseModel):
    request: Optional[LineGroupLineCreditCardTransactionRequest] = None
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: Optional[LineGroupLineCreditCardTransactionResponse] = None
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """


class LineGroupLineCustomField(BaseModel):
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


class LineGroupLineInventorySite(BaseModel):
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


class LineGroupLineInventorySiteLocation(BaseModel):
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


class LineGroupLineItem(BaseModel):
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


class LineGroupLineOverrideUnitOfMeasureSet(BaseModel):
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


class LineGroupLineSalesTaxCode(BaseModel):
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


class LineGroupLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales receipt line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this sales receipt line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineGroupLineClass] = FieldInfo(alias="class", default=None)
    """The sales receipt line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales receipt lines unless overridden here, at the
    transaction line level.
    """

    credit_card_transaction: Optional[LineGroupLineCreditCardTransaction] = FieldInfo(
        alias="creditCardTransaction", default=None
    )
    """
    The credit card transaction data for this sales receipt line's payment when
    using QuickBooks Merchant Services (QBMS).
    """

    custom_fields: List[LineGroupLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales receipt line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales receipt line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this sales receipt line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[LineGroupLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this sales
    receipt line is stored.
    """

    inventory_site_location: Optional[LineGroupLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales receipt line is stored.
    """

    item: Optional[LineGroupLineItem] = None
    """The item associated with this sales receipt line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this sales receipt line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_sales_receipt_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_receipt_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineGroupLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales receipt
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this sales receipt line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: Optional[str] = None
    """The price per unit for this sales receipt line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this sales receipt line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineGroupLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code for this sales receipt line, determining whether it is
    taxable or non-taxable. If set, this overrides any sales-tax codes defined on
    the parent transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this sales receipt line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this sales receipt line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales receipt line.

    Must be a valid unit within the item's available units of measure.
    """


class LineGroupOverrideUnitOfMeasureSet(BaseModel):
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


class LineGroup(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales receipt line group.

    This ID is unique across all transaction line types.
    """

    custom_fields: List[LineGroupCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales receipt line group object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales receipt line group."""

    item_group: LineGroupItemGroup = FieldInfo(alias="itemGroup")
    """
    The sales receipt line group's item group, representing a predefined set of
    items bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: List[LineGroupLine]
    """
    The sales receipt line group's line items, each representing a single product or
    service sold.
    """

    object_type: Literal["qbd_sales_receipt_line_group"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_receipt_line_group"`."""

    override_unit_of_measure_set: Optional[LineGroupOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales receipt
    line group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows
    you to select units from a different set than the item's default unit-of-measure
    set, which remains unchanged on the item itself. The override applies only to
    this specific line. For example, you can sell an item typically measured in
    volume units using weight units in a specific transaction by specifying a
    different unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item group associated with this sales receipt line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    should_print_items_in_group: bool = FieldInfo(alias="shouldPrintItemsInGroup")
    """
    Indicates whether the individual items in this sales receipt line group and
    their separate amounts appear on printed forms.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this sales receipt line group, equivalent to the
    sum of the amounts in `lines`, represented as a decimal string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales receipt line group.

    Must be a valid unit within the item's available units of measure.
    """


class LineClass(BaseModel):
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


class LineCreditCardTransactionRequest(BaseModel):
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

    name: str
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


class LineCreditCardTransactionResponse(BaseModel):
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


class LineCreditCardTransaction(BaseModel):
    request: Optional[LineCreditCardTransactionRequest] = None
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: Optional[LineCreditCardTransactionResponse] = None
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """


class LineCustomField(BaseModel):
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


class LineInventorySite(BaseModel):
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


class LineInventorySiteLocation(BaseModel):
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


class LineItem(BaseModel):
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


class LineOverrideUnitOfMeasureSet(BaseModel):
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


class LineSalesTaxCode(BaseModel):
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


class Line(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales receipt line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this sales receipt line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineClass] = FieldInfo(alias="class", default=None)
    """The sales receipt line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales receipt lines unless overridden here, at the
    transaction line level.
    """

    credit_card_transaction: Optional[LineCreditCardTransaction] = FieldInfo(
        alias="creditCardTransaction", default=None
    )
    """
    The credit card transaction data for this sales receipt line's payment when
    using QuickBooks Merchant Services (QBMS).
    """

    custom_fields: List[LineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales receipt line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales receipt line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this sales receipt line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[LineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this sales
    receipt line is stored.
    """

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales receipt line is stored.
    """

    item: Optional[LineItem] = None
    """The item associated with this sales receipt line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this sales receipt line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_sales_receipt_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_receipt_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this sales
    receipt line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all sales receipt lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales receipt
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this sales receipt line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: Optional[str] = None
    """The price per unit for this sales receipt line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this sales receipt line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code for this sales receipt line, determining whether it is
    taxable or non-taxable. If set, this overrides any sales-tax codes defined on
    the parent transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this sales receipt line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this sales receipt line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales receipt line.

    Must be a valid unit within the item's available units of measure.
    """


class PaymentMethod(BaseModel):
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


class SalesRepresentative(BaseModel):
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


class SalesTaxCode(BaseModel):
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


class SalesTaxItem(BaseModel):
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


class ShippingAddress(BaseModel):
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


class ShippingMethod(BaseModel):
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


class SalesReceipt(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales receipt.

    This ID is unique across all transaction types.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The sales receipt's billing address."""

    check_number: Optional[str] = FieldInfo(alias="checkNumber", default=None)
    """The check number of a check received for this sales receipt."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The sales receipt's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this sales receipt's line
    items unless overridden at the line item level.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales receipt was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_card_transaction: Optional[CreditCardTransaction] = FieldInfo(alias="creditCardTransaction", default=None)
    """
    The credit card transaction data for this sales receipt's payment when using
    QuickBooks Merchant Services (QBMS).
    """

    currency: Optional[Currency] = None
    """The sales receipt's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """
    The customer or customer-job to which the payment for this sales receipt is
    credited.
    """

    customer_message: Optional[CustomerMessage] = FieldInfo(alias="customerMessage", default=None)
    """The message to display to the customer on the sales receipt."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales receipt object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    deposit_to_account: Optional[DepositToAccount] = FieldInfo(alias="depositToAccount", default=None)
    """
    The account where the funds for this sales receipt will be or have been
    deposited.
    """

    document_template: Optional[DocumentTemplate] = FieldInfo(alias="documentTemplate", default=None)
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this sales receipt when printed or displayed.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """
    The date by which this sales receipt must be paid, in ISO 8601 format
    (YYYY-MM-DD).

    **NOTE**: For sales receipts, this field is often `null` because sales receipts
    are generally used for point-of-sale payments, where full payment is received at
    the time of purchase.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this sales receipt's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this sales receipt has not been completed."""

    is_queued_for_email: Optional[bool] = FieldInfo(alias="isQueuedForEmail", default=None)
    """
    Indicates whether this sales receipt is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this sales receipt is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: List[LineGroup] = FieldInfo(alias="lineGroups")
    """
    The sales receipt's line item groups, each representing a predefined set of
    related items.
    """

    lines: List[Line]
    """
    The sales receipt's line items, each representing a single product or service
    sold.
    """

    memo: Optional[str] = None
    """
    A memo or note for this sales receipt that appears in reports, but not on the
    sales receipt.
    """

    object_type: Literal["qbd_sales_receipt"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_receipt"`."""

    other_custom_field: Optional[str] = FieldInfo(alias="otherCustomField", default=None)
    """
    A built-in custom field for additional information specific to this sales
    receipt. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales receipts for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Unlike `otherCustomField1` and
    `otherCustomField2`, which are line item fields, this exists at the transaction
    level. Hidden by default in the QuickBooks UI.
    """

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)
    """The sales receipt's payment method (e.g., cash, check, credit card)."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this sales receipt, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this sales receipt object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The sales receipt's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code for this sales receipt, determining whether it is taxable or
    non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item: Optional[SalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
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

    sales_tax_percentage: Optional[str] = FieldInfo(alias="salesTaxPercentage", default=None)
    """
    The sales tax percentage applied to this sales receipt, represented as a decimal
    string.
    """

    sales_tax_total: str = FieldInfo(alias="salesTaxTotal")
    """
    The total amount of sales tax charged for this sales receipt, represented as a
    decimal string.
    """

    shipment_origin: Optional[str] = FieldInfo(alias="shipmentOrigin", default=None)
    """
    The origin location from where the product associated with this sales receipt is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The sales receipt's shipping address."""

    shipping_date: Optional[date] = FieldInfo(alias="shippingDate", default=None)
    """
    The date when the products or services for this sales receipt were shipped or
    are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method: Optional[ShippingMethod] = FieldInfo(alias="shippingMethod", default=None)
    """
    The shipping method used for this sales receipt, such as standard mail or
    overnight delivery.
    """

    subtotal: str
    """
    The subtotal of this sales receipt, which is the sum of all sales receipt lines
    before taxes and payments are applied, represented as a decimal string.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this sales receipt, equivalent to the sum of the
    amounts in `lines` and `lineGroups`, represented as a decimal string.
    """

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount of this sales receipt converted to the home currency
    of the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales receipt was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
