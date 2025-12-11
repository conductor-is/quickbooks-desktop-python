# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ClassCreateParams"]


class ClassCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of this class.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two classes could
    both have the `name` "Marketing", but they could have unique `fullName` values,
    such as "Department:Marketing" and "Internal:Marketing".

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this class is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent class one level above this one in the hierarchy.

    For example, if this class has a `fullName` of "Department:Marketing", its
    parent has a `fullName` of "Department". If this class is at the top level, this
    field will be `null`.
    """
