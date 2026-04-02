# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["McpServerCreateParams"]


class McpServerCreateParams(TypedDict, total=False):
    base_url: Required[str]
    """The HTTPS URL of the MCP server."""

    name: Required[str]

    authorization: Optional[str]
    """Raw Authorization header value (for example, 'Bearer <token>').

    Datagrid stores it as a secret and links it to this server. If both
    authorization and authorization_secret_id are provided, authorization takes
    precedence.
    """

    authorization_secret_id: Optional[str]
    """
    Secret ID containing the full Authorization header value to use when calling
    this MCP server.
    """

    icon_url: Optional[str]

    protocol_version: Optional[str]

    transport: Optional[Literal["http"]]
