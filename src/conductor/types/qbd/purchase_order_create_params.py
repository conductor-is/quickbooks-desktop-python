# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PurchaseOrderCreateParams",
    "LineGroup",
    "LineGroupCustomField",
    "Line",
    "LineCustomField",
    "ShippingAddress",
    "VendorAddress",
]


class PurchaseOrderCreateParams(TypedDict, total=False):
    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this purchase order, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The purchase order's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this purchase order's
    line items unless overridden at the line item level.
    """

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this purchase order when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """
    The date by which this purchase order must be paid, in ISO 8601 format
    (YYYY-MM-DD).
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this purchase order's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expected_date: Annotated[Union[str, date], PropertyInfo(alias="expectedDate", format="iso8601")]
    """
    The date on which shipment of this purchase order is expected to be completed,
    in ISO 8601 format (YYYY-MM-DD).
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this purchase
    order is stored.
    """

    is_queued_for_email: Annotated[bool, PropertyInfo(alias="isQueuedForEmail")]
    """
    Indicates whether this purchase order is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this purchase order is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: Annotated[Iterable[LineGroup], PropertyInfo(alias="lineGroups")]
    """
    The purchase order's line item groups, each representing a predefined set of
    related items.

    **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
    purchase order.
    """

    lines: Iterable[Line]
    """
    The purchase order's line items, each representing a single product or service
    ordered.

    **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
    purchase order.
    """

    memo: str
    """
    A memo or note for this purchase order that appears in reports, but not on the
    purchase order.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this purchase
    order. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all purchase orders for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    purchase order. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all purchase orders for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this purchase order, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this purchase order, determining whether it is taxable or
    non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
    This can be overridden on the purchase order's individual lines.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    shipment_origin: Annotated[str, PropertyInfo(alias="shipmentOrigin")]
    """
    The origin location from where the product associated with this purchase order
    is shipped. This is the point at which ownership and liability for goods
    transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
    this field, which stands for "freight on board". This field is informational and
    has no accounting implications.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The purchase order's shipping address."""

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]
    """
    The shipping method used for this purchase order, such as standard mail or
    overnight delivery.
    """

    ship_to_entity_id: Annotated[str, PropertyInfo(alias="shipToEntityId")]
    """
    The customer, vendor, employee, or other entity to whom this purchase order is
    to be shipped.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The purchase order's payment terms, defining when payment is due and any
    applicable discounts.
    """

    vendor_address: Annotated[VendorAddress, PropertyInfo(alias="vendorAddress")]
    """The address of the vendor who sent this purchase order."""

    vendor_id: Annotated[str, PropertyInfo(alias="vendorId")]
    """The vendor who sent this purchase order for goods or services purchased."""

    vendor_message: Annotated[str, PropertyInfo(alias="vendorMessage")]
    """A message to be printed on this purchase order for the vendor to read."""


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
    The purchase order line group's item group, representing a predefined set of
    items bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    custom_fields: Annotated[Iterable[LineGroupCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the purchase order line group object, added as
    user-defined data extensions, not included in the standard QuickBooks object.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item group associated with this purchase order line group is stored.
    """

    quantity: float
    """The quantity of the item group associated with this purchase order line group.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this purchase order line group.

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


class Line(TypedDict, total=False):
    amount: str
    """The monetary amount of this purchase order line, represented as a decimal
    string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The purchase order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all purchase order lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: Annotated[Iterable[LineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the purchase order line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: str
    """A description of this purchase order line."""

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this purchase order line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this purchase order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this purchase
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all purchase order lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    purchase order line. Unlike the user-defined fields in the `customFields` array,
    this is a standard QuickBooks field that exists for all purchase order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this purchase order line, overriding the default account
    associated with the item.
    """

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    If `account` refers to an Accounts-Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    quantity: float
    """The quantity of the item associated with this purchase order line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """

    rate: str
    """The price per unit for this purchase order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for this purchase order line, determining whether it is
    taxable or non-taxable. If set, this overrides any sales-tax codes defined on
    the parent transaction or the associated item.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    service_date: Annotated[Union[str, date], PropertyInfo(alias="serviceDate", format="iso8601")]
    """
    The date on which the service for this purchase order line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    sku: str
    """
    The purchase order line's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this purchase order line.

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


class VendorAddress(TypedDict, total=False):
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
