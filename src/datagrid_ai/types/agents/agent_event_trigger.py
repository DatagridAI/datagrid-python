# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentEventTrigger"]


class AgentEventTrigger(BaseModel):
    id: str
    """Unique identifier for the event trigger."""

    created_at: datetime
    """ISO 8601 timestamp of when the event trigger was created."""

    description: Optional[str] = None
    """User-provided description of what the App Event automation does."""

    enabled: bool
    """Whether the trigger is active.

    When `false` the agent does not run in response to the event until it is
    re-enabled.
    """

    name: Optional[str] = None
    """User-provided name for the App Event automation."""

    object: Literal["event_trigger"]
    """The object type, always 'event_trigger'."""

    response_thread: Optional[Literal["create_new_thread_each_time"]] = None
    """
    Controls how the agent's response conversation is threaded when the trigger
    fires. `create_new_thread_each_time` starts a fresh thread for every event; when
    omitted, responses reuse a single thread.
    """

    run_conditions: Optional[str] = None
    """
    Optional natural-language conditions that must hold for the agent to run when
    the event fires. When null, the agent runs on every matching event.
    """

    trigger_event: str
    """The event that fires the agent, in `"ResourceName:eventType"` format (e.g.

    `"Tasks:create"`, `"Project Users:update"`).
    """

    trigger_source: Literal["procore", "sharepoint"]
    """The external provider that emits the event."""

    updated_at: datetime
    """ISO 8601 timestamp of the last modification to the event trigger."""
