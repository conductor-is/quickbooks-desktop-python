# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomFieldDefinitionDeleteResponse"]


class CustomFieldDefinitionDeleteResponse(BaseModel):
    id: str
    """The identifier of the deleted custom field definition, which is its `name`."""

    deleted: bool
    """Indicates whether the custom field definition was deleted."""

    name: str
    """The name of the deleted custom field definition."""

    object_type: Literal["qbd_custom_field_definition"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_custom_field_definition"`."""

    owner_id: str = FieldInfo(alias="ownerId")
    """The owner of the deleted custom field definition."""
