# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    category: Required[
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

    instructions: Required[str]
    """The full instructions / system prompt for this skill."""

    name: Required[str]
    """Display name of the skill."""

    slash_key: Required[str]
    """The slash command key (e.g. `budget-check`). Must be unique within the scope."""

    description: Optional[str]
    """Short description.

    When omitted, an AI-generated description is produced from the instructions.
    """

    enabled: Optional[bool]
    """Whether the skill is active. Defaults to `true`."""

    preferred_tools: Optional[SequenceNotStr[str]]
    """Tool identifiers preferred by this skill."""

    required_tools: Optional[SequenceNotStr[str]]
    """Tool identifiers required by this skill."""

    scope: Optional[Literal["user", "account"]]
    """Ownership of the new skill.

    Defaults to `account` (company-owned). Pass `user` for a private skill that can
    later be promoted.
    """
