# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DataViewCreateParams"]


class DataViewCreateParams(TypedDict, total=False):
    knowledge_id: Required[str]
    """The id of the knowledge to create a data view for."""

    name: Required[str]
    """The name of the data view."""

    service_account_id: Required[str]
    """The id of the service account that will access this data view."""
