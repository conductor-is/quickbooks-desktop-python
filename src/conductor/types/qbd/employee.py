# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Employee",
    "AdditionalNote",
    "Address",
    "BillingRate",
    "CustomContactField",
    "CustomField",
    "EmergencyContact",
    "EmergencyContactPrimaryContact",
    "EmergencyContactSecondaryContact",
    "EmployeePayroll",
    "EmployeePayrollClass",
    "EmployeePayrollEarning",
    "EmployeePayrollEarningPayrollWageItem",
    "EmployeePayrollSickHours",
    "EmployeePayrollVacationHours",
    "Supervisor",
]


class AdditionalNote(BaseModel):
    id: float
    """The auto-incrementing identifier assigned by QuickBooks to this note."""

    date: Optional[datetime.date] = None
    """The date this note was last updated, in ISO 8601 format (YYYY-MM-DD)."""

    note: str
    """The text of this note."""


class Address(BaseModel):
    """The employee's address.

    If the company uses QuickBooks Payroll for this employee, this address must specify a complete address, including city, state, ZIP (or postal) code, and at least one line of the street address.
    """

    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the employee address."""

    country: Optional[str] = None
    """The country name of the employee address."""

    line1: Optional[str] = None
    """The first line of the employee address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the employee address, if needed (e.g., apartment, suite,
    unit, or building).
    """

    line3: Optional[str] = None
    """The third line of the employee address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the employee address, if needed."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the employee address."""

    state: Optional[str] = None
    """The U.S.

    state of the employee address. QuickBooks requires this field to be a U.S. state
    abbreviation (e.g., "CA" for California). See enum for all possible values.

    **NOTE:** This `state` field stays enum-constrained when creating or updating an
    employee because QuickBooks Desktop rejects non-standard values on input. In
    responses, though, we've seen QuickBooks return values outside its own enum
    (like 'ON'), so Conductor surfaces the raw QuickBooks string unchanged instead
    of enforcing the enum.
    """


class BillingRate(BaseModel):
    """
    The employee's billing rate, used to override service item rates in time tracking activities.
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


class CustomContactField(BaseModel):
    name: str
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Optional[str] = None
    """The value of the contact field."""


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

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
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class EmergencyContactPrimaryContact(BaseModel):
    """The employee's primary emergency contact."""

    name: str
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    relation: Optional[
        Literal["brother", "daughter", "father", "friend", "mother", "other", "partner", "sister", "son", "spouse"]
    ] = None
    """The relationship of the employee to the employee."""

    value: Optional[str] = None
    """The value of the contact field."""


class EmergencyContactSecondaryContact(BaseModel):
    """The employee's secondary emergency contact."""

    name: str
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    relation: Optional[
        Literal["brother", "daughter", "father", "friend", "mother", "other", "partner", "sister", "son", "spouse"]
    ] = None
    """The relationship of the employee to the employee."""

    value: Optional[str] = None
    """The value of the contact field."""


class EmergencyContact(BaseModel):
    """The employee's emergency contacts."""

    primary_contact: Optional[EmergencyContactPrimaryContact] = FieldInfo(alias="primaryContact", default=None)
    """The employee's primary emergency contact."""

    secondary_contact: Optional[EmergencyContactSecondaryContact] = FieldInfo(alias="secondaryContact", default=None)
    """The employee's secondary emergency contact."""


class EmployeePayrollClass(BaseModel):
    """The employee's class.

    Classes can be used to categorize objects into meaningful segments, such as department, location, or type of work. In QuickBooks, class tracking is off by default.
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


class EmployeePayrollEarningPayrollWageItem(BaseModel):
    """
    The payroll wage item that defines how this employee is paid (e.g., Regular Pay, Overtime Pay). This determines the payment scheme used for payroll calculations.
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


class EmployeePayrollEarning(BaseModel):
    payroll_wage_item: EmployeePayrollEarningPayrollWageItem = FieldInfo(alias="payrollWageItem")
    """
    The payroll wage item that defines how this employee is paid (e.g., Regular Pay,
    Overtime Pay). This determines the payment scheme used for payroll calculations.
    """

    rate: Optional[str] = None
    """The hourly rate for this employee, represented as a decimal string."""

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The hourly rate for this employee expressed as a percentage."""


class EmployeePayrollSickHours(BaseModel):
    """
    The employee's sick hours, including how sick time is accrued and the total hours accrued.
    """

    accrual_period: Optional[Literal["accrues_annually", "accrues_hourly", "accrues_per_paycheck"]] = FieldInfo(
        alias="accrualPeriod", default=None
    )
    """How frequently the employee's sick hours are accrued."""

    accrual_start_date: Optional[datetime.date] = FieldInfo(alias="accrualStartDate", default=None)
    """
    The date the employee's sick hours began to accrue, in ISO 8601 format
    (YYYY-MM-DD).
    """

    hours_accrued_per_period: Optional[str] = FieldInfo(alias="hoursAccruedPerPeriod", default=None)
    """
    The number of sick hours the employee will accrue per accrual period, in ISO
    8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
    represented as PT1H30M.
    """

    hours_available: Optional[str] = FieldInfo(alias="hoursAvailable", default=None)
    """
    The total number of sick hours currently available for the employee to use, in
    ISO 8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30
    minutes is represented as PT1H30M. Defaults to 0.
    """

    hours_used: Optional[str] = FieldInfo(alias="hoursUsed", default=None)
    """
    The number of sick hours the employee has used, in ISO 8601 format for time
    intervals (PTnHnMnS). For example, 1 hour and 30 minutes is represented as
    PT1H30M.
    """

    maximum_hours: Optional[str] = FieldInfo(alias="maximumHours", default=None)
    """
    The maximum number of sick hours the employee can accrue, in ISO 8601 format for
    time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is represented as
    PT1H30M.
    """

    resets_hours_each_year: Optional[bool] = FieldInfo(alias="resetsHoursEachYear", default=None)
    """
    Indicates whether the employee's sick hours reset to zero at the beginning of
    the new year.
    """


class EmployeePayrollVacationHours(BaseModel):
    """
    The employee's vacation hours, including how vacation time is accrued and the total hours accrued.
    """

    accrual_period: Optional[Literal["accrues_annually", "accrues_hourly", "accrues_per_paycheck"]] = FieldInfo(
        alias="accrualPeriod", default=None
    )
    """How frequently the employee's vacation hours are accrued."""

    accrual_start_date: Optional[datetime.date] = FieldInfo(alias="accrualStartDate", default=None)
    """
    The date the employee's vacation hours began to accrue, in ISO 8601 format
    (YYYY-MM-DD).
    """

    hours_accrued_per_period: Optional[str] = FieldInfo(alias="hoursAccruedPerPeriod", default=None)
    """
    The number of vacation hours the employee will accrue per accrual period, in ISO
    8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
    represented as PT1H30M.
    """

    hours_available: Optional[str] = FieldInfo(alias="hoursAvailable", default=None)
    """
    The total number of vacation hours currently available for the employee to use,
    in ISO 8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30
    minutes is represented as PT1H30M. Defaults to 0.
    """

    hours_used: Optional[str] = FieldInfo(alias="hoursUsed", default=None)
    """
    The number of vacation hours the employee has used, in ISO 8601 format for time
    intervals (PTnHnMnS). For example, 1 hour and 30 minutes is represented as
    PT1H30M.
    """

    maximum_hours: Optional[str] = FieldInfo(alias="maximumHours", default=None)
    """
    The maximum number of vacation hours the employee can accrue, in ISO 8601 format
    for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is represented
    as PT1H30M.
    """

    resets_hours_each_year: Optional[bool] = FieldInfo(alias="resetsHoursEachYear", default=None)
    """
    Indicates whether the employee's vacation hours reset to zero at the beginning
    of the new year.
    """


class EmployeePayroll(BaseModel):
    """The employee's payroll information."""

    class_: Optional[EmployeePayrollClass] = FieldInfo(alias="class", default=None)
    """The employee's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    earnings: List[EmployeePayrollEarning]
    """The employee's earnings."""

    pay_period: Optional[Literal["biweekly", "daily", "monthly", "quarterly", "semimonthly", "weekly", "yearly"]] = (
        FieldInfo(alias="payPeriod", default=None)
    )
    """How frequently this employee is paid (e.g., weekly, biweekly, monthly).

    This determines the schedule for generating paychecks.
    """

    sick_hours: Optional[EmployeePayrollSickHours] = FieldInfo(alias="sickHours", default=None)
    """
    The employee's sick hours, including how sick time is accrued and the total
    hours accrued.
    """

    use_time_data_to_create_paychecks: Optional[Literal["does_not_use_time_data", "not_set", "uses_time_data"]] = (
        FieldInfo(alias="useTimeDataToCreatePaychecks", default=None)
    )
    """
    Indicates whether this employee is using time-tracking data to create paychecks.
    """

    vacation_hours: Optional[EmployeePayrollVacationHours] = FieldInfo(alias="vacationHours", default=None)
    """
    The employee's vacation hours, including how vacation time is accrued and the
    total hours accrued.
    """


class Supervisor(BaseModel):
    """The employee's supervisor.

    Found in the "employment job details" section of the employee's record in QuickBooks.
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


class Employee(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this employee.

    This ID is unique across all employees but not across different QuickBooks
    object types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The employee's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this employee."""

    address: Optional[Address] = None
    """The employee's address.

    If the company uses QuickBooks Payroll for this employee, this address must
    specify a complete address, including city, state, ZIP (or postal) code, and at
    least one line of the street address.
    """

    adjusted_service_date: Optional[datetime.date] = FieldInfo(alias="adjustedServiceDate", default=None)
    """The adjusted service date for this employee, in ISO 8601 format (YYYY-MM-DD).

    This date accounts for previous employment periods or leaves that affect
    seniority.
    """

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The employee's alternate telephone number."""

    billing_rate: Optional[BillingRate] = FieldInfo(alias="billingRate", default=None)
    """
    The employee's billing rate, used to override service item rates in time
    tracking activities.
    """

    birth_date: Optional[datetime.date] = FieldInfo(alias="birthDate", default=None)
    """This employee's date of birth, in ISO 8601 format (YYYY-MM-DD)."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this employee was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """
    Additional custom contact fields for this employee, such as phone numbers or
    email addresses.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the employee object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    department: Optional[str] = None
    """The employee's department.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    description: Optional[str] = None
    """A description of this employee.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    disability_description: Optional[str] = FieldInfo(alias="disabilityDescription", default=None)
    """A description of this employee's disability."""

    disability_status: Optional[Literal["disabled", "non_disabled"]] = FieldInfo(alias="disabilityStatus", default=None)
    """Indicates whether this employee is disabled."""

    email: Optional[str] = None
    """The employee's email address."""

    emergency_contact: Optional[EmergencyContact] = FieldInfo(alias="emergencyContact", default=None)
    """The employee's emergency contacts."""

    employee_payroll: Optional[EmployeePayroll] = FieldInfo(alias="employeePayroll", default=None)
    """The employee's payroll information."""

    employee_type: Optional[Literal["officer", "owner", "regular", "statutory"]] = FieldInfo(
        alias="employeeType", default=None
    )
    """The employee type.

    This affects payroll taxes - a statutory employee is defined as an employee by
    statute. Note that owners/partners are typically on the "Other Names" list in
    QuickBooks, but if listed as an employee their type will be `owner`.
    """

    employment_status: Optional[Literal["full_time", "part_time"]] = FieldInfo(alias="employmentStatus", default=None)
    """Indicates whether this employee is a part-time or full-time employee."""

    ethnicity: Optional[
        Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
    ] = None
    """This employee's ethnicity."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    fax: Optional[str] = None
    """The employee's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The employee's first name."""

    gender: Optional[Literal["male", "female"]] = None
    """This employee's gender."""

    hired_date: Optional[datetime.date] = FieldInfo(alias="hiredDate", default=None)
    """The date this employee was hired, in ISO 8601 format (YYYY-MM-DD)."""

    i9_on_file_status: Optional[Literal["on_file", "not_on_file"]] = FieldInfo(alias="i9OnFileStatus", default=None)
    """Indicates whether this employee's I-9 is on file."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this employee is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The employee's job title."""

    key_employee_status: Optional[Literal["key_employee", "non_key_employee"]] = FieldInfo(
        alias="keyEmployeeStatus", default=None
    )
    """Indicates whether this employee is a key employee."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The employee's last name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The employee's middle name."""

    military_status: Optional[Literal["active", "reserve"]] = FieldInfo(alias="militaryStatus", default=None)
    """This employee's military status if they are a U.S. veteran."""

    mobile: Optional[str] = None
    """The employee's mobile phone number."""

    name: str
    """The case-insensitive unique name of this employee, unique across all employees.

    A concatenation of the employee's `firstName`, `middleName`, and `lastName`
    fields.

    **NOTE**: Employees do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    note: Optional[str] = None
    """A note or comment about this employee."""

    object_type: Literal["qbd_employee"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_employee"`."""

    original_hire_date: Optional[datetime.date] = FieldInfo(alias="originalHireDate", default=None)
    """The original hire date for this employee, in ISO 8601 format (YYYY-MM-DD)."""

    overtime_exempt_status: Optional[Literal["exempt", "non_exempt"]] = FieldInfo(
        alias="overtimeExemptStatus", default=None
    )
    """Indicates whether this employee is exempt from overtime pay.

    This classification is based on U.S. labor laws (FLSA).
    """

    pager: Optional[str] = None
    """The employee's pager number."""

    pager_pin: Optional[str] = FieldInfo(alias="pagerPin", default=None)
    """The employee's pager PIN."""

    phone: Optional[str] = None
    """The employee's primary telephone number."""

    print_as: Optional[str] = FieldInfo(alias="printAs", default=None)
    """The name to use when printing this employee from QuickBooks.

    By default, this is the same as the `name` field.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this employee object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    salutation: Optional[str] = None
    """
    The employee's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """

    ssn: Optional[str] = None
    """The employee's Social Security Number. The value can be with or without dashes.

    **NOTE**: This field cannot be changed after the employee is created.
    """

    supervisor: Optional[Supervisor] = None
    """The employee's supervisor.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    target_bonus: Optional[str] = FieldInfo(alias="targetBonus", default=None)
    """The target bonus for this employee, represented as a decimal string.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    termination_date: Optional[datetime.date] = FieldInfo(alias="terminationDate", default=None)
    """
    The date this employee's employment ended with the company, in ISO 8601 format
    (YYYY-MM-DD). This is also known as the released date or separation date.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this employee was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    us_citizenship_status: Optional[Literal["citizen", "non_citizen"]] = FieldInfo(
        alias="usCitizenshipStatus", default=None
    )
    """Indicates whether this employee is a U.S. citizen."""

    us_veteran_status: Optional[Literal["veteran", "non_veteran"]] = FieldInfo(alias="usVeteranStatus", default=None)
    """Indicates whether this employee is a U.S. veteran."""

    work_authorization_expiration_date: Optional[datetime.date] = FieldInfo(
        alias="workAuthorizationExpirationDate", default=None
    )
    """
    The date this employee's work authorization expires, in ISO 8601 format
    (YYYY-MM-DD).
    """
