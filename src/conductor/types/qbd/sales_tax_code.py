# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesTaxCode", "SalesTaxItem"]


class SalesTaxItem(BaseModel):
    """
    The sales-tax item used to calculate the actual tax amount for this sales-tax code's transactions by applying a specific tax rate collected for a single tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this field drives the actual tax calculation and reporting.
    """

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


class SalesTaxCode(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales-tax code.

    This ID is unique across all sales-tax codes but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales-tax code was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    description: Optional[str] = None
    """A description of this sales-tax code."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this sales-tax code is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    is_taxable: bool = FieldInfo(alias="isTaxable")
    """Indicates whether this sales-tax code is tracking taxable sales.

    This field cannot be modified once the sales-tax code has been used in a
    transaction.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax code, unique across all
    sales-tax codes. This short name will appear on sales forms to identify the tax
    status of an item.

    **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_sales_tax_code"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_code"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this sales-tax code object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_tax_item: Optional[SalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this sales-tax
    code's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales-tax code was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
