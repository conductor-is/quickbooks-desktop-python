# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .template import Template
from ..._models import BaseModel

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    data: List[Template]
    """The array of templates."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
