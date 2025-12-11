# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerTypeCreateParams"]


class CustomerTypeCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of this customer type.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two customer
    types could both have the `name` "Healthcare", but they could have unique
    `fullName` values, such as "Industry:Healthcare" and "Region:Healthcare".

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this customer type is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent customer type one level above this one in the hierarchy.

    For example, if this customer type has a `fullName` of "Industry:Healthcare",
    its parent has a `fullName` of "Industry". If this customer type is at the top
    level, this field will be `null`.
    """
