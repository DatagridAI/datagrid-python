# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventTriggerUpdateParams"]


class EventTriggerUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    description: Optional[str]
    """Updated description. Pass `null` to clear."""

    enabled: bool
    """Set to `true` to resume the trigger; `false` to pause it."""

    name: Optional[str]
    """Updated name. Pass `null` to clear."""

    response_thread: Optional[Literal["create_new_thread_each_time"]]
    """
    Controls how the agent's response conversation is threaded when the trigger
    fires. `create_new_thread_each_time` starts a fresh thread for every event; when
    omitted, responses reuse a single thread.
    """

    run_conditions: Optional[str]
    """Updated run conditions. Pass `null` to clear."""

    trigger_event: str
    """Updated event in `"ResourceName:eventType"` format.

    Omit to leave the current event unchanged.
    """
