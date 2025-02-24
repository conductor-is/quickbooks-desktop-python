# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthSession"]


class AuthSession(BaseModel):
    id: str
    """The unique identifier for this auth session."""

    auth_flow_url: str = FieldInfo(alias="authFlowUrl")
    """
    The URL of the authentication flow that you will pass to your client for your
    user to set up their integration connection.
    """

    client_secret: str = FieldInfo(alias="clientSecret")
    """The secret used in `authFlowUrl` to securely access the authentication flow."""

    created_at: str = FieldInfo(alias="createdAt")
    """The date and time when this auth session record was created."""

    end_user_id: str = FieldInfo(alias="endUserId")
    """The ID of the end-user for whom to create an integration connection."""

    expires_at: str = FieldInfo(alias="expiresAt")
    """The date and time when this auth session expires.

    By default, this value is 30 minutes from creation. You can extend this time by
    setting `linkExpiryMins` when creating the auth session.
    """

    object_type: Literal["auth_session"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"auth_session"`."""

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)
    """
    The URL to which Conductor will redirect your user to return to your app after
    they complete the authentication flow. If `null`, their browser tab will close
    instead.
    """
