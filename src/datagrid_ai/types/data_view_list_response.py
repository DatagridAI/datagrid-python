# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .data_view import DataView

__all__ = ["DataViewListResponse"]


class DataViewListResponse(BaseModel):
    data: List[DataView]
    """An array containing the data views."""

    object: Literal["list"]
