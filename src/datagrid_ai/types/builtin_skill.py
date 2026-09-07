# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BuiltinSkill"]


class BuiltinSkill(BaseModel):
    builtin_key: str
    """Unique identifier for this built-in skill definition."""

    category: str
    """Category bucket."""

    description: str
    """Short description shown in the skill picker."""

    instructions: str
    """The full instructions / system prompt."""

    name: str
    """Display name."""

    object: Literal["builtin_skill"]
    """The object type, always 'builtin_skill'."""

    preferred_tools: List[str]
    """Tool identifiers preferred by this skill."""

    required_tools: List[str]
    """Tool identifiers required by this skill."""

    slash_key: str
    """The slash command key."""
