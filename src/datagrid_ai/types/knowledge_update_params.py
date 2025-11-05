# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["KnowledgeUpdateParams"]


class KnowledgeUpdateParams(TypedDict, total=False):
    files: Optional[SequenceNotStr[FileTypes]]
    """The files to replace existing knowledge.

    When provided, all existing data will be removed from the knowledge and replaced
    with these files. Supported media types are `pdf`, `json`, `csv`, `text`, `png`,
    `jpeg`, `excel`, `google sheets`, `docx`, `pptx`.
    """

    name: Optional[str]
    """The new name for the `knowledge`."""
