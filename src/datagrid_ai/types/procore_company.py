# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ProcoreCompany"]


class ProcoreCompany(BaseModel):
    id: str
    """The Procore company ID."""

    name: str
    """The company name in Procore."""
