# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Table"]


class Table(BaseModel):
    """The `table` object represents a table within a knowledge."""

    id: str
    """The table identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the table was created."""

    knowledge_id: str
    """The id of the knowledge this table belongs to."""

    name: str
    """The name of the table."""

    object: Literal["table"]
    """The object type, which is always `table`."""

    updated_at: datetime
    """The ISO string for when the table was last updated."""
