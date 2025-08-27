# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeletedListObject"]


class DeletedListObject(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this deleted list-object.

    This ID is unique across all deleted list-objects but not across different
    QuickBooks object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this deleted list-object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    deleted_at: str = FieldInfo(alias="deletedAt")
    """
    The date and time when this deleted list-object was deleted, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    list_type: Literal[
        "account",
        "billing_rate",
        "class",
        "currency",
        "customer",
        "customer_message",
        "customer_type",
        "date_driven_terms",
        "employee",
        "inventory_site",
        "item_discount",
        "item_fixed_asset",
        "item_group",
        "item_inventory",
        "item_inventory_assembly",
        "item_non_inventory",
        "item_other_charge",
        "item_payment",
        "item_sales_tax",
        "item_sales_tax_group",
        "item_service",
        "item_subtotal",
        "job_type",
        "other_name",
        "payment_method",
        "payroll_item_non_wage",
        "payroll_item_wage",
        "price_level",
        "sales_representative",
        "sales_tax_code",
        "ship_method",
        "standard_terms",
        "to_do",
        "unit_of_measure_set",
        "vehicle",
        "vendor",
        "vendor_type",
        "workers_comp_code",
    ] = FieldInfo(alias="listType")
    """The type of deleted list object (i.e., non-transaction)."""

    object_type: Literal["qbd_deleted_list_object"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deleted_list_object"`."""
