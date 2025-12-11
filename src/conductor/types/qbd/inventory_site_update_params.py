# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventorySiteUpdateParams", "Address"]


class InventorySiteUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the inventory site object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    address: Address
    """The inventory site's address."""

    contact: str
    """The name of the primary contact person for this inventory site."""

    description: str
    """A description of this inventory site."""

    email: str
    """The inventory site's email address."""

    fax: str
    """The inventory site's fax number."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory site is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this inventory site, unique across all
    inventory sites.

    **NOTE**: Inventory sites do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory site one level above this one in the hierarchy."""

    phone: str
    """The inventory site's primary telephone number."""


class Address(TypedDict, total=False):
    """The inventory site's address."""

    city: str
    """The city, district, suburb, town, or village name of the site address.

    Maximum length: 31 characters.
    """

    country: str
    """The country name of the site address."""

    line1: str
    """The first line of the site address (e.g., street, PO Box, or company name).

    Maximum length: 41 characters.
    """

    line2: str
    """
    The second line of the site address, if needed (e.g., apartment, suite, unit, or
    building).

    Maximum length: 41 characters.
    """

    line3: str
    """The third line of the site address, if needed.

    Maximum length: 41 characters.
    """

    line4: str
    """The fourth line of the site address, if needed.

    Maximum length: 41 characters.
    """

    line5: str
    """The fifth line of the site address, if needed.

    Maximum length: 41 characters.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the site address.

    Maximum length: 13 characters.
    """

    state: str
    """The state, county, province, or region name of the site address.

    Maximum length: 21 characters.
    """
