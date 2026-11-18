# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgenticAutomation", "Scheduled"]


class Scheduled(BaseModel):
    cron: str
    """Five-field cron expression the automation fires on."""

    cron_description: Optional[str] = None
    """Human-readable reading of `cron`, when one is stored."""

    destination_id: Optional[str] = None
    """Datagrid conversation destination id, when one is stored."""

    destination_type: Optional[str] = None
    """Datagrid conversation destination, when one is stored."""

    thread_mode: Optional[str] = None
    """How the run's conversation is reused, when one is stored."""

    timezone: str
    """IANA timezone `cron` is interpreted in."""


class AgenticAutomation(BaseModel):
    id: str
    """Unique identifier for the automation."""

    agent_id: str
    """The ID of the agent this automation runs."""

    app_event: Optional[object] = None
    """App-event fields. Null for a scheduled automation."""

    created_at: datetime
    """ISO 8601 timestamp of when the automation was created."""

    creator_user_id: str
    """The user who created the automation."""

    description: Optional[str] = None
    """Free-text description of what this automation does."""

    enabled: bool
    """Whether the automation is active. When `false` the schedule is paused."""

    kind: Literal["scheduled"]
    """What the automation is. `scheduled` for this route."""

    last_run_at: Optional[datetime] = None
    """ISO 8601 timestamp of the latest run. Null until a run exists."""

    last_updated_by_id: str
    """The user who last updated the automation."""

    name: str
    """Human-readable name of the automation."""

    object: Literal["agentic_automation"]
    """The object type, always 'agentic_automation'."""

    output_channel_id: Optional[str] = None
    """Additional delivery address, when one is stored. Not set by this route."""

    output_channel_type: Optional[str] = None
    """Additional delivery transport, when one is stored. Not set by this route."""

    scheduled: Scheduled

    updated_at: datetime
    """ISO 8601 timestamp of the last modification."""
