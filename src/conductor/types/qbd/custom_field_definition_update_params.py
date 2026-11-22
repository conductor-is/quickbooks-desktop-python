# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomFieldDefinitionUpdateParams"]


class CustomFieldDefinitionUpdateParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    add_object_types: Annotated[
        List[
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
        ],
        PropertyInfo(alias="addObjectTypes"),
    ]
    """The types of records to also apply the custom field to.

    A public custom field takes only `"customer"`, `"vendor"`, `"employee"`, or
    `"item"`, and QuickBooks adds the matching transaction types itself.
    """

    name: str
    """The new name of the custom field.

    Its values stay with it, and the definition's `id` becomes the new name.
    """

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The owner of the custom field.

    Defaults to `"0"`, the owner of public custom fields, which QuickBooks users
    define and see. Any other owner is an application's GUID in braces, such as
    `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
    only in requests that name it.
    """

    remove_object_types: Annotated[
        List[
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
        ],
        PropertyInfo(alias="removeObjectTypes"),
    ]
    """The types of records to stop applying the custom field to.

    A public custom field takes only `"customer"`, `"vendor"`, `"employee"`, or
    `"item"`, and QuickBooks removes the matching transaction types itself.
    """
