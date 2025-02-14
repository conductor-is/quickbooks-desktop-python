# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
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
from ...types.qbd import customer_list_params, customer_create_params, customer_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.customer import Customer

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[customer_create_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        alternate_shipping_addresses: Iterable[customer_create_params.AlternateShippingAddress] | NotGiven = NOT_GIVEN,
        billing_address: customer_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc_email: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_create_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_projected_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_status: Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]
        | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["email", "mail", "none"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Creates a new customer.

        Args:
          name: The case-insensitive name of this customer. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two customers could both have the `name` "Website Redesign
              Project", but they could have unique `fullName` values, such as "ABC
              Corporation:Website Redesign Project" and "Baker:Website Redesign Project".

              Maximum length: 41 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this customer.

          additional_notes: Additional notes about this customer.

          alternate_contact: The name of a alternate contact person for this customer.

          alternate_phone: The customer's alternate telephone number.

          alternate_shipping_addresses: A list of additional shipping addresses for this customer. Useful when the
              customer has multiple shipping locations.

          billing_address: The customer's billing address.

          cc_email: An email address to carbon copy (CC) on communications with this customer.

          class_id: The customer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this customer. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this customer.

          credit_card: The customer's credit card information, including card type, number, and
              expiration date, used for processing credit card payments.

          credit_limit: The customer's credit limit, represented as a decimal string. This is the
              maximum amount of money this customer can spend before being billed. If `null`,
              there is no credit limit.

          currency_id: The customer's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this customer, such as phone numbers or
              email addresses.

          customer_type_id: The customer's type, used for categorizing customers into meaningful segments,
              such as industry or region.

          email: The customer's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The customer's fax number.

          first_name: The first name of the contact person for this customer.

              Maximum length: 25 characters.

          is_active: Indicates whether this customer is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_description: A brief description of this customer's job, if this object is a job (i.e.,
              sub-customer).

          job_end_date: The actual completion date of this customer's job, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_projected_end_date: The projected completion date for this customer's job, if applicable, in ISO
              8601 format (YYYY-MM-DD).

          job_start_date: The date when work on this customer's job began, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_status: The status of this customer's job, if this object is a job (i.e., sub-customer).

          job_title: The job title of the contact person for this customer.

          job_type_id: The type or category of this customer's job, if this object is a job (i.e.,
              sub-customer). Useful for classifying into meaningful segments (e.g., repair,
              installation, consulting).

          last_name: The last name of the contact person for this customer.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this customer.

              Maximum length: 5 characters.

          note: A note or comment about this customer.

          opening_balance: The opening balance of this customer's account, indicating the amount owed by
              this customer, represented as a decimal string.

          opening_balance_date: The date of the opening balance of this customer, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent customer one level above this one in the hierarchy. For example, if
              this customer has a `fullName` of "ABC Corporation:Website Redesign Project",
              its parent has a `fullName` of "ABC Corporation". If this customer is at the top
              level, this field will be `null`.

          phone: The customer's primary telephone number.

          preferred_delivery_method: The preferred method for delivering invoices and other documents to this
              customer.

          preferred_payment_method_id: The customer's preferred payment method (e.g., cash, check, credit card).

          price_level_id: The customer's custom price level that QuickBooks automatically applies to
              calculate item rates in new transactions (e.g., invoices, sales receipts, sales
              orders, and credit memos) for this customer. While applied automatically, this
              can be overridden when creating individual transactions. Note that transactions
              will not show the price level itself, only the final `rate` calculated from it.

          resale_number: The customer's resale number, used if the customer is purchasing items for
              resale. This number does not affect sales tax calculations or reports in
              QuickBooks.

          sales_representative_id: The customer's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The default sales-tax code for transactions with this customer, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this customer.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this customer's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          salutation: The formal salutation title that precedes the name of the contact person for
              this customer, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The customer's shipping address.

          tax_registration_number: The customer's tax registration number, for use in Canada or the UK.

          terms_id: The customer's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/customers",
            body=maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "alternate_shipping_addresses": alternate_shipping_addresses,
                    "billing_address": billing_address,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_item_id": sales_tax_item_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Retrieves a customer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_update_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[customer_update_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        alternate_shipping_addresses: Iterable[customer_update_params.AlternateShippingAddress] | NotGiven = NOT_GIVEN,
        billing_address: customer_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc_email: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_update_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_update_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_projected_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_status: Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]
        | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["email", "mail", "none"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Updates an existing customer.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to update.

          revision_number: The current QuickBooks-assigned revision number of the customer object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this customer.

          additional_notes: Additional notes about this customer.

          alternate_contact: The name of a alternate contact person for this customer.

          alternate_phone: The customer's alternate telephone number.

          alternate_shipping_addresses: A list of additional shipping addresses for this customer. Useful when the
              customer has multiple shipping locations.

          billing_address: The customer's billing address.

          cc_email: An email address to carbon copy (CC) on communications with this customer.

          class_id: The customer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this customer. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this customer.

          credit_card: The customer's credit card information, including card type, number, and
              expiration date, used for processing credit card payments.

          credit_limit: The customer's credit limit, represented as a decimal string. This is the
              maximum amount of money this customer can spend before being billed. If `null`,
              there is no credit limit.

          currency_id: The customer's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this customer, such as phone numbers or
              email addresses.

          customer_type_id: The customer's type, used for categorizing customers into meaningful segments,
              such as industry or region.

          email: The customer's email address.

          fax: The customer's fax number.

          first_name: The first name of the contact person for this customer.

              Maximum length: 25 characters.

          is_active: Indicates whether this customer is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_description: A brief description of this customer's job, if this object is a job (i.e.,
              sub-customer).

          job_end_date: The actual completion date of this customer's job, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_projected_end_date: The projected completion date for this customer's job, if applicable, in ISO
              8601 format (YYYY-MM-DD).

          job_start_date: The date when work on this customer's job began, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_status: The status of this customer's job, if this object is a job (i.e., sub-customer).

          job_title: The job title of the contact person for this customer.

          job_type_id: The type or category of this customer's job, if this object is a job (i.e.,
              sub-customer). Useful for classifying into meaningful segments (e.g., repair,
              installation, consulting).

          last_name: The last name of the contact person for this customer.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this customer.

              Maximum length: 5 characters.

          name: The case-insensitive name of this customer. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two customers could both have the `name` "Website Redesign
              Project", but they could have unique `fullName` values, such as "ABC
              Corporation:Website Redesign Project" and "Baker:Website Redesign Project".

              Maximum length: 41 characters.

          note: A note or comment about this customer.

          parent_id: The parent customer one level above this one in the hierarchy. For example, if
              this customer has a `fullName` of "ABC Corporation:Website Redesign Project",
              its parent has a `fullName` of "ABC Corporation". If this customer is at the top
              level, this field will be `null`.

          phone: The customer's primary telephone number.

          preferred_delivery_method: The preferred method for delivering invoices and other documents to this
              customer.

          preferred_payment_method_id: The customer's preferred payment method (e.g., cash, check, credit card).

          price_level_id: The customer's custom price level that QuickBooks automatically applies to
              calculate item rates in new transactions (e.g., invoices, sales receipts, sales
              orders, and credit memos) for this customer. While applied automatically, this
              can be overridden when creating individual transactions. Note that transactions
              will not show the price level itself, only the final `rate` calculated from it.

          resale_number: The customer's resale number, used if the customer is purchasing items for
              resale. This number does not affect sales tax calculations or reports in
              QuickBooks.

          sales_representative_id: The customer's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The default sales-tax code for transactions with this customer, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this customer.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this customer's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          salutation: The formal salutation title that precedes the name of the contact person for
              this customer, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The customer's shipping address.

          tax_registration_number: The customer's tax registration number, for use in Canada or the UK.

          terms_id: The customer's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/customers/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "alternate_shipping_addresses": alternate_shipping_addresses,
                    "billing_address": billing_address,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "note": note,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_item_id": sales_tax_item_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_greater_than: str | NotGiven = NOT_GIVEN,
        total_balance_greater_than_or_equal_to: str | NotGiven = NOT_GIVEN,
        total_balance_less_than: str | NotGiven = NOT_GIVEN,
        total_balance_less_than_or_equal_to: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Customer]:
        """Returns a list of customers.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for customers of these classes. A class is a way end-users can categorize
              customers in QuickBooks.

          currency_ids: Filter for customers in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific customers by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a customer, formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if a customer is under "ABC Corporation" and has the `name` "Website
              Redesign Project", its `fullName` would be "ABC Corporation:Website Redesign
              Project".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific customers by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for customers whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for customers whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for customers whose `name` is alphabetically greater than or equal to
              this value.

          name_starts_with: Filter for customers whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for customers whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for customers that are active, inactive, or both.

          total_balance: Filter for customers whose `totalBalance` equals this amount, represented as a
              decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than: Filter for customers whose `totalBalance` is greater than this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          total_balance_greater_than_or_equal_to: Filter for customers whose `totalBalance` is greater than or equal to this
              amount, represented as a decimal string. You can only use one total-balance
              filter at a time.

          total_balance_less_than: Filter for customers whose `totalBalance` is less than this amount, represented
              as a decimal string. You can only use one total-balance filter at a time.

          total_balance_less_than_or_equal_to: Filter for customers whose `totalBalance` is less than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          updated_after: Filter for customers updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for customers updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/customers",
            page=SyncCursorPage[Customer],
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
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
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
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[customer_create_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        alternate_shipping_addresses: Iterable[customer_create_params.AlternateShippingAddress] | NotGiven = NOT_GIVEN,
        billing_address: customer_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc_email: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_create_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_projected_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_status: Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]
        | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["email", "mail", "none"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Creates a new customer.

        Args:
          name: The case-insensitive name of this customer. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two customers could both have the `name` "Website Redesign
              Project", but they could have unique `fullName` values, such as "ABC
              Corporation:Website Redesign Project" and "Baker:Website Redesign Project".

              Maximum length: 41 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this customer.

          additional_notes: Additional notes about this customer.

          alternate_contact: The name of a alternate contact person for this customer.

          alternate_phone: The customer's alternate telephone number.

          alternate_shipping_addresses: A list of additional shipping addresses for this customer. Useful when the
              customer has multiple shipping locations.

          billing_address: The customer's billing address.

          cc_email: An email address to carbon copy (CC) on communications with this customer.

          class_id: The customer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this customer. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this customer.

          credit_card: The customer's credit card information, including card type, number, and
              expiration date, used for processing credit card payments.

          credit_limit: The customer's credit limit, represented as a decimal string. This is the
              maximum amount of money this customer can spend before being billed. If `null`,
              there is no credit limit.

          currency_id: The customer's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this customer, such as phone numbers or
              email addresses.

          customer_type_id: The customer's type, used for categorizing customers into meaningful segments,
              such as industry or region.

          email: The customer's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The customer's fax number.

          first_name: The first name of the contact person for this customer.

              Maximum length: 25 characters.

          is_active: Indicates whether this customer is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_description: A brief description of this customer's job, if this object is a job (i.e.,
              sub-customer).

          job_end_date: The actual completion date of this customer's job, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_projected_end_date: The projected completion date for this customer's job, if applicable, in ISO
              8601 format (YYYY-MM-DD).

          job_start_date: The date when work on this customer's job began, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_status: The status of this customer's job, if this object is a job (i.e., sub-customer).

          job_title: The job title of the contact person for this customer.

          job_type_id: The type or category of this customer's job, if this object is a job (i.e.,
              sub-customer). Useful for classifying into meaningful segments (e.g., repair,
              installation, consulting).

          last_name: The last name of the contact person for this customer.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this customer.

              Maximum length: 5 characters.

          note: A note or comment about this customer.

          opening_balance: The opening balance of this customer's account, indicating the amount owed by
              this customer, represented as a decimal string.

          opening_balance_date: The date of the opening balance of this customer, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent customer one level above this one in the hierarchy. For example, if
              this customer has a `fullName` of "ABC Corporation:Website Redesign Project",
              its parent has a `fullName` of "ABC Corporation". If this customer is at the top
              level, this field will be `null`.

          phone: The customer's primary telephone number.

          preferred_delivery_method: The preferred method for delivering invoices and other documents to this
              customer.

          preferred_payment_method_id: The customer's preferred payment method (e.g., cash, check, credit card).

          price_level_id: The customer's custom price level that QuickBooks automatically applies to
              calculate item rates in new transactions (e.g., invoices, sales receipts, sales
              orders, and credit memos) for this customer. While applied automatically, this
              can be overridden when creating individual transactions. Note that transactions
              will not show the price level itself, only the final `rate` calculated from it.

          resale_number: The customer's resale number, used if the customer is purchasing items for
              resale. This number does not affect sales tax calculations or reports in
              QuickBooks.

          sales_representative_id: The customer's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The default sales-tax code for transactions with this customer, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this customer.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this customer's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          salutation: The formal salutation title that precedes the name of the contact person for
              this customer, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The customer's shipping address.

          tax_registration_number: The customer's tax registration number, for use in Canada or the UK.

          terms_id: The customer's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/customers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "alternate_shipping_addresses": alternate_shipping_addresses,
                    "billing_address": billing_address,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_item_id": sales_tax_item_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Retrieves a customer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_update_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[customer_update_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        alternate_shipping_addresses: Iterable[customer_update_params.AlternateShippingAddress] | NotGiven = NOT_GIVEN,
        billing_address: customer_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc_email: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_update_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_update_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_projected_end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        job_status: Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]
        | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["email", "mail", "none"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["australia", "canada", "uk", "us"] | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        Updates an existing customer.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to update.

          revision_number: The current QuickBooks-assigned revision number of the customer object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_contacts: Additional alternate contacts for this customer.

          additional_notes: Additional notes about this customer.

          alternate_contact: The name of a alternate contact person for this customer.

          alternate_phone: The customer's alternate telephone number.

          alternate_shipping_addresses: A list of additional shipping addresses for this customer. Useful when the
              customer has multiple shipping locations.

          billing_address: The customer's billing address.

          cc_email: An email address to carbon copy (CC) on communications with this customer.

          class_id: The customer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          company_name: The name of the company associated with this customer. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this customer.

          credit_card: The customer's credit card information, including card type, number, and
              expiration date, used for processing credit card payments.

          credit_limit: The customer's credit limit, represented as a decimal string. This is the
              maximum amount of money this customer can spend before being billed. If `null`,
              there is no credit limit.

          currency_id: The customer's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          custom_contact_fields: Additional custom contact fields for this customer, such as phone numbers or
              email addresses.

          customer_type_id: The customer's type, used for categorizing customers into meaningful segments,
              such as industry or region.

          email: The customer's email address.

          fax: The customer's fax number.

          first_name: The first name of the contact person for this customer.

              Maximum length: 25 characters.

          is_active: Indicates whether this customer is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_description: A brief description of this customer's job, if this object is a job (i.e.,
              sub-customer).

          job_end_date: The actual completion date of this customer's job, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_projected_end_date: The projected completion date for this customer's job, if applicable, in ISO
              8601 format (YYYY-MM-DD).

          job_start_date: The date when work on this customer's job began, if applicable, in ISO 8601
              format (YYYY-MM-DD).

          job_status: The status of this customer's job, if this object is a job (i.e., sub-customer).

          job_title: The job title of the contact person for this customer.

          job_type_id: The type or category of this customer's job, if this object is a job (i.e.,
              sub-customer). Useful for classifying into meaningful segments (e.g., repair,
              installation, consulting).

          last_name: The last name of the contact person for this customer.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this customer.

              Maximum length: 5 characters.

          name: The case-insensitive name of this customer. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two customers could both have the `name` "Website Redesign
              Project", but they could have unique `fullName` values, such as "ABC
              Corporation:Website Redesign Project" and "Baker:Website Redesign Project".

              Maximum length: 41 characters.

          note: A note or comment about this customer.

          parent_id: The parent customer one level above this one in the hierarchy. For example, if
              this customer has a `fullName` of "ABC Corporation:Website Redesign Project",
              its parent has a `fullName` of "ABC Corporation". If this customer is at the top
              level, this field will be `null`.

          phone: The customer's primary telephone number.

          preferred_delivery_method: The preferred method for delivering invoices and other documents to this
              customer.

          preferred_payment_method_id: The customer's preferred payment method (e.g., cash, check, credit card).

          price_level_id: The customer's custom price level that QuickBooks automatically applies to
              calculate item rates in new transactions (e.g., invoices, sales receipts, sales
              orders, and credit memos) for this customer. While applied automatically, this
              can be overridden when creating individual transactions. Note that transactions
              will not show the price level itself, only the final `rate` calculated from it.

          resale_number: The customer's resale number, used if the customer is purchasing items for
              resale. This number does not affect sales tax calculations or reports in
              QuickBooks.

          sales_representative_id: The customer's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The default sales-tax code for transactions with this customer, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_country: The country for which sales tax is collected for this customer.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this customer's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          salutation: The formal salutation title that precedes the name of the contact person for
              this customer, such as "Mr.", "Ms.", or "Dr.".

          shipping_address: The customer's shipping address.

          tax_registration_number: The customer's tax registration number, for use in Canada or the UK.

          terms_id: The customer's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/customers/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "alternate_shipping_addresses": alternate_shipping_addresses,
                    "billing_address": billing_address,
                    "cc_email": cc_email,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "note": note,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "sales_tax_item_id": sales_tax_item_id,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_greater_than: str | NotGiven = NOT_GIVEN,
        total_balance_greater_than_or_equal_to: str | NotGiven = NOT_GIVEN,
        total_balance_less_than: str | NotGiven = NOT_GIVEN,
        total_balance_less_than_or_equal_to: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Customer, AsyncCursorPage[Customer]]:
        """Returns a list of customers.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for customers of these classes. A class is a way end-users can categorize
              customers in QuickBooks.

          currency_ids: Filter for customers in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific customers by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a customer, formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if a customer is under "ABC Corporation" and has the `name` "Website
              Redesign Project", its `fullName` would be "ABC Corporation:Website Redesign
              Project".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific customers by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for customers whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for customers whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for customers whose `name` is alphabetically greater than or equal to
              this value.

          name_starts_with: Filter for customers whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for customers whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for customers that are active, inactive, or both.

          total_balance: Filter for customers whose `totalBalance` equals this amount, represented as a
              decimal string. You can only use one total-balance filter at a time.

          total_balance_greater_than: Filter for customers whose `totalBalance` is greater than this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          total_balance_greater_than_or_equal_to: Filter for customers whose `totalBalance` is greater than or equal to this
              amount, represented as a decimal string. You can only use one total-balance
              filter at a time.

          total_balance_less_than: Filter for customers whose `totalBalance` is less than this amount, represented
              as a decimal string. You can only use one total-balance filter at a time.

          total_balance_less_than_or_equal_to: Filter for customers whose `totalBalance` is less than or equal to this amount,
              represented as a decimal string. You can only use one total-balance filter at a
              time.

          updated_after: Filter for customers updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for customers updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/customers",
            page=AsyncCursorPage[Customer],
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
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
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
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
