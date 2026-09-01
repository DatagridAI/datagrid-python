# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["McpServerHandleOAuthCallbackParams"]


class McpServerHandleOAuthCallbackParams(TypedDict, total=False):
    code: Required[str]
    """Authorization code returned by the OAuth authorization server on the callback."""

    redirect_uri: Required[str]
    """The same `redirect_uri` passed to `start-oauth`.

    HTTPS is required except for loopback (`http://localhost`, `http://127.0.0.1`,
    `http://[::1]`).
    """

    state: Required[str]
    """The `state` value the OAuth authorization server echoed on the callback.

    Must match the value returned from `start-oauth`.
    """
