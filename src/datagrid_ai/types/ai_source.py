# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AISource"]


class AISource(BaseModel):
    """A source cited in an AI-generated search answer."""

    index: int
    """1-based citation index corresponding to [N] references in the answer text."""

    node_id: str
    """Unique identifier of the source node in the search tree."""

    title: str
    """Human-readable title of the source."""

    type: Literal["file", "record", "table"]
    """
    The type of source: `file` (document/attachment), `record` (data row), or
    `table` (dataset).
    """

    dataset_name: Optional[str] = None
    """Name of the dataset this source belongs to, if applicable."""

    emoji: Optional[str] = None
    """Emoji icon for the source type (e.g., 📄 for files, 📊 for tables)."""

    page_numbers: Optional[List[int]] = None
    """Page numbers within a document where the relevant content was found."""

    table_name: Optional[str] = None
    """Name of the table this source belongs to, if applicable."""

    thumbnail_uri: Optional[str] = None
    """URI for a thumbnail preview of the source, if available."""

    url: Optional[str] = None
    """URL to view the source in the Datagrid web app."""
