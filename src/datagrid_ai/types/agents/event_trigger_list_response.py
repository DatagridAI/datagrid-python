# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .agent_event_trigger import AgentEventTrigger

__all__ = ["EventTriggerListResponse"]


class EventTriggerListResponse(BaseModel):
    data: List[AgentEventTrigger]
    """Array of event trigger objects for the agent (zero or one)."""

    has_more: bool
    """
    Always `false` — an agent has at most one event trigger, so results are never
    paginated.
    """

    object: Literal["list"]
    """The object type, always 'list'."""
