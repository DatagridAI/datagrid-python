# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .knowledge_metadata import KnowledgeMetadata

__all__ = ["TableMetadata"]


class TableMetadata(BaseModel):
    id: str
    """The unique identifier for the table."""

    knowledge: KnowledgeMetadata
    """The knowledge object that the table belongs to."""

    name: str
    """The name of the table."""

    object: Literal["table_metadata"]
    """The object type, which is always `table_metadata`."""

    url: str
    """The url of the table."""
