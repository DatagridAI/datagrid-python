# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProcoreProject"]


class ProcoreProject(BaseModel):
    id: str
    """The Procore project ID."""

    company_id: str
    """The Procore company ID the project belongs to."""

    name: str
    """The project name in Procore."""

    active: Optional[bool] = None
    """Whether the project is active in Procore, when reported."""

    project_number: Optional[str] = None
    """The project number in Procore, when set."""
