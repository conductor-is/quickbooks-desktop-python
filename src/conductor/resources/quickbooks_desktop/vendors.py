# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.quickbooks_desktop import vendor_list_params, vendor_create_params
from ...types.quickbooks_desktop.qbd_vendor import QbdVendor
from ...types.quickbooks_desktop.vendor_list_response import VendorListResponse

__all__ = ["VendorsResource", "AsyncVendorsResource"]


class VendorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VendorsResourceWithRawResponse:
        return VendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VendorsResourceWithStreamingResponse:
        return VendorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[vendor_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: List[str] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_address: vendor_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[vendor_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_eligible_for1099: bool | NotGiven = NOT_GIVEN,
        is_sales_tax_agency: bool | NotGiven = NOT_GIVEN,
        is_tax_on_tax: bool | NotGiven = NOT_GIVEN,
        is_tax_tracked_on_purchases: bool | NotGiven = NOT_GIVEN,
        is_tax_tracked_on_sales: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        open_balance: str | NotGiven = NOT_GIVEN,
        open_balance_date: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        prefill_account_ids: List[str] | NotGiven = NOT_GIVEN,
        reporting_period: Literal["Monthly", "Quarterly"] | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_return_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: vendor_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_id: str | NotGiven = NOT_GIVEN,
        tax_on_purchases_account_id: str | NotGiven = NOT_GIVEN,
        tax_on_sales_account_id: str | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdVendor:
        """
        Creates a vendor.

        Args:
          name: The vendor's case-insensitive unique name, unique across all vendors.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The vendor's account number.

          additional_contacts: Additional contacts.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The vendor's alternate contact name.

          alternate_phone: The vendor's alternate phone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The ID of the billing rate associated with this vendor. Use this rate to
              override a service-item's rate when recording a time-tracking transaction for
              this vendor.

          cc: The vendor's CC email address.

          check_name: The vendor's name as it will appear on checks sent to the vendor.

          class_id: The class associated with this object. Classes can be used to categorize objects
              or transactions by department, location, or other meaningful segments.

          company_name: The name of the vendor's business. This is used on invoices, checks, and other
              forms.

          contact: The vendor's contact name.

          credit_limit: The vendor's credit limit.

          currency_id: The ID of the currency associated with this vendor.

          custom_contact_fields: Additional custom contact fields.

          email: The vendor's email address.

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          fax: The vendor's fax number.

          first_name: The vendor's first name.

          is_active: Whether this vendor is active. QuickBooks hides inactive objects from most views
              and reports in the UI.

          is_eligible_for1099: Whether the vendor is eligible for 1099. If `true`, then the fields `taxId` and
              `billingAddress` are required.

          is_sales_tax_agency: Whether this vendor is a sales tax agency. If true, the vendor is responsible
              for collecting and remitting sales tax.

          is_tax_on_tax: Whether tax is charged on top of tax in Canada or the UK for this vendor.

          is_tax_tracked_on_purchases: Whether tax is tracked on purchases in Canada or the UK for this vendor.

          is_tax_tracked_on_sales: Whether tax is tracked on sales in Canada or the UK for this vendor.

          job_title: The vendor's job title.

          last_name: The vendor's last name.

          middle_name: The vendor's middle name.

          note: Additional information about this vendor.

          open_balance: The opening balance of this vendor's account. A positive number indicates money
              owed to this vendor.

          open_balance_date: The date of the opening balance for this vendor, in ISO 8601 format
              (YYYY-MM-DD).

          phone: The vendor's phone number.

          prefill_account_ids: The IDs of the accounts to prefill when entering bills for this vendor.

          sales_tax_code_id: The ID of the sales tax code associated with this vendor. Sales tax codes
              indicate whether items are taxable or non-taxable. Two default codes are 'Non'
              (non-taxable) and 'Tax' (taxable). This code determines how sales tax is applied
              to items related to this vendor. If QuickBooks is not set up to charge sales
              tax, it will assign the default non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected.

          sales_tax_return_id: The ID of the sales tax return associated with this vendor. This is used to
              track sales tax returns for this vendor.

          salutation: The vendor's formal salutation that precedes their name.

          shipping_address: The vendor's shipping address.

          tax_id: The vendor's tax ID.

          tax_on_purchases_account_id: The ID of the account used for taxes on purchases in Canada or the UK for this
              vendor.

          tax_on_sales_account_id: The ID of the account used for taxes on sales in Canada or the UK for this
              vendor.

          tax_registration_number: The tax registration number associated with this vendor.

          terms_id: The ID of the vendor's payment terms, which define how the vendor is paid.

          vendor_type_id: The ID of the vendor's type, used for categorization. This can represent
              industry, location, or other business-specific classifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/vendors",
            body=maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "billing_rate_id": billing_rate_id,
                    "cc": cc,
                    "check_name": check_name,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tax_on_tax": is_tax_on_tax,
                    "is_tax_tracked_on_purchases": is_tax_tracked_on_purchases,
                    "is_tax_tracked_on_sales": is_tax_tracked_on_sales,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "open_balance": open_balance,
                    "open_balance_date": open_balance_date,
                    "phone": phone,
                    "prefill_account_ids": prefill_account_ids,
                    "reporting_period": reporting_period,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                    "tax_on_purchases_account_id": tax_on_purchases_account_id,
                    "tax_on_sales_account_id": tax_on_sales_account_id,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_create_params.VendorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdVendor,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        class_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        currency_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_gt: str | NotGiven = NOT_GIVEN,
        total_balance_gte: str | NotGiven = NOT_GIVEN,
        total_balance_lt: str | NotGiven = NOT_GIVEN,
        total_balance_lte: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VendorListResponse:
        """
        Returns a list of vendors.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for vendors with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          class_id: Filter for vendors of this class or classes. A class is a way end-users can
              categorize vendors in QuickBooks.

          currency_id: Filter for vendors in this currency or currencies.

          cursor: The pagination token to use with the `cursor` request parameter to fetch the
              next set of results. This value was returned in the `nextCursor` field of the
              previous response when using the `limit` parameter.

          full_name: Filter for vendors with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for a vendor, and is created by prefixing the vendor's name
              with the names of each ancestor. If your request includes this parameter, all
              other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Include this parameter to paginate through the results. The `nextCursor` field
              in the response will contain the value to use with the `cursor` request
              parameter to fetch the next set of results.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          total_balance: Filter for objects whose `totalBalance` equals this amount. You can only use one
              total-balance filter at a time.

          total_balance_gt: Filter for objects whose `totalBalance` is greater than this amount. You can
              only use one total-balance filter at a time.

          total_balance_gte: Filter for objects whose `totalBalance` is greater than or equal to this amount.
              You can only use one total-balance filter at a time.

          total_balance_lt: Filter for objects whose `totalBalance` is less than this amount. You can only
              use one total-balance filter at a time.

          total_balance_lte: Filter for objects whose `totalBalance` is less than or equal to this amount.
              You can only use one total-balance filter at a time.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/vendors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "class_id": class_id,
                        "currency_id": currency_id,
                        "cursor": cursor,
                        "full_name": full_name,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_gt": total_balance_gt,
                        "total_balance_gte": total_balance_gte,
                        "total_balance_lt": total_balance_lt,
                        "total_balance_lte": total_balance_lte,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    vendor_list_params.VendorListParams,
                ),
            ),
            cast_to=VendorListResponse,
        )


class AsyncVendorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVendorsResourceWithRawResponse:
        return AsyncVendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVendorsResourceWithStreamingResponse:
        return AsyncVendorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[vendor_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: List[str] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_address: vendor_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[vendor_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_eligible_for1099: bool | NotGiven = NOT_GIVEN,
        is_sales_tax_agency: bool | NotGiven = NOT_GIVEN,
        is_tax_on_tax: bool | NotGiven = NOT_GIVEN,
        is_tax_tracked_on_purchases: bool | NotGiven = NOT_GIVEN,
        is_tax_tracked_on_sales: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        open_balance: str | NotGiven = NOT_GIVEN,
        open_balance_date: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        prefill_account_ids: List[str] | NotGiven = NOT_GIVEN,
        reporting_period: Literal["Monthly", "Quarterly"] | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_return_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: vendor_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_id: str | NotGiven = NOT_GIVEN,
        tax_on_purchases_account_id: str | NotGiven = NOT_GIVEN,
        tax_on_sales_account_id: str | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdVendor:
        """
        Creates a vendor.

        Args:
          name: The vendor's case-insensitive unique name, unique across all vendors.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The vendor's account number.

          additional_contacts: Additional contacts.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The vendor's alternate contact name.

          alternate_phone: The vendor's alternate phone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The ID of the billing rate associated with this vendor. Use this rate to
              override a service-item's rate when recording a time-tracking transaction for
              this vendor.

          cc: The vendor's CC email address.

          check_name: The vendor's name as it will appear on checks sent to the vendor.

          class_id: The class associated with this object. Classes can be used to categorize objects
              or transactions by department, location, or other meaningful segments.

          company_name: The name of the vendor's business. This is used on invoices, checks, and other
              forms.

          contact: The vendor's contact name.

          credit_limit: The vendor's credit limit.

          currency_id: The ID of the currency associated with this vendor.

          custom_contact_fields: Additional custom contact fields.

          email: The vendor's email address.

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          fax: The vendor's fax number.

          first_name: The vendor's first name.

          is_active: Whether this vendor is active. QuickBooks hides inactive objects from most views
              and reports in the UI.

          is_eligible_for1099: Whether the vendor is eligible for 1099. If `true`, then the fields `taxId` and
              `billingAddress` are required.

          is_sales_tax_agency: Whether this vendor is a sales tax agency. If true, the vendor is responsible
              for collecting and remitting sales tax.

          is_tax_on_tax: Whether tax is charged on top of tax in Canada or the UK for this vendor.

          is_tax_tracked_on_purchases: Whether tax is tracked on purchases in Canada or the UK for this vendor.

          is_tax_tracked_on_sales: Whether tax is tracked on sales in Canada or the UK for this vendor.

          job_title: The vendor's job title.

          last_name: The vendor's last name.

          middle_name: The vendor's middle name.

          note: Additional information about this vendor.

          open_balance: The opening balance of this vendor's account. A positive number indicates money
              owed to this vendor.

          open_balance_date: The date of the opening balance for this vendor, in ISO 8601 format
              (YYYY-MM-DD).

          phone: The vendor's phone number.

          prefill_account_ids: The IDs of the accounts to prefill when entering bills for this vendor.

          sales_tax_code_id: The ID of the sales tax code associated with this vendor. Sales tax codes
              indicate whether items are taxable or non-taxable. Two default codes are 'Non'
              (non-taxable) and 'Tax' (taxable). This code determines how sales tax is applied
              to items related to this vendor. If QuickBooks is not set up to charge sales
              tax, it will assign the default non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected.

          sales_tax_return_id: The ID of the sales tax return associated with this vendor. This is used to
              track sales tax returns for this vendor.

          salutation: The vendor's formal salutation that precedes their name.

          shipping_address: The vendor's shipping address.

          tax_id: The vendor's tax ID.

          tax_on_purchases_account_id: The ID of the account used for taxes on purchases in Canada or the UK for this
              vendor.

          tax_on_sales_account_id: The ID of the account used for taxes on sales in Canada or the UK for this
              vendor.

          tax_registration_number: The tax registration number associated with this vendor.

          terms_id: The ID of the vendor's payment terms, which define how the vendor is paid.

          vendor_type_id: The ID of the vendor's type, used for categorization. This can represent
              industry, location, or other business-specific classifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/vendors",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "billing_rate_id": billing_rate_id,
                    "cc": cc,
                    "check_name": check_name,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tax_on_tax": is_tax_on_tax,
                    "is_tax_tracked_on_purchases": is_tax_tracked_on_purchases,
                    "is_tax_tracked_on_sales": is_tax_tracked_on_sales,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "open_balance": open_balance,
                    "open_balance_date": open_balance_date,
                    "phone": phone,
                    "prefill_account_ids": prefill_account_ids,
                    "reporting_period": reporting_period,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                    "tax_on_purchases_account_id": tax_on_purchases_account_id,
                    "tax_on_sales_account_id": tax_on_sales_account_id,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_create_params.VendorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdVendor,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        class_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        currency_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_gt: str | NotGiven = NOT_GIVEN,
        total_balance_gte: str | NotGiven = NOT_GIVEN,
        total_balance_lt: str | NotGiven = NOT_GIVEN,
        total_balance_lte: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VendorListResponse:
        """
        Returns a list of vendors.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for vendors with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          class_id: Filter for vendors of this class or classes. A class is a way end-users can
              categorize vendors in QuickBooks.

          currency_id: Filter for vendors in this currency or currencies.

          cursor: The pagination token to use with the `cursor` request parameter to fetch the
              next set of results. This value was returned in the `nextCursor` field of the
              previous response when using the `limit` parameter.

          full_name: Filter for vendors with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for a vendor, and is created by prefixing the vendor's name
              with the names of each ancestor. If your request includes this parameter, all
              other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Include this parameter to paginate through the results. The `nextCursor` field
              in the response will contain the value to use with the `cursor` request
              parameter to fetch the next set of results.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          total_balance: Filter for objects whose `totalBalance` equals this amount. You can only use one
              total-balance filter at a time.

          total_balance_gt: Filter for objects whose `totalBalance` is greater than this amount. You can
              only use one total-balance filter at a time.

          total_balance_gte: Filter for objects whose `totalBalance` is greater than or equal to this amount.
              You can only use one total-balance filter at a time.

          total_balance_lt: Filter for objects whose `totalBalance` is less than this amount. You can only
              use one total-balance filter at a time.

          total_balance_lte: Filter for objects whose `totalBalance` is less than or equal to this amount.
              You can only use one total-balance filter at a time.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/vendors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "class_id": class_id,
                        "currency_id": currency_id,
                        "cursor": cursor,
                        "full_name": full_name,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_gt": total_balance_gt,
                        "total_balance_gte": total_balance_gte,
                        "total_balance_lt": total_balance_lt,
                        "total_balance_lte": total_balance_lte,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    vendor_list_params.VendorListParams,
                ),
            ),
            cast_to=VendorListResponse,
        )


class VendorsResourceWithRawResponse:
    def __init__(self, vendors: VendorsResource) -> None:
        self._vendors = vendors

        self.create = to_raw_response_wrapper(
            vendors.create,
        )
        self.list = to_raw_response_wrapper(
            vendors.list,
        )


class AsyncVendorsResourceWithRawResponse:
    def __init__(self, vendors: AsyncVendorsResource) -> None:
        self._vendors = vendors

        self.create = async_to_raw_response_wrapper(
            vendors.create,
        )
        self.list = async_to_raw_response_wrapper(
            vendors.list,
        )


class VendorsResourceWithStreamingResponse:
    def __init__(self, vendors: VendorsResource) -> None:
        self._vendors = vendors

        self.create = to_streamed_response_wrapper(
            vendors.create,
        )
        self.list = to_streamed_response_wrapper(
            vendors.list,
        )


class AsyncVendorsResourceWithStreamingResponse:
    def __init__(self, vendors: AsyncVendorsResource) -> None:
        self._vendors = vendors

        self.create = async_to_streamed_response_wrapper(
            vendors.create,
        )
        self.list = async_to_streamed_response_wrapper(
            vendors.list,
        )
