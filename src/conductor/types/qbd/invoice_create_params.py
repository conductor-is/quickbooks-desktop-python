# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InvoiceCreateParams",
    "ApplyCredit",
    "BillingAddress",
    "LineGroup",
    "LineGroupCustomField",
    "Line",
    "LineCustomField",
    "LineLinkToTransactionLine",
    "ShippingAddress",
]


class InvoiceCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer or customer-job associated with this invoice."""

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this invoice, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    apply_credits: Annotated[Iterable[ApplyCredit], PropertyInfo(alias="applyCredits")]
    """Credit memos to apply to this invoice, reducing its balance.

    This creates a link between this invoice and the specified credit memos.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transactions in this endpoint's response even when this request is
    successful. To see the transactions linked via this field, refetch the invoice
    and check the `linkedTransactions` response field. If fetching a list of
    invoices, you must also specify the parameter `includeLinkedTransactions=true`
    to see the `linkedTransactions` response field.
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The invoice's billing address."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this invoice's line items
    unless overridden at the line item level.
    """

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the invoice."""

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this invoice when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD).

    **NOTE**: If `dueDate` is excluded when creating this invoice, QuickBooks might
    determine the due date according to the terms set for this customer.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this invoice's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_finance_charge: Annotated[bool, PropertyInfo(alias="isFinanceCharge")]
    """Whether this invoice includes a finance charge.

    This field is immutable and can only be set during invoice creation.
    """

    is_pending: Annotated[bool, PropertyInfo(alias="isPending")]
    """Indicates whether this invoice has not been completed or is in a draft version."""

    is_queued_for_email: Annotated[bool, PropertyInfo(alias="isQueuedForEmail")]
    """
    Indicates whether this invoice is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this invoice is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: Annotated[Iterable[LineGroup], PropertyInfo(alias="lineGroups")]
    """
    The invoice's line item groups, each representing a predefined set of related
    items.
    """

    lines: Iterable[Line]
    """The invoice's line items, each representing a single product or service sold."""

    link_to_transaction_ids: Annotated[List[str], PropertyInfo(alias="linkToTransactionIds")]
    """
    IDs of existing transactions that you wish to link to this invoice, such as
    payments applied, credits used, or associated purchase orders. Note that this
    links entire transactions, not individual transaction lines. If you want to link
    individual lines in a transaction, instead use the field `linkToTransactionLine`
    on this invoice's lines, if available.

    Transactions can only be linked when creating this invoice and cannot be
    unlinked later.

    You can use both `linkToTransactionIds` (on this invoice) and
    `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
    to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
    will also return an error if you attempt to link a transaction that is empty or
    already closed.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transactions in this endpoint's response even when this request is
    successful. To see the transactions linked via this field, refetch the invoice
    and check the `linkedTransactions` response field. If fetching a list of
    invoices, you must also specify the parameter `includeLinkedTransactions=true`
    to see the `linkedTransactions` response field.
    """

    memo: str
    """A memo or note for this invoice that appears in reports, but not on the invoice.

    Use `customerMessage` to add a note to this invoice.
    """

    other_custom_field: Annotated[str, PropertyInfo(alias="otherCustomField")]
    """A built-in custom field for additional information specific to this invoice.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoices for convenience. Developers often
    use this field for tracking information that doesn't fit into other standard
    QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
    line item fields, this exists at the transaction level. Hidden by default in the
    QuickBooks UI.
    """

    purchase_order_number: Annotated[str, PropertyInfo(alias="purchaseOrderNumber")]
    """The customer's Purchase Order (PO) number associated with this invoice.

    This field is often used to cross-reference the invoice with the customer's
    purchasing system.
    """

    receivables_account_id: Annotated[str, PropertyInfo(alias="receivablesAccountId")]
    """
    The Accounts-Receivable (A/R) account to which this invoice is assigned, used to
    track the amount owed. If not specified, QuickBooks Desktop will use its default
    A/R account.

    **IMPORTANT**: If this invoice is linked to other transactions, this A/R account
    must match the `receivablesAccount` used in all linked transactions. For
    example, when refunding a credit card payment, the A/R account must match the
    one used in the original credit transactions being refunded.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this invoice, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user. When left blank in
    this create request, this field will be left blank in QuickBooks (i.e., it does
    _not_ auto-increment).
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The invoice's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this invoice, determining whether it is taxable or
    non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this invoice's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.

    For invoices, while using this field to specify a single tax item/group that
    applies uniformly is recommended, complex tax scenarios may require alternative
    approaches. In such cases, you can set this field to a 0% tax item
    (conventionally named "Tax Calculated On Invoice") and handle tax calculations
    through line items instead. When using line items for taxes, note that only
    individual tax items (not tax groups) can be used, subtotals can help apply a
    tax to multiple items but only the first tax line after a subtotal is calculated
    automatically (subsequent tax lines require manual amounts), and the rate column
    will always display the actual tax amount rather than the rate percentage.
    """

    shipment_origin: Annotated[str, PropertyInfo(alias="shipmentOrigin")]
    """
    The origin location from where the product associated with this invoice is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The invoice's shipping address."""

    shipping_date: Annotated[Union[str, date], PropertyInfo(alias="shippingDate", format="iso8601")]
    """
    The date when the products or services for this invoice were shipped or are
    expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]
    """
    The shipping method used for this invoice, such as standard mail or overnight
    delivery.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The invoice's payment terms, defining when payment is due and any applicable
    discounts.
    """


class ApplyCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """The amount of credit applied to this transaction.

    This could include customer deposits, payments, or credits. Represented as a
    decimal string.
    """

    credit_transaction_id: Required[Annotated[str, PropertyInfo(alias="creditTransactionId")]]
    """
    The unique identifier of the credit transaction (credit memo or vendor credit)
    to apply to this transaction.
    """

    override_credit_application: Annotated[bool, PropertyInfo(alias="overrideCreditApplication")]
    """Indicates whether to override the credit."""


class BillingAddress(TypedDict, total=False):
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


class LineGroupCustomField(TypedDict, total=False):
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


class LineGroup(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]
    """
    The invoice line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    custom_fields: Annotated[Iterable[LineGroupCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the invoice line group object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item group associated with this
    invoice line group is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item group associated with this invoice line group is stored.
    """

    quantity: float
    """The quantity of the item group associated with this invoice line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this invoice line group.

    Must be a valid unit within the item's available units of measure.
    """


class LineCustomField(TypedDict, total=False):
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


class LineLinkToTransactionLine(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The ID of the transaction to which to link this transaction."""

    transaction_line_id: Required[Annotated[str, PropertyInfo(alias="transactionLineId")]]
    """The ID of the transaction line to which to link this transaction."""


class Line(TypedDict, total=False):
    amount: str
    """The monetary amount of this invoice line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: Annotated[Iterable[LineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the invoice line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: str
    """A description of this invoice line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this invoice line
    is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this invoice line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this invoice line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    link_to_transaction_line: Annotated[LineLinkToTransactionLine, PropertyInfo(alias="linkToTransactionLine")]
    """An existing transaction line that you wish to link to this invoice line.

    Note that this only links to a single transaction line item, not an entire
    transaction. If you want to link an entire transaction and bring in all its
    lines, instead use the field `linkToTransactionIds` on the parent transaction,
    if available. For invoice lines, you can only link to sales orders; QuickBooks
    does not support linking invoice lines to other transaction types.

    Transaction lines can only be linked when creating this invoice line and cannot
    be unlinked later.

    **IMPORTANT**: If you use `linkToTransactionLine` on this invoice line, you
    cannot use the field `item` on this line (QuickBooks will return an error)
    because this field brings in all of the item information you need. You can,
    however, specify whatever `quantity` or `rate` that you want, or any other
    transaction line element other than `item`.

    If the parent transaction supports the `linkToTransactionIds` field, you can use
    both `linkToTransactionLine` (on this invoice line) and `linkToTransactionIds`
    (on its parent transaction) in the same request as long as they do NOT link to
    the same transaction (otherwise, QuickBooks will return an error). QuickBooks
    will also return an error if you attempt to link a transaction that is empty or
    already closed.

    **IMPORTANT**: By default, QuickBooks will not return any information about the
    linked transaction line in this endpoint's response even when this request is
    successful. To see the transaction line linked via this field, refetch the
    parent invoice and check the `linkedTransactions` response field. If fetching a
    list of invoices, you must also specify the parameter
    `includeLinkedTransactions=true` to see the `linkedTransactions` response field.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this invoice line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """A built-in custom field for additional information specific to this invoice
    line.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoice lines for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    invoice line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all invoice lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this invoice line, overriding the default account
    associated with the item.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this invoice line.

    This overrides any price level set on the corresponding customer. The resulting
    invoice line will not show this price level, only the final `rate` calculated
    from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    invoice line.
    """

    quantity: float
    """The quantity of the item associated with this invoice line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: str
    """The price per unit for this invoice line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this invoice line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this invoice line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this invoice line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Annotated[Union[str, date], PropertyInfo(alias="serviceDate", format="iso8601")]
    """
    The date on which the service for this invoice line was or will be performed, in
    ISO 8601 format (YYYY-MM-DD). This is particularly relevant for service items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this invoice line.

    Must be a valid unit within the item's available units of measure.
    """


class ShippingAddress(TypedDict, total=False):
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
