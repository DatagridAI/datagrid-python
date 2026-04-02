# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileObject", "Credits"]


class Credits(BaseModel):
    """Credit consumption for this file upload. `null` when the billing lookup fails."""

    consumed: float
    """The number of credits consumed by the operation."""


class FileObject(BaseModel):
    """The `File` object represents a document that has been uploaded to Datagrid."""

    id: str
    """The file identifier, which can be referenced in the API endpoints."""

    created_at: datetime
    """The ISO string for when the file was created."""

    filename: str
    """The name of the file"""

    media_type: str
    """The media type of the file."""

    object: Literal["file"]
    """The object type, which is always `file`."""

    credits: Optional[Credits] = None
    """Credit consumption for this file upload. `null` when the billing lookup fails."""

    expires_at: Optional[datetime] = None
    """
    The ISO timestamp when the file will expire and be automatically deleted, or
    null if the file does not expire.
    """
