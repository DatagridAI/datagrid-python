# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .agent_event_trigger import AgentEventTrigger

__all__ = ["EventTriggerUpdateResponse", "EventTriggerUpdateResponseWarning"]


class EventTriggerUpdateResponseWarning(BaseModel):
    code: str
    """Stable machine-readable identifier for the warning (e.g.

    `procore_not_connected`, `registration_failed`). Safe to branch on without
    parsing `message`.
    """

    message: str
    """Human-readable explanation of the warning."""


class EventTriggerUpdateResponse(AgentEventTrigger):
    warnings: List[EventTriggerUpdateResponseWarning]
    """Non-fatal issues surfaced while wiring up the trigger (e.g.

    Procore company/project/credential prerequisite gaps). An empty array means the
    trigger was configured with no issues. Each entry pairs a stable
    machine-readable `code` with a human-readable `message`.
    """
