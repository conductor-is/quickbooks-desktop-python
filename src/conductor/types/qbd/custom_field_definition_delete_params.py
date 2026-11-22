# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomFieldDefinitionDeleteParams"]


class CustomFieldDefinitionDeleteParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The owner of the custom field.

    Defaults to `"0"`, the owner of public custom fields, which QuickBooks users
    define and see. Any other owner is an application's GUID in braces, such as
    `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
    only in requests that name it.
    """
