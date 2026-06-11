# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BatchPredictionCreateParams", "Item"]


class BatchPredictionCreateParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """Files to process. Each item uses the shared `prompt` and `output_schema`."""

    model: Required[
        Literal[
            "gemini-2.0-flash",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.1-flash-lite",
            "gemini-3.5-flash",
            "gemini-2.5-pro",
            "gemini-3.1-pro-preview",
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4.1-mini",
            "gpt-4.1",
            "gpt-5-mini",
            "gpt-5",
            "gpt-5.1",
            "claude-sonnet-4@20250514",
            "claude-opus-4-1@20250805",
            "claude-haiku-4-5@20251001",
            "claude-sonnet-4-5@20250929",
            "claude-sonnet-4-6@default",
            "claude-opus-4-5@20251101",
            "claude-opus-4-6@default",
            "claude-opus-4-7",
            "claude-opus-4-8",
            "anthropic.claude-haiku-4-5-20251001-v1:0",
            "anthropic.claude-sonnet-4-5-20250929-v1:0",
            "anthropic.claude-sonnet-4-6",
            "anthropic.claude-opus-4-5-20251101-v1:0",
            "anthropic.claude-opus-4-6-v1",
            "anthropic.claude-opus-4-7",
            "anthropic.claude-opus-4-8",
            "amazon.nova-2-lite-v1:0",
        ]
    ]
    """LLM model to use for every item in the batch.

    Model availability is cloud-aware: AWS teamspaces accept Bedrock-native
    batch-capable models, while GCP teamspaces accept non-Bedrock batch-capable
    models and reject Bedrock-only ids. Deprecated gemini-2.0-flash is accepted for
    backward compatibility and automatically runs as gemini-3.1-flash-lite.
    """

    output_schema: Required[Dict[str, object]]
    """JSON Schema Draft 2020-12 describing each item output.

    The root schema must be `type: object`. The batch prediction API currently
    rejects `$defs`, `$ref`, `allOf`, `anyOf`, `not`, `oneOf`, and
    `patternProperties` anywhere in the schema.
    """

    prompt: Required[str]
    """Shared instruction applied to each item in the batch."""

    completion_window: Optional[Literal["24h"]]
    """Requested completion window.

    Defaults to `24h` when omitted; no other values are currently supported.
    """

    metadata: Optional[Dict[str, str]]
    """Optional metadata map with up to 16 entries.

    Metadata keys must be 64 characters or fewer and values must be 512 characters
    or fewer.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Item(TypedDict, total=False):
    custom_id: Required[str]
    """Caller-defined identifier.

    Must be unique within the batch and is echoed in result lines.
    """

    file_id: Required[str]
    """Existing Datagrid file id from the Files API.

    The file must be accessible from the authenticated teamspace.
    """

    page: Optional[int]
    """Optional 1-indexed page number for a paged document such as a PDF."""
