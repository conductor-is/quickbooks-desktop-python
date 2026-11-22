# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomFieldDefinition"]


class CustomFieldDefinition(BaseModel):
    id: str
    """
    The identifier of this custom field definition, which is its `name`, so it
    changes when the definition is renamed.
    """

    format: Optional[str] = None
    """
    The format QuickBooks applies to this custom field's values, as QuickBooks names
    it. QuickBooks does not report this for private custom fields.
    """

    is_required_for_list_objects: Optional[bool] = FieldInfo(alias="isRequiredForListObjects", default=None)
    """
    Indicates whether QuickBooks requires a value for this custom field on list
    objects, such as customers and items. QuickBooks does not report this for
    private custom fields.
    """

    is_required_for_transactions: Optional[bool] = FieldInfo(alias="isRequiredForTransactions", default=None)
    """
    Indicates whether QuickBooks requires a value for this custom field on
    transactions. QuickBooks does not report this for private custom fields.
    """

    name: str
    """The name of this custom field, unique among the custom fields of its owner.

    For a public custom field, this is the label QuickBooks shows.
    """

    object_type: Literal["qbd_custom_field_definition"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_custom_field_definition"`."""

    object_types: List[
        Literal[
            "account",
            "ar_refund_credit_card",
            "bill",
            "bill_payment_check",
            "bill_payment_credit_card",
            "build_assembly",
            "charge",
            "check",
            "company",
            "credit_card_charge",
            "credit_card_credit",
            "credit_memo",
            "customer",
            "deposit",
            "employee",
            "estimate",
            "inventory_adjustment",
            "invoice",
            "item",
            "item_receipt",
            "journal_entry",
            "other_name",
            "purchase_order",
            "receive_payment",
            "sales_order",
            "sales_receipt",
            "sales_tax_payment_check",
            "vendor",
            "vendor_credit",
        ]
    ] = FieldInfo(alias="objectTypes")
    """The types of records this custom field applies to.

    For a public custom field, this includes the transaction types QuickBooks adds
    itself: a customer, vendor, or employee custom field applies to the listed
    transactions themselves, and an item custom field to their lines.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The owner of this custom field: `"0"` for a public custom field, which
    QuickBooks users define and see, or an application's GUID in braces for a
    private custom field, which appears only in requests that name that owner.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field's values.

    Public custom fields are always `string_255_type`.
    """
