# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["Page", "Parent", "ParentParentPage", "ParentRootPage"]


class ParentParentPage(BaseModel):
    """The parent page reference, indicating where this page is nested"""

    page_id: str
    """The ID of the parent page. Required when type is 'page'"""

    type: Literal["page"]
    """The type of parent. 'page' indicates nested under a specific page"""


class ParentRootPage(BaseModel):
    """The root level object"""

    type: Literal["root"]
    """The type of parent. 'root' indicates at the root level"""


Parent: TypeAlias = Union[ParentParentPage, ParentRootPage]


class Page(BaseModel):
    """
    The `page` object represents a page that can contain knowledge and other pages in a hierarchical structure.
    """

    id: str
    """Unique identifier for the page (document resource ID)"""

    created_at: datetime
    """The ISO string for when the page was created"""

    name: str
    """The name of the page"""

    object: Literal["page"]
    """The object type, always 'page'"""

    parent: Parent
    """The parent object, indicating where the object is located in the hierarchy"""
