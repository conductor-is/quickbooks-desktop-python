# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CustomerCreateParams",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
    "AlternateShippingAddress",
    "BillingAddress",
    "CreditCard",
    "CustomContactField",
    "ShippingAddress",
]


class CustomerCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of this customer.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two customers
    could both have the `name` "Website Redesign Project", but they could have
    unique `fullName` values, such as "ABC Corporation:Website Redesign Project" and
    "Baker:Website Redesign Project".

    Maximum length: 41 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The customer's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    additional_contacts: Annotated[Iterable[AdditionalContact], PropertyInfo(alias="additionalContacts")]
    """Additional alternate contacts for this customer."""

    additional_notes: Annotated[Iterable[AdditionalNote], PropertyInfo(alias="additionalNotes")]
    """Additional notes about this customer."""

    alternate_contact: Annotated[str, PropertyInfo(alias="alternateContact")]
    """The name of a alternate contact person for this customer."""

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The customer's alternate telephone number."""

    alternate_shipping_addresses: Annotated[
        Iterable[AlternateShippingAddress], PropertyInfo(alias="alternateShippingAddresses")
    ]
    """A list of additional shipping addresses for this customer.

    Useful when the customer has multiple shipping locations.
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The customer's billing address."""

    cc_email: Annotated[str, PropertyInfo(alias="ccEmail")]
    """An email address to carbon copy (CC) on communications with this customer."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The customer's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """The name of the company associated with this customer.

    This name is used on invoices, checks, and other forms.
    """

    contact: str
    """The name of the primary contact person for this customer."""

    credit_card: Annotated[CreditCard, PropertyInfo(alias="creditCard")]
    """
    The customer's credit card information, including card type, number, and
    expiration date, used for processing credit card payments.
    """

    credit_limit: Annotated[str, PropertyInfo(alias="creditLimit")]
    """The customer's credit limit, represented as a decimal string.

    This is the maximum amount of money this customer can spend before being billed.
    If `null`, there is no credit limit.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The customer's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_contact_fields: Annotated[Iterable[CustomContactField], PropertyInfo(alias="customContactFields")]
    """
    Additional custom contact fields for this customer, such as phone numbers or
    email addresses.
    """

    customer_type_id: Annotated[str, PropertyInfo(alias="customerTypeId")]
    """
    The customer's type, used for categorizing customers into meaningful segments,
    such as industry or region.
    """

    email: str
    """The customer's email address."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    fax: str
    """The customer's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the contact person for this customer.

    Maximum length: 25 characters.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this customer is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    job_description: Annotated[str, PropertyInfo(alias="jobDescription")]
    """
    A brief description of this customer's job, if this object is a job (i.e.,
    sub-customer).
    """

    job_end_date: Annotated[Union[str, date], PropertyInfo(alias="jobEndDate", format="iso8601")]
    """
    The actual completion date of this customer's job, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_projected_end_date: Annotated[Union[str, date], PropertyInfo(alias="jobProjectedEndDate", format="iso8601")]
    """
    The projected completion date for this customer's job, if applicable, in ISO
    8601 format (YYYY-MM-DD).
    """

    job_start_date: Annotated[Union[str, date], PropertyInfo(alias="jobStartDate", format="iso8601")]
    """
    The date when work on this customer's job began, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_status: Annotated[
        Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"], PropertyInfo(alias="jobStatus")
    ]
    """
    The status of this customer's job, if this object is a job (i.e., sub-customer).
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The job title of the contact person for this customer."""

    job_type_id: Annotated[str, PropertyInfo(alias="jobTypeId")]
    """
    The type or category of this customer's job, if this object is a job (i.e.,
    sub-customer). Useful for classifying into meaningful segments (e.g., repair,
    installation, consulting).
    """

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the contact person for this customer.

    Maximum length: 25 characters.
    """

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The middle name of the contact person for this customer.

    Maximum length: 5 characters.
    """

    note: str
    """A note or comment about this customer."""

    opening_balance: Annotated[str, PropertyInfo(alias="openingBalance")]
    """
    The opening balance of this customer's account, indicating the amount owed by
    this customer, represented as a decimal string.
    """

    opening_balance_date: Annotated[Union[str, date], PropertyInfo(alias="openingBalanceDate", format="iso8601")]
    """
    The date of the opening balance of this customer, in ISO 8601 format
    (YYYY-MM-DD).
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent customer one level above this one in the hierarchy.

    For example, if this customer has a `fullName` of "ABC Corporation:Website
    Redesign Project", its parent has a `fullName` of "ABC Corporation". If this
    customer is at the top level, this field will be `null`.
    """

    phone: str
    """The customer's primary telephone number."""

    preferred_delivery_method: Annotated[
        Literal["email", "mail", "none"], PropertyInfo(alias="preferredDeliveryMethod")
    ]
    """
    The preferred method for delivering invoices and other documents to this
    customer.
    """

    preferred_payment_method_id: Annotated[str, PropertyInfo(alias="preferredPaymentMethodId")]
    """The customer's preferred payment method (e.g., cash, check, credit card)."""

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """
    The customer's custom price level that QuickBooks automatically applies to
    calculate item rates in new transactions (e.g., invoices, sales receipts, sales
    orders, and credit memos) for this customer. While applied automatically, this
    can be overridden when creating individual transactions. Note that transactions
    will not show the price level itself, only the final `rate` calculated from it.
    """

    resale_number: Annotated[str, PropertyInfo(alias="resaleNumber")]
    """
    The customer's resale number, used if the customer is purchasing items for
    resale. This number does not affect sales tax calculations or reports in
    QuickBooks.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The customer's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for transactions with this customer, determining
    whether the transactions are taxable or non-taxable. This can be overridden at
    the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_country: Annotated[Literal["australia", "canada", "uk", "us"], PropertyInfo(alias="salesTaxCountry")]
    """The country for which sales tax is collected for this customer."""

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this customer's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    salutation: str
    """
    The formal salutation title that precedes the name of the contact person for
    this customer, such as "Mr.", "Ms.", or "Dr.".
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The customer's shipping address."""

    tax_registration_number: Annotated[str, PropertyInfo(alias="taxRegistrationNumber")]
    """The customer's tax registration number, for use in Canada or the UK."""

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The customer's payment terms, defining when payment is due and any applicable
    discounts.
    """


class AdditionalContactCustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the contact field."""


class AdditionalContact(TypedDict, total=False):
    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The contact's first name.

    Maximum length: 25 characters.
    """

    custom_contact_fields: Annotated[
        Iterable[AdditionalContactCustomContactField], PropertyInfo(alias="customContactFields")
    ]
    """
    Additional custom contact fields for this contact, such as phone numbers or
    email addresses.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The contact's job title."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The contact's last name.

    Maximum length: 25 characters.
    """

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The contact's middle name.

    Maximum length: 5 characters.
    """

    salutation: str
    """
    The contact's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """


class AdditionalNote(TypedDict, total=False):
    note: Required[str]
    """The text of this note."""


class AlternateShippingAddress(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this shipping address, unique across all
    shipping addresses.

    **NOTE**: Shipping addresses do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 41 characters.
    """

    city: str
    """The city, district, suburb, town, or village name of the shipping address.

    Maximum length: 31 characters.
    """

    country: str
    """The country name of the shipping address."""

    is_default_shipping_address: Annotated[bool, PropertyInfo(alias="isDefaultShippingAddress")]
    """Indicates whether this shipping address is the default shipping address."""

    line1: str
    """The first line of the shipping address (e.g., street, PO Box, or company name).

    Maximum length: 41 characters.
    """

    line2: str
    """
    The second line of the shipping address, if needed (e.g., apartment, suite,
    unit, or building).

    Maximum length: 41 characters.
    """

    line3: str
    """The third line of the shipping address, if needed.

    Maximum length: 41 characters.
    """

    line4: str
    """The fourth line of the shipping address, if needed.

    Maximum length: 41 characters.
    """

    line5: str
    """The fifth line of the shipping address, if needed.

    Maximum length: 41 characters.
    """

    note: str
    """
    A note written at the bottom of the shipping address in the form in which it
    appears, such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the shipping address.

    Maximum length: 13 characters.
    """

    state: str
    """The state, county, province, or region name of the shipping address.

    Maximum length: 21 characters.
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


class CreditCard(TypedDict, total=False):
    address: str
    """The card's billing address."""

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


class CustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the contact field."""


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
