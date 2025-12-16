# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DataViewListParams"]


class DataViewListParams(TypedDict, total=False):
    service_account_id: Required[str]
    """The id of the service account to list data views for."""

    knowledge_id: str
    """The id of the knowledge to list data views for."""

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    offset: int
    """A cursor to use in pagination.

    `offset` is an integer that defines your place in the list. For example, if you
    make a list request and receive 100 objects, starting with `obj_bar`, your
    subsequent call can include `offset=100` to fetch the next page of the list.
    """
