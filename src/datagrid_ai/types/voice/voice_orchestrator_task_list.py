# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .voice_orchestrator_task import VoiceOrchestratorTask

__all__ = ["VoiceOrchestratorTaskList"]


class VoiceOrchestratorTaskList(BaseModel):
    data: List[VoiceOrchestratorTask]

    first_id: Optional[str] = None
    """
    The first task ID in this bounded list response, or null when the list is empty.
    """

    has_more: bool
    """Always false for the bounded voice task inbox."""

    last_id: Optional[str] = None
    """The last task ID in this bounded list response, or null when the list is empty."""

    object: Literal["list"]
