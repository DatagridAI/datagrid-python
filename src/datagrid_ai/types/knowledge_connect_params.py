# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KnowledgeConnectParams"]


class KnowledgeConnectParams(TypedDict, total=False):
    connection_id: Required[str]
    """The id of the connection to be used to create the knowledge."""
