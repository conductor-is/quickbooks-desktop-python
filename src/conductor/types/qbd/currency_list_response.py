# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .currency import Currency
from ..._models import BaseModel

__all__ = ["CurrencyListResponse"]


class CurrencyListResponse(BaseModel):
    data: List[Currency]
    """The array of currencies."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
