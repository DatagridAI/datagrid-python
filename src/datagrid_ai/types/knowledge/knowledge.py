# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "Knowledge",
    "Credits",
    "LastError",
    "Parent",
    "ParentParentPage",
    "ParentRootPage",
    "RowCounts",
    "Sync",
    "SyncTrigger",
]


class Credits(BaseModel):
    """Credit consumption for this knowledge.

    `null` when the knowledge is still being processed and the final cost is not yet known (e.g. immediately after creation or reindexing), or when the credit lookup fails. When present, `consumed` is the current summed spend for the knowledge's active tables — it is not necessarily the cost of the most recent request, nor the full lifetime spend.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class LastError(BaseModel):
    """The last terminal processing error for this knowledge, if any.

    Present when the latest asynchronous processing or re-index run ended unsuccessfully; `null` when the knowledge is `failed` only because every row ended in a persistent failed state.
    """

    code: Literal["out_of_credits", "unauthorized", "processing_error"]
    """A machine-readable error code for the most recent terminal processing failure."""

    message: str
    """A human-readable description of the most recent terminal processing failure."""


class ParentParentPage(BaseModel):
    """The parent page reference, indicating where this page is nested"""

    page_id: str
    """The ID of the parent page. Required when type is 'page'"""

    type: Literal["page"]
    """The type of parent. 'page' indicates nested under a specific page"""


class ParentRootPage(BaseModel):
    """The root level object"""

    type: Literal["root"]
    """The type of parent. 'root' indicates at the root level"""


Parent: TypeAlias = Union[ParentParentPage, ParentRootPage]


class RowCounts(BaseModel):
    """Row count statistics for the knowledge."""

    completed: float
    """The number of rows successfully learned."""

    failed: float
    """The number of rows that failed to be processed for learning."""

    total: float
    """The total number of rows in the knowledge."""


class SyncTrigger(BaseModel):
    """A cron-based schedule for syncing data"""

    cron_expression: str
    """Cron expression (e.g., '0 0 \\** \\** \\**' for daily at midnight)"""

    type: Literal["cron"]
    """The trigger type, which is always `cron`."""

    description: Optional[str] = None
    """Human-readable description of the schedule"""

    timezone: Optional[str] = None
    """IANA timezone (e.g., 'America/New_York'). Defaults to 'UTC' if not provided."""


class Sync(BaseModel):
    """Sync information for knowledge that syncs data from a connection"""

    connection_id: str
    """The ID of the connection used for syncing data to this knowledge"""

    enabled: bool
    """Whether data syncing from the connection is enabled"""

    trigger: Optional[SyncTrigger] = None
    """A cron-based schedule for syncing data"""


class Knowledge(BaseModel):
    """
    The `knowledge` object represents knowledge that an agent may leverage to respond.
    """

    id: str
    """The knowledge identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the knowledge was created."""

    credits: Optional[Credits] = None
    """Credit consumption for this knowledge.

    `null` when the knowledge is still being processed and the final cost is not yet
    known (e.g. immediately after creation or reindexing), or when the credit lookup
    fails. When present, `consumed` is the current summed spend for the knowledge's
    active tables — it is not necessarily the cost of the most recent request, nor
    the full lifetime spend.
    """

    last_error: Optional[LastError] = None
    """The last terminal processing error for this knowledge, if any.

    Present when the latest asynchronous processing or re-index run ended
    unsuccessfully; `null` when the knowledge is `failed` only because every row
    ended in a persistent failed state.
    """

    name: str
    """The name of the knowledge."""

    object: Literal["knowledge"]
    """The object type, which is always `knowledge`."""

    parent: Parent
    """The parent object, indicating where the object is located in the hierarchy"""

    row_counts: RowCounts
    """Row count statistics for the knowledge."""

    scope: Literal["teamspace", "organization"]
    """The visibility scope of the knowledge.

    'teamspace' means visible only within the owning teamspace. 'organization' means
    visible across all teamspaces in the same organization.
    """

    status: Literal["pending", "partial", "ready", "failed"]
    """The current knowledge status.

    `pending` indicates that processing has started but no rows have been learned
    yet. `partial` indicates that some rows are available, but processing is either
    still running or ended with incomplete results. `ready` indicates that
    processing finished successfully and the knowledge is fully available. `failed`
    indicates that no rows are currently available and the knowledge reached a
    terminal failure state, either because the latest asynchronous processing or
    re-index run ended unsuccessfully before any rows became available, or because
    every row ended in a persistent failed state.
    """

    sync: Optional[Sync] = None
    """Sync information for knowledge that syncs data from a connection"""

    teamspace_id: str
    """The ID of the teamspace that owns this knowledge."""

    updated_at: Optional[datetime] = None
    """The ISO string for when the knowledge was last updated."""
