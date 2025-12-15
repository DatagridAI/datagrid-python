# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServiceAccountCreateParams"]


class ServiceAccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the service account.

    Your organization's domain will automatically be prepended to the service
    account name. The name must only include letters (a-z, A-Z), numbers (0-9), and
    hyphens (-), and must be between 6 and 30 characters long.
    """

    type: Required[Literal["gcp"]]
    """The type of service account, currently only `gcp` is supported."""
