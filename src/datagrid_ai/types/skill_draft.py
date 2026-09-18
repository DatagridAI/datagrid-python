# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SkillDraft"]


class SkillDraft(BaseModel):
    category: Literal[
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
    """Category bucket for grouping in the skill picker."""

    description: str
    """Short description shown in the skill picker."""

    instructions: str
    """The full instructions / system prompt for this skill."""

    name: str
    """Suggested display name for the skill."""

    object: Literal["skill_draft"]
    """The object type, always 'skill_draft'."""

    preferred_tools: List[str]
    """Tool identifiers that this skill works best with."""

    required_tools: List[str]
    """Tool identifiers that this skill requires to function."""

    slash_key: str
    """Suggested slash command key (e.g.

    `budget-check`). Deduplicated within the draft list.
    """
