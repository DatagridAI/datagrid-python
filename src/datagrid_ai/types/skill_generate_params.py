# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["SkillGenerateParams"]


class SkillGenerateParams(TypedDict, total=False):
    file_ids: SequenceNotStr[str]
    """IDs of previously uploaded files to use as source material (e.g.

    SOP documents). Obtain file IDs via `POST /v1/files`. At least one of `prompt`
    or `file_ids` must be non-empty.
    """

    prompt: str
    """Natural-language description of the skill(s) to generate.

    At least one of `prompt` or `file_ids` must be non-empty.
    """
