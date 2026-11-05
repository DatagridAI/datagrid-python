# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tool_def import ToolDef
from .conversations.message import Message

__all__ = ["ConverseResponse", "ConverseResponseReasoning", "ConverseResponseSkill", "ConverseResponseToolCall"]


class ConverseResponseReasoning(BaseModel):
    id: str
    """The ID of the reasoning step."""

    status: Literal["in_progress", "completed", "failed"]
    """The current status of the reasoning step."""

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

    status: Literal["in_progress", "completed", "failed"]

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
    (full_agent).
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
