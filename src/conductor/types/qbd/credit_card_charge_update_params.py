# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditCardChargeUpdateParams", "ExpenseLine", "ItemLineGroup", "ItemLineGroupItemLine", "ItemLine"]


class CreditCardChargeUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the credit card charge object
    you are updating, which you can get by fetching the object first. Provide the
    most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    The bank or credit card account to which money is owed for this credit card
    charge.
    """

    clear_expense_lines: Annotated[bool, PropertyInfo(alias="clearExpenseLines")]
    """
    When `true`, removes all existing expense lines associated with this credit card
    charge. To modify or add individual expense lines, use the field `expenseLines`
    instead.
    """

    clear_item_lines: Annotated[bool, PropertyInfo(alias="clearItemLines")]
    """
    When `true`, removes all existing item lines associated with this credit card
    charge. To modify or add individual item lines, use the field `itemLines`
    instead.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this credit card charge's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: Annotated[Iterable[ExpenseLine], PropertyInfo(alias="expenseLines")]
    """
    The credit card charge's expense lines, each representing one line in this
    expense.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       expense lines for the credit card charge with this array. To keep any
       existing expense lines, you must include them in this array even if they have
       not changed. **Any expense lines not included will be removed.**

    2. To add a new expense line, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any expense lines, omit this field entirely to
       keep them unchanged.
    """

    item_line_groups: Annotated[Iterable[ItemLineGroup], PropertyInfo(alias="itemLineGroups")]
    """
    The credit card charge's item group lines, each representing a predefined set of
    items bundled together because they are commonly purchased together or grouped
    for faster entry.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       item group lines for the credit card charge with this array. To keep any
       existing item group lines, you must include them in this array even if they
       have not changed. **Any item group lines not included will be removed.**

    2. To add a new item group line, include it here with the `id` field set to
       `-1`.

    3. If you do not wish to modify any item group lines, omit this field entirely
       to keep them unchanged.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """
    The credit card charge's item lines, each representing the purchase of a
    specific item or service.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       item lines for the credit card charge with this array. To keep any existing
       item lines, you must include them in this array even if they have not
       changed. **Any item lines not included will be removed.**

    2. To add a new item line, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any item lines, omit this field entirely to keep
       them unchanged.
    """

    memo: str
    """A memo or note for this credit card charge."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    The vendor or company from whom merchandise or services were purchased for this
    credit card charge.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this credit card charge,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this credit card charge, determining whether it is
    taxable or non-taxable. If set, this overrides any sales-tax codes defined on
    the payee. This can be overridden on the credit card charge's individual lines.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD)."""


class ExpenseLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing expense line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new expense lines you wish to add.
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """The expense account being debited (increased) for this expense line.

    The corresponding account being credited is usually a liability account (e.g.,
    Accounts-Payable) or an asset account (e.g., Cash), depending on the transaction
    type.
    """

    amount: str
    """The monetary amount of this expense line, represented as a decimal string."""

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this expense line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The expense line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all expense lines unless overridden here, at the
    transaction line level.
    """

    memo: str
    """A memo or note for this expense line."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    If `account` refers to an Accounts-Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The expense line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this expense line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """


class ItemLineGroupItemLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item line you wish to
    retain or update.

    **IMPORTANT**: Set this field to `-1` for new item lines you wish to add.
    """

    amount: str
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`. This field cannot be cleared.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this item line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: str
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this item line."""

    description: str
    """A description of this item line."""

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this item line, overriding the default account associated
    with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this item line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: float
    """The quantity of the item associated with this item line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this item line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLineGroup(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item line group you
    wish to retain or update.

    **IMPORTANT**: Set this field to `-1` for new item line groups you wish to add.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The item line group's item group, representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    item_lines: Annotated[Iterable[ItemLineGroupItemLine], PropertyInfo(alias="itemLines")]
    """
    The item line group's item lines, each representing the purchase of a specific
    item or service.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       item lines for the item line group with this array. To keep any existing item
       lines, you must include them in this array even if they have not changed.
       **Any item lines not included will be removed.**

    2. To add a new item line, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any item lines, omit this field entirely to keep
       them unchanged.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this item line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: float
    """The quantity of the item group associated with this item line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this item line group.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item line you wish to
    retain or update.

    **IMPORTANT**: Set this field to `-1` for new item lines you wish to add.
    """

    amount: str
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`. This field cannot be cleared.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this item line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: str
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this item line."""

    description: str
    """A description of this item line."""

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this item line, overriding the default account associated
    with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this item line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: float
    """The quantity of the item associated with this item line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this item line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """
