# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Message",
    "Citation",
    "CitationSource",
    "Content",
    "ContentMessageContentText",
    "ContentMessageContentVoice",
    "ContentMessageContentVoiceAudioClip",
    "ContentMessageContentVoiceAudioClipParticipant",
    "ContentMessageContentVoiceTimelineEvent",
    "ContentMessageContentVoiceTimelineEventCitation",
    "ContentMessageContentVoiceTimelineEventCitationSource",
    "ContentMessageContentFile",
    "Credits",
]


class CitationSource(BaseModel):
    confirmations: List[str]
    """An array of text snippets from the source that confirm the citation."""

    source_name: str
    """Name of the source."""

    type: Literal["image", "pdf_page", "record", "web_search", "sql_query_result", "action"]

    source_id: Optional[str] = None
    """Id of the source."""

    source_uri: Optional[str] = None
    """URI of the source."""


class Citation(BaseModel):
    citation: str
    """The text snippet from the response that is being cited."""

    sources: List[CitationSource]
    """Array of sources that support this citation."""


class ContentMessageContentText(BaseModel):
    """Text content for a message."""

    text: str
    """The text content of the message."""

    type: Literal["text"]


class ContentMessageContentVoiceAudioClipParticipant(BaseModel):
    """Participant who spoke in this clip."""

    id: str

    type: Literal["user", "agent"]


class ContentMessageContentVoiceAudioClip(BaseModel):
    """A single audio clip from a voice message."""

    id: str
    """Unique identifier for the audio clip file.

    Use this ID with the files API to download the audio content.
    """

    audio_uri: str
    """Datagrid file URI for the audio file (WAV format)."""

    duration_ms: float
    """Duration of this audio clip in milliseconds."""

    participant: ContentMessageContentVoiceAudioClipParticipant
    """Participant who spoke in this clip."""

    start_time_ms: float
    """
    Start time of this clip relative to the beginning of the voice message, in
    milliseconds.
    """


class ContentMessageContentVoiceTimelineEventCitationSource(BaseModel):
    confirmations: List[str]
    """An array of text snippets from the source that confirm the citation."""

    source_name: str
    """Name of the source."""

    type: Literal["image", "pdf_page", "record", "web_search", "sql_query_result", "action"]

    source_id: Optional[str] = None
    """Id of the source."""

    source_uri: Optional[str] = None
    """URI of the source."""


class ContentMessageContentVoiceTimelineEventCitation(BaseModel):
    citation: str
    """The text snippet from the response that is being cited."""

    sources: List[ContentMessageContentVoiceTimelineEventCitationSource]
    """Array of sources that support this citation."""


class ContentMessageContentVoiceTimelineEvent(BaseModel):
    """
    A single event from a voice session timeline, representing either a transcript turn or a citation.
    """

    timestamp_ms: float
    """Timestamp offset from the start of the voice session, in milliseconds."""

    type: Literal["transcript", "citation"]
    """The type of timeline event."""

    citations: Optional[List[ContentMessageContentVoiceTimelineEventCitation]] = None
    """Citations for this event. Present when type is 'citation'."""

    role: Optional[Literal["user", "agent"]] = None
    """The role of the participant for this event."""

    text: Optional[str] = None
    """Plain text transcript for this turn. Present when type is 'transcript'."""


class ContentMessageContentVoice(BaseModel):
    """Voice content for a message."""

    audio_clips: List[ContentMessageContentVoiceAudioClip]
    """Array of audio clips with timestamps for synchronized playback."""

    duration_ms: Optional[float] = None
    """Total duration of the voice message in milliseconds."""

    transcript: str
    """User transcript of the voice message."""

    type: Literal["voice"]

    agent_transcript: Optional[str] = None
    """Agent transcript of the voice message (for agent role messages)."""

    timeline_events: Optional[List[ContentMessageContentVoiceTimelineEvent]] = None
    """Per-turn transcript and citation events in chronological order.

    Each entry is plain text with a timestamp offset from the start of the voice
    session. Present only for voice sessions that recorded timeline data.
    """


class ContentMessageContentFile(BaseModel):
    """File attachment content for a message.

    Represents a file that was uploaded as part of the user's message.
    """

    file_id: str
    """The ID of the attached file.

    Use this ID with the files API to download the file content.
    """

    type: Literal["input_file"]


Content: TypeAlias = Annotated[
    Union[ContentMessageContentText, ContentMessageContentVoice, ContentMessageContentFile],
    PropertyInfo(discriminator="type"),
]


class Credits(BaseModel):
    """Credit consumption for this converse turn.

    `null` for user-role messages and when retrieving messages from conversation history.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class Message(BaseModel):
    """The `conversation.message` object represents a message in a conversation."""

    id: str
    """The message identifier."""

    agent_id: str
    """The ID of the agent that sent or responded to the message."""

    citations: Optional[List[Citation]] = None
    """Array of citations that provide sources for factual statements in the response.

    Each citation includes the referenced text and its sources.
    """

    content: List[Content]
    """Contents of the message."""

    conversation_id: str
    """The ID of the conversation the message belongs to."""

    created_at: datetime
    """The ISO string for when the message was created."""

    credits: Optional[Credits] = None
    """Credit consumption for this converse turn.

    `null` for user-role messages and when retrieving messages from conversation
    history.
    """

    object: Literal["conversation.message"]
    """The object type, which is always `conversation.message`."""

    role: Literal["user", "agent"]
    """The role of the message sender - either 'user' or 'agent'."""
