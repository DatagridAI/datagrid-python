# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Knowledge", "RowCounts", "Sync", "SyncTrigger", "Credits"]


class RowCounts(BaseModel):
    """Row count statistics for the knowledge."""

    completed: float
    """The number of rows successfully learned."""

    failed: float
    """The number of rows that failed to be processed for learning."""

    total: float
    """The total number of rows in the knowledge."""


class SyncTrigger(BaseModel):
    """The cron schedule configuration for syncing data from the connection."""

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
    """The cron schedule configuration for syncing data from the connection."""


class Credits(BaseModel):
    consumed: float
    """The number of credits consumed by the knowledge."""


class Knowledge(BaseModel):
    """
    The `knowledge` object represents knowledge that an agent may leverage to respond.
    """

    id: str
    """The knowledge identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the knowledge was created."""

    name: str
    """The name of the knowledge"""

    object: Literal["knowledge"]
    """The object type, which is always `knowledge`."""

    row_counts: RowCounts
    """Row count statistics for the knowledge."""

    status: Literal["pending", "partial", "ready"]
    """
    The current knowledge status can be one of three values: `pending`, `partial`,
    or `ready`. `pending` indicates that the knowledge is awaiting learning and will
    not be used by the agent when responding. `partial` indicates that the knowledge
    is partially learned. The agent may use some aspects of it when responding.
    `ready` indicates that the knowledge is fully learned and will be completely
    utilized in responses.
    """

    sync: Optional[Sync] = None
    """Sync information for knowledge that syncs data from a connection"""

    credits: Optional[Credits] = None

    updated_at: Optional[datetime] = None
    """The ISO string for when the knowledge was last updated."""
