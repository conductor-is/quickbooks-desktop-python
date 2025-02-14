# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.qbd import class_list_params, class_create_params, class_update_params
from ..._base_client import make_request_options
from ...types.qbd.class_ import Class
from ...types.qbd.class_list_response import ClassListResponse

__all__ = ["ClassesResource", "AsyncClassesResource"]


class ClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return ClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return ClassesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Class:
        """Creates a new class.

        Args:
          name: The case-insensitive name of this class.

        Not guaranteed to be unique because it
              does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two classes could both have the `name` "Marketing", but they
              could have unique `fullName` values, such as "Department:Marketing" and
              "Internal:Marketing".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Indicates whether this class is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent class one level above this one in the hierarchy. For example, if this
              class has a `fullName` of "Department:Marketing", its parent has a `fullName` of
              "Department". If this class is at the top level, this field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/classes",
            body=maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                class_create_params.ClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
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
    ) -> Class:
        """
        Retrieves a class by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the class to retrieve.

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
            f"/quickbooks-desktop/classes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Class:
        """
        Updates an existing class.

        Args:
          id: The QuickBooks-assigned unique identifier of the class to update.

          revision_number: The current QuickBooks-assigned revision number of the class object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Indicates whether this class is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this class. Not guaranteed to be unique because it
              does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two classes could both have the `name` "Marketing", but they
              could have unique `fullName` values, such as "Department:Marketing" and
              "Internal:Marketing".

              Maximum length: 31 characters.

          parent_id: The parent class one level above this one in the hierarchy. For example, if this
              class has a `fullName` of "Department:Marketing", its parent has a `fullName` of
              "Department". If this class is at the top level, this field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/classes/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                },
                class_update_params.ClassUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassListResponse:
        """Returns a list of classes.

        NOTE: QuickBooks Desktop does not support pagination
        for classes; hence, there is no `cursor` parameter. Users typically have few
        classes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          full_names: Filter for specific classes by their full-name(s), case-insensitive. Like `id`,
              `fullName` is a unique identifier for a class, formed by by combining the names
              of its parent objects with its own `name`, separated by colons. For example, if
              a class is under "Department" and has the `name` "Marketing", its `fullName`
              would be "Department:Marketing".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific classes by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              classes. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all classes without limit,
              unlike paginated endpoints which default to 150 records. This is acceptable
              because classes typically have low record counts.

          name_contains:
              Filter for classes whose `name` contains this substring, case-insensitive. NOTE:
              If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for classes whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for classes whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for classes whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for classes whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for classes that are active, inactive, or both.

          updated_after: Filter for classes updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for classes updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/classes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class AsyncClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncClassesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Class:
        """Creates a new class.

        Args:
          name: The case-insensitive name of this class.

        Not guaranteed to be unique because it
              does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two classes could both have the `name` "Marketing", but they
              could have unique `fullName` values, such as "Department:Marketing" and
              "Internal:Marketing".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Indicates whether this class is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent class one level above this one in the hierarchy. For example, if this
              class has a `fullName` of "Department:Marketing", its parent has a `fullName` of
              "Department". If this class is at the top level, this field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/classes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                class_create_params.ClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
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
    ) -> Class:
        """
        Retrieves a class by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the class to retrieve.

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
            f"/quickbooks-desktop/classes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Class:
        """
        Updates an existing class.

        Args:
          id: The QuickBooks-assigned unique identifier of the class to update.

          revision_number: The current QuickBooks-assigned revision number of the class object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Indicates whether this class is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this class. Not guaranteed to be unique because it
              does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two classes could both have the `name` "Marketing", but they
              could have unique `fullName` values, such as "Department:Marketing" and
              "Internal:Marketing".

              Maximum length: 31 characters.

          parent_id: The parent class one level above this one in the hierarchy. For example, if this
              class has a `fullName` of "Department:Marketing", its parent has a `fullName` of
              "Department". If this class is at the top level, this field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/classes/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                },
                class_update_params.ClassUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Class,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassListResponse:
        """Returns a list of classes.

        NOTE: QuickBooks Desktop does not support pagination
        for classes; hence, there is no `cursor` parameter. Users typically have few
        classes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          full_names: Filter for specific classes by their full-name(s), case-insensitive. Like `id`,
              `fullName` is a unique identifier for a class, formed by by combining the names
              of its parent objects with its own `name`, separated by colons. For example, if
              a class is under "Department" and has the `name` "Marketing", its `fullName`
              would be "Department:Marketing".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific classes by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              classes. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all classes without limit,
              unlike paginated endpoints which default to 150 records. This is acceptable
              because classes typically have low record counts.

          name_contains:
              Filter for classes whose `name` contains this substring, case-insensitive. NOTE:
              If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for classes whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for classes whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for classes whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for classes whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for classes that are active, inactive, or both.

          updated_after: Filter for classes updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for classes updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/classes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class ClassesResourceWithRawResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.create = to_raw_response_wrapper(
            classes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            classes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            classes.update,
        )
        self.list = to_raw_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithRawResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.create = async_to_raw_response_wrapper(
            classes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            classes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            classes.update,
        )
        self.list = async_to_raw_response_wrapper(
            classes.list,
        )


class ClassesResourceWithStreamingResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.create = to_streamed_response_wrapper(
            classes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            classes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            classes.update,
        )
        self.list = to_streamed_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithStreamingResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.create = async_to_streamed_response_wrapper(
            classes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            classes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            classes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            classes.list,
        )
