# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgenticAutomationCreateScheduledParams"]


class AgenticAutomationCreateScheduledParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent this automation runs."""

    cron: Required[str]
    """
    Five-field cron expression (minute hour day month day-of-week) controlling when
    the automation fires. Seconds are not supported. The schedule must fire at most
    once every 15 minutes.
    """

    name: Required[str]
    """Human-readable name for the automation."""

    description: Optional[str]
    """Optional free-text description of what this automation does."""

    enabled: Optional[bool]
    """Whether the automation should be active immediately after creation.

    Defaults to `true` when omitted or null.
    """

    timezone: Optional[str]
    """IANA timezone identifier in which `cron` is interpreted.

    Defaults to `"UTC"` when omitted.
    """
