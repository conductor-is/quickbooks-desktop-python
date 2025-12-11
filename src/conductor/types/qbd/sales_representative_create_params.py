# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesRepresentativeCreateParams"]


class SalesRepresentativeCreateParams(TypedDict, total=False):
    entity_id: Required[Annotated[str, PropertyInfo(alias="entityId")]]
    """
    The sales representative's corresponding person entity in QuickBooks, stored as
    either an employee, vendor, or other-name entry.
    """

    initial: Required[str]
    """The initials of this sales representative's name.

    Maximum length: 5 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales representative is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """
