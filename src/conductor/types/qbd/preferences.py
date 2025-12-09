# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Preferences",
    "Accounting",
    "AppAccessRights",
    "FinanceCharges",
    "FinanceChargesFinanceChargeAccount",
    "ItemsAndInventory",
    "JobsAndEstimates",
    "MultiCurrency",
    "MultiCurrencyHomeCurrency",
    "MultiLocationInventory",
    "PurchasesAndVendors",
    "PurchasesAndVendorsDefaultDiscountAccount",
    "Reports",
    "SalesAndCustomers",
    "SalesAndCustomersDefaultShippingMethod",
    "SalesAndCustomersPriceLevels",
    "SalesTax",
    "SalesTaxDefaultItemSalesTax",
    "SalesTaxDefaultNonTaxableSalesTaxCode",
    "SalesTaxDefaultTaxableSalesTaxCode",
    "TimeTracking",
]


class Accounting(BaseModel):
    """The accounting preferences for this company file."""

    closing_date: Optional[date] = FieldInfo(alias="closingDate", default=None)
    """The company closing date set within this company file.

    (The QuickBooks Admin can assign a password restricting access to transactions
    that occurred before this date.)
    """

    default_transaction_class: Optional[Literal["accounts", "items", "names", "none"]] = FieldInfo(
        alias="defaultTransactionClass", default=None
    )
    """The default class assigned to transactions for this company file."""

    is_assigning_journal_entry_numbers: bool = FieldInfo(alias="isAssigningJournalEntryNumbers")
    """
    Indicates whether this company file is configured to automatically assign a
    number to each journal entry.
    """

    is_requiring_accounts: bool = FieldInfo(alias="isRequiringAccounts")
    """
    Indicates whether this company file is configured to require an account for new
    transactions. If `true`, a transaction cannot be recorded in the QuickBooks user
    interface unless it is assigned to an account. (However, transactions affected
    by this preference always require an account to be specified when added through
    the API.)
    """

    is_using_account_numbers: bool = FieldInfo(alias="isUsingAccountNumbers")
    """
    Indicates whether this company file is configured to record an account number
    for new accounts. If you include an account number when creating a new account
    while this preference is `false`, the account number will still be set, but will
    not be visible in the QuickBooks user interface.
    """

    is_using_audit_trail: bool = FieldInfo(alias="isUsingAuditTrail")
    """
    Indicates whether this company file is configured to log all transaction changes
    in the audit trail report. If `false`, QuickBooks logs only the most recent
    version of each transaction.
    """

    is_using_class_tracking: bool = FieldInfo(alias="isUsingClassTracking")
    """
    Indicates whether this company file is configured to use the `class` field on
    all transactions.
    """


class AppAccessRights(BaseModel):
    """The current application access rights for this company file."""

    automatic_login_user_name: Optional[str] = FieldInfo(alias="automaticLoginUserName", default=None)
    """
    If auto-login is allowed for this company file, specifies the user name that is
    allowed to use auto-login.
    """

    is_automatic_login_allowed: bool = FieldInfo(alias="isAutomaticLoginAllowed")
    """Indicates whether applications can use auto-login to access this company file."""

    is_personal_data_access_allowed: bool = FieldInfo(alias="isPersonalDataAccessAllowed")
    """
    Indicates whether access is allowed to personal (sensitive) data in this company
    file.
    """


class FinanceChargesFinanceChargeAccount(BaseModel):
    """
    The account used to track finance charges that customers pay for this company file. This is usually an income account.
    """

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


class FinanceCharges(BaseModel):
    """The finance charge preferences for this company file.

    These settings determine how late payment charges are calculated and applied to customer accounts.
    """

    annual_interest_rate: Optional[float] = FieldInfo(alias="annualInterestRate", default=None)
    """
    The interest rate that QuickBooks will use to calculate finance charges for this
    company file. Default is `0`.
    """

    calculate_charges_from: Literal["due_date", "invoice_or_billed_date"] = FieldInfo(alias="calculateChargesFrom")
    """The date from which finance charges are calculated for this company file.

    Default is `due_date`.
    """

    finance_charge_account: Optional[FinanceChargesFinanceChargeAccount] = FieldInfo(
        alias="financeChargeAccount", default=None
    )
    """
    The account used to track finance charges that customers pay for this company
    file. This is usually an income account.
    """

    grace_period: float = FieldInfo(alias="gracePeriod")
    """
    The number of days before finance charges apply to customers' overdue invoices
    for this company file. Default is `0`.
    """

    is_assessing_for_overdue_charges: bool = FieldInfo(alias="isAssessingForOverdueCharges")
    """
    Indicates whether this company file is configured to assess finance charges for
    overdue invoices. Default is `false`. (Note that laws vary about whether a
    company can charge interest on overdue interest payments.)
    """

    is_marked_to_be_printed: bool = FieldInfo(alias="isMarkedToBePrinted")
    """
    Indicates whether this company file is configured to mark all newly created
    finance-charge invoices as "to be printed". Default is `false`. The user can
    still change this preference for each individual invoice.
    """

    minimum_finance_charge: Optional[float] = FieldInfo(alias="minimumFinanceCharge", default=None)
    """
    The minimum finance charge that will be applied regardless of the amount overdue
    for this company file. Default is `0`.
    """


class ItemsAndInventory(BaseModel):
    """The item inventory preferences for this company file."""

    fifo_effective_date: Optional[date] = FieldInfo(alias="fifoEffectiveDate", default=None)
    """
    The date from which FIFO (First In, First Out) is used to calculate the value of
    inventory sold and on-hand for this company file, in ISO 8601 format
    (YYYY-MM-DD).
    """

    inventory_tracking_method: Optional[Literal["none", "serial_number", "lot_number"]] = FieldInfo(
        alias="inventoryTrackingMethod", default=None
    )
    """Specifies the type of inventory tracking that this company file uses."""

    is_barcode_enabled: Optional[bool] = FieldInfo(alias="isBarcodeEnabled", default=None)
    """Indicates whether barcode functionality is enabled for this company file."""

    is_bin_tracking_enabled: Optional[bool] = FieldInfo(alias="isBinTrackingEnabled", default=None)
    """Indicates whether bin tracking is enabled for this company file.

    When `true`, inventory can be tracked by bin locations within sites.
    """

    is_enhanced_inventory_receiving_enabled: Optional[bool] = FieldInfo(
        alias="isEnhancedInventoryReceivingEnabled", default=None
    )
    """
    Indicates whether enhanced inventory receiving is enabled for this company file.
    """

    is_fifo_enabled: Optional[bool] = FieldInfo(alias="isFifoEnabled", default=None)
    """
    Indicates whether this company file is configured to use FIFO (First In, First
    Out) to calculate the value of inventory sold and on-hand.
    """

    is_inventory_expiration_date_enabled: Optional[bool] = FieldInfo(
        alias="isInventoryExpirationDateEnabled", default=None
    )
    """
    Indicates whether expiration dates for inventory serial/lot numbers are enabled
    for this company file. This feature is supported from QuickBooks Desktop 2023.
    """

    is_tracking_on_build_assembly_enabled: Optional[bool] = FieldInfo(
        alias="isTrackingOnBuildAssemblyEnabled", default=None
    )
    """
    Indicates whether serial/lot number tracking is enabled for build assemblies in
    this company file.
    """

    is_tracking_on_inventory_adjustment_enabled: Optional[bool] = FieldInfo(
        alias="isTrackingOnInventoryAdjustmentEnabled", default=None
    )
    """
    Indicates whether serial/lot number tracking is enabled for inventory
    adjustments in this company file.
    """

    is_tracking_on_purchase_transactions_enabled: Optional[bool] = FieldInfo(
        alias="isTrackingOnPurchaseTransactionsEnabled", default=None
    )
    """
    Indicates whether serial/lot number tracking is enabled for purchase
    transactions in this company file.
    """

    is_tracking_on_sales_transactions_enabled: Optional[bool] = FieldInfo(
        alias="isTrackingOnSalesTransactionsEnabled", default=None
    )
    """
    Indicates whether serial/lot number tracking is enabled for sales transactions
    in this company file.
    """


class JobsAndEstimates(BaseModel):
    """The jobs and estimates preferences for this company file."""

    is_printing_items_with_zero_amounts: bool = FieldInfo(alias="isPrintingItemsWithZeroAmounts")
    """
    Indicates whether this company file is configured to print line items with zero
    amounts on progress invoices. This preference is only relevant if
    `isUsingProgressInvoicing` is `true`.
    """

    is_using_estimates: bool = FieldInfo(alias="isUsingEstimates")
    """Indicates whether this company file is configured to create estimates for jobs."""

    is_using_progress_invoicing: bool = FieldInfo(alias="isUsingProgressInvoicing")
    """
    Indicates whether this company file permits creating invoices for only a portion
    of an estimate.
    """


class MultiCurrencyHomeCurrency(BaseModel):
    """The currency that is set as the home currency for this company file.

    The home currency is normally the currency of the country where the business is physically located. Although a home currency other than US Dollars can be chosen, certain QuickBooks convenience features are available only with a home currency of US Dollars, such as the ability to download current exchange rates. Also, Intuit services such as payroll and online banking are only available in US Dollars. Once the home currency has been set and used in any transaction, it cannot be changed.
    """

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


class MultiCurrency(BaseModel):
    """The multi-currency preferences for this company file."""

    home_currency: Optional[MultiCurrencyHomeCurrency] = FieldInfo(alias="homeCurrency", default=None)
    """The currency that is set as the home currency for this company file.

    The home currency is normally the currency of the country where the business is
    physically located. Although a home currency other than US Dollars can be
    chosen, certain QuickBooks convenience features are available only with a home
    currency of US Dollars, such as the ability to download current exchange rates.
    Also, Intuit services such as payroll and online banking are only available in
    US Dollars. Once the home currency has been set and used in any transaction, it
    cannot be changed.
    """

    is_multi_currency_enabled: Optional[bool] = FieldInfo(alias="isMultiCurrencyEnabled", default=None)
    """Indicates whether the multicurrency feature is enabled for this company file.

    Once multicurrency is enabled for a company file, it cannot be disabled.
    """


class MultiLocationInventory(BaseModel):
    """The multi-location inventory preferences for this company file."""

    is_multi_location_inventory_available: Optional[bool] = FieldInfo(
        alias="isMultiLocationInventoryAvailable", default=None
    )
    """
    Indicates whether the multilocation inventory feature is available for this
    company file. When `true`, the feature can potentially be enabled.
    """

    is_multi_location_inventory_enabled: Optional[bool] = FieldInfo(
        alias="isMultiLocationInventoryEnabled", default=None
    )
    """
    Indicates whether the multilocation inventory feature is enabled for this
    company file. When `true`, inventory can be tracked across multiple locations.
    """


class PurchasesAndVendorsDefaultDiscountAccount(BaseModel):
    """The account used to track vendor discounts for this company file."""

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


class PurchasesAndVendors(BaseModel):
    """The purchases and vendors preferences for this company file."""

    days_bills_are_due: float = FieldInfo(alias="daysBillsAreDue")
    """
    The default number of days after receipt when bills are due for this company
    file.
    """

    default_discount_account: Optional[PurchasesAndVendorsDefaultDiscountAccount] = FieldInfo(
        alias="defaultDiscountAccount", default=None
    )
    """The account used to track vendor discounts for this company file."""

    is_automatically_using_discounts: bool = FieldInfo(alias="isAutomaticallyUsingDiscounts")
    """
    Indicates whether this company file is configured to automatically apply
    available vendor discounts or credits when paying bills.
    """

    is_using_inventory: bool = FieldInfo(alias="isUsingInventory")
    """Indicates whether this company file has inventory-related features enabled."""


class Reports(BaseModel):
    """The reporting preferences for this company file."""

    aging_report_basis: Literal["age_from_due_date", "age_from_transaction_date"] = FieldInfo(alias="agingReportBasis")
    """
    Determines how the aging periods are calculated in accounts receivable and
    accounts payable reports for this company file. When set to `age_from_due_date`,
    the overdue days shown in these reports begin with the due date on the invoice.
    When set to `age_from_transaction_date`, the overdue days begin with the date
    the transaction was created.
    """

    summary_report_basis: Literal["accrual", "cash"] = FieldInfo(alias="summaryReportBasis")
    """
    Indicates whether summary reports for this company file use cash-basis or
    accrual-basis bookkeeping. With `accrual` basis, transactions are recorded when
    they occur regardless of when payment is received or made. With `cash` basis,
    transactions are recorded only when payment is received or made.
    """


class SalesAndCustomersDefaultShippingMethod(BaseModel):
    """
    The default shipping method used in all "Ship Via" fields for this company file.
    """

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


class SalesAndCustomersPriceLevels(BaseModel):
    """
    The custom pricing settings for this company file that can be assigned to specific customers. When a price level is set for a customer, QuickBooks automatically applies these custom prices to new invoices, sales receipts, sales orders, and credit memos. These settings can be overridden when creating individual transactions, and price levels can also be specified on individual line items in supported sales transactions.
    """

    is_rounding_sales_price_up: Optional[bool] = FieldInfo(alias="isRoundingSalesPriceUp", default=None)
    """
    Indicates whether this company file is configured to round amounts up to the
    nearest whole dollar for fixed percentage price levels. This setting does not
    affect per-item price levels.
    """

    is_using_price_levels: bool = FieldInfo(alias="isUsingPriceLevels")
    """Indicates whether this company file has price levels enabled.

    When `true`, price levels can be created and used to automatically calculate
    custom pricing for different customers.
    """


class SalesAndCustomers(BaseModel):
    """The sales and customers preferences for this company file."""

    default_markup_percentage: Optional[str] = FieldInfo(alias="defaultMarkupPercentage", default=None)
    """
    The default percentage that an inventory item will be marked up from its cost
    for this company file.
    """

    default_shipment_origin: Optional[str] = FieldInfo(alias="defaultShipmentOrigin", default=None)
    """
    The default shipment-origin location (i.e., FOB - freight on board) from which
    invoiced products are shipped for this company file. This indicates the point at
    which ownership and liability for goods transfer from seller to buyer.
    """

    default_shipping_method: Optional[SalesAndCustomersDefaultShippingMethod] = FieldInfo(
        alias="defaultShippingMethod", default=None
    )
    """
    The default shipping method used in all "Ship Via" fields for this company file.
    """

    is_auto_applying_payments: bool = FieldInfo(alias="isAutoApplyingPayments")
    """
    Indicates whether this company file is configured to automatically apply a
    customer's payment to their outstanding invoices, beginning with the oldest
    invoice.
    """

    is_tracking_reimbursed_expenses_as_income: bool = FieldInfo(alias="isTrackingReimbursedExpensesAsIncome")
    """
    Indicates whether this company file is configured to track an expense and the
    customer's reimbursement for that expense in separate accounts. When `true`,
    reimbursements can be tracked as income rather than as a reduction of the
    original expense.
    """

    price_levels: Optional[SalesAndCustomersPriceLevels] = FieldInfo(alias="priceLevels", default=None)
    """
    The custom pricing settings for this company file that can be assigned to
    specific customers. When a price level is set for a customer, QuickBooks
    automatically applies these custom prices to new invoices, sales receipts, sales
    orders, and credit memos. These settings can be overridden when creating
    individual transactions, and price levels can also be specified on individual
    line items in supported sales transactions.
    """


class SalesTaxDefaultItemSalesTax(BaseModel):
    """The default tax code for sales for this company file."""

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


class SalesTaxDefaultNonTaxableSalesTaxCode(BaseModel):
    """The default tax code for non-taxable sales for this company file."""

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


class SalesTaxDefaultTaxableSalesTaxCode(BaseModel):
    """The default tax code for taxable sales for this company file."""

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


class SalesTax(BaseModel):
    """The sales-tax preferences for this company file.

    If sales tax is turned off in the user interface (that is, if "No" is selected for "Do You Charge Sales Tax?" in the sales tax preferences), then this field will be `null`.
    """

    default_item_sales_tax: SalesTaxDefaultItemSalesTax = FieldInfo(alias="defaultItemSalesTax")
    """The default tax code for sales for this company file."""

    default_non_taxable_sales_tax_code: SalesTaxDefaultNonTaxableSalesTaxCode = FieldInfo(
        alias="defaultNonTaxableSalesTaxCode"
    )
    """The default tax code for non-taxable sales for this company file."""

    default_taxable_sales_tax_code: SalesTaxDefaultTaxableSalesTaxCode = FieldInfo(alias="defaultTaxableSalesTaxCode")
    """The default tax code for taxable sales for this company file."""

    is_using_customer_tax_code: Optional[bool] = FieldInfo(alias="isUsingCustomerTaxCode", default=None)
    """
    Indicates whether this company file is configured to use tax codes for
    customers.
    """

    is_using_tax_inclusive_prices: Optional[bool] = FieldInfo(alias="isUsingTaxInclusivePrices", default=None)
    """
    Indicates whether this company file is configured to allow tax-inclusive prices.
    """

    is_using_vendor_tax_code: Optional[bool] = FieldInfo(alias="isUsingVendorTaxCode", default=None)
    """Indicates whether this company file is configured to use tax codes for vendors."""

    sales_tax_reporting_frequency: Literal["monthly", "quarterly", "annually"] = FieldInfo(
        alias="salesTaxReportingFrequency"
    )
    """The frequency at which sales tax reports are generated for this company file."""


class TimeTracking(BaseModel):
    """The time-tracking preferences for this company file.

    If time tracking is turned off in the user interface (that is, if "No" is selected for "Do You Track Time?" in the time tracking preferences), then this field will be `null`.
    """

    first_day_of_week: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] = (
        FieldInfo(alias="firstDayOfWeek")
    )
    """The first day of a weekly timesheet period for this company file."""


class Preferences(BaseModel):
    accounting: Accounting
    """The accounting preferences for this company file."""

    app_access_rights: AppAccessRights = FieldInfo(alias="appAccessRights")
    """The current application access rights for this company file."""

    finance_charges: FinanceCharges = FieldInfo(alias="financeCharges")
    """The finance charge preferences for this company file.

    These settings determine how late payment charges are calculated and applied to
    customer accounts.
    """

    items_and_inventory: Optional[ItemsAndInventory] = FieldInfo(alias="itemsAndInventory", default=None)
    """The item inventory preferences for this company file."""

    jobs_and_estimates: JobsAndEstimates = FieldInfo(alias="jobsAndEstimates")
    """The jobs and estimates preferences for this company file."""

    multi_currency: Optional[MultiCurrency] = FieldInfo(alias="multiCurrency", default=None)
    """The multi-currency preferences for this company file."""

    multi_location_inventory: Optional[MultiLocationInventory] = FieldInfo(alias="multiLocationInventory", default=None)
    """The multi-location inventory preferences for this company file."""

    purchases_and_vendors: PurchasesAndVendors = FieldInfo(alias="purchasesAndVendors")
    """The purchases and vendors preferences for this company file."""

    reports: Reports
    """The reporting preferences for this company file."""

    sales_and_customers: SalesAndCustomers = FieldInfo(alias="salesAndCustomers")
    """The sales and customers preferences for this company file."""

    sales_tax: Optional[SalesTax] = FieldInfo(alias="salesTax", default=None)
    """The sales-tax preferences for this company file.

    If sales tax is turned off in the user interface (that is, if "No" is selected
    for "Do You Charge Sales Tax?" in the sales tax preferences), then this field
    will be `null`.
    """

    time_tracking: Optional[TimeTracking] = FieldInfo(alias="timeTracking", default=None)
    """The time-tracking preferences for this company file.

    If time tracking is turned off in the user interface (that is, if "No" is
    selected for "Do You Track Time?" in the time tracking preferences), then this
    field will be `null`.
    """
