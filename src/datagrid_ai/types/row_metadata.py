# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .table_metadata import TableMetadata

__all__ = ["RowMetadata"]


class RowMetadata(BaseModel):
    id: str
    """The id of the row (**datagrid**uuid), unique within the table."""

    object: Literal["row_metadata"]
    """The object type, which is always `row_metadata`."""

    table: TableMetadata
    """The table that the row belongs to."""

    url: str
    """The url of the row of the table."""
