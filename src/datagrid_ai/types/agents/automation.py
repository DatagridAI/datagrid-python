# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Automation"]


class Automation(BaseModel):
    id: str
    """Unique identifier for the automation."""

    created_at: datetime
    """ISO 8601 timestamp of when the automation was created."""

    cron: Optional[str] = None
    """Five-field cron expression controlling when the automation fires (e.g.

    `"0 9 * * 1"` = every Monday at 09:00). Seconds are not supported. Must have a
    minimum inter-fire interval of 15 minutes.
    """

    description: Optional[str] = None
    """Optional free-text description of what this automation does."""

    enabled: bool
    """Whether the automation is active.

    When `false` the cron trigger is paused and no runs are scheduled until it is
    re-enabled.
    """

    name: str
    """Human-readable name of the automation."""

    object: Literal["automation"]
    """The object type, always 'automation'."""

    prompt: Optional[str] = None
    """The instruction text sent to the agent each time the automation fires.

    Supports Markdown.
    """

    thread_mode: Optional[Literal["new_thread", "same_conversation"]] = None
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

    timezone: Optional[str] = None
    """IANA timezone identifier in which `cron` is interpreted (e.g.

    `"America/New_York"`, `"UTC"`). Defaults to `"UTC"` when not provided on create.
    """

    destination_id: Optional[str] = None
    """The channel ID or user ID that identifies the destination.

    Required when `destination_type` is `channel` or `user_dm`; omit for `agent_dm`.
    """

    destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]] = None
    """Where the automation's conversation runs and results are delivered.

    - `agent_dm` — (default) Results are posted in the agent's own DM space. No
      `destination_id` is required.
    - `channel` — Results are posted in a specific Datagrid channel. Provide the
      channel ID in `destination_id`.
    - `user_dm` — Results are sent as a direct message to a specific user. Provide
      the user ID in `destination_id`.
    """

    notification_preference: Optional[Literal["always", "on_failure", "never"]] = None
    """Controls when users are notified about automation run outcomes.

    - `always` — Notify after every run regardless of success or failure. -
      `on_failure` — (default) Notify only when a run fails or produces an error.
    - `never` — Do not send notifications for this automation.
    """

    output_channel_id: Optional[str] = None
    """
    ID of an additional delivery channel (Slack channel, Teams channel, email
    address, etc.) where automation results are also posted.
    """

    output_channel_type: Optional[str] = None
    """The transport type of the output channel.

    One of `"email"`, `"slack"`, `"teams"`, `"sms"`.
    """

    prompt_file_ids: Optional[List[str]] = None
    """IDs of files attached to the automation prompt.

    These files are provided as context to the agent on every run.
    """

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp of the last modification."""
