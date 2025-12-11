# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .bills import (
    BillsResource,
    AsyncBillsResource,
    BillsResourceWithRawResponse,
    AsyncBillsResourceWithRawResponse,
    BillsResourceWithStreamingResponse,
    AsyncBillsResourceWithStreamingResponse,
)
from .checks import (
    ChecksResource,
    AsyncChecksResource,
    ChecksResourceWithRawResponse,
    AsyncChecksResourceWithRawResponse,
    ChecksResourceWithStreamingResponse,
    AsyncChecksResourceWithStreamingResponse,
)
from .classes import (
    ClassesResource,
    AsyncClassesResource,
    ClassesResourceWithRawResponse,
    AsyncClassesResourceWithRawResponse,
    ClassesResourceWithStreamingResponse,
    AsyncClassesResourceWithStreamingResponse,
)
from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
    CompanyResourceWithStreamingResponse,
    AsyncCompanyResourceWithStreamingResponse,
)
from .vendors import (
    VendorsResource,
    AsyncVendorsResource,
    VendorsResourceWithRawResponse,
    AsyncVendorsResourceWithRawResponse,
    VendorsResourceWithStreamingResponse,
    AsyncVendorsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)
from .employees import (
    EmployeesResource,
    AsyncEmployeesResource,
    EmployeesResourceWithRawResponse,
    AsyncEmployeesResourceWithRawResponse,
    EmployeesResourceWithStreamingResponse,
    AsyncEmployeesResourceWithStreamingResponse,
)
from .estimates import (
    EstimatesResource,
    AsyncEstimatesResource,
    EstimatesResourceWithRawResponse,
    AsyncEstimatesResourceWithRawResponse,
    EstimatesResourceWithStreamingResponse,
    AsyncEstimatesResourceWithStreamingResponse,
)
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from .transfers import (
    TransfersResource,
    AsyncTransfersResource,
    TransfersResourceWithRawResponse,
    AsyncTransfersResourceWithRawResponse,
    TransfersResourceWithStreamingResponse,
    AsyncTransfersResourceWithStreamingResponse,
)
from .currencies import (
    CurrenciesResource,
    AsyncCurrenciesResource,
    CurrenciesResourceWithRawResponse,
    AsyncCurrenciesResourceWithRawResponse,
    CurrenciesResourceWithStreamingResponse,
    AsyncCurrenciesResourceWithStreamingResponse,
)
from .item_sites import (
    ItemSitesResource,
    AsyncItemSitesResource,
    ItemSitesResourceWithRawResponse,
    AsyncItemSitesResourceWithRawResponse,
    ItemSitesResourceWithStreamingResponse,
    AsyncItemSitesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .item_groups import (
    ItemGroupsResource,
    AsyncItemGroupsResource,
    ItemGroupsResourceWithRawResponse,
    AsyncItemGroupsResourceWithRawResponse,
    ItemGroupsResourceWithStreamingResponse,
    AsyncItemGroupsResourceWithStreamingResponse,
)
from .other_names import (
    OtherNamesResource,
    AsyncOtherNamesResource,
    OtherNamesResourceWithRawResponse,
    AsyncOtherNamesResourceWithRawResponse,
    OtherNamesResourceWithStreamingResponse,
    AsyncOtherNamesResourceWithStreamingResponse,
)
from .preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from .credit_memos import (
    CreditMemosResource,
    AsyncCreditMemosResource,
    CreditMemosResourceWithRawResponse,
    AsyncCreditMemosResourceWithRawResponse,
    CreditMemosResourceWithStreamingResponse,
    AsyncCreditMemosResourceWithStreamingResponse,
)
from .price_levels import (
    PriceLevelsResource,
    AsyncPriceLevelsResource,
    PriceLevelsResourceWithRawResponse,
    AsyncPriceLevelsResourceWithRawResponse,
    PriceLevelsResourceWithStreamingResponse,
    AsyncPriceLevelsResourceWithStreamingResponse,
)
from .sales_orders import (
    SalesOrdersResource,
    AsyncSalesOrdersResource,
    SalesOrdersResourceWithRawResponse,
    AsyncSalesOrdersResourceWithRawResponse,
    SalesOrdersResourceWithStreamingResponse,
    AsyncSalesOrdersResourceWithStreamingResponse,
)
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from .item_receipts import (
    ItemReceiptsResource,
    AsyncItemReceiptsResource,
    ItemReceiptsResourceWithRawResponse,
    AsyncItemReceiptsResourceWithRawResponse,
    ItemReceiptsResourceWithStreamingResponse,
    AsyncItemReceiptsResourceWithStreamingResponse,
)
from .service_items import (
    ServiceItemsResource,
    AsyncServiceItemsResource,
    ServiceItemsResourceWithRawResponse,
    AsyncServiceItemsResourceWithRawResponse,
    ServiceItemsResourceWithStreamingResponse,
    AsyncServiceItemsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .customer_types import (
    CustomerTypesResource,
    AsyncCustomerTypesResource,
    CustomerTypesResourceWithRawResponse,
    AsyncCustomerTypesResourceWithRawResponse,
    CustomerTypesResourceWithStreamingResponse,
    AsyncCustomerTypesResourceWithStreamingResponse,
)
from .discount_items import (
    DiscountItemsResource,
    AsyncDiscountItemsResource,
    DiscountItemsResourceWithRawResponse,
    AsyncDiscountItemsResourceWithRawResponse,
    DiscountItemsResourceWithStreamingResponse,
    AsyncDiscountItemsResourceWithStreamingResponse,
)
from .sales_receipts import (
    SalesReceiptsResource,
    AsyncSalesReceiptsResource,
    SalesReceiptsResourceWithRawResponse,
    AsyncSalesReceiptsResourceWithRawResponse,
    SalesReceiptsResourceWithStreamingResponse,
    AsyncSalesReceiptsResourceWithStreamingResponse,
)
from .standard_terms import (
    StandardTermsResource,
    AsyncStandardTermsResource,
    StandardTermsResourceWithRawResponse,
    AsyncStandardTermsResourceWithRawResponse,
    StandardTermsResourceWithStreamingResponse,
    AsyncStandardTermsResourceWithStreamingResponse,
)
from .subtotal_items import (
    SubtotalItemsResource,
    AsyncSubtotalItemsResource,
    SubtotalItemsResourceWithRawResponse,
    AsyncSubtotalItemsResourceWithRawResponse,
    SubtotalItemsResourceWithStreamingResponse,
    AsyncSubtotalItemsResourceWithStreamingResponse,
)
from .vendor_credits import (
    VendorCreditsResource,
    AsyncVendorCreditsResource,
    VendorCreditsResourceWithRawResponse,
    AsyncVendorCreditsResourceWithRawResponse,
    VendorCreditsResourceWithStreamingResponse,
    AsyncVendorCreditsResourceWithStreamingResponse,
)
from .inventory_items import (
    InventoryItemsResource,
    AsyncInventoryItemsResource,
    InventoryItemsResourceWithRawResponse,
    AsyncInventoryItemsResourceWithRawResponse,
    InventoryItemsResourceWithStreamingResponse,
    AsyncInventoryItemsResourceWithStreamingResponse,
)
from .inventory_sites import (
    InventorySitesResource,
    AsyncInventorySitesResource,
    InventorySitesResourceWithRawResponse,
    AsyncInventorySitesResourceWithRawResponse,
    InventorySitesResourceWithStreamingResponse,
    AsyncInventorySitesResourceWithStreamingResponse,
)
from .journal_entries import (
    JournalEntriesResource,
    AsyncJournalEntriesResource,
    JournalEntriesResourceWithRawResponse,
    AsyncJournalEntriesResourceWithRawResponse,
    JournalEntriesResourceWithStreamingResponse,
    AsyncJournalEntriesResourceWithStreamingResponse,
)
from .payment_methods import (
    PaymentMethodsResource,
    AsyncPaymentMethodsResource,
    PaymentMethodsResourceWithRawResponse,
    AsyncPaymentMethodsResourceWithRawResponse,
    PaymentMethodsResourceWithStreamingResponse,
    AsyncPaymentMethodsResourceWithStreamingResponse,
)
from .purchase_orders import (
    PurchaseOrdersResource,
    AsyncPurchaseOrdersResource,
    PurchaseOrdersResourceWithRawResponse,
    AsyncPurchaseOrdersResourceWithRawResponse,
    PurchaseOrdersResourceWithStreamingResponse,
    AsyncPurchaseOrdersResourceWithStreamingResponse,
)
from .sales_tax_codes import (
    SalesTaxCodesResource,
    AsyncSalesTaxCodesResource,
    SalesTaxCodesResourceWithRawResponse,
    AsyncSalesTaxCodesResourceWithRawResponse,
    SalesTaxCodesResourceWithStreamingResponse,
    AsyncSalesTaxCodesResourceWithStreamingResponse,
)
from .sales_tax_items import (
    SalesTaxItemsResource,
    AsyncSalesTaxItemsResource,
    SalesTaxItemsResourceWithRawResponse,
    AsyncSalesTaxItemsResourceWithRawResponse,
    SalesTaxItemsResourceWithStreamingResponse,
    AsyncSalesTaxItemsResourceWithStreamingResponse,
)
from .build_assemblies import (
    BuildAssembliesResource,
    AsyncBuildAssembliesResource,
    BuildAssembliesResourceWithRawResponse,
    AsyncBuildAssembliesResourceWithRawResponse,
    BuildAssembliesResourceWithStreamingResponse,
    AsyncBuildAssembliesResourceWithStreamingResponse,
)
from .receive_payments import (
    ReceivePaymentsResource,
    AsyncReceivePaymentsResource,
    ReceivePaymentsResourceWithRawResponse,
    AsyncReceivePaymentsResourceWithRawResponse,
    ReceivePaymentsResourceWithStreamingResponse,
    AsyncReceivePaymentsResourceWithStreamingResponse,
)
from .account_tax_lines import (
    AccountTaxLinesResource,
    AsyncAccountTaxLinesResource,
    AccountTaxLinesResourceWithRawResponse,
    AsyncAccountTaxLinesResourceWithRawResponse,
    AccountTaxLinesResourceWithStreamingResponse,
    AsyncAccountTaxLinesResourceWithStreamingResponse,
)
from .date_driven_terms import (
    DateDrivenTermsResource,
    AsyncDateDrivenTermsResource,
    DateDrivenTermsResourceWithRawResponse,
    AsyncDateDrivenTermsResourceWithRawResponse,
    DateDrivenTermsResourceWithStreamingResponse,
    AsyncDateDrivenTermsResourceWithStreamingResponse,
)
from .other_charge_items import (
    OtherChargeItemsResource,
    AsyncOtherChargeItemsResource,
    OtherChargeItemsResourceWithRawResponse,
    AsyncOtherChargeItemsResourceWithRawResponse,
    OtherChargeItemsResourceWithStreamingResponse,
    AsyncOtherChargeItemsResourceWithStreamingResponse,
)
from .payroll_wage_items import (
    PayrollWageItemsResource,
    AsyncPayrollWageItemsResource,
    PayrollWageItemsResourceWithRawResponse,
    AsyncPayrollWageItemsResourceWithRawResponse,
    PayrollWageItemsResourceWithStreamingResponse,
    AsyncPayrollWageItemsResourceWithStreamingResponse,
)
from .bill_check_payments import (
    BillCheckPaymentsResource,
    AsyncBillCheckPaymentsResource,
    BillCheckPaymentsResourceWithRawResponse,
    AsyncBillCheckPaymentsResourceWithRawResponse,
    BillCheckPaymentsResourceWithStreamingResponse,
    AsyncBillCheckPaymentsResourceWithStreamingResponse,
)
from .credit_card_charges import (
    CreditCardChargesResource,
    AsyncCreditCardChargesResource,
    CreditCardChargesResourceWithRawResponse,
    AsyncCreditCardChargesResourceWithRawResponse,
    CreditCardChargesResourceWithStreamingResponse,
    AsyncCreditCardChargesResourceWithStreamingResponse,
)
from .credit_card_credits import (
    CreditCardCreditsResource,
    AsyncCreditCardCreditsResource,
    CreditCardCreditsResourceWithRawResponse,
    AsyncCreditCardCreditsResourceWithRawResponse,
    CreditCardCreditsResourceWithStreamingResponse,
    AsyncCreditCardCreditsResourceWithStreamingResponse,
)
from .credit_card_refunds import (
    CreditCardRefundsResource,
    AsyncCreditCardRefundsResource,
    CreditCardRefundsResourceWithRawResponse,
    AsyncCreditCardRefundsResourceWithRawResponse,
    CreditCardRefundsResourceWithStreamingResponse,
    AsyncCreditCardRefundsResourceWithStreamingResponse,
)
from .non_inventory_items import (
    NonInventoryItemsResource,
    AsyncNonInventoryItemsResource,
    NonInventoryItemsResourceWithRawResponse,
    AsyncNonInventoryItemsResourceWithRawResponse,
    NonInventoryItemsResourceWithStreamingResponse,
    AsyncNonInventoryItemsResourceWithStreamingResponse,
)
from .deleted_list_objects import (
    DeletedListObjectsResource,
    AsyncDeletedListObjectsResource,
    DeletedListObjectsResourceWithRawResponse,
    AsyncDeletedListObjectsResourceWithRawResponse,
    DeletedListObjectsResourceWithStreamingResponse,
    AsyncDeletedListObjectsResourceWithStreamingResponse,
)
from .deleted_transactions import (
    DeletedTransactionsResource,
    AsyncDeletedTransactionsResource,
    DeletedTransactionsResourceWithRawResponse,
    AsyncDeletedTransactionsResourceWithRawResponse,
    DeletedTransactionsResourceWithStreamingResponse,
    AsyncDeletedTransactionsResourceWithStreamingResponse,
)
from .unit_of_measure_sets import (
    UnitOfMeasureSetsResource,
    AsyncUnitOfMeasureSetsResource,
    UnitOfMeasureSetsResourceWithRawResponse,
    AsyncUnitOfMeasureSetsResourceWithRawResponse,
    UnitOfMeasureSetsResourceWithStreamingResponse,
    AsyncUnitOfMeasureSetsResourceWithStreamingResponse,
)
from .inventory_adjustments import (
    InventoryAdjustmentsResource,
    AsyncInventoryAdjustmentsResource,
    InventoryAdjustmentsResourceWithRawResponse,
    AsyncInventoryAdjustmentsResourceWithRawResponse,
    InventoryAdjustmentsResourceWithStreamingResponse,
    AsyncInventoryAdjustmentsResourceWithStreamingResponse,
)
from .sales_representatives import (
    SalesRepresentativesResource,
    AsyncSalesRepresentativesResource,
    SalesRepresentativesResourceWithRawResponse,
    AsyncSalesRepresentativesResourceWithRawResponse,
    SalesRepresentativesResourceWithStreamingResponse,
    AsyncSalesRepresentativesResourceWithStreamingResponse,
)
from .inventory_assembly_items import (
    InventoryAssemblyItemsResource,
    AsyncInventoryAssemblyItemsResource,
    InventoryAssemblyItemsResourceWithRawResponse,
    AsyncInventoryAssemblyItemsResourceWithRawResponse,
    InventoryAssemblyItemsResourceWithStreamingResponse,
    AsyncInventoryAssemblyItemsResourceWithStreamingResponse,
)
from .time_tracking_activities import (
    TimeTrackingActivitiesResource,
    AsyncTimeTrackingActivitiesResource,
    TimeTrackingActivitiesResourceWithRawResponse,
    AsyncTimeTrackingActivitiesResourceWithRawResponse,
    TimeTrackingActivitiesResourceWithStreamingResponse,
    AsyncTimeTrackingActivitiesResourceWithStreamingResponse,
)
from .bill_credit_card_payments import (
    BillCreditCardPaymentsResource,
    AsyncBillCreditCardPaymentsResource,
    BillCreditCardPaymentsResourceWithRawResponse,
    AsyncBillCreditCardPaymentsResourceWithRawResponse,
    BillCreditCardPaymentsResourceWithStreamingResponse,
    AsyncBillCreditCardPaymentsResourceWithStreamingResponse,
)
from ...types.qbd_health_check_response import QbdHealthCheckResponse

__all__ = ["QbdResource", "AsyncQbdResource"]


class QbdResource(SyncAPIResource):
    @cached_property
    def account_tax_lines(self) -> AccountTaxLinesResource:
        return AccountTaxLinesResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def bill_check_payments(self) -> BillCheckPaymentsResource:
        return BillCheckPaymentsResource(self._client)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResource:
        return BillCreditCardPaymentsResource(self._client)

    @cached_property
    def bills(self) -> BillsResource:
        return BillsResource(self._client)

    @cached_property
    def build_assemblies(self) -> BuildAssembliesResource:
        return BuildAssembliesResource(self._client)

    @cached_property
    def checks(self) -> ChecksResource:
        return ChecksResource(self._client)

    @cached_property
    def classes(self) -> ClassesResource:
        return ClassesResource(self._client)

    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResource:
        return CreditCardChargesResource(self._client)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResource:
        return CreditCardCreditsResource(self._client)

    @cached_property
    def credit_card_refunds(self) -> CreditCardRefundsResource:
        return CreditCardRefundsResource(self._client)

    @cached_property
    def credit_memos(self) -> CreditMemosResource:
        return CreditMemosResource(self._client)

    @cached_property
    def currencies(self) -> CurrenciesResource:
        return CurrenciesResource(self._client)

    @cached_property
    def customer_types(self) -> CustomerTypesResource:
        return CustomerTypesResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResource:
        return DateDrivenTermsResource(self._client)

    @cached_property
    def deleted_list_objects(self) -> DeletedListObjectsResource:
        return DeletedListObjectsResource(self._client)

    @cached_property
    def deleted_transactions(self) -> DeletedTransactionsResource:
        return DeletedTransactionsResource(self._client)

    @cached_property
    def discount_items(self) -> DiscountItemsResource:
        return DiscountItemsResource(self._client)

    @cached_property
    def employees(self) -> EmployeesResource:
        return EmployeesResource(self._client)

    @cached_property
    def estimates(self) -> EstimatesResource:
        return EstimatesResource(self._client)

    @cached_property
    def inventory_adjustments(self) -> InventoryAdjustmentsResource:
        return InventoryAdjustmentsResource(self._client)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResource:
        return InventoryAssemblyItemsResource(self._client)

    @cached_property
    def inventory_items(self) -> InventoryItemsResource:
        return InventoryItemsResource(self._client)

    @cached_property
    def inventory_sites(self) -> InventorySitesResource:
        return InventorySitesResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def item_groups(self) -> ItemGroupsResource:
        return ItemGroupsResource(self._client)

    @cached_property
    def item_receipts(self) -> ItemReceiptsResource:
        return ItemReceiptsResource(self._client)

    @cached_property
    def item_sites(self) -> ItemSitesResource:
        return ItemSitesResource(self._client)

    @cached_property
    def journal_entries(self) -> JournalEntriesResource:
        return JournalEntriesResource(self._client)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResource:
        return NonInventoryItemsResource(self._client)

    @cached_property
    def other_charge_items(self) -> OtherChargeItemsResource:
        return OtherChargeItemsResource(self._client)

    @cached_property
    def other_names(self) -> OtherNamesResource:
        return OtherNamesResource(self._client)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        return PaymentMethodsResource(self._client)

    @cached_property
    def payroll_wage_items(self) -> PayrollWageItemsResource:
        return PayrollWageItemsResource(self._client)

    @cached_property
    def preferences(self) -> PreferencesResource:
        return PreferencesResource(self._client)

    @cached_property
    def price_levels(self) -> PriceLevelsResource:
        return PriceLevelsResource(self._client)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResource:
        return PurchaseOrdersResource(self._client)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResource:
        return ReceivePaymentsResource(self._client)

    @cached_property
    def sales_orders(self) -> SalesOrdersResource:
        return SalesOrdersResource(self._client)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResource:
        return SalesReceiptsResource(self._client)

    @cached_property
    def sales_representatives(self) -> SalesRepresentativesResource:
        return SalesRepresentativesResource(self._client)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResource:
        return SalesTaxCodesResource(self._client)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResource:
        return SalesTaxItemsResource(self._client)

    @cached_property
    def service_items(self) -> ServiceItemsResource:
        return ServiceItemsResource(self._client)

    @cached_property
    def standard_terms(self) -> StandardTermsResource:
        return StandardTermsResource(self._client)

    @cached_property
    def subtotal_items(self) -> SubtotalItemsResource:
        return SubtotalItemsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def time_tracking_activities(self) -> TimeTrackingActivitiesResource:
        return TimeTrackingActivitiesResource(self._client)

    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def transfers(self) -> TransfersResource:
        return TransfersResource(self._client)

    @cached_property
    def unit_of_measure_sets(self) -> UnitOfMeasureSetsResource:
        return UnitOfMeasureSetsResource(self._client)

    @cached_property
    def vendor_credits(self) -> VendorCreditsResource:
        return VendorCreditsResource(self._client)

    @cached_property
    def vendors(self) -> VendorsResource:
        return VendorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> QbdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return QbdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QbdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return QbdResourceWithStreamingResponse(self)

    def health_check(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QbdHealthCheckResponse:
        """
        Checks whether the specified QuickBooks Desktop connection is active and can
        process requests end-to-end. This is useful for showing a "connection status"
        indicator in your app. If an error occurs, the typical Conductor error response
        will be returned. As with any request to QuickBooks Desktop, the health check
        may fail if the application is not running, the wrong company file is open, or
        if a modal dialog is open. Timeout is 60 seconds.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/health-check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdHealthCheckResponse,
        )


class AsyncQbdResource(AsyncAPIResource):
    @cached_property
    def account_tax_lines(self) -> AsyncAccountTaxLinesResource:
        return AsyncAccountTaxLinesResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResource:
        return AsyncBillCheckPaymentsResource(self._client)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResource:
        return AsyncBillCreditCardPaymentsResource(self._client)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        return AsyncBillsResource(self._client)

    @cached_property
    def build_assemblies(self) -> AsyncBuildAssembliesResource:
        return AsyncBuildAssembliesResource(self._client)

    @cached_property
    def checks(self) -> AsyncChecksResource:
        return AsyncChecksResource(self._client)

    @cached_property
    def classes(self) -> AsyncClassesResource:
        return AsyncClassesResource(self._client)

    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResource:
        return AsyncCreditCardChargesResource(self._client)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResource:
        return AsyncCreditCardCreditsResource(self._client)

    @cached_property
    def credit_card_refunds(self) -> AsyncCreditCardRefundsResource:
        return AsyncCreditCardRefundsResource(self._client)

    @cached_property
    def credit_memos(self) -> AsyncCreditMemosResource:
        return AsyncCreditMemosResource(self._client)

    @cached_property
    def currencies(self) -> AsyncCurrenciesResource:
        return AsyncCurrenciesResource(self._client)

    @cached_property
    def customer_types(self) -> AsyncCustomerTypesResource:
        return AsyncCustomerTypesResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResource:
        return AsyncDateDrivenTermsResource(self._client)

    @cached_property
    def deleted_list_objects(self) -> AsyncDeletedListObjectsResource:
        return AsyncDeletedListObjectsResource(self._client)

    @cached_property
    def deleted_transactions(self) -> AsyncDeletedTransactionsResource:
        return AsyncDeletedTransactionsResource(self._client)

    @cached_property
    def discount_items(self) -> AsyncDiscountItemsResource:
        return AsyncDiscountItemsResource(self._client)

    @cached_property
    def employees(self) -> AsyncEmployeesResource:
        return AsyncEmployeesResource(self._client)

    @cached_property
    def estimates(self) -> AsyncEstimatesResource:
        return AsyncEstimatesResource(self._client)

    @cached_property
    def inventory_adjustments(self) -> AsyncInventoryAdjustmentsResource:
        return AsyncInventoryAdjustmentsResource(self._client)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResource:
        return AsyncInventoryAssemblyItemsResource(self._client)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResource:
        return AsyncInventoryItemsResource(self._client)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResource:
        return AsyncInventorySitesResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def item_groups(self) -> AsyncItemGroupsResource:
        return AsyncItemGroupsResource(self._client)

    @cached_property
    def item_receipts(self) -> AsyncItemReceiptsResource:
        return AsyncItemReceiptsResource(self._client)

    @cached_property
    def item_sites(self) -> AsyncItemSitesResource:
        return AsyncItemSitesResource(self._client)

    @cached_property
    def journal_entries(self) -> AsyncJournalEntriesResource:
        return AsyncJournalEntriesResource(self._client)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResource:
        return AsyncNonInventoryItemsResource(self._client)

    @cached_property
    def other_charge_items(self) -> AsyncOtherChargeItemsResource:
        return AsyncOtherChargeItemsResource(self._client)

    @cached_property
    def other_names(self) -> AsyncOtherNamesResource:
        return AsyncOtherNamesResource(self._client)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        return AsyncPaymentMethodsResource(self._client)

    @cached_property
    def payroll_wage_items(self) -> AsyncPayrollWageItemsResource:
        return AsyncPayrollWageItemsResource(self._client)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        return AsyncPreferencesResource(self._client)

    @cached_property
    def price_levels(self) -> AsyncPriceLevelsResource:
        return AsyncPriceLevelsResource(self._client)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResource:
        return AsyncPurchaseOrdersResource(self._client)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResource:
        return AsyncReceivePaymentsResource(self._client)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResource:
        return AsyncSalesOrdersResource(self._client)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResource:
        return AsyncSalesReceiptsResource(self._client)

    @cached_property
    def sales_representatives(self) -> AsyncSalesRepresentativesResource:
        return AsyncSalesRepresentativesResource(self._client)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResource:
        return AsyncSalesTaxCodesResource(self._client)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResource:
        return AsyncSalesTaxItemsResource(self._client)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResource:
        return AsyncServiceItemsResource(self._client)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResource:
        return AsyncStandardTermsResource(self._client)

    @cached_property
    def subtotal_items(self) -> AsyncSubtotalItemsResource:
        return AsyncSubtotalItemsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def time_tracking_activities(self) -> AsyncTimeTrackingActivitiesResource:
        return AsyncTimeTrackingActivitiesResource(self._client)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        return AsyncTransfersResource(self._client)

    @cached_property
    def unit_of_measure_sets(self) -> AsyncUnitOfMeasureSetsResource:
        return AsyncUnitOfMeasureSetsResource(self._client)

    @cached_property
    def vendor_credits(self) -> AsyncVendorCreditsResource:
        return AsyncVendorCreditsResource(self._client)

    @cached_property
    def vendors(self) -> AsyncVendorsResource:
        return AsyncVendorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQbdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQbdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQbdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncQbdResourceWithStreamingResponse(self)

    async def health_check(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QbdHealthCheckResponse:
        """
        Checks whether the specified QuickBooks Desktop connection is active and can
        process requests end-to-end. This is useful for showing a "connection status"
        indicator in your app. If an error occurs, the typical Conductor error response
        will be returned. As with any request to QuickBooks Desktop, the health check
        may fail if the application is not running, the wrong company file is open, or
        if a modal dialog is open. Timeout is 60 seconds.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/health-check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdHealthCheckResponse,
        )


class QbdResourceWithRawResponse:
    def __init__(self, qbd: QbdResource) -> None:
        self._qbd = qbd

        self.health_check = to_raw_response_wrapper(
            qbd.health_check,
        )

    @cached_property
    def account_tax_lines(self) -> AccountTaxLinesResourceWithRawResponse:
        return AccountTaxLinesResourceWithRawResponse(self._qbd.account_tax_lines)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._qbd.accounts)

    @cached_property
    def bill_check_payments(self) -> BillCheckPaymentsResourceWithRawResponse:
        return BillCheckPaymentsResourceWithRawResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResourceWithRawResponse:
        return BillCreditCardPaymentsResourceWithRawResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> BillsResourceWithRawResponse:
        return BillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def build_assemblies(self) -> BuildAssembliesResourceWithRawResponse:
        return BuildAssembliesResourceWithRawResponse(self._qbd.build_assemblies)

    @cached_property
    def checks(self) -> ChecksResourceWithRawResponse:
        return ChecksResourceWithRawResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> ClassesResourceWithRawResponse:
        return ClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._qbd.company)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithRawResponse:
        return CreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResourceWithRawResponse:
        return CreditCardCreditsResourceWithRawResponse(self._qbd.credit_card_credits)

    @cached_property
    def credit_card_refunds(self) -> CreditCardRefundsResourceWithRawResponse:
        return CreditCardRefundsResourceWithRawResponse(self._qbd.credit_card_refunds)

    @cached_property
    def credit_memos(self) -> CreditMemosResourceWithRawResponse:
        return CreditMemosResourceWithRawResponse(self._qbd.credit_memos)

    @cached_property
    def currencies(self) -> CurrenciesResourceWithRawResponse:
        return CurrenciesResourceWithRawResponse(self._qbd.currencies)

    @cached_property
    def customer_types(self) -> CustomerTypesResourceWithRawResponse:
        return CustomerTypesResourceWithRawResponse(self._qbd.customer_types)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResourceWithRawResponse:
        return DateDrivenTermsResourceWithRawResponse(self._qbd.date_driven_terms)

    @cached_property
    def deleted_list_objects(self) -> DeletedListObjectsResourceWithRawResponse:
        return DeletedListObjectsResourceWithRawResponse(self._qbd.deleted_list_objects)

    @cached_property
    def deleted_transactions(self) -> DeletedTransactionsResourceWithRawResponse:
        return DeletedTransactionsResourceWithRawResponse(self._qbd.deleted_transactions)

    @cached_property
    def discount_items(self) -> DiscountItemsResourceWithRawResponse:
        return DiscountItemsResourceWithRawResponse(self._qbd.discount_items)

    @cached_property
    def employees(self) -> EmployeesResourceWithRawResponse:
        return EmployeesResourceWithRawResponse(self._qbd.employees)

    @cached_property
    def estimates(self) -> EstimatesResourceWithRawResponse:
        return EstimatesResourceWithRawResponse(self._qbd.estimates)

    @cached_property
    def inventory_adjustments(self) -> InventoryAdjustmentsResourceWithRawResponse:
        return InventoryAdjustmentsResourceWithRawResponse(self._qbd.inventory_adjustments)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResourceWithRawResponse:
        return InventoryAssemblyItemsResourceWithRawResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> InventoryItemsResourceWithRawResponse:
        return InventoryItemsResourceWithRawResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> InventorySitesResourceWithRawResponse:
        return InventorySitesResourceWithRawResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def item_groups(self) -> ItemGroupsResourceWithRawResponse:
        return ItemGroupsResourceWithRawResponse(self._qbd.item_groups)

    @cached_property
    def item_receipts(self) -> ItemReceiptsResourceWithRawResponse:
        return ItemReceiptsResourceWithRawResponse(self._qbd.item_receipts)

    @cached_property
    def item_sites(self) -> ItemSitesResourceWithRawResponse:
        return ItemSitesResourceWithRawResponse(self._qbd.item_sites)

    @cached_property
    def journal_entries(self) -> JournalEntriesResourceWithRawResponse:
        return JournalEntriesResourceWithRawResponse(self._qbd.journal_entries)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResourceWithRawResponse:
        return NonInventoryItemsResourceWithRawResponse(self._qbd.non_inventory_items)

    @cached_property
    def other_charge_items(self) -> OtherChargeItemsResourceWithRawResponse:
        return OtherChargeItemsResourceWithRawResponse(self._qbd.other_charge_items)

    @cached_property
    def other_names(self) -> OtherNamesResourceWithRawResponse:
        return OtherNamesResourceWithRawResponse(self._qbd.other_names)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithRawResponse:
        return PaymentMethodsResourceWithRawResponse(self._qbd.payment_methods)

    @cached_property
    def payroll_wage_items(self) -> PayrollWageItemsResourceWithRawResponse:
        return PayrollWageItemsResourceWithRawResponse(self._qbd.payroll_wage_items)

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        return PreferencesResourceWithRawResponse(self._qbd.preferences)

    @cached_property
    def price_levels(self) -> PriceLevelsResourceWithRawResponse:
        return PriceLevelsResourceWithRawResponse(self._qbd.price_levels)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResourceWithRawResponse:
        return PurchaseOrdersResourceWithRawResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResourceWithRawResponse:
        return ReceivePaymentsResourceWithRawResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> SalesOrdersResourceWithRawResponse:
        return SalesOrdersResourceWithRawResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResourceWithRawResponse:
        return SalesReceiptsResourceWithRawResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_representatives(self) -> SalesRepresentativesResourceWithRawResponse:
        return SalesRepresentativesResourceWithRawResponse(self._qbd.sales_representatives)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResourceWithRawResponse:
        return SalesTaxCodesResourceWithRawResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResourceWithRawResponse:
        return SalesTaxItemsResourceWithRawResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> ServiceItemsResourceWithRawResponse:
        return ServiceItemsResourceWithRawResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithRawResponse:
        return StandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def subtotal_items(self) -> SubtotalItemsResourceWithRawResponse:
        return SubtotalItemsResourceWithRawResponse(self._qbd.subtotal_items)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._qbd.templates)

    @cached_property
    def time_tracking_activities(self) -> TimeTrackingActivitiesResourceWithRawResponse:
        return TimeTrackingActivitiesResourceWithRawResponse(self._qbd.time_tracking_activities)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._qbd.transactions)

    @cached_property
    def transfers(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self._qbd.transfers)

    @cached_property
    def unit_of_measure_sets(self) -> UnitOfMeasureSetsResourceWithRawResponse:
        return UnitOfMeasureSetsResourceWithRawResponse(self._qbd.unit_of_measure_sets)

    @cached_property
    def vendor_credits(self) -> VendorCreditsResourceWithRawResponse:
        return VendorCreditsResourceWithRawResponse(self._qbd.vendor_credits)

    @cached_property
    def vendors(self) -> VendorsResourceWithRawResponse:
        return VendorsResourceWithRawResponse(self._qbd.vendors)


class AsyncQbdResourceWithRawResponse:
    def __init__(self, qbd: AsyncQbdResource) -> None:
        self._qbd = qbd

        self.health_check = async_to_raw_response_wrapper(
            qbd.health_check,
        )

    @cached_property
    def account_tax_lines(self) -> AsyncAccountTaxLinesResourceWithRawResponse:
        return AsyncAccountTaxLinesResourceWithRawResponse(self._qbd.account_tax_lines)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._qbd.accounts)

    @cached_property
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResourceWithRawResponse:
        return AsyncBillCheckPaymentsResourceWithRawResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResourceWithRawResponse:
        return AsyncBillCreditCardPaymentsResourceWithRawResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithRawResponse:
        return AsyncBillsResourceWithRawResponse(self._qbd.bills)

    @cached_property
    def build_assemblies(self) -> AsyncBuildAssembliesResourceWithRawResponse:
        return AsyncBuildAssembliesResourceWithRawResponse(self._qbd.build_assemblies)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithRawResponse:
        return AsyncChecksResourceWithRawResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithRawResponse:
        return AsyncClassesResourceWithRawResponse(self._qbd.classes)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._qbd.company)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithRawResponse:
        return AsyncCreditCardChargesResourceWithRawResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResourceWithRawResponse:
        return AsyncCreditCardCreditsResourceWithRawResponse(self._qbd.credit_card_credits)

    @cached_property
    def credit_card_refunds(self) -> AsyncCreditCardRefundsResourceWithRawResponse:
        return AsyncCreditCardRefundsResourceWithRawResponse(self._qbd.credit_card_refunds)

    @cached_property
    def credit_memos(self) -> AsyncCreditMemosResourceWithRawResponse:
        return AsyncCreditMemosResourceWithRawResponse(self._qbd.credit_memos)

    @cached_property
    def currencies(self) -> AsyncCurrenciesResourceWithRawResponse:
        return AsyncCurrenciesResourceWithRawResponse(self._qbd.currencies)

    @cached_property
    def customer_types(self) -> AsyncCustomerTypesResourceWithRawResponse:
        return AsyncCustomerTypesResourceWithRawResponse(self._qbd.customer_types)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResourceWithRawResponse:
        return AsyncDateDrivenTermsResourceWithRawResponse(self._qbd.date_driven_terms)

    @cached_property
    def deleted_list_objects(self) -> AsyncDeletedListObjectsResourceWithRawResponse:
        return AsyncDeletedListObjectsResourceWithRawResponse(self._qbd.deleted_list_objects)

    @cached_property
    def deleted_transactions(self) -> AsyncDeletedTransactionsResourceWithRawResponse:
        return AsyncDeletedTransactionsResourceWithRawResponse(self._qbd.deleted_transactions)

    @cached_property
    def discount_items(self) -> AsyncDiscountItemsResourceWithRawResponse:
        return AsyncDiscountItemsResourceWithRawResponse(self._qbd.discount_items)

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithRawResponse:
        return AsyncEmployeesResourceWithRawResponse(self._qbd.employees)

    @cached_property
    def estimates(self) -> AsyncEstimatesResourceWithRawResponse:
        return AsyncEstimatesResourceWithRawResponse(self._qbd.estimates)

    @cached_property
    def inventory_adjustments(self) -> AsyncInventoryAdjustmentsResourceWithRawResponse:
        return AsyncInventoryAdjustmentsResourceWithRawResponse(self._qbd.inventory_adjustments)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResourceWithRawResponse:
        return AsyncInventoryAssemblyItemsResourceWithRawResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResourceWithRawResponse:
        return AsyncInventoryItemsResourceWithRawResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResourceWithRawResponse:
        return AsyncInventorySitesResourceWithRawResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._qbd.invoices)

    @cached_property
    def item_groups(self) -> AsyncItemGroupsResourceWithRawResponse:
        return AsyncItemGroupsResourceWithRawResponse(self._qbd.item_groups)

    @cached_property
    def item_receipts(self) -> AsyncItemReceiptsResourceWithRawResponse:
        return AsyncItemReceiptsResourceWithRawResponse(self._qbd.item_receipts)

    @cached_property
    def item_sites(self) -> AsyncItemSitesResourceWithRawResponse:
        return AsyncItemSitesResourceWithRawResponse(self._qbd.item_sites)

    @cached_property
    def journal_entries(self) -> AsyncJournalEntriesResourceWithRawResponse:
        return AsyncJournalEntriesResourceWithRawResponse(self._qbd.journal_entries)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResourceWithRawResponse:
        return AsyncNonInventoryItemsResourceWithRawResponse(self._qbd.non_inventory_items)

    @cached_property
    def other_charge_items(self) -> AsyncOtherChargeItemsResourceWithRawResponse:
        return AsyncOtherChargeItemsResourceWithRawResponse(self._qbd.other_charge_items)

    @cached_property
    def other_names(self) -> AsyncOtherNamesResourceWithRawResponse:
        return AsyncOtherNamesResourceWithRawResponse(self._qbd.other_names)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        return AsyncPaymentMethodsResourceWithRawResponse(self._qbd.payment_methods)

    @cached_property
    def payroll_wage_items(self) -> AsyncPayrollWageItemsResourceWithRawResponse:
        return AsyncPayrollWageItemsResourceWithRawResponse(self._qbd.payroll_wage_items)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        return AsyncPreferencesResourceWithRawResponse(self._qbd.preferences)

    @cached_property
    def price_levels(self) -> AsyncPriceLevelsResourceWithRawResponse:
        return AsyncPriceLevelsResourceWithRawResponse(self._qbd.price_levels)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResourceWithRawResponse:
        return AsyncPurchaseOrdersResourceWithRawResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResourceWithRawResponse:
        return AsyncReceivePaymentsResourceWithRawResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResourceWithRawResponse:
        return AsyncSalesOrdersResourceWithRawResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResourceWithRawResponse:
        return AsyncSalesReceiptsResourceWithRawResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_representatives(self) -> AsyncSalesRepresentativesResourceWithRawResponse:
        return AsyncSalesRepresentativesResourceWithRawResponse(self._qbd.sales_representatives)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResourceWithRawResponse:
        return AsyncSalesTaxCodesResourceWithRawResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResourceWithRawResponse:
        return AsyncSalesTaxItemsResourceWithRawResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResourceWithRawResponse:
        return AsyncServiceItemsResourceWithRawResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithRawResponse:
        return AsyncStandardTermsResourceWithRawResponse(self._qbd.standard_terms)

    @cached_property
    def subtotal_items(self) -> AsyncSubtotalItemsResourceWithRawResponse:
        return AsyncSubtotalItemsResourceWithRawResponse(self._qbd.subtotal_items)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._qbd.templates)

    @cached_property
    def time_tracking_activities(self) -> AsyncTimeTrackingActivitiesResourceWithRawResponse:
        return AsyncTimeTrackingActivitiesResourceWithRawResponse(self._qbd.time_tracking_activities)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._qbd.transactions)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self._qbd.transfers)

    @cached_property
    def unit_of_measure_sets(self) -> AsyncUnitOfMeasureSetsResourceWithRawResponse:
        return AsyncUnitOfMeasureSetsResourceWithRawResponse(self._qbd.unit_of_measure_sets)

    @cached_property
    def vendor_credits(self) -> AsyncVendorCreditsResourceWithRawResponse:
        return AsyncVendorCreditsResourceWithRawResponse(self._qbd.vendor_credits)

    @cached_property
    def vendors(self) -> AsyncVendorsResourceWithRawResponse:
        return AsyncVendorsResourceWithRawResponse(self._qbd.vendors)


class QbdResourceWithStreamingResponse:
    def __init__(self, qbd: QbdResource) -> None:
        self._qbd = qbd

        self.health_check = to_streamed_response_wrapper(
            qbd.health_check,
        )

    @cached_property
    def account_tax_lines(self) -> AccountTaxLinesResourceWithStreamingResponse:
        return AccountTaxLinesResourceWithStreamingResponse(self._qbd.account_tax_lines)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._qbd.accounts)

    @cached_property
    def bill_check_payments(self) -> BillCheckPaymentsResourceWithStreamingResponse:
        return BillCheckPaymentsResourceWithStreamingResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> BillCreditCardPaymentsResourceWithStreamingResponse:
        return BillCreditCardPaymentsResourceWithStreamingResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> BillsResourceWithStreamingResponse:
        return BillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def build_assemblies(self) -> BuildAssembliesResourceWithStreamingResponse:
        return BuildAssembliesResourceWithStreamingResponse(self._qbd.build_assemblies)

    @cached_property
    def checks(self) -> ChecksResourceWithStreamingResponse:
        return ChecksResourceWithStreamingResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> ClassesResourceWithStreamingResponse:
        return ClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._qbd.company)

    @cached_property
    def credit_card_charges(self) -> CreditCardChargesResourceWithStreamingResponse:
        return CreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> CreditCardCreditsResourceWithStreamingResponse:
        return CreditCardCreditsResourceWithStreamingResponse(self._qbd.credit_card_credits)

    @cached_property
    def credit_card_refunds(self) -> CreditCardRefundsResourceWithStreamingResponse:
        return CreditCardRefundsResourceWithStreamingResponse(self._qbd.credit_card_refunds)

    @cached_property
    def credit_memos(self) -> CreditMemosResourceWithStreamingResponse:
        return CreditMemosResourceWithStreamingResponse(self._qbd.credit_memos)

    @cached_property
    def currencies(self) -> CurrenciesResourceWithStreamingResponse:
        return CurrenciesResourceWithStreamingResponse(self._qbd.currencies)

    @cached_property
    def customer_types(self) -> CustomerTypesResourceWithStreamingResponse:
        return CustomerTypesResourceWithStreamingResponse(self._qbd.customer_types)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> DateDrivenTermsResourceWithStreamingResponse:
        return DateDrivenTermsResourceWithStreamingResponse(self._qbd.date_driven_terms)

    @cached_property
    def deleted_list_objects(self) -> DeletedListObjectsResourceWithStreamingResponse:
        return DeletedListObjectsResourceWithStreamingResponse(self._qbd.deleted_list_objects)

    @cached_property
    def deleted_transactions(self) -> DeletedTransactionsResourceWithStreamingResponse:
        return DeletedTransactionsResourceWithStreamingResponse(self._qbd.deleted_transactions)

    @cached_property
    def discount_items(self) -> DiscountItemsResourceWithStreamingResponse:
        return DiscountItemsResourceWithStreamingResponse(self._qbd.discount_items)

    @cached_property
    def employees(self) -> EmployeesResourceWithStreamingResponse:
        return EmployeesResourceWithStreamingResponse(self._qbd.employees)

    @cached_property
    def estimates(self) -> EstimatesResourceWithStreamingResponse:
        return EstimatesResourceWithStreamingResponse(self._qbd.estimates)

    @cached_property
    def inventory_adjustments(self) -> InventoryAdjustmentsResourceWithStreamingResponse:
        return InventoryAdjustmentsResourceWithStreamingResponse(self._qbd.inventory_adjustments)

    @cached_property
    def inventory_assembly_items(self) -> InventoryAssemblyItemsResourceWithStreamingResponse:
        return InventoryAssemblyItemsResourceWithStreamingResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> InventoryItemsResourceWithStreamingResponse:
        return InventoryItemsResourceWithStreamingResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> InventorySitesResourceWithStreamingResponse:
        return InventorySitesResourceWithStreamingResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def item_groups(self) -> ItemGroupsResourceWithStreamingResponse:
        return ItemGroupsResourceWithStreamingResponse(self._qbd.item_groups)

    @cached_property
    def item_receipts(self) -> ItemReceiptsResourceWithStreamingResponse:
        return ItemReceiptsResourceWithStreamingResponse(self._qbd.item_receipts)

    @cached_property
    def item_sites(self) -> ItemSitesResourceWithStreamingResponse:
        return ItemSitesResourceWithStreamingResponse(self._qbd.item_sites)

    @cached_property
    def journal_entries(self) -> JournalEntriesResourceWithStreamingResponse:
        return JournalEntriesResourceWithStreamingResponse(self._qbd.journal_entries)

    @cached_property
    def non_inventory_items(self) -> NonInventoryItemsResourceWithStreamingResponse:
        return NonInventoryItemsResourceWithStreamingResponse(self._qbd.non_inventory_items)

    @cached_property
    def other_charge_items(self) -> OtherChargeItemsResourceWithStreamingResponse:
        return OtherChargeItemsResourceWithStreamingResponse(self._qbd.other_charge_items)

    @cached_property
    def other_names(self) -> OtherNamesResourceWithStreamingResponse:
        return OtherNamesResourceWithStreamingResponse(self._qbd.other_names)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithStreamingResponse:
        return PaymentMethodsResourceWithStreamingResponse(self._qbd.payment_methods)

    @cached_property
    def payroll_wage_items(self) -> PayrollWageItemsResourceWithStreamingResponse:
        return PayrollWageItemsResourceWithStreamingResponse(self._qbd.payroll_wage_items)

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        return PreferencesResourceWithStreamingResponse(self._qbd.preferences)

    @cached_property
    def price_levels(self) -> PriceLevelsResourceWithStreamingResponse:
        return PriceLevelsResourceWithStreamingResponse(self._qbd.price_levels)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersResourceWithStreamingResponse:
        return PurchaseOrdersResourceWithStreamingResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> ReceivePaymentsResourceWithStreamingResponse:
        return ReceivePaymentsResourceWithStreamingResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> SalesOrdersResourceWithStreamingResponse:
        return SalesOrdersResourceWithStreamingResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> SalesReceiptsResourceWithStreamingResponse:
        return SalesReceiptsResourceWithStreamingResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_representatives(self) -> SalesRepresentativesResourceWithStreamingResponse:
        return SalesRepresentativesResourceWithStreamingResponse(self._qbd.sales_representatives)

    @cached_property
    def sales_tax_codes(self) -> SalesTaxCodesResourceWithStreamingResponse:
        return SalesTaxCodesResourceWithStreamingResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> SalesTaxItemsResourceWithStreamingResponse:
        return SalesTaxItemsResourceWithStreamingResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> ServiceItemsResourceWithStreamingResponse:
        return ServiceItemsResourceWithStreamingResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> StandardTermsResourceWithStreamingResponse:
        return StandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def subtotal_items(self) -> SubtotalItemsResourceWithStreamingResponse:
        return SubtotalItemsResourceWithStreamingResponse(self._qbd.subtotal_items)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._qbd.templates)

    @cached_property
    def time_tracking_activities(self) -> TimeTrackingActivitiesResourceWithStreamingResponse:
        return TimeTrackingActivitiesResourceWithStreamingResponse(self._qbd.time_tracking_activities)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._qbd.transactions)

    @cached_property
    def transfers(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self._qbd.transfers)

    @cached_property
    def unit_of_measure_sets(self) -> UnitOfMeasureSetsResourceWithStreamingResponse:
        return UnitOfMeasureSetsResourceWithStreamingResponse(self._qbd.unit_of_measure_sets)

    @cached_property
    def vendor_credits(self) -> VendorCreditsResourceWithStreamingResponse:
        return VendorCreditsResourceWithStreamingResponse(self._qbd.vendor_credits)

    @cached_property
    def vendors(self) -> VendorsResourceWithStreamingResponse:
        return VendorsResourceWithStreamingResponse(self._qbd.vendors)


class AsyncQbdResourceWithStreamingResponse:
    def __init__(self, qbd: AsyncQbdResource) -> None:
        self._qbd = qbd

        self.health_check = async_to_streamed_response_wrapper(
            qbd.health_check,
        )

    @cached_property
    def account_tax_lines(self) -> AsyncAccountTaxLinesResourceWithStreamingResponse:
        return AsyncAccountTaxLinesResourceWithStreamingResponse(self._qbd.account_tax_lines)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._qbd.accounts)

    @cached_property
    def bill_check_payments(self) -> AsyncBillCheckPaymentsResourceWithStreamingResponse:
        return AsyncBillCheckPaymentsResourceWithStreamingResponse(self._qbd.bill_check_payments)

    @cached_property
    def bill_credit_card_payments(self) -> AsyncBillCreditCardPaymentsResourceWithStreamingResponse:
        return AsyncBillCreditCardPaymentsResourceWithStreamingResponse(self._qbd.bill_credit_card_payments)

    @cached_property
    def bills(self) -> AsyncBillsResourceWithStreamingResponse:
        return AsyncBillsResourceWithStreamingResponse(self._qbd.bills)

    @cached_property
    def build_assemblies(self) -> AsyncBuildAssembliesResourceWithStreamingResponse:
        return AsyncBuildAssembliesResourceWithStreamingResponse(self._qbd.build_assemblies)

    @cached_property
    def checks(self) -> AsyncChecksResourceWithStreamingResponse:
        return AsyncChecksResourceWithStreamingResponse(self._qbd.checks)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithStreamingResponse:
        return AsyncClassesResourceWithStreamingResponse(self._qbd.classes)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._qbd.company)

    @cached_property
    def credit_card_charges(self) -> AsyncCreditCardChargesResourceWithStreamingResponse:
        return AsyncCreditCardChargesResourceWithStreamingResponse(self._qbd.credit_card_charges)

    @cached_property
    def credit_card_credits(self) -> AsyncCreditCardCreditsResourceWithStreamingResponse:
        return AsyncCreditCardCreditsResourceWithStreamingResponse(self._qbd.credit_card_credits)

    @cached_property
    def credit_card_refunds(self) -> AsyncCreditCardRefundsResourceWithStreamingResponse:
        return AsyncCreditCardRefundsResourceWithStreamingResponse(self._qbd.credit_card_refunds)

    @cached_property
    def credit_memos(self) -> AsyncCreditMemosResourceWithStreamingResponse:
        return AsyncCreditMemosResourceWithStreamingResponse(self._qbd.credit_memos)

    @cached_property
    def currencies(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        return AsyncCurrenciesResourceWithStreamingResponse(self._qbd.currencies)

    @cached_property
    def customer_types(self) -> AsyncCustomerTypesResourceWithStreamingResponse:
        return AsyncCustomerTypesResourceWithStreamingResponse(self._qbd.customer_types)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._qbd.customers)

    @cached_property
    def date_driven_terms(self) -> AsyncDateDrivenTermsResourceWithStreamingResponse:
        return AsyncDateDrivenTermsResourceWithStreamingResponse(self._qbd.date_driven_terms)

    @cached_property
    def deleted_list_objects(self) -> AsyncDeletedListObjectsResourceWithStreamingResponse:
        return AsyncDeletedListObjectsResourceWithStreamingResponse(self._qbd.deleted_list_objects)

    @cached_property
    def deleted_transactions(self) -> AsyncDeletedTransactionsResourceWithStreamingResponse:
        return AsyncDeletedTransactionsResourceWithStreamingResponse(self._qbd.deleted_transactions)

    @cached_property
    def discount_items(self) -> AsyncDiscountItemsResourceWithStreamingResponse:
        return AsyncDiscountItemsResourceWithStreamingResponse(self._qbd.discount_items)

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithStreamingResponse:
        return AsyncEmployeesResourceWithStreamingResponse(self._qbd.employees)

    @cached_property
    def estimates(self) -> AsyncEstimatesResourceWithStreamingResponse:
        return AsyncEstimatesResourceWithStreamingResponse(self._qbd.estimates)

    @cached_property
    def inventory_adjustments(self) -> AsyncInventoryAdjustmentsResourceWithStreamingResponse:
        return AsyncInventoryAdjustmentsResourceWithStreamingResponse(self._qbd.inventory_adjustments)

    @cached_property
    def inventory_assembly_items(self) -> AsyncInventoryAssemblyItemsResourceWithStreamingResponse:
        return AsyncInventoryAssemblyItemsResourceWithStreamingResponse(self._qbd.inventory_assembly_items)

    @cached_property
    def inventory_items(self) -> AsyncInventoryItemsResourceWithStreamingResponse:
        return AsyncInventoryItemsResourceWithStreamingResponse(self._qbd.inventory_items)

    @cached_property
    def inventory_sites(self) -> AsyncInventorySitesResourceWithStreamingResponse:
        return AsyncInventorySitesResourceWithStreamingResponse(self._qbd.inventory_sites)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._qbd.invoices)

    @cached_property
    def item_groups(self) -> AsyncItemGroupsResourceWithStreamingResponse:
        return AsyncItemGroupsResourceWithStreamingResponse(self._qbd.item_groups)

    @cached_property
    def item_receipts(self) -> AsyncItemReceiptsResourceWithStreamingResponse:
        return AsyncItemReceiptsResourceWithStreamingResponse(self._qbd.item_receipts)

    @cached_property
    def item_sites(self) -> AsyncItemSitesResourceWithStreamingResponse:
        return AsyncItemSitesResourceWithStreamingResponse(self._qbd.item_sites)

    @cached_property
    def journal_entries(self) -> AsyncJournalEntriesResourceWithStreamingResponse:
        return AsyncJournalEntriesResourceWithStreamingResponse(self._qbd.journal_entries)

    @cached_property
    def non_inventory_items(self) -> AsyncNonInventoryItemsResourceWithStreamingResponse:
        return AsyncNonInventoryItemsResourceWithStreamingResponse(self._qbd.non_inventory_items)

    @cached_property
    def other_charge_items(self) -> AsyncOtherChargeItemsResourceWithStreamingResponse:
        return AsyncOtherChargeItemsResourceWithStreamingResponse(self._qbd.other_charge_items)

    @cached_property
    def other_names(self) -> AsyncOtherNamesResourceWithStreamingResponse:
        return AsyncOtherNamesResourceWithStreamingResponse(self._qbd.other_names)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        return AsyncPaymentMethodsResourceWithStreamingResponse(self._qbd.payment_methods)

    @cached_property
    def payroll_wage_items(self) -> AsyncPayrollWageItemsResourceWithStreamingResponse:
        return AsyncPayrollWageItemsResourceWithStreamingResponse(self._qbd.payroll_wage_items)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        return AsyncPreferencesResourceWithStreamingResponse(self._qbd.preferences)

    @cached_property
    def price_levels(self) -> AsyncPriceLevelsResourceWithStreamingResponse:
        return AsyncPriceLevelsResourceWithStreamingResponse(self._qbd.price_levels)

    @cached_property
    def purchase_orders(self) -> AsyncPurchaseOrdersResourceWithStreamingResponse:
        return AsyncPurchaseOrdersResourceWithStreamingResponse(self._qbd.purchase_orders)

    @cached_property
    def receive_payments(self) -> AsyncReceivePaymentsResourceWithStreamingResponse:
        return AsyncReceivePaymentsResourceWithStreamingResponse(self._qbd.receive_payments)

    @cached_property
    def sales_orders(self) -> AsyncSalesOrdersResourceWithStreamingResponse:
        return AsyncSalesOrdersResourceWithStreamingResponse(self._qbd.sales_orders)

    @cached_property
    def sales_receipts(self) -> AsyncSalesReceiptsResourceWithStreamingResponse:
        return AsyncSalesReceiptsResourceWithStreamingResponse(self._qbd.sales_receipts)

    @cached_property
    def sales_representatives(self) -> AsyncSalesRepresentativesResourceWithStreamingResponse:
        return AsyncSalesRepresentativesResourceWithStreamingResponse(self._qbd.sales_representatives)

    @cached_property
    def sales_tax_codes(self) -> AsyncSalesTaxCodesResourceWithStreamingResponse:
        return AsyncSalesTaxCodesResourceWithStreamingResponse(self._qbd.sales_tax_codes)

    @cached_property
    def sales_tax_items(self) -> AsyncSalesTaxItemsResourceWithStreamingResponse:
        return AsyncSalesTaxItemsResourceWithStreamingResponse(self._qbd.sales_tax_items)

    @cached_property
    def service_items(self) -> AsyncServiceItemsResourceWithStreamingResponse:
        return AsyncServiceItemsResourceWithStreamingResponse(self._qbd.service_items)

    @cached_property
    def standard_terms(self) -> AsyncStandardTermsResourceWithStreamingResponse:
        return AsyncStandardTermsResourceWithStreamingResponse(self._qbd.standard_terms)

    @cached_property
    def subtotal_items(self) -> AsyncSubtotalItemsResourceWithStreamingResponse:
        return AsyncSubtotalItemsResourceWithStreamingResponse(self._qbd.subtotal_items)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._qbd.templates)

    @cached_property
    def time_tracking_activities(self) -> AsyncTimeTrackingActivitiesResourceWithStreamingResponse:
        return AsyncTimeTrackingActivitiesResourceWithStreamingResponse(self._qbd.time_tracking_activities)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._qbd.transactions)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self._qbd.transfers)

    @cached_property
    def unit_of_measure_sets(self) -> AsyncUnitOfMeasureSetsResourceWithStreamingResponse:
        return AsyncUnitOfMeasureSetsResourceWithStreamingResponse(self._qbd.unit_of_measure_sets)

    @cached_property
    def vendor_credits(self) -> AsyncVendorCreditsResourceWithStreamingResponse:
        return AsyncVendorCreditsResourceWithStreamingResponse(self._qbd.vendor_credits)

    @cached_property
    def vendors(self) -> AsyncVendorsResourceWithStreamingResponse:
        return AsyncVendorsResourceWithStreamingResponse(self._qbd.vendors)
