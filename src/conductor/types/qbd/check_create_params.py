# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CheckCreateParams",
    "Address",
    "ApplyToTransaction",
    "ExpenseLine",
    "ExpenseLineCustomField",
    "ItemGroupLine",
    "ItemGroupLineCustomField",
    "ItemLine",
    "ItemLineCustomField",
    "ItemLineLinkToTransactionLine",
]


class CheckCreateParams(TypedDict, total=False):
    bank_account_id: Required[Annotated[str, PropertyInfo(alias="bankAccountId")]]
    """
    The bank account from which the funds are being drawn for this check; e.g.,
    Checking or Savings. This check will decrease the balance of this account.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date written on this check, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    address: Address
    """The address that is printed on the check."""

    apply_to_transactions: Annotated[Iterable[ApplyToTransaction], PropertyInfo(alias="applyToTransactions")]
    """Transactions to be paid by this check.

    This will create a link between this check and the specified transactions.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transactions in this endpoint's response even when this request is
    successful. To see the transactions linked via this field, refetch the check and
    check the `linkedTransactions` response field. If fetching a list of checks, you
    must also specify the parameter `includeLinkedTransactions=true` to see the
    `linkedTransactions` response field.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this check's currency and the home currency in
    QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: Annotated[Iterable[ExpenseLine], PropertyInfo(alias="expenseLines")]
    """The check's expense lines, each representing one line in this expense."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this check is included in the queue of documents for
    QuickBooks to print.
    """

    item_group_lines: Annotated[Iterable[ItemGroupLine], PropertyInfo(alias="itemGroupLines")]
    """
    The check's item group lines, each representing a predefined set of items
    bundled together because they are commonly purchased together or grouped for
    faster entry.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """
    The check's item lines, each representing the purchase of a specific item or
    service.
    """

    memo: str
    """The memo that is printed on this check."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """The person or company who will receive this check."""

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this check, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user. When left blank in
    this create request, this field will be left blank in QuickBooks (i.e., it does
    _not_ auto-increment).

    **IMPORTANT**: For checks, this field is the check number.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this check, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the payee.
    This can be overridden on the check's individual lines.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """


class Address(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the address.

    Maximum length: 31 characters.
    """

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name).

    Maximum length: 41 characters.
    """

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).

    Maximum length: 41 characters.
    """

    line3: str
    """The third line of the address, if needed.

    Maximum length: 41 characters.
    """

    line4: str
    """The fourth line of the address, if needed.

    Maximum length: 41 characters.
    """

    line5: str
    """The fifth line of the address, if needed.

    Maximum length: 41 characters.
    """

    note: str
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address.

    Maximum length: 13 characters.
    """

    state: str
    """The state, county, province, or region name of the address.

    Maximum length: 21 characters.
    """


class ApplyToTransaction(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the transaction to be paid by this check."""

    amount: str
    """
    The monetary amount from this check to apply to the specified transaction,
    represented as a decimal string.
    """


class ExpenseLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class ExpenseLine(TypedDict, total=False):
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

    custom_fields: Annotated[Iterable[ExpenseLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the expense line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
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


class ItemGroupLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class ItemGroupLine(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]
    """
    The item group line's item group, representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    custom_fields: Annotated[Iterable[ItemGroupLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the item group line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item group associated with this item
    group line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item group associated with this item group line is stored.
    """

    quantity: float
    """The quantity of the item group associated with this item group line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this item group line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class ItemLineLinkToTransactionLine(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the transaction to which to link this transaction."""

    transaction_line_id: Required[Annotated[str, PropertyInfo(alias="transactionLineId")]]
    """The ID of the transaction line to which to link this transaction."""


class ItemLine(TypedDict, total=False):
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

    custom_fields: Annotated[Iterable[ItemLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the item line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

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

    link_to_transaction_line: Annotated[ItemLineLinkToTransactionLine, PropertyInfo(alias="linkToTransactionLine")]
    """An existing transaction line that you wish to link to this item line.

    Note that this only links to a single transaction line item, not an entire
    transaction. If you want to link an entire transaction and bring in all its
    lines, instead use the field `linkToTransactionIds` on the parent transaction,
    if available. If the parent transaction is a bill or an item receipt, you can
    only link to purchase orders; QuickBooks does not support linking these
    transactions to other transaction types.

    Transaction lines can only be linked when creating this item line and cannot be
    unlinked later.

    **IMPORTANT**: If you use `linkToTransactionLine` on this item line, you cannot
    use the field `item` on this line (QuickBooks will return an error) because this
    field brings in all of the item information you need. You can, however, specify
    whatever `quantity` or `rate` that you want, or any other transaction line
    element other than `item`.

    If the parent transaction supports the `linkToTransactionIds` field, you can use
    both `linkToTransactionLine` (on this item line) and `linkToTransactionIds` (on
    its parent transaction) in the same request as long as they do NOT link to the
    same transaction (otherwise, QuickBooks will return an error). QuickBooks will
    also return an error if you attempt to link a transaction that is empty or
    already closed.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transaction line in this endpoint's response even when this request is
    successful. To see the transaction line linked via this field, refetch the
    parent transaction and check the `linkedTransactions` response field. If
    fetching a list of transactions, you must also specify the parameter
    `includeLinkedTransactions=true` to see the `linkedTransactions` response field.
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
