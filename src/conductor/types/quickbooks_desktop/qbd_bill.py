# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdBill",
    "AccountsPayableAccount",
    "Currency",
    "CustomField",
    "ExpenseLine",
    "ExpenseLineAccount",
    "ExpenseLineClass",
    "ExpenseLineCustomer",
    "ExpenseLineCustomField",
    "ExpenseLineSalesRepresentative",
    "ExpenseLineSalesTaxCode",
    "ItemGroupLine",
    "ItemGroupLineCustomField",
    "ItemGroupLineItemGroup",
    "ItemGroupLineItem",
    "ItemGroupLineItemClass",
    "ItemGroupLineItemCustomer",
    "ItemGroupLineItemCustomField",
    "ItemGroupLineItemInventorySite",
    "ItemGroupLineItemInventorySiteLocation",
    "ItemGroupLineItemItem",
    "ItemGroupLineItemOverrideUnitOfMeasure",
    "ItemGroupLineItemSalesRepresentative",
    "ItemGroupLineItemSalesTaxCode",
    "ItemLine",
    "ItemLineClass",
    "ItemLineCustomer",
    "ItemLineCustomField",
    "ItemLineInventorySite",
    "ItemLineInventorySiteLocation",
    "ItemLineItem",
    "ItemLineOverrideUnitOfMeasure",
    "ItemLineSalesRepresentative",
    "ItemLineSalesTaxCode",
    "LinkedTransaction",
    "SalesTaxCode",
    "Terms",
    "Vendor",
    "VendorAddress",
]


class AccountsPayableAccount(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class Currency(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class CustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ExpenseLineAccount(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ExpenseLineClass(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ExpenseLineCustomer(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ExpenseLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ExpenseLineSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ExpenseLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ExpenseLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    account: Optional[ExpenseLineAccount] = None

    amount: Optional[str] = None

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billable status of this line item."""

    class_: Optional[ExpenseLineClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    customer: Optional[ExpenseLineCustomer] = None

    custom_fields: List[ExpenseLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    memo: Optional[str] = None

    sales_representative: Optional[ExpenseLineSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The expense's sales representative."""

    sales_tax_code: Optional[ExpenseLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """


class ItemGroupLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemGroupLineItemGroup(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemClass(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemCustomer(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemGroupLineItemInventorySite(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemItem(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemOverrideUnitOfMeasure(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItemSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemGroupLineItem(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billable status of this line item."""

    class_: Optional[ItemGroupLineItemClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    cost: Optional[str] = None

    customer: Optional[ItemGroupLineItemCustomer] = None

    custom_fields: List[ItemGroupLineItemCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    inventory_site: Optional[ItemGroupLineItemInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The inventory site location where the item is stored."""

    inventory_site_location: Optional[ItemGroupLineItemInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """The location within the inventory site where the item is stored."""

    item: Optional[ItemGroupLineItemItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    override_unit_of_measure: Optional[ItemGroupLineItemOverrideUnitOfMeasure] = FieldInfo(
        alias="overrideUnitOfMeasure", default=None
    )

    quantity: Optional[float] = None

    sales_representative: Optional[ItemGroupLineItemSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The item's sales representative."""

    sales_tax_code: Optional[ItemGroupLineItemSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class ItemGroupLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    custom_fields: List[ItemGroupLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    item_group: ItemGroupLineItemGroup = FieldInfo(alias="itemGroup")

    items: List[ItemGroupLineItem]

    quantity: Optional[float] = None

    total_amount: str = FieldInfo(alias="totalAmount")

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class ItemLineClass(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineCustomer(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemLineInventorySite(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineItem(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineOverrideUnitOfMeasure(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class ItemLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billable status of this line item."""

    class_: Optional[ItemLineClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    cost: Optional[str] = None

    customer: Optional[ItemLineCustomer] = None

    custom_fields: List[ItemLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    inventory_site: Optional[ItemLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The inventory site location where the item is stored."""

    inventory_site_location: Optional[ItemLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """The location within the inventory site where the item is stored."""

    item: Optional[ItemLineItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    override_unit_of_measure: Optional[ItemLineOverrideUnitOfMeasure] = FieldInfo(
        alias="overrideUnitOfMeasure", default=None
    )

    quantity: Optional[float] = None

    sales_representative: Optional[ItemLineSalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The item's sales representative."""

    sales_tax_code: Optional[ItemLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class LinkedTransaction(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction, unique across all
    transactions.
    """

    amount: str

    link_type: Optional[Literal["amount", "quantity"]] = FieldInfo(alias="linkType", default=None)
    """
    Indicates how transactions are linked: "amount" denotes an amount-based link
    (e.g., an invoice linked to a payment), and "quantity" denotes a quantity-based
    link (e.g., an invoice created from a sales order based on the quantity of items
    received).
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """The user-defined identifier for the transaction.

    It is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. Case sensitive.
    """

    transaction_date: str = FieldInfo(alias="transactionDate")

    transaction_type: Literal[
        "bill_payment_check",
        "bill_payment_credit_card",
        "build_assembly",
        "charge",
        "check",
        "credit_card_charge",
        "credit_card_credit",
        "credit_memo",
        "deposit",
        "estimate",
        "inventory_adjustment",
        "invoice",
        "item_receipt",
        "journal_entry",
        "liability_adjustment",
        "paycheck",
        "payroll_liability_check",
        "purchase_order",
        "receive_payment",
        "sales_order",
        "sales_receipt",
        "sales_tax_payment_check",
        "transfer",
        "vendor_credit",
        "ytd_adjustment",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction."""


class SalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class Terms(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class Vendor(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class VendorAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class QbdBill(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction, unique across all
    transactions.
    """

    accounts_payable_account: Optional[AccountsPayableAccount] = FieldInfo(alias="accountsPayableAccount", default=None)
    """The accounts payable account in QuickBooks to which the bill is assigned.

    This account is used to track the amount owed to the vendor.
    """

    amount_due: str = FieldInfo(alias="amountDue")
    """The total monetary amount of the bill, as a string-encoded decimal.

    This will be the sum of the amounts on the bill's expense lines, item lines, and
    item group lines. This will equal `openAmount` plus any credits or discounts.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The total monetary amount of the transaction converted to the account's base
    currency, as a string-encoded decimal.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The bill's currency."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    due_date: Optional[str] = FieldInfo(alias="dueDate", default=None)
    """The date by which the bill must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The exchange rate between this currency and the account's base currency at the
    time of the transaction, expressed as a decimal value (e.g., `1.2345` for 1 EUR
    = 1.2345 USD if USD is the base currency).
    """

    expense_lines: List[ExpenseLine] = FieldInfo(alias="expenseLines")
    """
    The expense lines on the bill, specifying the accounts and amounts for the goods
    or services purchased.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    is_paid: Optional[bool] = FieldInfo(alias="isPaid", default=None)
    """Whether the bill has been fully paid."""

    item_group_lines: List[ItemGroupLine] = FieldInfo(alias="itemGroupLines")

    item_lines: List[ItemLine] = FieldInfo(alias="itemLines")

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")

    memo: Optional[str] = None
    """A note or description of the bill, as entered by the user."""

    object_type: Literal["qbd_bill"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill"`."""

    open_amount: Optional[str] = FieldInfo(alias="openAmount", default=None)
    """The remaining amount due on the bill, as a string-encoded decimal.

    This will equal `amountDue` minus any credits or discounts.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """The user-defined identifier for the transaction.

    It is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. Case sensitive.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    terms: Optional[Terms] = None
    """The bill's payment terms."""

    transaction_date: str = FieldInfo(alias="transactionDate")
    """The date of the bill, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when the object was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    vendor: Vendor
    """
    The vendor or company from whom the bill is received for goods or services
    purchased.
    """

    vendor_address: Optional[VendorAddress] = FieldInfo(alias="vendorAddress", default=None)

    version: str
    """The current version identifier of the object that changes with each
    modification.

    Provide this value when updating the object to verify you are working with the
    latest version; mismatched values will fail.
    """
