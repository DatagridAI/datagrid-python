# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["SkillUpdateParams"]


class SkillUpdateParams(TypedDict, total=False):
    category: Optional[
        Literal[
            "document_analysis",
            "construction_project_management",
            "financial_analysis",
            "estimation",
            "quality_and_safety",
            "scheduling",
            "contracts_and_legal",
            "data_and_reporting",
            "research",
            "communication",
            "general_productivity",
        ]
    ]
    """Category bucket."""

    description: Optional[str]
    """Short description.

    Pass an empty string to clear it and re-enable AI generation.
    """

    enabled: Optional[bool]
    """Whether the skill is active."""

    instructions: Optional[str]
    """The full instructions / system prompt."""

    name: Optional[str]
    """Display name of the skill."""

    preferred_tools: Optional[SequenceNotStr[str]]
    """Tool identifiers preferred by this skill."""

    required_tools: Optional[SequenceNotStr[str]]
    """Tool identifiers required by this skill."""

    slash_key: Optional[str]
    """The slash command key.

    Must use lowercase letters, digits, and single dashes, start and end with a
    letter or digit, and be unique within the scope.
    """
