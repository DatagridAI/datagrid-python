# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Skill"]


class Skill(BaseModel):
    id: str
    """Unique identifier for the skill."""

    account_id: Optional[str] = None
    """The account (company) that owns this skill.

    `null` for `user`-scope and `builtin` skills.
    """

    builtin_key: Optional[str] = None
    """
    For company overrides of built-in skills: the identifier of the underlying
    built-in. `null` for user-authored skills.
    """

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

    created_at: datetime
    """ISO timestamp when this skill was created."""

    creator_id: Optional[str] = None
    """ID of the user who created this skill.

    `null` for built-in skills that have never been edited.
    """

    description: str
    """Short description shown in the skill picker."""

    enabled: bool
    """Whether the skill is active and available for selection."""

    instructions: str
    """The full instructions / system prompt for this skill."""

    name: str
    """Display name of the skill."""

    object: Literal["skill"]
    """The object type, always 'skill'."""

    preferred_tools: List[str]
    """Tool identifiers that this skill works best with."""

    promoted_at: Optional[datetime] = None
    """ISO timestamp when this skill was promoted to company scope.

    `null` for `user`-scope skills.
    """

    required_tools: List[str]
    """Tool identifiers that this skill requires to function."""

    scope: Literal["user", "account", "builtin"]
    """Ownership scope.

    `user` = private (author only), `account` = company-owned, `builtin` = global
    default.
    """

    slash_key: str
    """The slash command key used to invoke this skill (e.g. `budget-check`)."""

    updated_at: datetime
    """ISO timestamp when this skill was last updated."""
