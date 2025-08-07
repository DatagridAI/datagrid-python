# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the secret"""

    value: Required[str]
    """The secret value to store"""
