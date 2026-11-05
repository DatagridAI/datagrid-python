# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProcoreProjectConnection"]


class ProcoreProjectConnection(BaseModel):
    company_id: str

    connected: bool
    """The same value the project list reports for this project."""

    object: Literal["procore_project_connection"]

    project_id: str
