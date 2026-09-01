# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["McpServerStartOAuthParams"]


class McpServerStartOAuthParams(TypedDict, total=False):
    redirect_uri: Required[str]
    """OAuth redirect URI.

    HTTPS is required except for loopback (`http://localhost`, `http://127.0.0.1`,
    `http://[::1]`).
    """
