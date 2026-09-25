# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Summary"]


class Summary(BaseModel):
    """The `summary` object represents indexed summary content.

    Row, table, and file records contain generated summaries; page records contain the indexed page extraction body.
    """

    id: str
    """The summary identifier."""

    created_at: Optional[datetime] = None
    """The ISO string for when the summary was created.

    `null` for records that have not finished indexing.
    """

    is_vectorized: bool
    """Whether the summary has been embedded and is available for retrieval."""

    object: Literal["summary"]
    """The object type, which is always `summary`."""

    record_type: Literal["row", "table", "file", "page"]
    """The kind of summary content: per source row, table, file, or page."""

    summary: Optional[str] = None
    """The indexed body as markdown.

    For pages this is the page extraction body; for other record types it is
    generated summary content. `null` for records that have not finished indexing.
    """

    table_id: str
    """The id of the table this summary belongs to."""

    updated_at: Optional[datetime] = None
    """The ISO string for when the summary was last updated.

    `null` for records that have not finished indexing.
    """

    primary_key: Optional[str] = None
    """The primary key of the source row for a row summary.

    `null` for table, file, and page summaries.
    """

    source_data: Optional[Dict[str, builtins.object]] = None
    """The source row data used to generate the summary.

    `null` when unavailable or not applicable.
    """

    title: Optional[str] = None
    """The generated title, when available."""
