# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OtherNameUpdateParams", "Address"]


class OtherNameUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the other-name object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The other-name's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    address: Address
    """The other-name's address."""

    alternate_contact: Annotated[str, PropertyInfo(alias="alternateContact")]
    """The name of a alternate contact person for this other-name."""

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The other-name's alternate telephone number."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """The name of the company associated with this other-name.

    This name is used on invoices, checks, and other forms.
    """

    contact: str
    """The name of the primary contact person for this other-name."""

    email: str
    """The other-name's email address."""

    fax: str
    """The other-name's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the contact person for this other-name.

    Maximum length: 25 characters.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this other-name is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the contact person for this other-name.

    Maximum length: 25 characters.
    """

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The middle name of the contact person for this other-name.

    Maximum length: 5 characters.
    """

    name: str
    """
    The case-insensitive unique name of this other-name, unique across all
    other-names.

    **NOTE**: Other-names do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    note: str
    """A note or comment about this other-name."""

    phone: str
    """The other-name's primary telephone number."""

    salutation: str
    """
    The formal salutation title that precedes the name of the contact person for
    this other-name, such as "Mr.", "Ms.", or "Dr.".
    """


class Address(TypedDict, total=False):
    """The other-name's address."""

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
