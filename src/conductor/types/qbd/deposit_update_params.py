# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DepositUpdateParams", "CashBack", "Line"]


class DepositUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the deposit object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    cash_back: Annotated[CashBack, PropertyInfo(alias="cashBack")]
    """
    Cash back taken out of this deposit and recorded to another account, such as
    Petty Cash.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The deposit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international
    values. For user-defined currencies, all values are editable.
    """

    deposit_to_account_id: Annotated[str, PropertyInfo(alias="depositToAccountId")]
    """The account where the funds for this deposit will be deposited."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this deposit's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    lines: Iterable[Line]
    """
    The deposit's deposit lines, each representing either an existing payment
    selected for deposit or a manual transfer from another account into the deposit
    account.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       deposit lines for the deposit with this array. To keep any existing deposit
       lines, you must include them in this array even if they have not changed.
       **Any deposit lines not included will be removed.**

    2. To add a new deposit line, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any deposit lines, omit this field entirely to
       keep them unchanged.
    """

    memo: str
    """A memo or note for this deposit."""

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this deposit, in ISO 8601 format (YYYY-MM-DD)."""


class CashBack(TypedDict, total=False):
    """
    Cash back taken out of this deposit and recorded to another account, such as Petty Cash.
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    The account where this deposit cash-back line's cash-back amount is recorded,
    such as Petty Cash. This amount reduces the total credited to the deposit's
    destination account.
    """

    amount: str
    """
    The cash-back amount taken out of the deposit and recorded to this deposit
    cash-back line's account, represented as a decimal string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """

    memo: str
    """A memo or note for this deposit cash-back line."""


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing deposit line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new deposit lines you wish to add.
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    For a manual deposit line, the account that the funds are transferred from into
    the deposit's destination account. To deposit an existing payment instead, use
    `paymentTransactionId` and, when needed, `paymentTransactionLineId`.
    """

    amount: str
    """
    For a manual deposit line, the amount transferred from the line's account into
    the deposit's destination account, represented as a decimal string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """

    check_number: Annotated[str, PropertyInfo(alias="checkNumber")]
    """The check number of a check received for this deposit line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The deposit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """
    The customer, vendor, employee, or person on QuickBooks's "Other Names" list
    associated with this manual deposit line.
    """

    memo: str
    """A memo or note for this deposit line."""

    override_check_number: Annotated[str, PropertyInfo(alias="overrideCheckNumber")]
    """
    The check number to use for this deposit line, overriding the check number from
    the existing payment line.

    Maximum length: 11 characters.
    """

    override_class_id: Annotated[str, PropertyInfo(alias="overrideClassId")]
    """
    The class to use for this deposit line, overriding the class from the existing
    payment line.
    """

    override_memo: Annotated[str, PropertyInfo(alias="overrideMemo")]
    """
    The memo to use for this deposit line, overriding the memo from the existing
    payment line.

    Maximum length: 4095 characters.
    """

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """The deposit line's payment method (e.g., cash, check, credit card)."""

    payment_transaction_id: Annotated[str, PropertyInfo(alias="paymentTransactionId")]
    """The ID of an existing undeposited payment to include in this deposit line.

    Use the `paymentTransactionId` from a payments-to-deposit result, or the `id`
    from the original receive-payment response. If the source payment has multiple
    depositable lines and you omit `paymentTransactionLineId`, QuickBooks Desktop
    deposits only the first line.
    """

    payment_transaction_line_id: Annotated[str, PropertyInfo(alias="paymentTransactionLineId")]
    """
    The line ID for the specific undeposited payment line to include in this deposit
    line. Use the `paymentTransactionLineId` from a payments-to-deposit result. If
    the source payment has multiple depositable lines, provide this field with
    `paymentTransactionId` to choose the exact line.
    """
