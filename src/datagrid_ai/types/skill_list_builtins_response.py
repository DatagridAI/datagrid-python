# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .builtin_skill import BuiltinSkill

__all__ = ["SkillListBuiltinsResponse"]


class SkillListBuiltinsResponse(BaseModel):
    data: List[BuiltinSkill]
    """Array of built-in skill definitions."""

    has_more: bool
    """Whether there are more results available.

    Always false for the built-in catalog.
    """

    object: Literal["list"]
    """The object type, always 'list'."""
