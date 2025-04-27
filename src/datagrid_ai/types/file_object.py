# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileObject"]


class FileObject(BaseModel):
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
