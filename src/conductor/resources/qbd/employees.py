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
from ...types.qbd import employee_list_params, employee_create_params, employee_update_params
from ..._base_client import make_request_options
from ...types.qbd.employee import Employee
from ...types.qbd.employee_list_response import EmployeeListResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_notes: Iterable[employee_create_params.AdditionalNote] | Omit = omit,
        address: employee_create_params.Address | Omit = omit,
        adjusted_service_date: Union[str, date] | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_rate_id: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        custom_contact_fields: Iterable[employee_create_params.CustomContactField] | Omit = omit,
        department: str | Omit = omit,
        description: str | Omit = omit,
        disability_description: str | Omit = omit,
        disability_status: Literal["disabled", "non_disabled"] | Omit = omit,
        email: str | Omit = omit,
        emergency_contact: employee_create_params.EmergencyContact | Omit = omit,
        employee_payroll: employee_create_params.EmployeePayroll | Omit = omit,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | Omit = omit,
        employment_status: Literal["full_time", "part_time"] | Omit = omit,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["male", "female"] | Omit = omit,
        hired_date: Union[str, date] | Omit = omit,
        i9_on_file_status: Literal["on_file", "not_on_file"] | Omit = omit,
        is_active: bool | Omit = omit,
        job_title: str | Omit = omit,
        key_employee_status: Literal["key_employee", "non_key_employee"] | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        military_status: Literal["active", "reserve"] | Omit = omit,
        mobile: str | Omit = omit,
        note: str | Omit = omit,
        original_hire_date: Union[str, date] | Omit = omit,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | Omit = omit,
        pager: str | Omit = omit,
        pager_pin: str | Omit = omit,
        phone: str | Omit = omit,
        print_as: str | Omit = omit,
        salutation: str | Omit = omit,
        ssn: str | Omit = omit,
        supervisor_id: str | Omit = omit,
        target_bonus: str | Omit = omit,
        termination_date: Union[str, date] | Omit = omit,
        us_citizenship_status: Literal["citizen", "non_citizen"] | Omit = omit,
        us_veteran_status: Literal["veteran", "non_veteran"] | Omit = omit,
        work_authorization_expiration_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Creates an employee record that captures personal details, contact information,
        employment dates, and payroll settings in a single request so the employee is
        ready for scheduling, time tracking, and payroll processing.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

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
              tracking activities.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Retrieves an employee by ID.

        **IMPORTANT:** If you need to fetch multiple specific employees by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to retrieve.

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
        account_number: str | Omit = omit,
        additional_notes: Iterable[employee_update_params.AdditionalNote] | Omit = omit,
        address: employee_update_params.Address | Omit = omit,
        adjusted_service_date: Union[str, date] | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_rate_id: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        custom_contact_fields: Iterable[employee_update_params.CustomContactField] | Omit = omit,
        department: str | Omit = omit,
        description: str | Omit = omit,
        disability_description: str | Omit = omit,
        disability_status: Literal["disabled", "non_disabled"] | Omit = omit,
        email: str | Omit = omit,
        emergency_contact: employee_update_params.EmergencyContact | Omit = omit,
        employee_payroll: employee_update_params.EmployeePayroll | Omit = omit,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | Omit = omit,
        employment_status: Literal["full_time", "part_time"] | Omit = omit,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        hired_date: Union[str, date] | Omit = omit,
        i9_on_file_status: Literal["on_file", "not_on_file"] | Omit = omit,
        is_active: bool | Omit = omit,
        job_title: str | Omit = omit,
        key_employee_status: Literal["key_employee", "non_key_employee"] | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        military_status: Literal["active", "reserve"] | Omit = omit,
        mobile: str | Omit = omit,
        note: str | Omit = omit,
        original_hire_date: Union[str, date] | Omit = omit,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | Omit = omit,
        pager: str | Omit = omit,
        pager_pin: str | Omit = omit,
        phone: str | Omit = omit,
        print_as: str | Omit = omit,
        salutation: str | Omit = omit,
        supervisor_id: str | Omit = omit,
        target_bonus: str | Omit = omit,
        termination_date: Union[str, date] | Omit = omit,
        us_citizenship_status: Literal["citizen", "non_citizen"] | Omit = omit,
        us_veteran_status: Literal["veteran", "non_veteran"] | Omit = omit,
        work_authorization_expiration_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Updates an employee record, allowing you to revise contact details, employment
        status dates, supervisory assignments, payroll configuration, and additional
        notes to keep workforce data current.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to update.

          revision_number: The current QuickBooks-assigned revision number of the employee object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

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
              tracking activities.

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
    ) -> EmployeeListResponse:
        """Returns a list of employees.

        NOTE: QuickBooks Desktop does not support
        pagination for employees; hence, there is no `cursor` parameter. Users typically
        have few employees.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific employees by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              employees. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all employees without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because employees typically have low record counts.

          name_contains: Filter for employees whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for employees whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for employees whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific employees by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an employee.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for employees whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for employees whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for employees that are active, inactive, or both.

          updated_after: Filter for employees updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for employees updated on or before this date/time. Accepts the following
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
        return self._get(
            "/quickbooks-desktop/employees",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        conductor_end_user_id: str,
        account_number: str | Omit = omit,
        additional_notes: Iterable[employee_create_params.AdditionalNote] | Omit = omit,
        address: employee_create_params.Address | Omit = omit,
        adjusted_service_date: Union[str, date] | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_rate_id: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        custom_contact_fields: Iterable[employee_create_params.CustomContactField] | Omit = omit,
        department: str | Omit = omit,
        description: str | Omit = omit,
        disability_description: str | Omit = omit,
        disability_status: Literal["disabled", "non_disabled"] | Omit = omit,
        email: str | Omit = omit,
        emergency_contact: employee_create_params.EmergencyContact | Omit = omit,
        employee_payroll: employee_create_params.EmployeePayroll | Omit = omit,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | Omit = omit,
        employment_status: Literal["full_time", "part_time"] | Omit = omit,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | Omit = omit,
        external_id: str | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["male", "female"] | Omit = omit,
        hired_date: Union[str, date] | Omit = omit,
        i9_on_file_status: Literal["on_file", "not_on_file"] | Omit = omit,
        is_active: bool | Omit = omit,
        job_title: str | Omit = omit,
        key_employee_status: Literal["key_employee", "non_key_employee"] | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        military_status: Literal["active", "reserve"] | Omit = omit,
        mobile: str | Omit = omit,
        note: str | Omit = omit,
        original_hire_date: Union[str, date] | Omit = omit,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | Omit = omit,
        pager: str | Omit = omit,
        pager_pin: str | Omit = omit,
        phone: str | Omit = omit,
        print_as: str | Omit = omit,
        salutation: str | Omit = omit,
        ssn: str | Omit = omit,
        supervisor_id: str | Omit = omit,
        target_bonus: str | Omit = omit,
        termination_date: Union[str, date] | Omit = omit,
        us_citizenship_status: Literal["citizen", "non_citizen"] | Omit = omit,
        us_veteran_status: Literal["veteran", "non_veteran"] | Omit = omit,
        work_authorization_expiration_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Creates an employee record that captures personal details, contact information,
        employment dates, and payroll settings in a single request so the employee is
        ready for scheduling, time tracking, and payroll processing.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

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
              tracking activities.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Retrieves an employee by ID.

        **IMPORTANT:** If you need to fetch multiple specific employees by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to retrieve.

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
        account_number: str | Omit = omit,
        additional_notes: Iterable[employee_update_params.AdditionalNote] | Omit = omit,
        address: employee_update_params.Address | Omit = omit,
        adjusted_service_date: Union[str, date] | Omit = omit,
        alternate_phone: str | Omit = omit,
        billing_rate_id: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        custom_contact_fields: Iterable[employee_update_params.CustomContactField] | Omit = omit,
        department: str | Omit = omit,
        description: str | Omit = omit,
        disability_description: str | Omit = omit,
        disability_status: Literal["disabled", "non_disabled"] | Omit = omit,
        email: str | Omit = omit,
        emergency_contact: employee_update_params.EmergencyContact | Omit = omit,
        employee_payroll: employee_update_params.EmployeePayroll | Omit = omit,
        employee_type: Literal["officer", "owner", "regular", "statutory"] | Omit = omit,
        employment_status: Literal["full_time", "part_time"] | Omit = omit,
        ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
        | Omit = omit,
        fax: str | Omit = omit,
        first_name: str | Omit = omit,
        hired_date: Union[str, date] | Omit = omit,
        i9_on_file_status: Literal["on_file", "not_on_file"] | Omit = omit,
        is_active: bool | Omit = omit,
        job_title: str | Omit = omit,
        key_employee_status: Literal["key_employee", "non_key_employee"] | Omit = omit,
        last_name: str | Omit = omit,
        middle_name: str | Omit = omit,
        military_status: Literal["active", "reserve"] | Omit = omit,
        mobile: str | Omit = omit,
        note: str | Omit = omit,
        original_hire_date: Union[str, date] | Omit = omit,
        overtime_exempt_status: Literal["exempt", "non_exempt"] | Omit = omit,
        pager: str | Omit = omit,
        pager_pin: str | Omit = omit,
        phone: str | Omit = omit,
        print_as: str | Omit = omit,
        salutation: str | Omit = omit,
        supervisor_id: str | Omit = omit,
        target_bonus: str | Omit = omit,
        termination_date: Union[str, date] | Omit = omit,
        us_citizenship_status: Literal["citizen", "non_citizen"] | Omit = omit,
        us_veteran_status: Literal["veteran", "non_veteran"] | Omit = omit,
        work_authorization_expiration_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Updates an employee record, allowing you to revise contact details, employment
        status dates, supervisory assignments, payroll configuration, and additional
        notes to keep workforce data current.

        Args:
          id: The QuickBooks-assigned unique identifier of the employee to update.

          revision_number: The current QuickBooks-assigned revision number of the employee object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

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
              tracking activities.

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
    ) -> EmployeeListResponse:
        """Returns a list of employees.

        NOTE: QuickBooks Desktop does not support
        pagination for employees; hence, there is no `cursor` parameter. Users typically
        have few employees.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific employees by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              employees. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all employees without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because employees typically have low record counts.

          name_contains: Filter for employees whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for employees whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for employees whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific employees by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an employee.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for employees whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for employees whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for employees that are active, inactive, or both.

          updated_after: Filter for employees updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for employees updated on or before this date/time. Accepts the following
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
        return await self._get(
            "/quickbooks-desktop/employees",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
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
