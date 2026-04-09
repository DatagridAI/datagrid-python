# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["VoiceStartSessionParams", "Config", "User", "VoiceConfig"]


class VoiceStartSessionParams(TypedDict, total=False):
    agent_id: Optional[str]
    """The ID of the agent to use for the voice conversation.

    If not provided, the default agent is used.
    """

    config: Optional[Config]
    """
    Override the agent config for this voice session. Only prompt overrides are
    supported — voice sessions always use Gemini Live, so LLM model, agent model,
    planning prompt, and tool settings are not applicable.
    """

    conversation_id: Optional[str]
    """The ID of an existing conversation to continue.

    If not provided, a new conversation will be created.
    """

    ephemeral: Optional[bool]
    """
    When true, the session is ephemeral and will not save messages to conversation
    history.
    """

    file_ids: Optional[SequenceNotStr[str]]
    """Array of file IDs to attach to the voice conversation."""

    initial_context: Optional[str]
    """Optional context text for the voice session.

    When provided, the AI will start by briefly explaining this content before
    listening for user input.
    """

    initial_message: Optional[str]
    """Optional initial user message.

    When provided, the system greeting is skipped and the AI responds directly to
    this text (e.g. a suggested prompt). Takes precedence over initial_context.
    """

    knowledge_ids: Optional[SequenceNotStr[str]]
    """Array of knowledge IDs to make accessible to the agent."""

    page_ids: Optional[SequenceNotStr[str]]
    """Array of page IDs to make accessible to the agent.

    The page and all knowledge under it will be accessible.
    """

    secret_ids: Optional[SequenceNotStr[str]]
    """Array of secret IDs to include in the context."""

    user: Optional[User]
    """User information override for converse calls.

    All fields are optional - only provided fields will override the default user
    information.
    """

    voice_config: Optional[VoiceConfig]
    """Voice session configuration options."""


class Config(TypedDict, total=False):
    """
    Override the agent config for this voice session.
    Only prompt overrides are supported — voice sessions always use Gemini Live,
    so LLM model, agent model, planning prompt, and tool settings are not applicable.
    """

    custom_prompt: Optional[str]
    """Custom instructions for the AI Agent during the voice session."""

    system_prompt: Optional[str]
    """Directs your AI Agent's operational behavior during the voice session."""


class User(TypedDict, total=False):
    """User information override for converse calls.

    All fields are optional - only provided fields will override the default user information.
    """

    email: Optional[str]
    """Override the user's email for this converse call."""

    first_name: Optional[str]
    """Override the user's first name for this converse call."""

    last_name: Optional[str]
    """Override the user's last name for this converse call."""


class VoiceConfig(TypedDict, total=False):
    """Voice session configuration options."""

    input_transcription: Optional[bool]
    """Enable transcription of user input audio. Default: true."""

    output_transcription: Optional[bool]
    """Enable transcription of agent output audio. Default: true."""

    segment_max_duration_ms: Optional[float]
    """Maximum duration in milliseconds of a buffered segment before force-commit.

    Default: 180000 (3 minutes).
    """

    silence_commit_ms: Optional[float]
    """
    Duration of silence (no agent audio) in milliseconds before auto-committing a
    segment. Default: 30000 (30 seconds).
    """

    silence_discard_ratio: Optional[float]
    """Discard a segment if this fraction (0-1) of its audio is silence.

    Default: 0.9 (90% silence threshold).
    """

    voice_preset: Optional[str]
    """Voice preset to use (e.g., 'sage', 'nova', 'spark').

    If not provided, uses the agent's configured voice preset or the default.
    """
