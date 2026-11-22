# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import (
    custom_field_definition_list_params,
    custom_field_definition_create_params,
    custom_field_definition_delete_params,
    custom_field_definition_update_params,
)
from ..._base_client import make_request_options
from ...types.qbd.custom_field_definition import CustomFieldDefinition
from ...types.qbd.custom_field_definition_list_response import CustomFieldDefinitionListResponse
from ...types.qbd.custom_field_definition_delete_response import CustomFieldDefinitionDeleteResponse

__all__ = ["CustomFieldDefinitionsResource", "AsyncCustomFieldDefinitionsResource"]


class CustomFieldDefinitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomFieldDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return CustomFieldDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return CustomFieldDefinitionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ],
        conductor_end_user_id: str,
        owner_id: str | Omit = omit,
        type: Literal[
            "amount_type",
            "date_time_type",
            "integer_type",
            "percent_type",
            "price_type",
            "quantity_type",
            "string_1024_type",
            "string_255_type",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinition:
        """Creates a custom field and assigns it to the types of records you list.

        To give
        it a value on a record, use the set-custom-fields endpoint of that record's
        type.

        Args:
          name: The name of the custom field, unique among the custom fields of its owner. For a
              public custom field, this is the label QuickBooks shows.

          object_types: The types of records the custom field applies to. A public custom field takes
              either `"item"` or any of `"customer"`, `"vendor"`, and `"employee"`, and
              QuickBooks adds transaction types itself, which the returned definition's
              `objectTypes` lists: a customer, vendor, or employee custom field applies to
              those transactions themselves, and an item custom field to their lines. A
              private custom field takes any of these types.

          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          type: The data type of the custom field's values. Defaults to `"string_255_type"`, the
              only type QuickBooks accepts for a public custom field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/custom-field-definitions",
            body=maybe_transform(
                {
                    "name": name,
                    "object_types": object_types,
                    "owner_id": owner_id,
                    "type": type,
                },
                custom_field_definition_create_params.CustomFieldDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldDefinition,
        )

    def update(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        add_object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        remove_object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinition:
        """Renames a custom field or changes the types of records it applies to.

        The `id`
        in the path is the custom field's current name.

        Args:
          id: The `id` of the custom field definition, which is its name. QuickBooks matches
              the name without regard to letter case.

          conductor_end_user_id: The ID of the End-User to receive this request.

          add_object_types: The types of records to also apply the custom field to. A public custom field
              takes only `"customer"`, `"vendor"`, `"employee"`, or `"item"`, and QuickBooks
              adds the matching transaction types itself.

          name: The new name of the custom field. Its values stay with it, and the definition's
              `id` becomes the new name.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          remove_object_types: The types of records to stop applying the custom field to. A public custom field
              takes only `"customer"`, `"vendor"`, `"employee"`, or `"item"`, and QuickBooks
              removes the matching transaction types itself.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            path_template("/quickbooks-desktop/custom-field-definitions/{id}", id=id),
            body=maybe_transform(
                {
                    "add_object_types": add_object_types,
                    "name": name,
                    "owner_id": owner_id,
                    "remove_object_types": remove_object_types,
                },
                custom_field_definition_update_params.CustomFieldDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldDefinition,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        owner_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinitionListResponse:
        """
        Returns the company file's custom field definitions: each custom field's name,
        the type of its values, and the types of records it applies to. A record's
        `customFields` include only the custom fields that have a value on that record,
        so use this list to find every custom field you can set.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_ids: The owners whose custom field definitions to return. Defaults to `["0"]`, the
              owner of public custom fields, which QuickBooks users define and see. To get an
              application's private custom fields, add its owner ID, a GUID in braces. Only
              the owners you list are returned, so keep `"0"` in the list to also get the
              public ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/custom-field-definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"owner_ids": owner_ids}, custom_field_definition_list_params.CustomFieldDefinitionListParams
                ),
            ),
            cast_to=CustomFieldDefinitionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        owner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinitionDeleteResponse:
        """
        Deletes a custom field definition, so QuickBooks stops returning the custom
        field.

        **IMPORTANT**: Deleting a public custom field does not erase its values.
        QuickBooks keeps them on the records, and a public custom field created later
        for the same kind of record (customers, vendors, and employees, or items) can
        show them under its own name. To remove the values for good, clear them with
        each record type's set-custom-fields endpoint before deleting the definition. A
        deleted private custom field's values do not come back under another name, but
        its owner cannot create another custom field with the same name.

        Args:
          id: The `id` of the custom field definition, which is its name. QuickBooks matches
              the name without regard to letter case.

          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._delete(
            path_template("/quickbooks-desktop/custom-field-definitions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"owner_id": owner_id}, custom_field_definition_delete_params.CustomFieldDefinitionDeleteParams
                ),
            ),
            cast_to=CustomFieldDefinitionDeleteResponse,
        )


class AsyncCustomFieldDefinitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomFieldDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncCustomFieldDefinitionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ],
        conductor_end_user_id: str,
        owner_id: str | Omit = omit,
        type: Literal[
            "amount_type",
            "date_time_type",
            "integer_type",
            "percent_type",
            "price_type",
            "quantity_type",
            "string_1024_type",
            "string_255_type",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinition:
        """Creates a custom field and assigns it to the types of records you list.

        To give
        it a value on a record, use the set-custom-fields endpoint of that record's
        type.

        Args:
          name: The name of the custom field, unique among the custom fields of its owner. For a
              public custom field, this is the label QuickBooks shows.

          object_types: The types of records the custom field applies to. A public custom field takes
              either `"item"` or any of `"customer"`, `"vendor"`, and `"employee"`, and
              QuickBooks adds transaction types itself, which the returned definition's
              `objectTypes` lists: a customer, vendor, or employee custom field applies to
              those transactions themselves, and an item custom field to their lines. A
              private custom field takes any of these types.

          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          type: The data type of the custom field's values. Defaults to `"string_255_type"`, the
              only type QuickBooks accepts for a public custom field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/custom-field-definitions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_types": object_types,
                    "owner_id": owner_id,
                    "type": type,
                },
                custom_field_definition_create_params.CustomFieldDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldDefinition,
        )

    async def update(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        add_object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        owner_id: str | Omit = omit,
        remove_object_types: List[
            Literal[
                "account",
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "company",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "customer",
                "deposit",
                "employee",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item",
                "item_receipt",
                "journal_entry",
                "other_name",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "vendor",
                "vendor_credit",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinition:
        """Renames a custom field or changes the types of records it applies to.

        The `id`
        in the path is the custom field's current name.

        Args:
          id: The `id` of the custom field definition, which is its name. QuickBooks matches
              the name without regard to letter case.

          conductor_end_user_id: The ID of the End-User to receive this request.

          add_object_types: The types of records to also apply the custom field to. A public custom field
              takes only `"customer"`, `"vendor"`, `"employee"`, or `"item"`, and QuickBooks
              adds the matching transaction types itself.

          name: The new name of the custom field. Its values stay with it, and the definition's
              `id` becomes the new name.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          remove_object_types: The types of records to stop applying the custom field to. A public custom field
              takes only `"customer"`, `"vendor"`, `"employee"`, or `"item"`, and QuickBooks
              removes the matching transaction types itself.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            path_template("/quickbooks-desktop/custom-field-definitions/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "add_object_types": add_object_types,
                    "name": name,
                    "owner_id": owner_id,
                    "remove_object_types": remove_object_types,
                },
                custom_field_definition_update_params.CustomFieldDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldDefinition,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        owner_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinitionListResponse:
        """
        Returns the company file's custom field definitions: each custom field's name,
        the type of its values, and the types of records it applies to. A record's
        `customFields` include only the custom fields that have a value on that record,
        so use this list to find every custom field you can set.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_ids: The owners whose custom field definitions to return. Defaults to `["0"]`, the
              owner of public custom fields, which QuickBooks users define and see. To get an
              application's private custom fields, add its owner ID, a GUID in braces. Only
              the owners you list are returned, so keep `"0"` in the list to also get the
              public ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/custom-field-definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"owner_ids": owner_ids}, custom_field_definition_list_params.CustomFieldDefinitionListParams
                ),
            ),
            cast_to=CustomFieldDefinitionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        owner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldDefinitionDeleteResponse:
        """
        Deletes a custom field definition, so QuickBooks stops returning the custom
        field.

        **IMPORTANT**: Deleting a public custom field does not erase its values.
        QuickBooks keeps them on the records, and a public custom field created later
        for the same kind of record (customers, vendors, and employees, or items) can
        show them under its own name. To remove the values for good, clear them with
        each record type's set-custom-fields endpoint before deleting the definition. A
        deleted private custom field's values do not come back under another name, but
        its owner cannot create another custom field with the same name.

        Args:
          id: The `id` of the custom field definition, which is its name. QuickBooks matches
              the name without regard to letter case.

          conductor_end_user_id: The ID of the End-User to receive this request.

          owner_id: The owner of the custom field. Defaults to `"0"`, the owner of public custom
              fields, which QuickBooks users define and see. Any other owner is an
              application's GUID in braces, such as
              `"{6B063959-81B0-4622-85D6-F548C8CCB517}"`, whose private custom fields appear
              only in requests that name it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._delete(
            path_template("/quickbooks-desktop/custom-field-definitions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"owner_id": owner_id}, custom_field_definition_delete_params.CustomFieldDefinitionDeleteParams
                ),
            ),
            cast_to=CustomFieldDefinitionDeleteResponse,
        )


class CustomFieldDefinitionsResourceWithRawResponse:
    def __init__(self, custom_field_definitions: CustomFieldDefinitionsResource) -> None:
        self._custom_field_definitions = custom_field_definitions

        self.create = to_raw_response_wrapper(
            custom_field_definitions.create,
        )
        self.update = to_raw_response_wrapper(
            custom_field_definitions.update,
        )
        self.list = to_raw_response_wrapper(
            custom_field_definitions.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_field_definitions.delete,
        )


class AsyncCustomFieldDefinitionsResourceWithRawResponse:
    def __init__(self, custom_field_definitions: AsyncCustomFieldDefinitionsResource) -> None:
        self._custom_field_definitions = custom_field_definitions

        self.create = async_to_raw_response_wrapper(
            custom_field_definitions.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_field_definitions.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_field_definitions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_field_definitions.delete,
        )


class CustomFieldDefinitionsResourceWithStreamingResponse:
    def __init__(self, custom_field_definitions: CustomFieldDefinitionsResource) -> None:
        self._custom_field_definitions = custom_field_definitions

        self.create = to_streamed_response_wrapper(
            custom_field_definitions.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_field_definitions.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_field_definitions.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_field_definitions.delete,
        )


class AsyncCustomFieldDefinitionsResourceWithStreamingResponse:
    def __init__(self, custom_field_definitions: AsyncCustomFieldDefinitionsResource) -> None:
        self._custom_field_definitions = custom_field_definitions

        self.create = async_to_streamed_response_wrapper(
            custom_field_definitions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_field_definitions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_field_definitions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_field_definitions.delete,
        )
