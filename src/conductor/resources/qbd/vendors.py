# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import vendor_list_params, vendor_create_params, vendor_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.vendor import Vendor

__all__ = ["VendorsResource", "AsyncVendorsResource"]


class VendorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VendorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return VendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VendorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return VendorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_contacts: Iterable[vendor_create_params.AdditionalContact] | Omit = omit,
        additional_notes: Iterable[vendor_create_params.AdditionalNote] | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_address: vendor_create_params.BillingAddress | Omit = omit,
        billing_rate_id: str | Omit = omit,
        cc_email: str | Omit = omit,
        class_id: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        credit_limit: str | Omit = omit,
        currency_id: str | Omit = omit,
        custom_contact_fields: Iterable[vendor_create_params.CustomContactField] | Omit = omit,
        default_expense_account_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_compounding_tax: bool | Omit = omit,
        is_eligible_for1099: bool | Omit = omit,
        is_sales_tax_agency: bool | Omit = omit,
        is_tracking_purchase_tax: bool | Omit = omit,
        is_tracking_sales_tax: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name_on_check: str | Omit = omit,
        note: str | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, date] | Omit = omit,
        phone: str | Omit = omit,
        purchase_tax_account_id: str | Omit = omit,
        reporting_period: Literal["monthly", "quarterly"] | Omit = omit,
        sales_tax_account_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | Omit = omit,
        sales_tax_return_id: str | Omit = omit,
        salutation: str | Omit = omit,
        shipping_address: vendor_create_params.ShippingAddress | Omit = omit,
        tax_identification_number: str | Omit = omit,
        tax_registration_number: str | Omit = omit,
        terms_id: str | Omit = omit,
        vendor_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Creates a new vendor.

        Args:
          name: The case-insensitive unique name of this vendor, unique across all vendors.

              **NOTE**: Vendors do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 41 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The vendor's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this vendor.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The name of a alternate contact person for this vendor.

          alternate_phone: The vendor's alternate telephone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The vendor's billing rate, used to override service item rates in time tracking
              activities.

          cc_email: An email address to carbon copy (CC) on communications with this vendor.

          class_id: The vendor's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this vendor. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this vendor.

          credit_limit: The vendor's credit limit, represented as a decimal string. This is the maximum
              amount of money that can be spent being before billed by this vendor. If `null`,
              there is no credit limit.

          currency_id: The vendor's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this vendor, such as phone numbers or email
              addresses.

          default_expense_account_ids: The expense accounts to prefill when entering bills for this vendor.

          email: The vendor's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The vendor's fax number.

          first_name: The first name of the contact person for this vendor.

              Maximum length: 25 characters.

          is_active: Indicates whether this vendor is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          is_compounding_tax: Indicates whether tax is charged on top of tax for this vendor, for use in
              Canada or the UK.

          is_eligible_for1099: Indicates whether this vendor is eligible to receive a 1099 form for tax
              reporting purposes. When `true`, then the fields `taxId` and `billingAddress`
              are required.

          is_sales_tax_agency: Indicates whether this vendor is a sales tax agency.

          is_tracking_purchase_tax: Indicates whether tax is tracked on purchases for this vendor, for use in Canada
              or the UK.

          is_tracking_sales_tax: Indicates whether tax is tracked on sales for this vendor, for use in Canada or
              the UK.

          job_title: The job title of the contact person for this vendor.

          last_name: The last name of the contact person for this vendor.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this vendor.

              Maximum length: 5 characters.

          name_on_check: The vendor's name as it should appear on checks issued to this vendor.

          note: A note or comment about this vendor.

          opening_balance: The opening balance of this vendor's account, indicating the amount owed to this
              vendor, represented as a decimal string.

          opening_balance_date: The date of the opening balance of this vendor, in ISO 8601 format (YYYY-MM-DD).

          phone: The vendor's primary telephone number.

          purchase_tax_account_id: The account used for tracking taxes on purchases for this vendor, for use in
              Canada or the UK.

          reporting_period: The vendor's tax reporting period, for use in Canada or the UK.

          sales_tax_account_id: The account used for tracking taxes on sales for this vendor, for use in Canada
              or the UK.

          sales_tax_code_id: The default sales-tax code for transactions with this vendor, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this vendor.

          sales_tax_return_id: The vendor's sales tax return information, used for tracking and reporting sales
              tax liabilities.

          salutation: The formal salutation title that precedes the name of the contact person for
              this vendor, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The vendor's shipping address.

          tax_identification_number: The vendor's tax identification number (e.g., EIN or SSN).

          tax_registration_number: The vendor's tax registration number, for use in Canada or the UK.

          terms_id: The vendor's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_type_id: The vendor's type, used for categorizing vendors into meaningful segments, such
              as industry or region.

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
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "default_expense_account_ids": default_expense_account_ids,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_compounding_tax": is_compounding_tax,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tracking_purchase_tax": is_tracking_purchase_tax,
                    "is_tracking_sales_tax": is_tracking_sales_tax,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name_on_check": name_on_check,
                    "note": note,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "phone": phone,
                    "purchase_tax_account_id": purchase_tax_account_id,
                    "reporting_period": reporting_period,
                    "sales_tax_account_id": sales_tax_account_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_identification_number": tax_identification_number,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_create_params.VendorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Retrieves a vendor by ID.

        **IMPORTANT:** If you need to fetch multiple specific vendors by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/vendors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_contacts: Iterable[vendor_update_params.AdditionalContact] | Omit = omit,
        additional_notes: Iterable[vendor_update_params.AdditionalNote] | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_address: vendor_update_params.BillingAddress | Omit = omit,
        billing_rate_id: str | Omit = omit,
        cc_email: str | Omit = omit,
        class_id: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        credit_limit: str | Omit = omit,
        currency_id: str | Omit = omit,
        custom_contact_fields: Iterable[vendor_update_params.CustomContactField] | Omit = omit,
        default_expense_account_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_compounding_tax: bool | Omit = omit,
        is_eligible_for1099: bool | Omit = omit,
        is_sales_tax_agency: bool | Omit = omit,
        is_tracking_purchase_tax: bool | Omit = omit,
        is_tracking_sales_tax: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name: str | Omit = omit,
        name_on_check: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        purchase_tax_account_id: str | Omit = omit,
        reporting_period: Literal["monthly", "quarterly"] | Omit = omit,
        sales_tax_account_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | Omit = omit,
        sales_tax_return_id: str | Omit = omit,
        salutation: str | Omit = omit,
        shipping_address: vendor_update_params.ShippingAddress | Omit = omit,
        tax_identification_number: str | Omit = omit,
        tax_registration_number: str | Omit = omit,
        terms_id: str | Omit = omit,
        vendor_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Updates an existing vendor.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor to update.

          revision_number: The current QuickBooks-assigned revision number of the vendor object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The vendor's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this vendor.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The name of a alternate contact person for this vendor.

          alternate_phone: The vendor's alternate telephone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The vendor's billing rate, used to override service item rates in time tracking
              activities.

          cc_email: An email address to carbon copy (CC) on communications with this vendor.

          class_id: The vendor's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this vendor. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this vendor.

          credit_limit: The vendor's credit limit, represented as a decimal string. This is the maximum
              amount of money that can be spent being before billed by this vendor. If `null`,
              there is no credit limit.

          currency_id: The vendor's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this vendor, such as phone numbers or email
              addresses.

          default_expense_account_ids: The expense accounts to prefill when entering bills for this vendor.

          email: The vendor's email address.

          fax: The vendor's fax number.

          first_name: The first name of the contact person for this vendor.

              Maximum length: 25 characters.

          is_active: Indicates whether this vendor is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          is_compounding_tax: Indicates whether tax is charged on top of tax for this vendor, for use in
              Canada or the UK.

          is_eligible_for1099: Indicates whether this vendor is eligible to receive a 1099 form for tax
              reporting purposes. When `true`, then the fields `taxId` and `billingAddress`
              are required.

          is_sales_tax_agency: Indicates whether this vendor is a sales tax agency.

          is_tracking_purchase_tax: Indicates whether tax is tracked on purchases for this vendor, for use in Canada
              or the UK.

          is_tracking_sales_tax: Indicates whether tax is tracked on sales for this vendor, for use in Canada or
              the UK.

          job_title: The job title of the contact person for this vendor.

          last_name: The last name of the contact person for this vendor.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this vendor.

              Maximum length: 5 characters.

          name: The case-insensitive unique name of this vendor, unique across all vendors.

              **NOTE**: Vendors do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 41 characters.

          name_on_check: The vendor's name as it should appear on checks issued to this vendor.

          note: A note or comment about this vendor.

          phone: The vendor's primary telephone number.

          purchase_tax_account_id: The account used for tracking taxes on purchases for this vendor, for use in
              Canada or the UK.

          reporting_period: The vendor's tax reporting period, for use in Canada or the UK.

          sales_tax_account_id: The account used for tracking taxes on sales for this vendor, for use in Canada
              or the UK.

          sales_tax_code_id: The default sales-tax code for transactions with this vendor, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this vendor.

          sales_tax_return_id: The vendor's sales tax return information, used for tracking and reporting sales
              tax liabilities.

          salutation: The formal salutation title that precedes the name of the contact person for
              this vendor, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The vendor's shipping address.

          tax_identification_number: The vendor's tax identification number (e.g., EIN or SSN).

          tax_registration_number: The vendor's tax registration number, for use in Canada or the UK.

          terms_id: The vendor's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_type_id: The vendor's type, used for categorizing vendors into meaningful segments, such
              as industry or region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/vendors/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "billing_rate_id": billing_rate_id,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "default_expense_account_ids": default_expense_account_ids,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_compounding_tax": is_compounding_tax,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tracking_purchase_tax": is_tracking_purchase_tax,
                    "is_tracking_sales_tax": is_tracking_sales_tax,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "name_on_check": name_on_check,
                    "note": note,
                    "phone": phone,
                    "purchase_tax_account_id": purchase_tax_account_id,
                    "reporting_period": reporting_period,
                    "sales_tax_account_id": sales_tax_account_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_identification_number": tax_identification_number,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_update_params.VendorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        total_balance: str | Omit = omit,
        total_balance_greater_than: str | Omit = omit,
        total_balance_greater_than_or_equal_to: str | Omit = omit,
        total_balance_less_than: str | Omit = omit,
        total_balance_less_than_or_equal_to: str | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Vendor]:
        """Returns a list of vendors.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for vendors of these classes. A class is a way end-users can categorize
              vendors in QuickBooks.

          currency_ids: Filter for vendors in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific vendors by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for vendors whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for vendors whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for vendors whose `name` is alphabetically greater than or equal to this
              value.

          names: Filter for specific vendors by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a vendor.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for vendors whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for vendors whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for vendors that are active, inactive, or both.

          total_balance: Filter for vendors whose `totalBalance` equals this amount, represented as a
              decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than: Filter for vendors whose `totalBalance` is greater than this amount, represented
              as a decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than_or_equal_to: Filter for vendors whose `totalBalance` is greater than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          total_balance_less_than: Filter for vendors whose `totalBalance` is less than this amount, represented as
              a decimal string. You can only use one total-balance filter at a time.

          total_balance_less_than_or_equal_to: Filter for vendors whose `totalBalance` is less than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          updated_after: Filter for vendors updated on or after this date/time. Accepts the following ISO
              8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for vendors updated on or before this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/vendors",
            page=SyncCursorPage[Vendor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_greater_than": total_balance_greater_than,
                        "total_balance_greater_than_or_equal_to": total_balance_greater_than_or_equal_to,
                        "total_balance_less_than": total_balance_less_than,
                        "total_balance_less_than_or_equal_to": total_balance_less_than_or_equal_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    vendor_list_params.VendorListParams,
                ),
            ),
            model=Vendor,
        )


class AsyncVendorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVendorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVendorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncVendorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_contacts: Iterable[vendor_create_params.AdditionalContact] | Omit = omit,
        additional_notes: Iterable[vendor_create_params.AdditionalNote] | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_address: vendor_create_params.BillingAddress | Omit = omit,
        billing_rate_id: str | Omit = omit,
        cc_email: str | Omit = omit,
        class_id: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        credit_limit: str | Omit = omit,
        currency_id: str | Omit = omit,
        custom_contact_fields: Iterable[vendor_create_params.CustomContactField] | Omit = omit,
        default_expense_account_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_compounding_tax: bool | Omit = omit,
        is_eligible_for1099: bool | Omit = omit,
        is_sales_tax_agency: bool | Omit = omit,
        is_tracking_purchase_tax: bool | Omit = omit,
        is_tracking_sales_tax: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name_on_check: str | Omit = omit,
        note: str | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, date] | Omit = omit,
        phone: str | Omit = omit,
        purchase_tax_account_id: str | Omit = omit,
        reporting_period: Literal["monthly", "quarterly"] | Omit = omit,
        sales_tax_account_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | Omit = omit,
        sales_tax_return_id: str | Omit = omit,
        salutation: str | Omit = omit,
        shipping_address: vendor_create_params.ShippingAddress | Omit = omit,
        tax_identification_number: str | Omit = omit,
        tax_registration_number: str | Omit = omit,
        terms_id: str | Omit = omit,
        vendor_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Creates a new vendor.

        Args:
          name: The case-insensitive unique name of this vendor, unique across all vendors.

              **NOTE**: Vendors do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 41 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The vendor's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this vendor.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The name of a alternate contact person for this vendor.

          alternate_phone: The vendor's alternate telephone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The vendor's billing rate, used to override service item rates in time tracking
              activities.

          cc_email: An email address to carbon copy (CC) on communications with this vendor.

          class_id: The vendor's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this vendor. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this vendor.

          credit_limit: The vendor's credit limit, represented as a decimal string. This is the maximum
              amount of money that can be spent being before billed by this vendor. If `null`,
              there is no credit limit.

          currency_id: The vendor's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this vendor, such as phone numbers or email
              addresses.

          default_expense_account_ids: The expense accounts to prefill when entering bills for this vendor.

          email: The vendor's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The vendor's fax number.

          first_name: The first name of the contact person for this vendor.

              Maximum length: 25 characters.

          is_active: Indicates whether this vendor is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          is_compounding_tax: Indicates whether tax is charged on top of tax for this vendor, for use in
              Canada or the UK.

          is_eligible_for1099: Indicates whether this vendor is eligible to receive a 1099 form for tax
              reporting purposes. When `true`, then the fields `taxId` and `billingAddress`
              are required.

          is_sales_tax_agency: Indicates whether this vendor is a sales tax agency.

          is_tracking_purchase_tax: Indicates whether tax is tracked on purchases for this vendor, for use in Canada
              or the UK.

          is_tracking_sales_tax: Indicates whether tax is tracked on sales for this vendor, for use in Canada or
              the UK.

          job_title: The job title of the contact person for this vendor.

          last_name: The last name of the contact person for this vendor.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this vendor.

              Maximum length: 5 characters.

          name_on_check: The vendor's name as it should appear on checks issued to this vendor.

          note: A note or comment about this vendor.

          opening_balance: The opening balance of this vendor's account, indicating the amount owed to this
              vendor, represented as a decimal string.

          opening_balance_date: The date of the opening balance of this vendor, in ISO 8601 format (YYYY-MM-DD).

          phone: The vendor's primary telephone number.

          purchase_tax_account_id: The account used for tracking taxes on purchases for this vendor, for use in
              Canada or the UK.

          reporting_period: The vendor's tax reporting period, for use in Canada or the UK.

          sales_tax_account_id: The account used for tracking taxes on sales for this vendor, for use in Canada
              or the UK.

          sales_tax_code_id: The default sales-tax code for transactions with this vendor, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this vendor.

          sales_tax_return_id: The vendor's sales tax return information, used for tracking and reporting sales
              tax liabilities.

          salutation: The formal salutation title that precedes the name of the contact person for
              this vendor, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The vendor's shipping address.

          tax_identification_number: The vendor's tax identification number (e.g., EIN or SSN).

          tax_registration_number: The vendor's tax registration number, for use in Canada or the UK.

          terms_id: The vendor's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_type_id: The vendor's type, used for categorizing vendors into meaningful segments, such
              as industry or region.

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
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "default_expense_account_ids": default_expense_account_ids,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_compounding_tax": is_compounding_tax,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tracking_purchase_tax": is_tracking_purchase_tax,
                    "is_tracking_sales_tax": is_tracking_sales_tax,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name_on_check": name_on_check,
                    "note": note,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "phone": phone,
                    "purchase_tax_account_id": purchase_tax_account_id,
                    "reporting_period": reporting_period,
                    "sales_tax_account_id": sales_tax_account_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_identification_number": tax_identification_number,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_create_params.VendorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    async def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Retrieves a vendor by ID.

        **IMPORTANT:** If you need to fetch multiple specific vendors by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/vendors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_contacts: Iterable[vendor_update_params.AdditionalContact] | Omit = omit,
        additional_notes: Iterable[vendor_update_params.AdditionalNote] | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_address: vendor_update_params.BillingAddress | Omit = omit,
        billing_rate_id: str | Omit = omit,
        cc_email: str | Omit = omit,
        class_id: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        credit_limit: str | Omit = omit,
        currency_id: str | Omit = omit,
        custom_contact_fields: Iterable[vendor_update_params.CustomContactField] | Omit = omit,
        default_expense_account_ids: SequenceNotStr[str] | Omit = omit,
        email: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_compounding_tax: bool | Omit = omit,
        is_eligible_for1099: bool | Omit = omit,
        is_sales_tax_agency: bool | Omit = omit,
        is_tracking_purchase_tax: bool | Omit = omit,
        is_tracking_sales_tax: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name: str | Omit = omit,
        name_on_check: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        purchase_tax_account_id: str | Omit = omit,
        reporting_period: Literal["monthly", "quarterly"] | Omit = omit,
        sales_tax_account_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | Omit = omit,
        sales_tax_return_id: str | Omit = omit,
        salutation: str | Omit = omit,
        shipping_address: vendor_update_params.ShippingAddress | Omit = omit,
        tax_identification_number: str | Omit = omit,
        tax_registration_number: str | Omit = omit,
        terms_id: str | Omit = omit,
        vendor_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Vendor:
        """
        Updates an existing vendor.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor to update.

          revision_number: The current QuickBooks-assigned revision number of the vendor object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The vendor's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this vendor.

          additional_notes: Additional notes about this vendor.

          alternate_contact: The name of a alternate contact person for this vendor.

          alternate_phone: The vendor's alternate telephone number.

          billing_address: The vendor's billing address.

          billing_rate_id: The vendor's billing rate, used to override service item rates in time tracking
              activities.

          cc_email: An email address to carbon copy (CC) on communications with this vendor.

          class_id: The vendor's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this vendor. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this vendor.

          credit_limit: The vendor's credit limit, represented as a decimal string. This is the maximum
              amount of money that can be spent being before billed by this vendor. If `null`,
              there is no credit limit.

          currency_id: The vendor's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this vendor, such as phone numbers or email
              addresses.

          default_expense_account_ids: The expense accounts to prefill when entering bills for this vendor.

          email: The vendor's email address.

          fax: The vendor's fax number.

          first_name: The first name of the contact person for this vendor.

              Maximum length: 25 characters.

          is_active: Indicates whether this vendor is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          is_compounding_tax: Indicates whether tax is charged on top of tax for this vendor, for use in
              Canada or the UK.

          is_eligible_for1099: Indicates whether this vendor is eligible to receive a 1099 form for tax
              reporting purposes. When `true`, then the fields `taxId` and `billingAddress`
              are required.

          is_sales_tax_agency: Indicates whether this vendor is a sales tax agency.

          is_tracking_purchase_tax: Indicates whether tax is tracked on purchases for this vendor, for use in Canada
              or the UK.

          is_tracking_sales_tax: Indicates whether tax is tracked on sales for this vendor, for use in Canada or
              the UK.

          job_title: The job title of the contact person for this vendor.

          last_name: The last name of the contact person for this vendor.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this vendor.

              Maximum length: 5 characters.

          name: The case-insensitive unique name of this vendor, unique across all vendors.

              **NOTE**: Vendors do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 41 characters.

          name_on_check: The vendor's name as it should appear on checks issued to this vendor.

          note: A note or comment about this vendor.

          phone: The vendor's primary telephone number.

          purchase_tax_account_id: The account used for tracking taxes on purchases for this vendor, for use in
              Canada or the UK.

          reporting_period: The vendor's tax reporting period, for use in Canada or the UK.

          sales_tax_account_id: The account used for tracking taxes on sales for this vendor, for use in Canada
              or the UK.

          sales_tax_code_id: The default sales-tax code for transactions with this vendor, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this vendor.

          sales_tax_return_id: The vendor's sales tax return information, used for tracking and reporting sales
              tax liabilities.

          salutation: The formal salutation title that precedes the name of the contact person for
              this vendor, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The vendor's shipping address.

          tax_identification_number: The vendor's tax identification number (e.g., EIN or SSN).

          tax_registration_number: The vendor's tax registration number, for use in Canada or the UK.

          terms_id: The vendor's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_type_id: The vendor's type, used for categorizing vendors into meaningful segments, such
              as industry or region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/vendors/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "billing_rate_id": billing_rate_id,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "default_expense_account_ids": default_expense_account_ids,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_compounding_tax": is_compounding_tax,
                    "is_eligible_for1099": is_eligible_for1099,
                    "is_sales_tax_agency": is_sales_tax_agency,
                    "is_tracking_purchase_tax": is_tracking_purchase_tax,
                    "is_tracking_sales_tax": is_tracking_sales_tax,
                    "job_title": job_title,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "name_on_check": name_on_check,
                    "note": note,
                    "phone": phone,
                    "purchase_tax_account_id": purchase_tax_account_id,
                    "reporting_period": reporting_period,
                    "sales_tax_account_id": sales_tax_account_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_return_id": sales_tax_return_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_identification_number": tax_identification_number,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                    "vendor_type_id": vendor_type_id,
                },
                vendor_update_params.VendorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Vendor,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        total_balance: str | Omit = omit,
        total_balance_greater_than: str | Omit = omit,
        total_balance_greater_than_or_equal_to: str | Omit = omit,
        total_balance_less_than: str | Omit = omit,
        total_balance_less_than_or_equal_to: str | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Vendor, AsyncCursorPage[Vendor]]:
        """Returns a list of vendors.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for vendors of these classes. A class is a way end-users can categorize
              vendors in QuickBooks.

          currency_ids: Filter for vendors in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific vendors by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for vendors whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for vendors whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for vendors whose `name` is alphabetically greater than or equal to this
              value.

          names: Filter for specific vendors by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a vendor.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for vendors whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for vendors whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for vendors that are active, inactive, or both.

          total_balance: Filter for vendors whose `totalBalance` equals this amount, represented as a
              decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than: Filter for vendors whose `totalBalance` is greater than this amount, represented
              as a decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than_or_equal_to: Filter for vendors whose `totalBalance` is greater than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          total_balance_less_than: Filter for vendors whose `totalBalance` is less than this amount, represented as
              a decimal string. You can only use one total-balance filter at a time.

          total_balance_less_than_or_equal_to: Filter for vendors whose `totalBalance` is less than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          updated_after: Filter for vendors updated on or after this date/time. Accepts the following ISO
              8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for vendors updated on or before this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/vendors",
            page=AsyncCursorPage[Vendor],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_greater_than": total_balance_greater_than,
                        "total_balance_greater_than_or_equal_to": total_balance_greater_than_or_equal_to,
                        "total_balance_less_than": total_balance_less_than,
                        "total_balance_less_than_or_equal_to": total_balance_less_than_or_equal_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    vendor_list_params.VendorListParams,
                ),
            ),
            model=Vendor,
        )


class VendorsResourceWithRawResponse:
    def __init__(self, vendors: VendorsResource) -> None:
        self._vendors = vendors

        self.create = to_raw_response_wrapper(
            vendors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vendors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vendors.update,
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
        self.retrieve = async_to_raw_response_wrapper(
            vendors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vendors.update,
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
        self.retrieve = to_streamed_response_wrapper(
            vendors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vendors.update,
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
        self.retrieve = async_to_streamed_response_wrapper(
            vendors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vendors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vendors.list,
        )
