# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .template import Template
from ..._models import BaseModel

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    data: List[Template]
    """The array of templates."""

    has_more: bool = FieldInfo(alias="hasMore")
    """Indicates whether there are more objects to be fetched."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """
    The `nextCursor` is a pagination token returned in the response when you use the
    `limit` parameter in your request. To retrieve subsequent pages of results,
    include this token as the value of the `cursor` request parameter in your
    following API calls.

    **NOTE**: The `nextCursor` value remains constant throughout the pagination
    process for a specific list instance; continue to use the same `nextCursor`
    token in each request to fetch additional pages.
    """

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    remaining_count: Optional[float] = FieldInfo(alias="remainingCount", default=None)
    """The number of objects remaining to be fetched."""

    url: str
    """The endpoint URL where this list can be accessed."""
