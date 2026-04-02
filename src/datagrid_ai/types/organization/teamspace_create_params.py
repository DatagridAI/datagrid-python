# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamspaceCreateParams"]


class TeamspaceCreateParams(TypedDict, total=False):
    access: Required[Literal["open", "closed"]]
    """Open teamspaces allow all organization members to join without admin approval.

    Access for users who join this way is limited to conversations with agents in
    this teamspace.

    Closed teamspaces require admin approval to join.
    """

    name: Required[str]
    """The name of the teamspace"""

    cloud_provider: Optional[Literal["aws", "gcp"]]
    """Cloud provider for this teamspace.

    Determines storage (S3/GCS) and model providers (Bedrock/Vertex). Immutable
    after creation. Defaults to `gcp` if not specified.
    """
