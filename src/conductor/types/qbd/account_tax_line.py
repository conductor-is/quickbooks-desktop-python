# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountTaxLine"]


class AccountTaxLine(BaseModel):
    tax_line_id: float = FieldInfo(alias="taxLineId")
    """The identifier of the tax line associated with this account tax line.

    You can see a list of all available values for this field by calling the
    endpoint for account tax lines.
    """

    tax_line_name: Optional[str] = FieldInfo(alias="taxLineName", default=None)
    """
    The name of the tax line associated with this account tax line, as it appears on
    the tax form.
    """
