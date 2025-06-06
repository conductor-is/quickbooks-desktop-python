# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxCodeCreateParams"]


class SalesTaxCodeCreateParams(TypedDict, total=False):
    is_taxable: Required[Annotated[bool, PropertyInfo(alias="isTaxable")]]
    """Indicates whether this sales-tax code is tracking taxable sales.

    This field cannot be modified once the sales-tax code has been used in a
    transaction.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this sales-tax code, unique across all
    sales-tax codes. This short name will appear on sales forms to identify the tax
    status of an item.

    **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 3 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    description: str
    """A description of this sales-tax code."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax code is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this sales-tax
    code's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """
