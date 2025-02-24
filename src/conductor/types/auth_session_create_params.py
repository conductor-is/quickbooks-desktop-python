# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthSessionCreateParams"]


class AuthSessionCreateParams(TypedDict, total=False):
    end_user_id: Required[Annotated[str, PropertyInfo(alias="endUserId")]]
    """The ID of the end-user for whom to create the integration connection."""

    publishable_key: Required[Annotated[str, PropertyInfo(alias="publishableKey")]]
    """
    Your Conductor publishable key, which we use to create the auth session's
    `authFlowUrl`.
    """

    link_expiry_mins: Annotated[float, PropertyInfo(alias="linkExpiryMins")]
    """The number of minutes after which the auth session will expire.

    Must be at least 15 minutes and no more than 7 days. If not provided, defaults
    to 30 minutes.
    """

    redirect_url: Annotated[str, PropertyInfo(alias="redirectUrl")]
    """
    The URL to which Conductor will redirect the end-user to return to your app
    after they complete the authentication flow. If not provided, their browser tab
    will close instead.
    """
