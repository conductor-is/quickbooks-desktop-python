# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndUser", "IntegrationConnection"]


class IntegrationConnection(BaseModel):
    id: str
    """The unique identifier for this integration connection."""

    created_at: str = FieldInfo(alias="createdAt")
    """The date and time when this integration connection record was created."""

    integration_slug: Literal["quickbooks_desktop"] = FieldInfo(alias="integrationSlug")
    """The identifier of the third-party platform to integrate."""

    last_request_at: Optional[str] = FieldInfo(alias="lastRequestAt", default=None)
    """The date and time of your last API request to this integration connection."""

    last_successful_request_at: Optional[str] = FieldInfo(alias="lastSuccessfulRequestAt", default=None)
    """
    The date and time of your last _successful_ API request to this integration
    connection. A successful request means the integration fully processed and
    returned a response without any errors end-to-end.
    """

    object_type: Literal["integration_connection"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"integration_connection"`."""


class EndUser(BaseModel):
    id: str
    """The unique identifier for this end-user.

    You must save this value to your database because it is how you identify which
    of your users to receive your API requests.
    """

    company_name: str = FieldInfo(alias="companyName")
    """The end-user's company name that will be shown elsewhere in Conductor."""

    created_at: str = FieldInfo(alias="createdAt")
    """The date and time when this end-user record was created."""

    email: str
    """The end-user's email address for identification purposes."""

    integration_connections: List[IntegrationConnection] = FieldInfo(alias="integrationConnections")
    """The end-user's integration connections."""

    object_type: Literal["end_user"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"end_user"`."""

    source_id: str = FieldInfo(alias="sourceId")
    """The end-user's unique identifier from your system.

    Maps users between your database and Conductor.
    """
