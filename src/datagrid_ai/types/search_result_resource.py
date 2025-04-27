# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .row_metadata import RowMetadata
from .table_metadata import TableMetadata
from .message_metadata import MessageMetadata
from .knowledge_metadata import KnowledgeMetadata
from .attachment_metadata import AttachmentMetadata

__all__ = ["SearchResultResource"]

SearchResultResource: TypeAlias = Union[
    KnowledgeMetadata, TableMetadata, RowMetadata, AttachmentMetadata, MessageMetadata
]
