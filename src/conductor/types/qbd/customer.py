# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Customer",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
    "AlternateShippingAddress",
    "BillingAddress",
    "Class",
    "CreditCard",
    "Currency",
    "CustomContactField",
    "CustomerType",
    "CustomField",
    "JobType",
    "Parent",
    "PreferredPaymentMethod",
    "PriceLevel",
    "SalesRepresentative",
    "SalesTaxCode",
    "SalesTaxItem",
    "ShippingAddress",
    "Terms",
]


class AdditionalContactCustomContactField(BaseModel):
    name: str
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Optional[str] = None
    """The value of the contact field."""


class AdditionalContact(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this contact.

    This ID is unique across all contacts but not across different QuickBooks object
    types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this contact was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_contact_fields: List[AdditionalContactCustomContactField] = FieldInfo(alias="customContactFields")
    """
    Additional custom contact fields for this contact, such as phone numbers or
    email addresses.
    """

    first_name: str = FieldInfo(alias="firstName")
    """The contact's first name."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The contact's job title."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The contact's last name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The contact's middle name."""

    name: Optional[str] = None
    """The contact's full name."""

    object_type: Literal["qbd_contact"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_contact"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this contact object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    salutation: Optional[str] = None
    """
    The contact's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this contact was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """


class AdditionalNote(BaseModel):
    id: float
    """The auto-incrementing identifier assigned by QuickBooks to this note."""

    date: Optional[datetime.date] = None
    """The date this note was last updated, in ISO 8601 format (YYYY-MM-DD)."""

    note: str
    """The text of this note."""


class AlternateShippingAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the shipping address."""

    country: Optional[str] = None
    """The country name of the shipping address."""

    is_default_shipping_address: Optional[bool] = FieldInfo(alias="isDefaultShippingAddress", default=None)
    """Indicates whether this shipping address is the default shipping address."""

    line1: Optional[str] = None
    """The first line of the shipping address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the shipping address, if needed (e.g., apartment, suite,
    unit, or building).
    """

    line3: Optional[str] = None
    """The third line of the shipping address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the shipping address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the shipping address, if needed."""

    name: str
    """
    The case-insensitive unique name of this shipping address, unique across all
    shipping addresses.

    **NOTE**: Shipping addresses do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    note: Optional[str] = None
    """
    A note written at the bottom of the shipping address in the form in which it
    appears, such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the shipping address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the shipping address."""


class BillingAddress(BaseModel):
    """The customer's billing address."""

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
    """The customer's class.

    Classes can be used to categorize objects into meaningful segments, such as department, location, or type of work. In QuickBooks, class tracking is off by default.
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


class CreditCard(BaseModel):
    """
    The customer's credit card information, including card type, number, and expiration date, used for processing credit card payments.
    """

    address: Optional[str] = None
    """The card's billing address."""

    expiration_month: Optional[float] = FieldInfo(alias="expirationMonth", default=None)
    """The month when the credit card expires."""

    expiration_year: Optional[float] = FieldInfo(alias="expirationYear", default=None)
    """The year when the credit card expires."""

    name: Optional[str] = None
    """The cardholder's name on the card."""

    number: Optional[str] = None
    """The credit card number. Must be masked with lower case "x" and no dashes."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The card's billing address ZIP or postal code."""


class Currency(BaseModel):
    """The customer's currency.

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


class CustomContactField(BaseModel):
    name: str
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Optional[str] = None
    """The value of the contact field."""


class CustomerType(BaseModel):
    """
    The customer's type, used for categorizing customers into meaningful segments, such as industry or region.
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


class JobType(BaseModel):
    """
    The type or category of this customer's job, if this object is a job (i.e., sub-customer). Useful for classifying into meaningful segments (e.g., repair, installation, consulting).
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


class Parent(BaseModel):
    """The parent customer one level above this one in the hierarchy.

    For example, if this customer has a `fullName` of "ABC Corporation:Website Redesign Project", its parent has a `fullName` of "ABC Corporation". If this customer is at the top level, this field will be `null`.
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


class PreferredPaymentMethod(BaseModel):
    """The customer's preferred payment method (e.g., cash, check, credit card)."""

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


class PriceLevel(BaseModel):
    """
    The customer's custom price level that QuickBooks automatically applies to calculate item rates in new transactions (e.g., invoices, sales receipts, sales orders, and credit memos) for this customer. While applied automatically, this can be overridden when creating individual transactions. Note that transactions will not show the price level itself, only the final `rate` calculated from it.
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


class SalesRepresentative(BaseModel):
    """The customer's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
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


class SalesTaxCode(BaseModel):
    """
    The default sales-tax code for transactions with this customer, determining whether the transactions are taxable or non-taxable. This can be overridden at the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign the default non-taxable code to all sales.
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


class SalesTaxItem(BaseModel):
    """
    The sales-tax item used to calculate the actual tax amount for this customer's transactions by applying a specific tax rate collected for a single tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this field drives the actual tax calculation and reporting.
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


class ShippingAddress(BaseModel):
    """The customer's shipping address."""

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


class Terms(BaseModel):
    """
    The customer's payment terms, defining when payment is due and any applicable discounts.
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
    id: str
    """The unique identifier assigned by QuickBooks to this customer.

    This ID is unique across all customers but not across different QuickBooks
    object types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The customer's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    additional_contacts: List[AdditionalContact] = FieldInfo(alias="additionalContacts")
    """Additional alternate contacts for this customer."""

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this customer."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The name of a alternate contact person for this customer."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The customer's alternate telephone number."""

    alternate_shipping_addresses: List[AlternateShippingAddress] = FieldInfo(alias="alternateShippingAddresses")
    """A list of additional shipping addresses for this customer.

    Useful when the customer has multiple shipping locations.
    """

    balance: Optional[str] = None
    """
    The current balance owed by this customer, excluding balances from any jobs
    (i.e., sub-customers), represented as a decimal string. Compare with
    `totalBalance`. A positive number indicates money owed by the customer.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The customer's billing address."""

    cc_email: Optional[str] = FieldInfo(alias="ccEmail", default=None)
    """An email address to carbon copy (CC) on communications with this customer."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The customer's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the company associated with this customer.

    This name is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The name of the primary contact person for this customer."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this customer was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    credit_card: Optional[CreditCard] = FieldInfo(alias="creditCard", default=None)
    """
    The customer's credit card information, including card type, number, and
    expiration date, used for processing credit card payments.
    """

    credit_limit: Optional[str] = FieldInfo(alias="creditLimit", default=None)
    """The customer's credit limit, represented as a decimal string.

    This is the maximum amount of money this customer can spend before being billed.
    If `null`, there is no credit limit.
    """

    currency: Optional[Currency] = None
    """The customer's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """
    Additional custom contact fields for this customer, such as phone numbers or
    email addresses.
    """

    customer_type: Optional[CustomerType] = FieldInfo(alias="customerType", default=None)
    """
    The customer's type, used for categorizing customers into meaningful segments,
    such as industry or region.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the customer object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The customer's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    fax: Optional[str] = None
    """The customer's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the contact person for this customer."""

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this customer, formed by
    combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if a customer is under "ABC Corporation" and
    has the `name` "Website Redesign Project", its `fullName` would be "ABC
    Corporation:Website Redesign Project".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    customer objects. However, `fullName` can still be arbitrarily changed by the
    QuickBooks user when they modify the underlying `name` field.

    **IMPORTANT**: If this object is a job (i.e., a sub-customer), this value would
    likely be the job's `name` prefixed by the customer's `name`.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this customer is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    job_description: Optional[str] = FieldInfo(alias="jobDescription", default=None)
    """
    A brief description of this customer's job, if this object is a job (i.e.,
    sub-customer).
    """

    job_end_date: Optional[datetime.date] = FieldInfo(alias="jobEndDate", default=None)
    """
    The actual completion date of this customer's job, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_projected_end_date: Optional[datetime.date] = FieldInfo(alias="jobProjectedEndDate", default=None)
    """
    The projected completion date for this customer's job, if applicable, in ISO
    8601 format (YYYY-MM-DD).
    """

    job_start_date: Optional[datetime.date] = FieldInfo(alias="jobStartDate", default=None)
    """
    The date when work on this customer's job began, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_status: Optional[Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]] = FieldInfo(
        alias="jobStatus", default=None
    )
    """
    The status of this customer's job, if this object is a job (i.e., sub-customer).
    """

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The job title of the contact person for this customer."""

    job_type: Optional[JobType] = FieldInfo(alias="jobType", default=None)
    """
    The type or category of this customer's job, if this object is a job (i.e.,
    sub-customer). Useful for classifying into meaningful segments (e.g., repair,
    installation, consulting).
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the contact person for this customer."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The middle name of the contact person for this customer."""

    name: str
    """The case-insensitive name of this customer.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two customers
    could both have the `name` "Website Redesign Project", but they could have
    unique `fullName` values, such as "ABC Corporation:Website Redesign Project" and
    "Baker:Website Redesign Project".
    """

    note: Optional[str] = None
    """A note or comment about this customer."""

    object_type: Literal["qbd_customer"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_customer"`."""

    parent: Optional[Parent] = None
    """The parent customer one level above this one in the hierarchy.

    For example, if this customer has a `fullName` of "ABC Corporation:Website
    Redesign Project", its parent has a `fullName` of "ABC Corporation". If this
    customer is at the top level, this field will be `null`.
    """

    phone: Optional[str] = None
    """The customer's primary telephone number."""

    preferred_delivery_method: Optional[Literal["email", "mail", "none"]] = FieldInfo(
        alias="preferredDeliveryMethod", default=None
    )
    """
    The preferred method for delivering invoices and other documents to this
    customer.
    """

    preferred_payment_method: Optional[PreferredPaymentMethod] = FieldInfo(alias="preferredPaymentMethod", default=None)
    """The customer's preferred payment method (e.g., cash, check, credit card)."""

    price_level: Optional[PriceLevel] = FieldInfo(alias="priceLevel", default=None)
    """
    The customer's custom price level that QuickBooks automatically applies to
    calculate item rates in new transactions (e.g., invoices, sales receipts, sales
    orders, and credit memos) for this customer. While applied automatically, this
    can be overridden when creating individual transactions. Note that transactions
    will not show the price level itself, only the final `rate` calculated from it.
    """

    resale_number: Optional[str] = FieldInfo(alias="resaleNumber", default=None)
    """
    The customer's resale number, used if the customer is purchasing items for
    resale. This number does not affect sales tax calculations or reports in
    QuickBooks.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this customer object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The customer's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The default sales-tax code for transactions with this customer, determining
    whether the transactions are taxable or non-taxable. This can be overridden at
    the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_country: Optional[Literal["australia", "canada", "uk", "us"]] = FieldInfo(
        alias="salesTaxCountry", default=None
    )
    """The country for which sales tax is collected for this customer."""

    sales_tax_item: Optional[SalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this customer's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    salutation: Optional[str] = None
    """
    The formal salutation title that precedes the name of the contact person for
    this customer, such as "Mr.", "Ms.", or "Dr.".
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The customer's shipping address."""

    sublevel: float
    """The depth level of this customer in the hierarchy.

    A top-level customer has a `sublevel` of 0; each subsequent sublevel increases
    this number by 1. For example, a customer with a `fullName` of "ABC
    Corporation:Website Redesign Project" would have a `sublevel` of 1. When
    `sublevel` is 0, this object is a customer; when `sublevel` is greater than 0,
    this object is typically a job (i.e., a sub-customer).
    """

    tax_registration_number: Optional[str] = FieldInfo(alias="taxRegistrationNumber", default=None)
    """The customer's tax registration number, for use in Canada or the UK."""

    terms: Optional[Terms] = None
    """
    The customer's payment terms, defining when payment is due and any applicable
    discounts.
    """

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)
    """
    The combined balance of this customer and all of this customer's jobs (i.e.,
    sub-customers), represented as a decimal string. If there are no sub-customers,
    `totalBalance` and `balance` are equal. A positive number indicates money owed
    by the customer.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this customer was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
