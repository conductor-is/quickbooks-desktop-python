# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .report import Report

__all__ = ["ReportPayrollSummaryResponse"]


class ReportPayrollSummaryResponse(Report):
    category: Literal["payroll_summary"]  # type: ignore

    report_type: Literal["employee_earnings_summary", "payroll_liability_balances", "payroll_summary"] = FieldInfo(
        alias="reportType"
    )  # type: ignore

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
