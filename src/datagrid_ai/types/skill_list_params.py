# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SkillListParams"]


class SkillListParams(TypedDict, total=False):
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

    enabled: bool
    """Filter by enabled status."""

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    scope: Literal["user", "account", "teamspace", "builtin"]
    """Return only skills of this scope.

    `user` is the caller's own private skills, `account` company-owned skills
    invocable here, `teamspace` skills assigned to the caller's teamspace, and
    `builtin` the global catalogue. Omit to return everything the caller can invoke.
    """

    search: str
    """Optional search string to filter skills by name or slash key.

    Case-insensitive partial match.
    """
