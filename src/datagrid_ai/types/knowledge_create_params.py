# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["KnowledgeCreateParams"]


class KnowledgeCreateParams(TypedDict, total=False):
    connection_id: Optional[str]
    """The id of the connection to be used to create the knowledge."""

    files: Optional[List[FileTypes]]
    """The files to be uploaded and learned.

    Supported media types are `pdf`, `json`, `csv`, `text`, `png`, `jpeg`, `excel`,
    `google sheets`.
    """

    name: Optional[str]
    """The name of the knowledge."""
