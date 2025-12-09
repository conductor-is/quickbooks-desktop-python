# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InventorySite", "Address", "Parent"]


class Address(BaseModel):
    """The inventory site's address."""

    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the site address."""

    country: Optional[str] = None
    """The country name of the site address."""

    line1: Optional[str] = None
    """The first line of the site address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the site address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the site address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the site address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the site address, if needed."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the site address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the site address."""


class Parent(BaseModel):
    """The parent inventory site one level above this one in the hierarchy."""

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


class InventorySite(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this inventory site.

    This ID is unique across all inventory sites but not across different QuickBooks
    object types.
    """

    address: Optional[Address] = None
    """The inventory site's address."""

    contact: Optional[str] = None
    """The name of the primary contact person for this inventory site."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this inventory site was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    description: Optional[str] = None
    """A description of this inventory site."""

    email: Optional[str] = None
    """The inventory site's email address."""

    fax: Optional[str] = None
    """The inventory site's fax number."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this inventory site is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """
    Indicates whether this inventory site is the default site used when no specific
    site is provided during the creation of other objects.
    """

    name: str
    """
    The case-insensitive unique name of this inventory site, unique across all
    inventory sites.

    **NOTE**: Inventory sites do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_inventory_site"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_site"`."""

    parent: Optional[Parent] = None
    """The parent inventory site one level above this one in the hierarchy."""

    phone: Optional[str] = None
    """The inventory site's primary telephone number."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this inventory site object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this inventory site was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
