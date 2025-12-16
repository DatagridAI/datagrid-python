# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Message", "Citation", "CitationKnowledge", "Content", "Credits"]


class CitationKnowledge(BaseModel):
    confirmations: List[str]
    """An array of text snippets from the knowledge that confirm the citation."""

    knowledge_name: str
    """Name of the knowledge."""

    type: Literal["image", "pdf_page", "record", "web_search", "sql_query_result", "action"]

    knowledge_id: Optional[str] = None
    """Id of the knowledge."""


class Citation(BaseModel):
    citation: str
    """The text snippet from the response that is being cited."""

    knowledges: List[CitationKnowledge]
    """Array of knowledges that support this citation."""


class Content(BaseModel):
    text: str

    type: Literal["text"]


class Credits(BaseModel):
    consumed: float
    """The number of credits consumed by the converse call."""


class Message(BaseModel):
    """The `conversation.message` object represents a message in a conversation."""

    id: str
    """The message identifier."""

    agent_id: str
    """The ID of the agent that sent or responded to the message."""

    citations: Optional[List[Citation]] = None
    """
    Array of citations that provide knowledges for factual statements in the
    response. Each citation includes the referenced text and its knowledges.
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
