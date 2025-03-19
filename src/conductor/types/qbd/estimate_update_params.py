# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EstimateUpdateParams", "BillingAddress", "LineGroup", "LineGroupLine", "Line", "ShippingAddress"]


class EstimateUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the estimate object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The estimate's billing address."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The estimate's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this estimate's line
    items unless overridden at the line item level.
    """

    create_change_order: Annotated[bool, PropertyInfo(alias="createChangeOrder")]
    """
    When `true`, creates a "change order" that appears in this estimate's
    description field in QuickBooks's estimate form, specifying exactly what changed
    in this update request, the dollar amount of each change, and the net dollar
    change to this estimate.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this estimate."""

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the estimate."""

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this estimate when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this estimate's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this estimate is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    is_queued_for_email: Annotated[bool, PropertyInfo(alias="isQueuedForEmail")]
    """
    Indicates whether this estimate is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    line_groups: Annotated[Iterable[LineGroup], PropertyInfo(alias="lineGroups")]
    """
    The estimate's line item groups, each representing a predefined set of related
    items.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line item groups for the estimate with this array. To keep any existing line
       item groups, you must include them in this array even if they have not
       changed. **Any line item groups not included will be removed.**

    2. To add a new line item group, include it here with the `id` field set to
       `-1`.

    3. If you do not wish to modify any line item groups, omit this field entirely
       to keep them unchanged.
    """

    lines: Iterable[Line]
    """The estimate's line items, each representing a single product or service quoted.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line items for the estimate with this array. To keep any existing line items,
       you must include them in this array even if they have not changed. **Any line
       items not included will be removed.**

    2. To add a new line item, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any line items, omit this field entirely to keep
       them unchanged.
    """

    memo: str
    """
    A memo or note for this estimate that appears in reports, but not on the
    estimate. Use `customerMessage` to add a note to this estimate.
    """

    other_custom_field: Annotated[str, PropertyInfo(alias="otherCustomField")]
    """A built-in custom field for additional information specific to this estimate.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all estimates for convenience. Developers often
    use this field for tracking information that doesn't fit into other standard
    QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
    line item fields, this exists at the transaction level. Hidden by default in the
    QuickBooks UI.
    """

    purchase_order_number: Annotated[str, PropertyInfo(alias="purchaseOrderNumber")]
    """The customer's Purchase Order (PO) number associated with this estimate.

    This field is often used to cross-reference the estimate with the customer's
    purchasing system.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this estimate, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The estimate's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this estimate, determining whether it is taxable or
    non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this estimate's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    shipment_origin: Annotated[str, PropertyInfo(alias="shipmentOrigin")]
    """
    The origin location from where the product associated with this estimate is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The estimate's shipping address."""

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The estimate's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this estimate, in ISO 8601 format (YYYY-MM-DD)."""


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
    The QuickBooks-assigned unique identifier of an existing estimate line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new estimate lines you wish to add.
    """

    amount: str
    """The monetary amount of this estimate line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The estimate line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all estimate lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this estimate line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this estimate
    line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this estimate line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this estimate line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    markup_rate: Annotated[str, PropertyInfo(alias="markupRate")]
    """
    The markup that will be passed on to the customer for this item on this estimate
    line. `amount = (quantity * rate) * (1 + markupRate)`
    """

    markup_rate_percent: Annotated[str, PropertyInfo(alias="markupRatePercent")]
    """
    The markup, expressed as a percentage, that will be passed on to the customer
    for this item on this estimate line.
    `amount = (quantity * rate) * (1 + markupRatePercent/100)`
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this estimate
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all estimate lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    estimate line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all estimate lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this estimate line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this estimate line.

    This overrides any price level set on the corresponding customer. The resulting
    estimate line will not show this price level, only the final `rate` calculated
    from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    estimate line.
    """

    quantity: float
    """The quantity of the item associated with this estimate line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: str
    """The price per unit for this estimate line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this estimate line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this estimate line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this estimate line.

    Must be a valid unit within the item's available units of measure.
    """


class LineGroup(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing estimate line group you
    wish to retain or update.

    **IMPORTANT**: Set this field to `-1` for new estimate line groups you wish to
    add.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The estimate line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: Iterable[LineGroupLine]
    """
    The estimate line group's line items, each representing a single product or
    service quoted.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       line items for the estimate line group with this array. To keep any existing
       line items, you must include them in this array even if they have not
       changed. **Any line items not included will be removed.**

    2. To add a new line item, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any line items, omit this field entirely to keep
       them unchanged.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this estimate line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: float
    """The quantity of the item group associated with this estimate line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this estimate line group.

    Must be a valid unit within the item's available units of measure.
    """


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing estimate line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new estimate lines you wish to add.
    """

    amount: str
    """The monetary amount of this estimate line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The estimate line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all estimate lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this estimate line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this estimate
    line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this estimate line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this estimate line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    markup_rate: Annotated[str, PropertyInfo(alias="markupRate")]
    """
    The markup that will be passed on to the customer for this item on this estimate
    line. `amount = (quantity * rate) * (1 + markupRate)`
    """

    markup_rate_percent: Annotated[str, PropertyInfo(alias="markupRatePercent")]
    """
    The markup, expressed as a percentage, that will be passed on to the customer
    for this item on this estimate line.
    `amount = (quantity * rate) * (1 + markupRatePercent/100)`
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this estimate
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all estimate lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    estimate line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all estimate lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this estimate line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this estimate line.

    This overrides any price level set on the corresponding customer. The resulting
    estimate line will not show this price level, only the final `rate` calculated
    from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    estimate line.
    """

    quantity: float
    """The quantity of the item associated with this estimate line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: str
    """The price per unit for this estimate line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this estimate line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this estimate line, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the parent
    transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this estimate line.

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
