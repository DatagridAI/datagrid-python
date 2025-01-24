# File created for custom code changes based on our OpenAPI spec.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._models import BaseModel
from ..._utils._transform import PropertyInfo

__all__ = [
    "Event",
    "EventConverseStatusEvent",
    "EventConverseStatusEventData",
    "EventConverseContentMessageDeltaEvent",
    "EventConverseContentMessageDeltaEventData",
    "EventConverseContentMessageDeltaEventDataDelta",
    "AgentStreamEvent",
]


class EventConverseStatusEventData(BaseModel):
    agent_id: str
    """The ID of the agent used for the converse."""

    conversation_id: str
    """The ID of the agent conversation."""

    status: str
    """Name of the status"""


class EventConverseStatusEvent(BaseModel):
    data: EventConverseStatusEventData

    event: Literal["start", "end"]


class EventConverseContentMessageDeltaEventDataDelta(BaseModel):
    text: str

    event: Literal["text"]


class EventConverseContentMessageDeltaEventData(BaseModel):
    delta: EventConverseContentMessageDeltaEventDataDelta
    """Delta of the response message produced by the agent."""


class EventConverseContentMessageDeltaEvent(BaseModel):
    data: EventConverseContentMessageDeltaEventData

    event: Literal["delta"]
    """Type of the event which is always delta"""


Event: TypeAlias = Union[EventConverseStatusEvent, EventConverseContentMessageDeltaEvent]

AgentStreamEvent: TypeAlias = Annotated[
    Union[EventConverseStatusEvent, EventConverseContentMessageDeltaEvent], PropertyInfo(discriminator="event")
]
