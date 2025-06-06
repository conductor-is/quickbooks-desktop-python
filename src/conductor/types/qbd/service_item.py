# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ServiceItem",
    "Class",
    "CustomField",
    "Parent",
    "SalesAndPurchaseDetails",
    "SalesAndPurchaseDetailsExpenseAccount",
    "SalesAndPurchaseDetailsIncomeAccount",
    "SalesAndPurchaseDetailsPreferredVendor",
    "SalesAndPurchaseDetailsPurchaseTaxCode",
    "SalesOrPurchaseDetails",
    "SalesOrPurchaseDetailsPostingAccount",
    "SalesTaxCode",
    "UnitOfMeasureSet",
]


class Class(BaseModel):
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


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
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
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class Parent(BaseModel):
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


class SalesAndPurchaseDetailsExpenseAccount(BaseModel):
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


class SalesAndPurchaseDetailsIncomeAccount(BaseModel):
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


class SalesAndPurchaseDetailsPreferredVendor(BaseModel):
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


class SalesAndPurchaseDetailsPurchaseTaxCode(BaseModel):
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


class SalesAndPurchaseDetails(BaseModel):
    expense_account: SalesAndPurchaseDetailsExpenseAccount = FieldInfo(alias="expenseAccount")
    """The expense account used to track costs from purchases of this item."""

    income_account: SalesAndPurchaseDetailsIncomeAccount = FieldInfo(alias="incomeAccount")
    """The income account used to track revenue from sales of this item."""

    preferred_vendor: Optional[SalesAndPurchaseDetailsPreferredVendor] = FieldInfo(
        alias="preferredVendor", default=None
    )
    """The preferred vendor from whom this item is typically purchased."""

    purchase_cost: Optional[str] = FieldInfo(alias="purchaseCost", default=None)
    """
    The cost at which this item is purchased from vendors, represented as a decimal
    string.
    """

    purchase_description: Optional[str] = FieldInfo(alias="purchaseDescription", default=None)
    """
    The description of this item that appears on purchase forms (e.g., checks,
    bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code: Optional[SalesAndPurchaseDetailsPurchaseTaxCode] = FieldInfo(
        alias="purchaseTaxCode", default=None
    )
    """The tax code applied to purchases of this item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Optional[str] = FieldInfo(alias="salesDescription", default=None)
    """
    The description of this item that appears on sales forms (e.g., invoices, sales
    receipts) when sold to customers.
    """

    sales_price: Optional[str] = FieldInfo(alias="salesPrice", default=None)
    """
    The price at which this item is sold to customers, represented as a decimal
    string.
    """


class SalesOrPurchaseDetailsPostingAccount(BaseModel):
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


class SalesOrPurchaseDetails(BaseModel):
    description: Optional[str] = None
    """A description of this item."""

    posting_account: Optional[SalesOrPurchaseDetailsPostingAccount] = FieldInfo(alias="postingAccount", default=None)
    """The posting account to which transactions involving this item are posted.

    This could be an income account when selling or an expense account when
    purchasing.
    """

    price: Optional[str] = None
    """
    The price at which this item is purchased or sold, represented as a decimal
    string.
    """

    price_percentage: Optional[str] = FieldInfo(alias="pricePercentage", default=None)
    """
    The price of this item expressed as a percentage, used instead of `price` when
    the item's cost is calculated as a percentage of another amount. For example, a
    service item that costs a percentage of another item's price.
    """


class SalesTaxCode(BaseModel):
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


class UnitOfMeasureSet(BaseModel):
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


class ServiceItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this service item.

    This ID is unique across all service items but not across different QuickBooks
    object types.
    """

    barcode: Optional[str] = None
    """The service item's barcode."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The service item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this service item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the service item object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this service item, formed by
    combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if a service item is under "Consulting" and
    has the `name` "Web-Design", its `fullName` would be "Consulting:Web-Design".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    service item objects. However, `fullName` can still be arbitrarily changed by
    the QuickBooks user when they modify the underlying `name` field.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this service item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """The case-insensitive name of this service item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two service items
    could both have the `name` "Web-Design", but they could have unique `fullName`
    values, such as "Consulting:Web-Design" and "Contracting:Web-Design".
    """

    object_type: Literal["qbd_service_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_service_item"`."""

    parent: Optional[Parent] = None
    """The parent service item one level above this one in the hierarchy.

    For example, if this service item has a `fullName` of "Consulting:Web-Design",
    its parent has a `fullName` of "Consulting". If this service item is at the top
    level, this field will be `null`.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this service item object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_and_purchase_details: Optional[SalesAndPurchaseDetails] = FieldInfo(
        alias="salesAndPurchaseDetails", default=None
    )
    """
    Details for service items that are both purchased and sold, such as reimbursable
    expenses or inventory items that are bought from vendors and sold to customers.

    **IMPORTANT**: A service item will have either `salesAndPurchaseDetails` or
    `salesOrPurchaseDetails`, but never both because an item cannot have both
    configurations.
    """

    sales_or_purchase_details: Optional[SalesOrPurchaseDetails] = FieldInfo(
        alias="salesOrPurchaseDetails", default=None
    )
    """
    Details for service items that are exclusively sold or exclusively purchased,
    but not both. This typically applies to non-inventory items (like a purchased
    office supply that isn't resold) or service items (like consulting services that
    are sold but not purchased).

    **IMPORTANT**: A service item will have either `salesAndPurchaseDetails` or
    `salesOrPurchaseDetails`, but never both because an item cannot have both
    configurations.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The default sales-tax code for this service item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sublevel: float
    """The depth level of this service item in the hierarchy.

    A top-level service item has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, a service item with a `fullName` of
    "Consulting:Web-Design" would have a `sublevel` of 1.
    """

    unit_of_measure_set: Optional[UnitOfMeasureSet] = FieldInfo(alias="unitOfMeasureSet", default=None)
    """
    The unit-of-measure set associated with this service item, which consists of a
    base unit and related units.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this service item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
