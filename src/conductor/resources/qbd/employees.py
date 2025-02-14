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
from ...types.qbd import employee_list_params, employee_create_params, employee_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.employee import Employee

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[employee_create_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        address: employee_create_params.Address | NotGiven = NOT_GIVEN,
        adjusted_service_date: Union[str, date] | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date] | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[employee_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        department: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disability_description: str | NotGiven = NOT_GIVEN,
        disability_status: Literal["disabled", "non_disabled"] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        emergency_contact: employee_create_params.EmergencyContact | NotGiven = NOT_GIVEN,
        employee_payroll: employee_create_params.EmployeePayroll | NotGiven = NOT_GIVEN,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | NotGiven = NOT_GIVEN,
        employment_status: Literal["full_time", "part_time"] | NotGiven = NOT_GIVEN,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        gender: Literal["male", "female"] | NotGiven = NOT_GIVEN,
        hired_date: Union[str, date] | NotGiven = NOT_GIVEN,
        i9_on_file_status: Literal["on_file", "not_on_file"] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        key_employee_status: Literal["key_employee", "non_key_employee"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        military_status: Literal["active", "reserve"] | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        original_hire_date: Union[str, date] | NotGiven = NOT_GIVEN,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | NotGiven = NOT_GIVEN,
        pager: str | NotGiven = NOT_GIVEN,
        pager_pin: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        print_as: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        supervisor_id: str | NotGiven = NOT_GIVEN,
        target_bonus: str | NotGiven = NOT_GIVEN,
        termination_date: Union[str, date] | NotGiven = NOT_GIVEN,
        us_citizenship_status: Literal["citizen", "non_citizen"] | NotGiven = NOT_GIVEN,
        us_veteran_status: Literal["veteran", "non_veteran"] | NotGiven = NOT_GIVEN,
        work_authorization_expiration_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Creates a new employee.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The employee's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_notes: Additional notes about this employee.

          address: The employee's address.

              If the company uses QuickBooks Payroll for this employee, this address must
              specify a complete address, including city, state, ZIP (or postal) code, and at
              least one line of the street address.

          adjusted_service_date: The adjusted service date for this employee, in ISO 8601 format (YYYY-MM-DD).
              This date accounts for previous employment periods or leaves that affect
              seniority.

          alternate_phone: The employee's alternate telephone number.

          billing_rate_id: The employee's billing rate, used to override service item rates in time
              tracking transactions.

          birth_date: This employee's date of birth, in ISO 8601 format (YYYY-MM-DD).

          custom_contact_fields: Additional custom contact fields for this employee, such as phone numbers or
              email addresses.

          department: The employee's department. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          description: A description of this employee. Found in the "employment job details" section of
              the employee's record in QuickBooks.

          disability_description: A description of this employee's disability.

          disability_status: Indicates whether this employee is disabled.

          email: The employee's email address.

          emergency_contact: The employee's emergency contacts.

          employee_payroll: The employee's payroll information.

          employee_type: The employee type. This affects payroll taxes - a statutory employee is defined
              as an employee by statute. Note that owners/partners are typically on the "Other
              Names" list in QuickBooks, but if listed as an employee their type will be
              `owner`.

          employment_status: Indicates whether this employee is a part-time or full-time employee.

          ethnicity: This employee's ethnicity.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The employee's fax number.

          first_name: The employee's first name.

              Maximum length: 25 characters.

          gender: This employee's gender.

          hired_date: The date this employee was hired, in ISO 8601 format (YYYY-MM-DD).

          i9_on_file_status: Indicates whether this employee's I-9 is on file.

          is_active: Indicates whether this employee is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_title: The employee's job title.

          key_employee_status: Indicates whether this employee is a key employee.

          last_name: The employee's last name.

              Maximum length: 25 characters.

          middle_name: The employee's middle name.

              Maximum length: 5 characters.

          military_status: This employee's military status if they are a U.S. veteran.

          mobile: The employee's mobile phone number.

          note: A note or comment about this employee.

          original_hire_date: The original hire date for this employee, in ISO 8601 format (YYYY-MM-DD).

          overtime_exempt_status: Indicates whether this employee is exempt from overtime pay. This classification
              is based on U.S. labor laws (FLSA).

          pager: The employee's pager number.

          pager_pin: The employee's pager PIN.

          phone: The employee's primary telephone number.

          print_as: The name to use when printing this employee from QuickBooks. By default, this is
              the same as the `name` field.

          salutation: The employee's formal salutation title that precedes their name, such as "Mr.",
              "Ms.", or "Dr.".

          ssn: The employee's Social Security Number. The value can be with or without dashes.

              **NOTE**: This field cannot be changed after the employee is created.

          supervisor_id: The employee's supervisor. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          target_bonus: The target bonus for this employee, represented as a decimal string. Found in
              the "employment job details" section of the employee's record in QuickBooks.

          termination_date: The date this employee's employment ended with the company, in ISO 8601 format
              (YYYY-MM-DD). This is also known as the released date or separation date.

          us_citizenship_status: Indicates whether this employee is a U.S. citizen.

          us_veteran_status: Indicates whether this employee is a U.S. veteran.

          work_authorization_expiration_date: The date this employee's work authorization expires, in ISO 8601 format
              (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/employees",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "additional_notes": additional_notes,
                    "address": address,
                    "adjusted_service_date": adjusted_service_date,
                    "alternate_phone": alternate_phone,
                    "billing_rate_id": billing_rate_id,
                    "birth_date": birth_date,
                    "custom_contact_fields": custom_contact_fields,
                    "department": department,
                    "description": description,
                    "disability_description": disability_description,
                    "disability_status": disability_status,
                    "email": email,
                    "emergency_contact": emergency_contact,
                    "employee_payroll": employee_payroll,
                    "employee_type": employee_type,
                    "employment_status": employment_status,
                    "ethnicity": ethnicity,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "gender": gender,
                    "hired_date": hired_date,
                    "i9_on_file_status": i9_on_file_status,
                    "is_active": is_active,
                    "job_title": job_title,
                    "key_employee_status": key_employee_status,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "military_status": military_status,
                    "mobile": mobile,
                    "note": note,
                    "original_hire_date": original_hire_date,
                    "overtime_exempt_status": overtime_exempt_status,
                    "pager": pager,
                    "pager_pin": pager_pin,
                    "phone": phone,
                    "print_as": print_as,
                    "salutation": salutation,
                    "ssn": ssn,
                    "supervisor_id": supervisor_id,
                    "target_bonus": target_bonus,
                    "termination_date": termination_date,
                    "us_citizenship_status": us_citizenship_status,
                    "us_veteran_status": us_veteran_status,
                    "work_authorization_expiration_date": work_authorization_expiration_date,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
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
    ) -> Employee:
        """
        Retrieves an employee by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to retrieve.

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
            f"/quickbooks-desktop/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[employee_update_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        address: employee_update_params.Address | NotGiven = NOT_GIVEN,
        adjusted_service_date: Union[str, date] | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date] | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[employee_update_params.CustomContactField] | NotGiven = NOT_GIVEN,
        department: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disability_description: str | NotGiven = NOT_GIVEN,
        disability_status: Literal["disabled", "non_disabled"] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        emergency_contact: employee_update_params.EmergencyContact | NotGiven = NOT_GIVEN,
        employee_payroll: employee_update_params.EmployeePayroll | NotGiven = NOT_GIVEN,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | NotGiven = NOT_GIVEN,
        employment_status: Literal["full_time", "part_time"] | NotGiven = NOT_GIVEN,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        hired_date: Union[str, date] | NotGiven = NOT_GIVEN,
        i9_on_file_status: Literal["on_file", "not_on_file"] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        key_employee_status: Literal["key_employee", "non_key_employee"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        military_status: Literal["active", "reserve"] | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        original_hire_date: Union[str, date] | NotGiven = NOT_GIVEN,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | NotGiven = NOT_GIVEN,
        pager: str | NotGiven = NOT_GIVEN,
        pager_pin: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        print_as: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        supervisor_id: str | NotGiven = NOT_GIVEN,
        target_bonus: str | NotGiven = NOT_GIVEN,
        termination_date: Union[str, date] | NotGiven = NOT_GIVEN,
        us_citizenship_status: Literal["citizen", "non_citizen"] | NotGiven = NOT_GIVEN,
        us_veteran_status: Literal["veteran", "non_veteran"] | NotGiven = NOT_GIVEN,
        work_authorization_expiration_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Updates an existing employee.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to update.

          revision_number: The current QuickBooks-assigned revision number of the employee object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The employee's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_notes: Additional notes about this employee.

          address: The employee's address.

              If the company uses QuickBooks Payroll for this employee, this address must
              specify a complete address, including city, state, ZIP (or postal) code, and at
              least one line of the street address.

          adjusted_service_date: The adjusted service date for this employee, in ISO 8601 format (YYYY-MM-DD).
              This date accounts for previous employment periods or leaves that affect
              seniority.

          alternate_phone: The employee's alternate telephone number.

          billing_rate_id: The employee's billing rate, used to override service item rates in time
              tracking transactions.

          birth_date: This employee's date of birth, in ISO 8601 format (YYYY-MM-DD).

          custom_contact_fields: Additional custom contact fields for this employee, such as phone numbers or
              email addresses.

          department: The employee's department. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          description: A description of this employee. Found in the "employment job details" section of
              the employee's record in QuickBooks.

          disability_description: A description of this employee's disability.

          disability_status: Indicates whether this employee is disabled.

          email: The employee's email address.

          emergency_contact: The employee's emergency contacts.

          employee_payroll: The employee's payroll information.

          employee_type: The employee type. This affects payroll taxes - a statutory employee is defined
              as an employee by statute. Note that owners/partners are typically on the "Other
              Names" list in QuickBooks, but if listed as an employee their type will be
              `owner`.

          employment_status: Indicates whether this employee is a part-time or full-time employee.

          ethnicity: This employee's ethnicity.

          fax: The employee's fax number.

          first_name: The employee's first name.

              Maximum length: 25 characters.

          hired_date: The date this employee was hired, in ISO 8601 format (YYYY-MM-DD).

          i9_on_file_status: Indicates whether this employee's I-9 is on file.

          is_active: Indicates whether this employee is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_title: The employee's job title.

          key_employee_status: Indicates whether this employee is a key employee.

          last_name: The employee's last name.

              Maximum length: 25 characters.

          middle_name: The employee's middle name.

              Maximum length: 5 characters.

          military_status: This employee's military status if they are a U.S. veteran.

          mobile: The employee's mobile phone number.

          note: A note or comment about this employee.

          original_hire_date: The original hire date for this employee, in ISO 8601 format (YYYY-MM-DD).

          overtime_exempt_status: Indicates whether this employee is exempt from overtime pay. This classification
              is based on U.S. labor laws (FLSA).

          pager: The employee's pager number.

          pager_pin: The employee's pager PIN.

          phone: The employee's primary telephone number.

          print_as: The name to use when printing this employee from QuickBooks. By default, this is
              the same as the `name` field.

          salutation: The employee's formal salutation title that precedes their name, such as "Mr.",
              "Ms.", or "Dr.".

          supervisor_id: The employee's supervisor. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          target_bonus: The target bonus for this employee, represented as a decimal string. Found in
              the "employment job details" section of the employee's record in QuickBooks.

          termination_date: The date this employee's employment ended with the company, in ISO 8601 format
              (YYYY-MM-DD). This is also known as the released date or separation date.

          us_citizenship_status: Indicates whether this employee is a U.S. citizen.

          us_veteran_status: Indicates whether this employee is a U.S. veteran.

          work_authorization_expiration_date: The date this employee's work authorization expires, in ISO 8601 format
              (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/employees/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_notes": additional_notes,
                    "address": address,
                    "adjusted_service_date": adjusted_service_date,
                    "alternate_phone": alternate_phone,
                    "billing_rate_id": billing_rate_id,
                    "birth_date": birth_date,
                    "custom_contact_fields": custom_contact_fields,
                    "department": department,
                    "description": description,
                    "disability_description": disability_description,
                    "disability_status": disability_status,
                    "email": email,
                    "emergency_contact": emergency_contact,
                    "employee_payroll": employee_payroll,
                    "employee_type": employee_type,
                    "employment_status": employment_status,
                    "ethnicity": ethnicity,
                    "fax": fax,
                    "first_name": first_name,
                    "hired_date": hired_date,
                    "i9_on_file_status": i9_on_file_status,
                    "is_active": is_active,
                    "job_title": job_title,
                    "key_employee_status": key_employee_status,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "military_status": military_status,
                    "mobile": mobile,
                    "note": note,
                    "original_hire_date": original_hire_date,
                    "overtime_exempt_status": overtime_exempt_status,
                    "pager": pager,
                    "pager_pin": pager_pin,
                    "phone": phone,
                    "print_as": print_as,
                    "salutation": salutation,
                    "supervisor_id": supervisor_id,
                    "target_bonus": target_bonus,
                    "termination_date": termination_date,
                    "us_citizenship_status": us_citizenship_status,
                    "us_veteran_status": us_veteran_status,
                    "work_authorization_expiration_date": work_authorization_expiration_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> SyncCursorPage[Employee]:
        """Returns a list of employees.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific employees by their QuickBooks-assigned unique identifier(s).

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

          name_contains: Filter for employees whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for employees whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for employees whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific employees by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an employee.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for employees whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for employees whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for employees that are active, inactive, or both.

          updated_after: Filter for employees updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for employees updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/employees",
            page=SyncCursorPage[Employee],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    employee_list_params.EmployeeListParams,
                ),
            ),
            model=Employee,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[employee_create_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        address: employee_create_params.Address | NotGiven = NOT_GIVEN,
        adjusted_service_date: Union[str, date] | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date] | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[employee_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        department: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disability_description: str | NotGiven = NOT_GIVEN,
        disability_status: Literal["disabled", "non_disabled"] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        emergency_contact: employee_create_params.EmergencyContact | NotGiven = NOT_GIVEN,
        employee_payroll: employee_create_params.EmployeePayroll | NotGiven = NOT_GIVEN,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | NotGiven = NOT_GIVEN,
        employment_status: Literal["full_time", "part_time"] | NotGiven = NOT_GIVEN,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        gender: Literal["male", "female"] | NotGiven = NOT_GIVEN,
        hired_date: Union[str, date] | NotGiven = NOT_GIVEN,
        i9_on_file_status: Literal["on_file", "not_on_file"] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        key_employee_status: Literal["key_employee", "non_key_employee"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        military_status: Literal["active", "reserve"] | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        original_hire_date: Union[str, date] | NotGiven = NOT_GIVEN,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | NotGiven = NOT_GIVEN,
        pager: str | NotGiven = NOT_GIVEN,
        pager_pin: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        print_as: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        supervisor_id: str | NotGiven = NOT_GIVEN,
        target_bonus: str | NotGiven = NOT_GIVEN,
        termination_date: Union[str, date] | NotGiven = NOT_GIVEN,
        us_citizenship_status: Literal["citizen", "non_citizen"] | NotGiven = NOT_GIVEN,
        us_veteran_status: Literal["veteran", "non_veteran"] | NotGiven = NOT_GIVEN,
        work_authorization_expiration_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Creates a new employee.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The employee's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_notes: Additional notes about this employee.

          address: The employee's address.

              If the company uses QuickBooks Payroll for this employee, this address must
              specify a complete address, including city, state, ZIP (or postal) code, and at
              least one line of the street address.

          adjusted_service_date: The adjusted service date for this employee, in ISO 8601 format (YYYY-MM-DD).
              This date accounts for previous employment periods or leaves that affect
              seniority.

          alternate_phone: The employee's alternate telephone number.

          billing_rate_id: The employee's billing rate, used to override service item rates in time
              tracking transactions.

          birth_date: This employee's date of birth, in ISO 8601 format (YYYY-MM-DD).

          custom_contact_fields: Additional custom contact fields for this employee, such as phone numbers or
              email addresses.

          department: The employee's department. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          description: A description of this employee. Found in the "employment job details" section of
              the employee's record in QuickBooks.

          disability_description: A description of this employee's disability.

          disability_status: Indicates whether this employee is disabled.

          email: The employee's email address.

          emergency_contact: The employee's emergency contacts.

          employee_payroll: The employee's payroll information.

          employee_type: The employee type. This affects payroll taxes - a statutory employee is defined
              as an employee by statute. Note that owners/partners are typically on the "Other
              Names" list in QuickBooks, but if listed as an employee their type will be
              `owner`.

          employment_status: Indicates whether this employee is a part-time or full-time employee.

          ethnicity: This employee's ethnicity.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          fax: The employee's fax number.

          first_name: The employee's first name.

              Maximum length: 25 characters.

          gender: This employee's gender.

          hired_date: The date this employee was hired, in ISO 8601 format (YYYY-MM-DD).

          i9_on_file_status: Indicates whether this employee's I-9 is on file.

          is_active: Indicates whether this employee is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_title: The employee's job title.

          key_employee_status: Indicates whether this employee is a key employee.

          last_name: The employee's last name.

              Maximum length: 25 characters.

          middle_name: The employee's middle name.

              Maximum length: 5 characters.

          military_status: This employee's military status if they are a U.S. veteran.

          mobile: The employee's mobile phone number.

          note: A note or comment about this employee.

          original_hire_date: The original hire date for this employee, in ISO 8601 format (YYYY-MM-DD).

          overtime_exempt_status: Indicates whether this employee is exempt from overtime pay. This classification
              is based on U.S. labor laws (FLSA).

          pager: The employee's pager number.

          pager_pin: The employee's pager PIN.

          phone: The employee's primary telephone number.

          print_as: The name to use when printing this employee from QuickBooks. By default, this is
              the same as the `name` field.

          salutation: The employee's formal salutation title that precedes their name, such as "Mr.",
              "Ms.", or "Dr.".

          ssn: The employee's Social Security Number. The value can be with or without dashes.

              **NOTE**: This field cannot be changed after the employee is created.

          supervisor_id: The employee's supervisor. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          target_bonus: The target bonus for this employee, represented as a decimal string. Found in
              the "employment job details" section of the employee's record in QuickBooks.

          termination_date: The date this employee's employment ended with the company, in ISO 8601 format
              (YYYY-MM-DD). This is also known as the released date or separation date.

          us_citizenship_status: Indicates whether this employee is a U.S. citizen.

          us_veteran_status: Indicates whether this employee is a U.S. veteran.

          work_authorization_expiration_date: The date this employee's work authorization expires, in ISO 8601 format
              (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/employees",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "additional_notes": additional_notes,
                    "address": address,
                    "adjusted_service_date": adjusted_service_date,
                    "alternate_phone": alternate_phone,
                    "billing_rate_id": billing_rate_id,
                    "birth_date": birth_date,
                    "custom_contact_fields": custom_contact_fields,
                    "department": department,
                    "description": description,
                    "disability_description": disability_description,
                    "disability_status": disability_status,
                    "email": email,
                    "emergency_contact": emergency_contact,
                    "employee_payroll": employee_payroll,
                    "employee_type": employee_type,
                    "employment_status": employment_status,
                    "ethnicity": ethnicity,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "gender": gender,
                    "hired_date": hired_date,
                    "i9_on_file_status": i9_on_file_status,
                    "is_active": is_active,
                    "job_title": job_title,
                    "key_employee_status": key_employee_status,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "military_status": military_status,
                    "mobile": mobile,
                    "note": note,
                    "original_hire_date": original_hire_date,
                    "overtime_exempt_status": overtime_exempt_status,
                    "pager": pager,
                    "pager_pin": pager_pin,
                    "phone": phone,
                    "print_as": print_as,
                    "salutation": salutation,
                    "ssn": ssn,
                    "supervisor_id": supervisor_id,
                    "target_bonus": target_bonus,
                    "termination_date": termination_date,
                    "us_citizenship_status": us_citizenship_status,
                    "us_veteran_status": us_veteran_status,
                    "work_authorization_expiration_date": work_authorization_expiration_date,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
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
    ) -> Employee:
        """
        Retrieves an employee by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to retrieve.

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
            f"/quickbooks-desktop/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_notes: Iterable[employee_update_params.AdditionalNote] | NotGiven = NOT_GIVEN,
        address: employee_update_params.Address | NotGiven = NOT_GIVEN,
        adjusted_service_date: Union[str, date] | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_rate_id: str | NotGiven = NOT_GIVEN,
        birth_date: Union[str, date] | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[employee_update_params.CustomContactField] | NotGiven = NOT_GIVEN,
        department: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disability_description: str | NotGiven = NOT_GIVEN,
        disability_status: Literal["disabled", "non_disabled"] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        emergency_contact: employee_update_params.EmergencyContact | NotGiven = NOT_GIVEN,
        employee_payroll: employee_update_params.EmployeePayroll | NotGiven = NOT_GIVEN,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | NotGiven = NOT_GIVEN,
        employment_status: Literal["full_time", "part_time"] | NotGiven = NOT_GIVEN,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        hired_date: Union[str, date] | NotGiven = NOT_GIVEN,
        i9_on_file_status: Literal["on_file", "not_on_file"] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        key_employee_status: Literal["key_employee", "non_key_employee"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        military_status: Literal["active", "reserve"] | NotGiven = NOT_GIVEN,
        mobile: str | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        original_hire_date: Union[str, date] | NotGiven = NOT_GIVEN,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | NotGiven = NOT_GIVEN,
        pager: str | NotGiven = NOT_GIVEN,
        pager_pin: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        print_as: str | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        supervisor_id: str | NotGiven = NOT_GIVEN,
        target_bonus: str | NotGiven = NOT_GIVEN,
        termination_date: Union[str, date] | NotGiven = NOT_GIVEN,
        us_citizenship_status: Literal["citizen", "non_citizen"] | NotGiven = NOT_GIVEN,
        us_veteran_status: Literal["veteran", "non_veteran"] | NotGiven = NOT_GIVEN,
        work_authorization_expiration_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Updates an existing employee.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to update.

          revision_number: The current QuickBooks-assigned revision number of the employee object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The employee's account number, which appears in the QuickBooks chart of
              accounts, reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          additional_notes: Additional notes about this employee.

          address: The employee's address.

              If the company uses QuickBooks Payroll for this employee, this address must
              specify a complete address, including city, state, ZIP (or postal) code, and at
              least one line of the street address.

          adjusted_service_date: The adjusted service date for this employee, in ISO 8601 format (YYYY-MM-DD).
              This date accounts for previous employment periods or leaves that affect
              seniority.

          alternate_phone: The employee's alternate telephone number.

          billing_rate_id: The employee's billing rate, used to override service item rates in time
              tracking transactions.

          birth_date: This employee's date of birth, in ISO 8601 format (YYYY-MM-DD).

          custom_contact_fields: Additional custom contact fields for this employee, such as phone numbers or
              email addresses.

          department: The employee's department. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          description: A description of this employee. Found in the "employment job details" section of
              the employee's record in QuickBooks.

          disability_description: A description of this employee's disability.

          disability_status: Indicates whether this employee is disabled.

          email: The employee's email address.

          emergency_contact: The employee's emergency contacts.

          employee_payroll: The employee's payroll information.

          employee_type: The employee type. This affects payroll taxes - a statutory employee is defined
              as an employee by statute. Note that owners/partners are typically on the "Other
              Names" list in QuickBooks, but if listed as an employee their type will be
              `owner`.

          employment_status: Indicates whether this employee is a part-time or full-time employee.

          ethnicity: This employee's ethnicity.

          fax: The employee's fax number.

          first_name: The employee's first name.

              Maximum length: 25 characters.

          hired_date: The date this employee was hired, in ISO 8601 format (YYYY-MM-DD).

          i9_on_file_status: Indicates whether this employee's I-9 is on file.

          is_active: Indicates whether this employee is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          job_title: The employee's job title.

          key_employee_status: Indicates whether this employee is a key employee.

          last_name: The employee's last name.

              Maximum length: 25 characters.

          middle_name: The employee's middle name.

              Maximum length: 5 characters.

          military_status: This employee's military status if they are a U.S. veteran.

          mobile: The employee's mobile phone number.

          note: A note or comment about this employee.

          original_hire_date: The original hire date for this employee, in ISO 8601 format (YYYY-MM-DD).

          overtime_exempt_status: Indicates whether this employee is exempt from overtime pay. This classification
              is based on U.S. labor laws (FLSA).

          pager: The employee's pager number.

          pager_pin: The employee's pager PIN.

          phone: The employee's primary telephone number.

          print_as: The name to use when printing this employee from QuickBooks. By default, this is
              the same as the `name` field.

          salutation: The employee's formal salutation title that precedes their name, such as "Mr.",
              "Ms.", or "Dr.".

          supervisor_id: The employee's supervisor. Found in the "employment job details" section of the
              employee's record in QuickBooks.

          target_bonus: The target bonus for this employee, represented as a decimal string. Found in
              the "employment job details" section of the employee's record in QuickBooks.

          termination_date: The date this employee's employment ended with the company, in ISO 8601 format
              (YYYY-MM-DD). This is also known as the released date or separation date.

          us_citizenship_status: Indicates whether this employee is a U.S. citizen.

          us_veteran_status: Indicates whether this employee is a U.S. veteran.

          work_authorization_expiration_date: The date this employee's work authorization expires, in ISO 8601 format
              (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/employees/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "additional_notes": additional_notes,
                    "address": address,
                    "adjusted_service_date": adjusted_service_date,
                    "alternate_phone": alternate_phone,
                    "billing_rate_id": billing_rate_id,
                    "birth_date": birth_date,
                    "custom_contact_fields": custom_contact_fields,
                    "department": department,
                    "description": description,
                    "disability_description": disability_description,
                    "disability_status": disability_status,
                    "email": email,
                    "emergency_contact": emergency_contact,
                    "employee_payroll": employee_payroll,
                    "employee_type": employee_type,
                    "employment_status": employment_status,
                    "ethnicity": ethnicity,
                    "fax": fax,
                    "first_name": first_name,
                    "hired_date": hired_date,
                    "i9_on_file_status": i9_on_file_status,
                    "is_active": is_active,
                    "job_title": job_title,
                    "key_employee_status": key_employee_status,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "military_status": military_status,
                    "mobile": mobile,
                    "note": note,
                    "original_hire_date": original_hire_date,
                    "overtime_exempt_status": overtime_exempt_status,
                    "pager": pager,
                    "pager_pin": pager_pin,
                    "phone": phone,
                    "print_as": print_as,
                    "salutation": salutation,
                    "supervisor_id": supervisor_id,
                    "target_bonus": target_bonus,
                    "termination_date": termination_date,
                    "us_citizenship_status": us_citizenship_status,
                    "us_veteran_status": us_veteran_status,
                    "work_authorization_expiration_date": work_authorization_expiration_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[Employee, AsyncCursorPage[Employee]]:
        """Returns a list of employees.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific employees by their QuickBooks-assigned unique identifier(s).

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

          name_contains: Filter for employees whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for employees whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for employees whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific employees by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an employee.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for employees whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for employees whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for employees that are active, inactive, or both.

          updated_after: Filter for employees updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for employees updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/employees",
            page=AsyncCursorPage[Employee],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    employee_list_params.EmployeeListParams,
                ),
            ),
            model=Employee,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.create = to_raw_response_wrapper(
            employees.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employees.update,
        )
        self.list = to_raw_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.create = async_to_raw_response_wrapper(
            employees.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employees.update,
        )
        self.list = async_to_raw_response_wrapper(
            employees.list,
        )


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.create = to_streamed_response_wrapper(
            employees.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employees.update,
        )
        self.list = to_streamed_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.create = async_to_streamed_response_wrapper(
            employees.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employees.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employees.list,
        )
