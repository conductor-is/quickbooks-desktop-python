# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.qbd import other_name_list_params, other_name_create_params, other_name_update_params
from ..._base_client import make_request_options
from ...types.qbd.other_name import OtherName
from ...types.qbd.other_name_list_response import OtherNameListResponse

__all__ = ["OtherNamesResource", "AsyncOtherNamesResource"]


class OtherNamesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OtherNamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return OtherNamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OtherNamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return OtherNamesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        address: other_name_create_params.Address | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        salutation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherName:
        """
        Creates a new other-name.

        Args:
          name: The case-insensitive unique name of this other-name, unique across all
              other-names.

              **NOTE**: Other-names do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The other-name's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          address: The other-name's address.

          alternate_contact: The name of a alternate contact person for this other-name.

          alternate_phone: The other-name's alternate telephone number.

          company_name: The name of the company associated with this other-name. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this other-name.

          email: The other-name's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The other-name's fax number.

          first_name: The first name of the contact person for this other-name.

              Maximum length: 25 characters.

          is_active: Indicates whether this other-name is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          last_name: The last name of the contact person for this other-name.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this other-name.

              Maximum length: 5 characters.

          note: A note or comment about this other-name.

          phone: The other-name's primary telephone number.

          salutation: The formal salutation title that precedes the name of the contact person for
              this other-name, such as "Mr.", "Ms.", or "Dr.".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/other-names",
            body=maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "address": address,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "company_name": company_name,
                    "contact": contact,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "phone": phone,
                    "salutation": salutation,
                },
                other_name_create_params.OtherNameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
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
    ) -> OtherName:
        """
        Retrieves an other-name by ID.

        **IMPORTANT:** If you need to fetch multiple specific other-names by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the other-name to retrieve.

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
            f"/quickbooks-desktop/other-names/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        address: other_name_update_params.Address | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        email: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        salutation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherName:
        """
        Updates an existing other-name.

        Args:
          id: The QuickBooks-assigned unique identifier of the other-name to update.

          revision_number: The current QuickBooks-assigned revision number of the other-name object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The other-name's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          address: The other-name's address.

          alternate_contact: The name of a alternate contact person for this other-name.

          alternate_phone: The other-name's alternate telephone number.

          company_name: The name of the company associated with this other-name. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this other-name.

          email: The other-name's email address.

          fax: The other-name's fax number.

          first_name: The first name of the contact person for this other-name.

              Maximum length: 25 characters.

          is_active: Indicates whether this other-name is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          last_name: The last name of the contact person for this other-name.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this other-name.

              Maximum length: 5 characters.

          name: The case-insensitive unique name of this other-name, unique across all
              other-names.

              **NOTE**: Other-names do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          note: A note or comment about this other-name.

          phone: The other-name's primary telephone number.

          salutation: The formal salutation title that precedes the name of the contact person for
              this other-name, such as "Mr.", "Ms.", or "Dr.".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/other-names/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "address": address,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "company_name": company_name,
                    "contact": contact,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "note": note,
                    "phone": phone,
                    "salutation": salutation,
                },
                other_name_update_params.OtherNameUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherNameListResponse:
        """Returns a list of other-names.

        NOTE: QuickBooks Desktop does not support
        pagination for other-names; hence, there is no `cursor` parameter. Users
        typically have few other-names.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific other-names by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              other-names. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all other-names without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because other-names typically have low record counts.

          name_contains: Filter for other-names whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for other-names whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for other-names whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific other-names by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an other-name.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for other-names whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for other-names whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for other-names that are active, inactive, or both.

          updated_after: Filter for other-names updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for other-names updated on or before this date/time. Accepts the
              following ISO 8601 formats:

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
        return self._get(
            "/quickbooks-desktop/other-names",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    other_name_list_params.OtherNameListParams,
                ),
            ),
            cast_to=OtherNameListResponse,
        )


class AsyncOtherNamesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOtherNamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOtherNamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOtherNamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncOtherNamesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        address: other_name_create_params.Address | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        salutation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherName:
        """
        Creates a new other-name.

        Args:
          name: The case-insensitive unique name of this other-name, unique across all
              other-names.

              **NOTE**: Other-names do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The other-name's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          address: The other-name's address.

          alternate_contact: The name of a alternate contact person for this other-name.

          alternate_phone: The other-name's alternate telephone number.

          company_name: The name of the company associated with this other-name. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this other-name.

          email: The other-name's email address.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The other-name's fax number.

          first_name: The first name of the contact person for this other-name.

              Maximum length: 25 characters.

          is_active: Indicates whether this other-name is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          last_name: The last name of the contact person for this other-name.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this other-name.

              Maximum length: 5 characters.

          note: A note or comment about this other-name.

          phone: The other-name's primary telephone number.

          salutation: The formal salutation title that precedes the name of the contact person for
              this other-name, such as "Mr.", "Ms.", or "Dr.".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/other-names",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "address": address,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "company_name": company_name,
                    "contact": contact,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "note": note,
                    "phone": phone,
                    "salutation": salutation,
                },
                other_name_create_params.OtherNameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
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
    ) -> OtherName:
        """
        Retrieves an other-name by ID.

        **IMPORTANT:** If you need to fetch multiple specific other-names by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the other-name to retrieve.

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
            f"/quickbooks-desktop/other-names/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        address: other_name_update_params.Address | Omit = omit,
        alternate_contact: str | Omit = omit,
        alternate_phone: str | Omit = omit,
        company_name: str | Omit = omit,
        contact: str | Omit = omit,
        email: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        name: str | Omit = omit,
        note: str | Omit = omit,
        phone: str | Omit = omit,
        salutation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherName:
        """
        Updates an existing other-name.

        Args:
          id: The QuickBooks-assigned unique identifier of the other-name to update.

          revision_number: The current QuickBooks-assigned revision number of the other-name object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_number: The other-name's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          address: The other-name's address.

          alternate_contact: The name of a alternate contact person for this other-name.

          alternate_phone: The other-name's alternate telephone number.

          company_name: The name of the company associated with this other-name. This name is used on
              invoices, checks, and other forms.

          contact: The name of the primary contact person for this other-name.

          email: The other-name's email address.

          fax: The other-name's fax number.

          first_name: The first name of the contact person for this other-name.

              Maximum length: 25 characters.

          is_active: Indicates whether this other-name is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          last_name: The last name of the contact person for this other-name.

              Maximum length: 25 characters.

          middle_name: The middle name of the contact person for this other-name.

              Maximum length: 5 characters.

          name: The case-insensitive unique name of this other-name, unique across all
              other-names.

              **NOTE**: Other-names do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          note: A note or comment about this other-name.

          phone: The other-name's primary telephone number.

          salutation: The formal salutation title that precedes the name of the contact person for
              this other-name, such as "Mr.", "Ms.", or "Dr.".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/other-names/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "address": address,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "company_name": company_name,
                    "contact": contact,
                    "email": email,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "name": name,
                    "note": note,
                    "phone": phone,
                    "salutation": salutation,
                },
                other_name_update_params.OtherNameUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherName,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherNameListResponse:
        """Returns a list of other-names.

        NOTE: QuickBooks Desktop does not support
        pagination for other-names; hence, there is no `cursor` parameter. Users
        typically have few other-names.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific other-names by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              other-names. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all other-names without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because other-names typically have low record counts.

          name_contains: Filter for other-names whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for other-names whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for other-names whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific other-names by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an other-name.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for other-names whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for other-names whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for other-names that are active, inactive, or both.

          updated_after: Filter for other-names updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for other-names updated on or before this date/time. Accepts the
              following ISO 8601 formats:

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
        return await self._get(
            "/quickbooks-desktop/other-names",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    other_name_list_params.OtherNameListParams,
                ),
            ),
            cast_to=OtherNameListResponse,
        )


class OtherNamesResourceWithRawResponse:
    def __init__(self, other_names: OtherNamesResource) -> None:
        self._other_names = other_names

        self.create = to_raw_response_wrapper(
            other_names.create,
        )
        self.retrieve = to_raw_response_wrapper(
            other_names.retrieve,
        )
        self.update = to_raw_response_wrapper(
            other_names.update,
        )
        self.list = to_raw_response_wrapper(
            other_names.list,
        )


class AsyncOtherNamesResourceWithRawResponse:
    def __init__(self, other_names: AsyncOtherNamesResource) -> None:
        self._other_names = other_names

        self.create = async_to_raw_response_wrapper(
            other_names.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            other_names.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            other_names.update,
        )
        self.list = async_to_raw_response_wrapper(
            other_names.list,
        )


class OtherNamesResourceWithStreamingResponse:
    def __init__(self, other_names: OtherNamesResource) -> None:
        self._other_names = other_names

        self.create = to_streamed_response_wrapper(
            other_names.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            other_names.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            other_names.update,
        )
        self.list = to_streamed_response_wrapper(
            other_names.list,
        )


class AsyncOtherNamesResourceWithStreamingResponse:
    def __init__(self, other_names: AsyncOtherNamesResource) -> None:
        self._other_names = other_names

        self.create = async_to_streamed_response_wrapper(
            other_names.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            other_names.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            other_names.update,
        )
        self.list = async_to_streamed_response_wrapper(
            other_names.list,
        )
