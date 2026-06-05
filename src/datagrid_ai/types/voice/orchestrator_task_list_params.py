# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["OrchestratorTaskListParams"]


class OrchestratorTaskListParams(TypedDict, total=False):
    conversation_id: str

    limit: int

    status: SequenceNotStr[str]
    """Status filter.

    Repeat the parameter for multiple statuses (`?status=queued&status=running`);
    comma-separated values are also accepted. Supported values: queued, running,
    completed, failed, cancelled.
    """
