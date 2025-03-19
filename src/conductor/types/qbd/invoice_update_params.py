# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InvoiceUpdateParams",
    "ApplyCredit",
    "BillingAddress",
    "LineGroup",
    "LineGroupLine",
    "Line",
    "ShippingAddress",
]


class InvoiceUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the invoice object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

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

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this invoice."""

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the invoice."""

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this invoice when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this invoice's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
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

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line item groups for the invoice with this array. To keep any existing line
       item groups, you must include them in this array even if they have not
       changed. **Any line item groups not included will be removed.**

    2. To add a new line item group, include it here with the `id` field set to
       `-1`.

    3. If you do not wish to modify any line item groups, omit this field entirely
       to keep them unchanged.
    """

    lines: Iterable[Line]
    """The invoice's line items, each representing a single product or service sold.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line items for the invoice with this array. To keep any existing line items,
       you must include them in this array even if they have not changed. **Any line
       items not included will be removed.**

    2. To add a new line item, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any line items, omit this field entirely to keep
       them unchanged.
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
    unique and can be arbitrarily changed by the QuickBooks user.
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

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this invoice, in ISO 8601 format (YYYY-MM-DD)."""


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


class LineGroupLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new invoice lines you wish to add.
    """

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

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
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


class LineGroup(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line group you
    wish to retain or update.

    **IMPORTANT**: Set this field to `-1` for new invoice line groups you wish to
    add.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The invoice line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: Iterable[LineGroupLine]
    """
    The invoice line group's line items, each representing a single product or
    service sold.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line items for the invoice line group with this array. To keep any existing
       line items, you must include them in this array even if they have not
       changed. **Any line items not included will be removed.**

    2. To add a new line item, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any line items, omit this field entirely to keep
       them unchanged.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
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


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new invoice lines you wish to add.
    """

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

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
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
