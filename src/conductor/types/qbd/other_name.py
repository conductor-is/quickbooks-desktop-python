# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OtherName", "Address", "CustomField"]


class Address(BaseModel):
    """The other-name's address."""

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


class OtherName(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this other-name.

    This ID is unique across all other-names but not across different QuickBooks
    object types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The other-name's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    address: Optional[Address] = None
    """The other-name's address."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The name of a alternate contact person for this other-name."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The other-name's alternate telephone number."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the company associated with this other-name.

    This name is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The name of the primary contact person for this other-name."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this other-name was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the other-name object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The other-name's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    fax: Optional[str] = None
    """The other-name's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the contact person for this other-name."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this other-name is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the contact person for this other-name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The middle name of the contact person for this other-name."""

    name: str
    """
    The case-insensitive unique name of this other-name, unique across all
    other-names.

    **NOTE**: Other-names do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    note: Optional[str] = None
    """A note or comment about this other-name."""

    object_type: Literal["qbd_other_name"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_other_name"`."""

    phone: Optional[str] = None
    """The other-name's primary telephone number."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this other-name object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    salutation: Optional[str] = None
    """
    The formal salutation title that precedes the name of the contact person for
    this other-name, such as "Mr.", "Ms.", or "Dr.".
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this other-name was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
