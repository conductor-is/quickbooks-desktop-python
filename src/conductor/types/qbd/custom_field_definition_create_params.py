# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomFieldDefinitionCreateParams"]


class CustomFieldDefinitionCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique among the custom fields of its owner.

    For a public custom field, this is the label QuickBooks shows.
    """

    object_types: Required[
        Annotated[
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
            PropertyInfo(alias="objectTypes"),
        ]
    ]
    """The types of records the custom field applies to.

    A public custom field takes either `"item"` or any of `"customer"`, `"vendor"`,
    and `"employee"`, and QuickBooks adds transaction types itself, which the
    returned definition's `objectTypes` lists: a customer, vendor, or employee
    custom field applies to those transactions themselves, and an item custom field
    to their lines. A private custom field takes any of these types.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    owner_id: Annotated[str, PropertyInfo(alias="ownerId")]
    """The owner of the custom field.

    Defaults to `"0"`, the owner of public custom fields, which QuickBooks users
    define and see. Any other owner is an application's GUID in braces, such as
    `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
    only in requests that name it.
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
    """The data type of the custom field's values.

    Defaults to `"string_255_type"`, the only type QuickBooks accepts for a public
    custom field.
    """
