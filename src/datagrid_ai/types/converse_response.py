# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConverseResponse", "Citation", "CitationSource", "Content", "Credits"]


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


class Content(BaseModel):
    text: str

    type: Literal["text"]


class Credits(BaseModel):
    consumed: float
    """The number of credits consumed by the converse call."""


class ConverseResponse(BaseModel):
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

    object: Literal["conversation.message"]
    """The object type, which is always `conversation.message`."""

    role: Literal["user", "agent"]
    """The role of the message sender - either 'user' or 'agent'."""
