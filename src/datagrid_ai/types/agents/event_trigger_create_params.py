# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventTriggerCreateParams"]


class EventTriggerCreateParams(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the trigger should be active immediately.

    Set to `false` to create it in a paused state.
    """

    trigger_event: Required[str]
    """The event that fires the agent, in `"ResourceName:eventType"` format (e.g.

    `"Tasks:create"`). Required even when `enabled` is `false`.
    """

    trigger_source: Required[Literal["procore", "sharepoint", "egnyte"]]
    """The external provider that emits the event."""

    description: Optional[str]
    """Optional description of what the App Event automation does."""

    name: Optional[str]
    """Optional name for the App Event automation."""

    response_thread: Optional[Literal["create_new_thread_each_time"]]
    """
    Controls how the agent's response conversation is threaded when the trigger
    fires. `create_new_thread_each_time` starts a fresh thread for every event; when
    omitted, responses reuse a single thread.
    """

    run_conditions: Optional[str]
    """
    Optional natural-language conditions that must hold for the agent to run when
    the event fires.
    """
