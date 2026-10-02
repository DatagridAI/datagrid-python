# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageSubmitFeedbackParams"]


class MessageSubmitFeedbackParams(TypedDict, total=False):
    conversation_id: Required[str]

    like: Required[Literal[1, -1]]
    """`1` for thumbs up, `-1` for thumbs down."""

    feedback: Optional[str]
    """Optional free-text comment."""

    ui_surface: Optional[Literal["datagrid_web", "procore_embed", "field_ai_mobile"]]
    """Client surface where the user submitted feedback."""
