# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    """An agent model or LLM that can be selected for a conversation."""

    id: str
    """
    The value to pass as `config.agent_model` (for `agent` models) or
    `config.llm_model` (for `llm` models).
    """

    available: bool
    """Whether the model runs as requested for the current user and teamspace.

    When `false`, the request is still accepted but a default model is used instead.
    """

    family: Optional[str] = None
    """The model line this LLM belongs to across versions, as a snake_case token, e.g.

    `claude_opus` or `gemini_pro`. The same family is shared by a model served on
    different platforms. Always `null` for `agent` models.
    """

    name: str
    """The display name of the model."""

    object: Literal["model"]
    """The object type, which is always `model`."""

    provider: str
    """The company that provides the model."""

    type: Literal["agent", "llm"]
    """Whether the model is an agent model or an LLM."""
