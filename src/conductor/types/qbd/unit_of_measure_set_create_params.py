# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UnitOfMeasureSetCreateParams", "BaseUnit", "DefaultUnit", "RelatedUnit"]


class UnitOfMeasureSetCreateParams(TypedDict, total=False):
    base_unit: Required[Annotated[BaseUnit, PropertyInfo(alias="baseUnit")]]
    """The unit-of-measure set's base unit used to track and price item quantities.

    If the company file is enabled for a single unit of measure per item, the base
    unit is the only unit available on transaction line items. If enabled for
    multiple units per item, the base unit is the default unless overridden by the
    set's default units.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this unit-of-measure set, unique across all
    unit-of-measure sets. To ensure this set appears in the QuickBooks UI for
    companies configured with a single unit per item, prefix the name with "By the"
    (e.g., "By the Barrel").

    **NOTE**: Unit-of-measure sets do not have a `fullName` field because they are
    not hierarchical objects, which is why `name` is unique for them but not for
    objects that have parents.

    Maximum length: 31 characters.
    """

    unit_of_measure_type: Required[
        Annotated[
            Literal["area", "count", "length", "other", "time", "volume", "weight"],
            PropertyInfo(alias="unitOfMeasureType"),
        ]
    ]
    """The unit-of-measure set's type.

    Use "other" for a custom type defined in QuickBooks.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    default_units: Annotated[Iterable[DefaultUnit], PropertyInfo(alias="defaultUnits")]
    """
    The unit-of-measure set's default units to appear in the U/M field on
    transaction line items. You can specify separate defaults for purchases, sales,
    and shipping.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this unit-of-measure set is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    related_units: Annotated[Iterable[RelatedUnit], PropertyInfo(alias="relatedUnits")]
    """
    The unit-of-measure set's related units, each specifying how many base units
    they represent (conversion ratio).
    """


class BaseUnit(TypedDict, total=False):
    """The unit-of-measure set's base unit used to track and price item quantities.

    If the company file is enabled for a single unit of measure per item, the base unit is the only unit available on transaction line items. If enabled for multiple units per item, the base unit is the default unless overridden by the set's default units.
    """

    abbreviation: Required[str]
    """
    The base unit's short identifier shown in the QuickBooks U/M field on
    transaction line items.

    Maximum length: 31 characters.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this base unit, unique across all base
    units.

    **NOTE**: Base units do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """


class DefaultUnit(TypedDict, total=False):
    unit: Required[str]
    """The unit name for this default unit, as displayed in the U/M field.

    If the company file is enabled for multiple units per item, this appears as an
    available unit for the item. Must correspond to the base unit or a related unit
    defined in this set.

    Maximum length: 31 characters.
    """

    unit_used_for: Required[Annotated[Literal["purchase", "sales", "shipping"], PropertyInfo(alias="unitUsedFor")]]
    """
    Where this default unit is used as the default: purchase line items, sales line
    items, or shipping lines.
    """


class RelatedUnit(TypedDict, total=False):
    abbreviation: Required[str]
    """
    The related unit's short identifier shown in the QuickBooks U/M field on
    transaction line items.

    Maximum length: 31 characters.
    """

    conversion_ratio: Required[Annotated[str, PropertyInfo(alias="conversionRatio")]]
    """The number of base units in this related unit, represented as a decimal string.

    For example, if the base unit is "box" and this related unit is "case" with
    `conversionRatio` = "10", that means there are 10 boxes in one case.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this related unit, unique across all related
    units.

    **NOTE**: Related units do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """
