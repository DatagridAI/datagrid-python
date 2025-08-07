# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConverseResponse", "Content", "Citation", "CitationKnowledge", "Credits"]


class Content(BaseModel):
    text: str


class CitationKnowledge(BaseModel):
    confirmations: List[str]
    """An array of text snippets from the knowledge that confirm the citation."""

    knowledge_id: str
    """Id of the knowledge."""

    type: Literal["image", "pdf_page", "record", "web_search", "sql_query_result"]


class Citation(BaseModel):
    citation: str
    """The text snippet from the response that is being cited."""

    knowledges: List[CitationKnowledge]
    """Array of knowledges that support this citation."""


class Credits(BaseModel):
    consumed: float
    """The number of credits consumed by the converse call."""


class ConverseResponse(BaseModel):
    agent_id: str
    """The ID of the agent used for the converse."""

    content: List[Content]
    """Contents of the converse response."""

    conversation_id: str
    """The ID of the agent conversation."""

    object: Literal["conversation.message"]

    citations: Optional[List[Citation]] = None
    """
    Array of citations that provide knowledges for factual statements in the
    response. Each citation includes the referenced text and its knowledges.
    """

    credits: Optional[Credits] = None
