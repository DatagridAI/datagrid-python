# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SearchResultResourceType"]

SearchResultResourceType: TypeAlias = Literal[
    "knowledge_metadata", "table_metadata", "row_metadata", "attachment_metadata", "message_metadata"
]
