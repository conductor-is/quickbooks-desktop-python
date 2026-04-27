# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BillCreditCardPaymentVoidResponse"]


class BillCreditCardPaymentVoidResponse(BaseModel):
    id: str
    """
    The QuickBooks-assigned unique identifier of the voided bill credit card
    payment.
    """

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """
    The date and time when this bill credit card payment was created, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss+hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """

    object_type: Literal["qbd_bill_credit_card_payment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill_credit_card_payment"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the voided bill credit card
    payment.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """
    The date and time when this bill credit card payment was last updated, in ISO
    8601 format (YYYY-MM-DDThh:mm:ss+hh:mm), which QuickBooks Desktop interprets in
    the local timezone of the end-user's computer.
    """

    voided: bool
    """Indicates whether the bill credit card payment was voided."""
