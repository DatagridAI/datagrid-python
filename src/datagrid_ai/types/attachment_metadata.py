# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .row_metadata import RowMetadata
from .message_metadata import MessageMetadata

__all__ = ["AttachmentMetadata", "Source", "Page"]

Source: TypeAlias = Union[MessageMetadata, RowMetadata]


class Page(BaseModel):
    page_number: float
    """The page number of the attachment."""

    page_number: float = FieldInfo(alias="pageNumber")
    """DEPRECATED use page_number instead."""

    url: str
    """The url of the blob of the page."""


class AttachmentMetadata(BaseModel):
    """Metadata of an attachment object"""

    media_type: str
    """The media type of the attachment."""

    name: str
    """The name of the attachment."""

    object: Literal["attachment_metadata"]
    """The object type, which is always `attachment_metadata`."""

    source: Source
    """The source of the attachment."""

    url: str
    """The url of the blob of the attachment."""

    page: Optional[Page] = None
