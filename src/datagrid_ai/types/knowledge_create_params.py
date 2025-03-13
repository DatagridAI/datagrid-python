# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["KnowledgeCreateParams"]


class KnowledgeCreateParams(TypedDict, total=False):
    files: Required[List[FileTypes]]
    """The files to be uploaded and learned.

    Supported media types are `pdf`, `json`, `csv`, `text`, `png`, `jpeg`, `excel`,
    `google sheets`.
    """

    name: str
    """The name of the knowledge."""
