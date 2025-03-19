# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Transfer", "Class", "SourceAccount", "TargetAccount"]


class Class(BaseModel):
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


class SourceAccount(BaseModel):
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


class TargetAccount(BaseModel):
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


class Transfer(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this transfer.

    This ID is unique across all transaction types.
    """

    amount: str
    """The monetary amount of this transfer, represented as a decimal string."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The transfer's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this transfer was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    memo: Optional[str] = None
    """A memo or note for this transfer."""

    object_type: Literal["qbd_transfer"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_transfer"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this transfer object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    source_account: SourceAccount = FieldInfo(alias="sourceAccount")
    """The account from which money will be transferred."""

    source_account_balance: Optional[str] = FieldInfo(alias="sourceAccountBalance", default=None)
    """The balance of the account from which money will be transferred."""

    target_account: TargetAccount = FieldInfo(alias="targetAccount")
    """The account to which money will be transferred."""

    target_account_balance: Optional[str] = FieldInfo(alias="targetAccountBalance", default=None)
    """The balance of the account to which money will be transferred."""

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this transfer, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this transfer was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
