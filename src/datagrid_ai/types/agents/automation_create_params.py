# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AutomationCreateParams"]


class AutomationCreateParams(TypedDict, total=False):
    cron: Required[str]
    """
    Five-field cron expression (minute hour day month day-of-week) controlling when
    the automation fires. Seconds are not supported. The schedule must fire at most
    once every 15 minutes — finer-grained expressions are rejected with a 400 error.
    """

    name: Required[str]
    """Human-readable name for the automation."""

    prompt: Required[str]
    """The instruction text sent to the agent each time the automation fires.

    Supports Markdown. This is the agent's task for the run. Must not be empty or
    whitespace-only.
    """

    description: Optional[str]
    """Optional free-text description of what this automation does."""

    destination_id: Optional[str]
    """The channel ID or user ID for the conversation destination.

    Required when `destination_type` is `channel` or `user_dm`; omit for `agent_dm`.
    """

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
    """Whether the automation should be active immediately after creation.

    Defaults to `true` when omitted or null. Set to `false` to create the automation
    in a paused state — it will not fire until explicitly enabled via the Update
    automation endpoint.
    """

    notification_preference: Optional[Literal["always", "on_failure", "never"]]
    """Controls when users are notified about automation run outcomes.

    - `always` — Notify after every run regardless of success or failure. -
      `on_failure` — (default) Notify only when a run fails or produces an error.
    - `never` — Do not send notifications for this automation.
    """

    output_channel_id: Optional[str]
    """
    ID of an additional delivery channel (Slack, Teams, email, etc.) where the
    agent's output is also delivered after each run. Must be provided together with
    `output_channel_type` — supplying one without the other is rejected with a 400
    error. This is an external transport address, not a Datagrid-owned resource —
    it's validated against the caller's own connected integrations at delivery time.
    """

    output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]]
    """Transport type of `output_channel_id`.

    One of `"email"`, `"slack"`, `"teams"`, `"sms"`. Must be provided together with
    `output_channel_id`.
    """

    prompt_file_ids: Optional[SequenceNotStr[str]]
    """IDs of files to attach as context for every run of this automation.

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
    """IANA timezone identifier in which `cron` is interpreted.

    Defaults to `"UTC"` when omitted.
    """
