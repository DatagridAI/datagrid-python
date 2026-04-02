# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .data_view import DataView

__all__ = ["DataViewCreateResponse", "DataViewCreateResponseCredits"]


class DataViewCreateResponseCredits(BaseModel):
    """Credit consumption for this data-view creation.

    `consumed` reflects the warehouse setup work billed for the request. `null` when the billing write fails after the data view is successfully created.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class DataViewCreateResponse(DataView):
    """
    The `data_view` object represents a view into a knowledge source that can be accessed through a service account.
    """

    credits: Optional[DataViewCreateResponseCredits] = None
    """Credit consumption for this data-view creation.

    `consumed` reflects the warehouse setup work billed for the request. `null` when
    the billing write fails after the data view is successfully created.
    """
