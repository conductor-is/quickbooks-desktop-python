# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndUserDeleteResponse"]


class EndUserDeleteResponse(BaseModel):
    id: str
    """The ID of the deleted end-user."""

    deleted: bool
    """Indicates whether the end-user was deleted."""

    object_type: Literal["end_user"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"end_user"`."""
