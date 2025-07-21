# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .employee import Employee
from ..._models import BaseModel

__all__ = ["EmployeeListResponse"]


class EmployeeListResponse(BaseModel):
    data: List[Employee]
    """The array of employees."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
