# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AutomationUpdateParams"]


class AutomationUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    cron: Optional[str]
    """Updated five-field cron expression.

    The same 15-minute minimum interval rule applies. Pass `null` to leave the
    schedule unchanged.
    """

    description: Optional[str]
    """Updated description."""

    destination_id: Optional[str]
    """Updated destination channel or user ID."""

    destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]]
    """Where the automation's conversation runs and results are delivered.

    - `agent_dm` — (default) Results are posted in the agent's own DM space. No
      `destination_id` is required.
    - `channel` — Results are posted in a specific Datagrid channel. Provide the
      channel ID in `destination_id`.
    - `user_dm` — Results are sent as a direct message to a specific user. Provide
      the user ID in `destination_id`.
    """

    enabled: Optional[bool]
    """Set to `true` to resume scheduling; `false` to pause.

    Pausing does not delete the automation or its history. Null is treated as unset
    (no change).
    """

    name: Optional[str]
    """Updated human-readable name for the automation."""

    notification_preference: Optional[Literal["always", "on_failure", "never"]]
    """Controls when users are notified about automation run outcomes.

    - `always` — Notify after every run regardless of success or failure. -
      `on_failure` — (default) Notify only when a run fails or produces an error.
    - `never` — Do not send notifications for this automation.
    """

    output_channel_id: Optional[str]
    """Updated output delivery channel ID.

    Must be provided together with `output_channel_type` in the resulting
    configuration — supplying one without the other is rejected with a 400 error.
    This is an external transport address, not a Datagrid-owned resource — it's
    validated against the caller's own connected integrations at delivery time.
    """

    output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]]
    """Updated transport type for the output channel.

    One of `"email"`, `"slack"`, `"teams"`, `"sms"`. Must be provided together with
    `output_channel_id` in the resulting configuration.
    """

    prompt: Optional[str]
    """Updated instruction text for the agent.

    Pass `null` to leave unchanged. Must not be empty or whitespace-only.
    """

    prompt_file_ids: Optional[SequenceNotStr[str]]
    """Updated list of file IDs to attach as context.

    Each file must exist and belong to the caller's teamspace, or the request is
    rejected with a 404 error. Limited to 20 IDs per request.
    """

    thread_mode: Optional[Literal["new_thread", "same_conversation"]]
    """
    Controls whether each scheduled run creates a fresh conversation thread or
    continues in the same persistent conversation.

    - `new_thread` — (default) Each run starts a new conversation. Results are
      isolated; the agent has no memory of prior runs unless it uses agent memory
      tools.
    - `same_conversation` — Every run appends to the same conversation thread. The
      agent sees the full history of prior runs, which is useful for incremental
      summaries or stateful workflows.
    """

    timezone: Optional[str]
    """Updated IANA timezone. Pass `null` to leave unchanged."""
