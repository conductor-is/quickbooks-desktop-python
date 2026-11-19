# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesOrderSetCustomFieldsParams", "CustomField", "Line", "LineCustomField"]


class SalesOrderSetCustomFieldsParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    custom_fields: Annotated[Iterable[CustomField], PropertyInfo(alias="customFields")]
    """
    The custom field values to set or clear on the sales order itself, not on its
    lines. Custom fields you leave out keep their values.
    """

    lines: Iterable[Line]
    """The lines of the sales order whose custom field values to set or clear.

    Lines you leave out are not changed.
    """


class CustomField(TypedDict, total=False):
    name: Required[str]
    """
    The name of the custom field, as its definition and a record's `customFields`
    show it. QuickBooks matches the name without regard to letter case.
    """

    value: Required[str]
    """The value to set, which replaces the custom field's current value if it has one.

    Send an empty string (`""`) to clear the custom field. A public custom field's
    value can have at most 30 characters, the most QuickBooks keeps.
    """

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The owner of the custom field.

    Defaults to `"0"`, the owner of public custom fields, which QuickBooks users
    define and see. Any other owner is an application's GUID in braces, such as
    `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
    only in requests that name it.
    """


class LineCustomField(TypedDict, total=False):
    name: Required[str]
    """
    The name of the custom field, as its definition and a record's `customFields`
    show it. QuickBooks matches the name without regard to letter case.
    """

    value: Required[str]
    """The value to set, which replaces the custom field's current value if it has one.

    Send an empty string (`""`) to clear the custom field. A public custom field's
    value can have at most 30 characters, the most QuickBooks keeps.
    """

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The owner of the custom field.

    Defaults to `"0"`, the owner of public custom fields, which QuickBooks users
    define and see. Any other owner is an application's GUID in braces, such as
    `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
    only in requests that name it.
    """


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of the sales order line, line group,
    or line inside a line group.
    """

    custom_fields: Required[Annotated[Iterable[LineCustomField], PropertyInfo(alias="customFields")]]
    """The custom field values to set or clear on this line.

    Custom fields you leave out keep their values.
    """
