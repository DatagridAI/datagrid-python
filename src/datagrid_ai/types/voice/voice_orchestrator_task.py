# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VoiceOrchestratorTask", "PendingAction"]


class PendingAction(BaseModel):
    """
    Present on retrieve responses when the delegated agent halted on an approval-required action that is still awaiting user review. Omitted from list responses and once the action has been submitted.
    """

    action_name: str

    agent_explanation: str

    payload_id: str

    connector_id: Optional[str] = None

    submit_button_text: Optional[str] = None

    tool_id: Optional[str] = None


class VoiceOrchestratorTask(BaseModel):
    created_at: datetime

    expires_at: datetime

    status: Literal["queued", "running", "completed", "failed", "cancelled"]
    """
    `cancelled` is reserved for terminal task records produced by future
    cancellation flows; this API does not currently expose a cancel operation.
    """

    task: str

    task_id: str

    updated_at: datetime

    acknowledged_at: Optional[datetime] = None

    agent_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    conversation_id: Optional[str] = None

    error_message: Optional[str] = None

    parent_task_id: Optional[str] = None
    """
    Present when this task was created by follow_up_task to continue an earlier
    delegated task.
    """

    pending_action: Optional[PendingAction] = None
    """
    Present on retrieve responses when the delegated agent halted on an
    approval-required action that is still awaiting user review. Omitted from list
    responses and once the action has been submitted.
    """

    result: Optional[str] = None
    """Present on retrieve responses when a user-owned task has a result.

    Omitted from list responses.
    """
