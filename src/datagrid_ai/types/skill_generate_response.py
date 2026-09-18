# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .skill_draft import SkillDraft

__all__ = ["SkillGenerateResponse"]


class SkillGenerateResponse(BaseModel):
    data: List[SkillDraft]
    """Array of generated skill drafts. Pass each to `POST /v1/skills` to persist."""

    has_more: bool
    """Whether there are more results. Always false for generate."""

    object: Literal["list"]
    """The object type, always 'list'."""
