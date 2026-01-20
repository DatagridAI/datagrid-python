# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["PageListParams", "Parent", "ParentParentPage", "ParentRootPage"]


class PageListParams(TypedDict, total=False):
    after: str
    """A cursor to use in pagination.

    `after` is an object ID that defines your place in the list. For example, if you
    make a list request and receive 100 objects, ending with `obj_foo`, your
    subsequent call can include `after=obj_foo` to fetch the next page of the list.
    """

    before: str
    """A cursor to use in pagination.

    `before` is an object ID that defines your place in the list. For example, if
    you make a list request and receive 100 objects, starting with `obj_bar`, your
    subsequent call can include `before=obj_bar` to fetch the previous page of the
    list.
    """

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    parent: Parent
    """Filter pages by parent.

    Pass `{"type":"root"}` to get root-level pages, or
    `{"type":"page","page_id":"page_123"}` to get pages nested under a specific
    page. If not specified, returns all pages.
    """


class ParentParentPage(TypedDict, total=False):
    """The parent page reference, indicating where this page is nested"""

    page_id: Required[str]
    """The ID of the parent page. Required when type is 'page'"""

    type: Required[Literal["page"]]
    """The type of parent. 'page' indicates nested under a specific page"""


class ParentRootPage(TypedDict, total=False):
    """The root level object"""

    type: Required[Literal["root"]]
    """The type of parent. 'root' indicates at the root level"""


Parent: TypeAlias = Union[ParentParentPage, ParentRootPage]
