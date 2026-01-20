# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["KnowledgeUpdateParams", "Parent", "ParentParentPage", "ParentRootPage", "Sync", "SyncTrigger"]


class KnowledgeUpdateParams(TypedDict, total=False):
    files: Optional[SequenceNotStr[FileTypes]]
    """The files to replace existing knowledge.

    When provided, all existing data will be removed from the knowledge and replaced
    with these files. Supported media types are `pdf`, `json`, `csv`, `text`, `png`,
    `jpeg`, `excel`, `google sheets`, `docx`, `pptx`.
    """

    name: Optional[str]
    """The new name for the `knowledge`."""

    parent: Optional[Parent]
    """Move the knowledge to a different parent page."""

    sync: Optional[Sync]
    """Sync configuration updates.

    Note: For multipart/form-data, this should be sent as a JSON string.
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


class SyncTrigger(TypedDict, total=False):
    """Update the trigger to a cron schedule.

    Only CronBasedTrigger is supported for updates.
    """

    cron_expression: Required[str]
    """Cron expression (e.g., '0 0 \\** \\** \\**' for daily at midnight)"""

    type: Required[Literal["cron"]]
    """The trigger type, which is always `cron`."""

    description: Optional[str]
    """Human-readable description of the schedule"""

    timezone: str
    """IANA timezone (e.g., 'America/New_York'). Defaults to 'UTC' if not provided."""


class Sync(TypedDict, total=False):
    """Sync configuration updates.

    Note: For multipart/form-data, this should be sent as a JSON string.
    """

    enabled: bool
    """Enable or disable syncing data from the connection"""

    trigger: SyncTrigger
    """Update the trigger to a cron schedule.

    Only CronBasedTrigger is supported for updates.
    """
