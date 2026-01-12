# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Record"]


class Record(BaseModel):
    """The `record` object represents a single record within a table."""

    id: str
    """The record identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the record was created."""

    data: Dict[str, object]
    """The actual record data as a JSON object."""

    object: Literal["record"]
    """The object type, which is always `record`."""

    table_id: str
    """The id of the table this record belongs to."""

    updated_at: datetime
    """The ISO string for when the record was last updated."""
