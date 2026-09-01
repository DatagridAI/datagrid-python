# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StartMcpOAuthResponse"]


class StartMcpOAuthResponse(BaseModel):
    authorization_url: str
    """
    URL to redirect the end user to so they can complete the OAuth authorization
    consent.
    """

    object: Literal["mcp_oauth_start"]

    state: str
    """
    Opaque state value bound to this OAuth flow, echoed by the authorization server
    on the callback for CSRF protection.
    """
