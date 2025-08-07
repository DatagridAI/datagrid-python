# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IFrameEventType"]

IFrameEventType: TypeAlias = Literal[
    "datagrid-api/error",
    "datagrid-api/connection-created",
    "datagrid-api/connection-updated",
    "datagrid-api/content-loaded",
    "datagrid-api/resize",
    "datagrid-api/knowledge-created",
]
