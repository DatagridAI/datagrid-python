# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tool_def import ToolDef
from .conversations.message import Message

__all__ = [
    "ConverseResponse",
    "ConverseResponseDelegation",
    "ConverseResponseReasoning",
    "ConverseResponseSkill",
    "ConverseResponseToolCall",
]


class ConverseResponseDelegation(BaseModel):
    """A delegation call to a specialist agent that finished.

    A delegation still running when the turn ends is not listed.
    """

    id: str
    """Identifies the delegation. Matches the `id` of its `delegation` events."""

    agent_id: str
    """The ID of the specialist agent."""

    agent_name: str
    """The name of the specialist agent."""

    credits_consumed: Optional[float] = None
    """Credits the specialist's run consumed. Null when the run reported no charge."""

    elapsed_ms: Optional[float] = None
    """How long the specialist's run took, in milliseconds.

    Null when it was not measured.
    """

    is_partial: bool
    """
    True when the specialist's text was salvaged mid-run rather than returned in
    full.
    """

    status: Literal["completed", "failed", "timed_out", "budget_exhausted", "cancelled"]
    """
    Why the run ended: `completed`, or a failure (`failed`, `timed_out`,
    `budget_exhausted`, `cancelled`). `cancelled` means the user or host stopped the
    run.
    """


class ConverseResponseReasoning(BaseModel):
    id: str
    """The ID of the reasoning step."""

    status: Literal["in_progress", "completed", "failed", "cancelled"]
    """The current status of the reasoning step.

    `cancelled` when the conversation was stopped while the step was in progress.
    """

    type: Literal["reasoning"]
    """The type of the delta, which is always reasoning."""

    executed_in_parallel: Optional[bool] = None
    """Whether this reasoning step was executed in parallel with other steps."""

    execution_time_ms: Optional[float] = None
    """The execution time of the reasoning step in milliseconds."""

    output: Optional[str] = None
    """The output of the reasoning step.

    Only present when status is completed or failed.
    """

    task: Optional[str] = None
    """The task description for this reasoning step."""


class ConverseResponseSkill(BaseModel):
    """A skill that was force-activated for this turn."""

    id: str
    """The unique identifier of the skill."""

    name: str
    """The human-readable name of the skill."""

    scope: Literal["account", "builtin"]
    """The visibility scope of the skill.

    `user` (private) never appears here: `skill_ids` and `slash_keys` can only name
    account-shared or builtin skills.
    """

    slash_key: str
    """The slash key used to invoke the skill (without leading slash)."""


class ConverseResponseToolCall(BaseModel):
    id: str
    """The ID of the tool call."""

    status: Literal["in_progress", "completed", "failed", "cancelled"]
    """The status of the tool call.

    `cancelled` when the conversation was stopped while the tool call was in
    progress.
    """

    tool: ToolDef
    """The `Tool` object represents a tool that can be used by agents."""

    type: Literal["tool_call"]

    executed_in_parallel: Optional[bool] = None
    """Whether this tool call was executed in parallel with other tool calls."""

    output: Optional[str] = None
    """The output of the tool call."""


class ConverseResponse(Message):
    """The `conversation.message` object represents a message in a conversation."""

    chat_mode: Optional[Literal["full_agent", "light_agent", "llm_router"]] = None
    """
    The chat mode used for this response (web app: Execute = full_agent, Extended =
    light_agent, Ask = llm_router). Auto mode currently runs and reports as Execute
    (full_agent). A turn that runs on the orchestrator agent always runs and reports
    as full_agent, whatever `chat_mode` was requested.
    """

    delegations: Optional[List[ConverseResponseDelegation]] = None
    """Each delegation the orchestrator made on this turn, in the order they finished.

    One entry per delegation call, not per specialist run: a message sent to a
    specialist that is still running is its own entry, and only the entry that ended
    the run carries its `credits_consumed`. `credits.consumed` includes what they
    consumed. Null when no delegation finished, and on turns that do not run on the
    orchestrator agent.
    """

    generated_title: Optional[str] = None
    """Auto-generated conversation title for this turn.

    Null when title generation does not run or fails.
    """

    reasoning: Optional[List[ConverseResponseReasoning]] = None
    """Array of reasoning steps that occurred during this response.

    Only includes steps with status completed or failed.
    """

    skills: Optional[List[ConverseResponseSkill]] = None
    """
    Array of skills that were force-activated for this turn via `skill_ids` or
    `slash_keys`. Null when no skills were explicitly requested, or when none of the
    requested skills survived resolution for this turn.
    """

    tool_calls: Optional[List[ConverseResponseToolCall]] = None
    """Array of tool calls that were executed during this response."""
