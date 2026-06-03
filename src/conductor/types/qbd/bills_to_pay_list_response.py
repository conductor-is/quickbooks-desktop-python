# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .bill_to_pay import BillToPay

__all__ = ["BillsToPayListResponse"]


class BillsToPayListResponse(BaseModel):
    data: List[BillToPay]
    """The array of bills-to-pay records.

    Each record has either a `bill` object or a `credit` object, and the other
    branch is `null`.
    """

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
