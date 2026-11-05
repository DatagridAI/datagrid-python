# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .procore_project import ProcoreProject

__all__ = ["ProcoreProjectList"]


class ProcoreProjectList(BaseModel):
    data: List[ProcoreProject]

    has_more: bool
    """Whether another page follows."""

    next_page: Optional[int] = None
    """The `page` value for the next page, or `null` on the last page."""

    object: Literal["list"]
