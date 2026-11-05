# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .procore_company import ProcoreCompany

__all__ = ["ProcoreCompanyList"]


class ProcoreCompanyList(BaseModel):
    data: List[ProcoreCompany]

    has_more: bool
    """Whether another page follows."""

    next_page: Optional[int] = None
    """The `page` value for the next page, or `null` on the last page."""

    object: Literal["list"]
