# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .custom_field_definition import CustomFieldDefinition

__all__ = ["CustomFieldDefinitionListResponse"]


class CustomFieldDefinitionListResponse(BaseModel):
    data: List[CustomFieldDefinition]
    """The array of custom field definitions."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
