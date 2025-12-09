# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Company",
    "AccountantCopy",
    "Address",
    "AddressForCustomer",
    "CustomField",
    "LegalAddress",
    "SubscribedServices",
    "SubscribedServicesService",
]


class AccountantCopy(BaseModel):
    """Information about the accountant's copy for this company file.

    An accountant's copy allows an accountant to make changes while the business continues normal operations. It includes a dividing date that defines the fiscal period the accountant can work on, with restrictions on transactions and accounts within that period. While an accountant copy exists, users cannot modify transactions dated on or before the dividing date, cannot add subaccounts to existing accounts, and cannot edit, merge, or make existing accounts inactive.
    """

    accountant_copy_exists: bool = FieldInfo(alias="accountantCopyExists")
    """Indicates whether an accountant copy has been made for this company file.

    An accountant copy allows an accountant to work on the books while the business
    continues daily operations.
    """

    dividing_date: Optional[str] = FieldInfo(alias="dividingDate", default=None)
    """
    The fiscal period dividing date for accountant work, in ISO 8601 format
    (YYYY-MM-DD). While an accountant copy exists, transactions within this period
    cannot be modified or created. New accounts can be added, but existing accounts
    cannot have new subaccounts, be edited, merged, or made inactive. List items
    cannot be deleted or merged.
    """


class Address(BaseModel):
    """
    The company's address, used on its invoices, checks, and other forms (along with `companyName`). This is different from the company's legal address used on tax forms and pay stubs (along with `legalCompanyName`).
    """

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


class AddressForCustomer(BaseModel):
    """The address where this company receives mail from its customers."""

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


class LegalAddress(BaseModel):
    """
    The company's legal address used on its tax forms and pay stubs (along with `legalCompanyName`). This is different from the company's `address` used on invoices, checks, and other forms (along with `companyName`).
    """

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


class SubscribedServicesService(BaseModel):
    domain: Optional[str] = None
    """The domain of this subscribed service"""

    name: str
    """The case-insensitive unique name of this service, unique across all services.

    **NOTE**: Services do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    service_status: Optional[Literal["active", "expired", "never", "pending", "suspended", "terminated", "trial"]] = (
        FieldInfo(alias="serviceStatus", default=None)
    )
    """The status of this service's subscription."""


class SubscribedServices(BaseModel):
    """
    The Intuit services that this company is or has been subscribed to, such as Intuit Payroll.
    """

    services: List[SubscribedServicesService]
    """
    The list of Intuit services that this company is or has been subscribed to, for
    example, Intuit Payroll, QBMS.
    """


class Company(BaseModel):
    accountant_copy: Optional[AccountantCopy] = FieldInfo(alias="accountantCopy", default=None)
    """Information about the accountant's copy for this company file.

    An accountant's copy allows an accountant to make changes while the business
    continues normal operations. It includes a dividing date that defines the fiscal
    period the accountant can work on, with restrictions on transactions and
    accounts within that period. While an accountant copy exists, users cannot
    modify transactions dated on or before the dividing date, cannot add subaccounts
    to existing accounts, and cannot edit, merge, or make existing accounts
    inactive.
    """

    address: Optional[Address] = None
    """
    The company's address, used on its invoices, checks, and other forms (along with
    `companyName`). This is different from the company's legal address used on tax
    forms and pay stubs (along with `legalCompanyName`).
    """

    address_for_customer: Optional[AddressForCustomer] = FieldInfo(alias="addressForCustomer", default=None)
    """The address where this company receives mail from its customers."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the QuickBooks user's business associated with this company.

    This name is used on invoices, checks, and other forms, while `legalCompanyName`
    is used on tax forms and pay stubs.
    """

    company_type: Optional[str] = FieldInfo(alias="companyType", default=None)
    """
    The company type, which the QuickBooks user selected from a list when creating
    the company file.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the company object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    ein: Optional[str] = None
    """The company's Employer Identification Number."""

    email: Optional[str] = None
    """The company's email address."""

    fax: Optional[str] = None
    """The company's fax number."""

    fiscal_year_start_month: Optional[
        Literal[
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]
    ] = FieldInfo(alias="fiscalYearStartMonth", default=None)
    """
    The first month of this company's fiscal year, which determines the default date
    range for financial reports.
    """

    income_tax_year_start_month: Optional[
        Literal[
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]
    ] = FieldInfo(alias="incomeTaxYearStartMonth", default=None)
    """
    The first month of this company's income tax year, which determines the default
    date range for financial reports.
    """

    is_sample_company_file: bool = FieldInfo(alias="isSampleCompanyFile")
    """
    Indicates whether the connected QuickBooks company file is a "sample file",
    which is a mock company file used for testing.
    """

    legal_address: Optional[LegalAddress] = FieldInfo(alias="legalAddress", default=None)
    """
    The company's legal address used on its tax forms and pay stubs (along with
    `legalCompanyName`). This is different from the company's `address` used on
    invoices, checks, and other forms (along with `companyName`).
    """

    legal_company_name: Optional[str] = FieldInfo(alias="legalCompanyName", default=None)
    """The legal name of this company's business, as specified in QuickBooks.

    This value is used on tax forms and pay stubs, while `companyName` is used on
    invoices, checks, and other forms.
    """

    phone: Optional[str] = None
    """The company's primary telephone number."""

    ssn: Optional[str] = None
    """The company's Social Security Number. The value can be with or without dashes.

    **NOTE**: This field cannot be changed after the company is created.
    """

    subscribed_services: Optional[SubscribedServices] = FieldInfo(alias="subscribedServices", default=None)
    """
    The Intuit services that this company is or has been subscribed to, such as
    Intuit Payroll.
    """

    tax_form: Optional[
        Literal[
            "form_1040", "form_1065", "form_1120", "form_1120s", "form_990", "form_990pf", "form_990t", "other_or_none"
        ]
    ] = FieldInfo(alias="taxForm", default=None)
    """The tax form that the QuickBooks user expects to file for this company's taxes.

    When a specific tax form is selected (any value other than `other_or_none`),
    QuickBooks allows associating each account with a specific tax form line. This
    association appears in account query responses.
    """

    website: Optional[str] = None
    """The company's public website."""
