# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["KnowledgeCreateParams", "Parent", "ParentParentPage", "ParentRootPage"]


class KnowledgeCreateParams(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
    """The files to be uploaded and learned.

    Supported media types are `pdf`, `json`, `csv`, `text`, `png`, `jpeg`, `excel`,
    `google sheets`, `docx`, `pptx`.
    """

    name: Optional[str]
    """The name of the knowledge."""

    parent: Optional[Parent]
    """The parent page to nest this knowledge under.

    If not provided, knowledge will be created at the root level.
    """


class ParentParentPage(TypedDict, total=False):
    """The parent page reference, indicating where this page is nested"""

    page_id: Required[str]
    """The ID of the parent page. Required when type is 'page'"""

    type: Required[Literal["page"]]
    """The type of parent. 'page' indicates nested under a specific page"""


class ParentRootPage(TypedDict, total=False):
    """The root level object"""

    type: Required[Literal["root"]]
    """The type of parent. 'root' indicates at the root level"""


Parent: TypeAlias = Union[ParentParentPage, ParentRootPage]
