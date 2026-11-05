# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IdentityProcore"]


class IdentityProcore(BaseModel):
    company_id: str
    """The Procore company ID the current teamspace's account is linked to."""

    company_name: str
    """The name of the linked Procore company, as stored in Datagrid."""

    project_id: Optional[str] = None
    """The Procore project ID the current teamspace is bound to.

    Omitted when the teamspace is not project-scoped.
    """

    zone: Optional[str] = None
    """The Procore zone the company lives in. Omitted when unknown."""
