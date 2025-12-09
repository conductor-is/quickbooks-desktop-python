# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnitOfMeasureSet", "BaseUnit", "DefaultUnit", "RelatedUnit"]


class BaseUnit(BaseModel):
    """The unit-of-measure set's base unit used to track and price item quantities.

    If the company file is enabled for a single unit of measure per item, the base unit is the only unit available on transaction line items. If enabled for multiple units per item, the base unit is the default unless overridden by the set's default units.
    """

    abbreviation: str
    """
    The base unit's short identifier shown in the QuickBooks U/M field on
    transaction line items.
    """

    name: str
    """
    The case-insensitive unique name of this base unit, unique across all base
    units.

    **NOTE**: Base units do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """


class DefaultUnit(BaseModel):
    unit: str
    """The unit name for this default unit, as displayed in the U/M field.

    If the company file is enabled for multiple units per item, this appears as an
    available unit for the item. Must correspond to the base unit or a related unit
    defined in this set.
    """

    unit_used_for: Literal["purchase", "sales", "shipping"] = FieldInfo(alias="unitUsedFor")
    """
    Where this default unit is used as the default: purchase line items, sales line
    items, or shipping lines.
    """


class RelatedUnit(BaseModel):
    abbreviation: str
    """
    The related unit's short identifier shown in the QuickBooks U/M field on
    transaction line items.
    """

    conversion_ratio: str = FieldInfo(alias="conversionRatio")
    """The number of base units in this related unit, represented as a decimal string.

    For example, if the base unit is "box" and this related unit is "case" with
    `conversionRatio` = "10", that means there are 10 boxes in one case.
    """

    name: str
    """
    The case-insensitive unique name of this related unit, unique across all related
    units.

    **NOTE**: Related units do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """


class UnitOfMeasureSet(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this unit-of-measure set.

    This ID is unique across all unit-of-measure sets but not across different
    QuickBooks object types.
    """

    base_unit: BaseUnit = FieldInfo(alias="baseUnit")
    """The unit-of-measure set's base unit used to track and price item quantities.

    If the company file is enabled for a single unit of measure per item, the base
    unit is the only unit available on transaction line items. If enabled for
    multiple units per item, the base unit is the default unless overridden by the
    set's default units.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this unit-of-measure set was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    default_units: List[DefaultUnit] = FieldInfo(alias="defaultUnits")
    """
    The unit-of-measure set's default units to appear in the U/M field on
    transaction line items. You can specify separate defaults for purchases, sales,
    and shipping.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this unit-of-measure set is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this unit-of-measure set, unique across all
    unit-of-measure sets. To ensure this set appears in the QuickBooks UI for
    companies configured with a single unit per item, prefix the name with "By the"
    (e.g., "By the Barrel").

    **NOTE**: Unit-of-measure sets do not have a `fullName` field because they are
    not hierarchical objects, which is why `name` is unique for them but not for
    objects that have parents.
    """

    object_type: Literal["qbd_unit_of_measure_set"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_unit_of_measure_set"`."""

    related_units: List[RelatedUnit] = FieldInfo(alias="relatedUnits")
    """
    The unit-of-measure set's related units, each specifying how many base units
    they represent (conversion ratio).
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this unit-of-measure set
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    unit_of_measure_type: Literal["area", "count", "length", "other", "time", "volume", "weight"] = FieldInfo(
        alias="unitOfMeasureType"
    )
    """The unit-of-measure set's type.

    Use "other" for a custom type defined in QuickBooks.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this unit-of-measure set was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """
