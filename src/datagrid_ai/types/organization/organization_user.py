# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OrganizationUser", "Permissions"]


class Permissions(BaseModel):
    """The roles assigned to the user in the organization"""

    role: Literal["owner", "admin", "member", "contributor", "collaborator"]
    """The role to assign to the user in the organization. Available roles:

    - **owner**: Organization owner. Can manage organization settings, users and
      create new teamspaces.
    - **admin**: Organization administrator. Can manage organization settings, users
      and create new teamspaces.
    - **member**: Standard organization member. Can create new teamspaces.
    - **contributor**: Limited access. Can read shared resources. Cannot create new
      teamspaces.
    - **collaborator**: Limited access. Cannot read shared resources. Cannot create
      new teamspaces.
    """


class OrganizationUser(BaseModel):
    """Represents a user in an organization"""

    id: str
    """The unique identifier of the user"""

    email: str
    """The email address of the user"""

    first_name: str
    """The first name of the user"""

    last_name: str
    """The last name of the user"""

    permissions: Permissions
    """The roles assigned to the user in the organization"""
