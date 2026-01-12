# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DataViewCreateParams"]


class DataViewCreateParams(TypedDict, total=False):
    bigquery_dataset_name: Required[str]
    """The name of the BigQuery dataset containing views to the data.

    Your organization's domain will be automatically prepended to the name.
    """

    knowledge_id: Required[str]
    """The id of the knowledge to create a data view for."""

    service_account_id: Required[str]
    """The id of the service account that will access this data view."""
