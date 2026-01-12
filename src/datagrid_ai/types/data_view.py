# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataView"]


class DataView(BaseModel):
    """
    The `data_view` object represents a view into a knowledge source that can be accessed through a service account.
    """

    id: str
    """The data view identifier."""

    bigquery_dataset_name: str
    """The name of the BigQuery dataset containing views to the data."""

    created_at: datetime
    """The ISO string for when the data view was created."""

    knowledge_id: str
    """The id of the knowledge this data view is for."""

    object: Literal["data_view"]
    """The object type, which is always `data_view`."""

    service_account_id: str
    """The id of the service account that can access this data view."""
