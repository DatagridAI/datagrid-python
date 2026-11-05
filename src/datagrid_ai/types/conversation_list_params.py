# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .conversation_sort_field import ConversationSortField

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
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

    direction: Literal["asc", "desc"]
    """The direction to sort the results."""

    has_messages: bool
    """When true, excludes conversations that never had a message sent (e.g.

    abandoned sessions). Defaults to false, returning every conversation regardless
    of message count. Changing this value between requests that reuse the same
    `before`/`after` cursor is not supported — the cursor was computed against a
    different result set, so pass a consistent value for the lifetime of a given
    pagination sequence.
    """

    has_voice_messages: bool
    """
    When true, restricts the list to conversations that contain at least one voice
    message. Defaults to false, returning conversations regardless of modality.
    Changing this value between requests that reuse the same `before`/`after` cursor
    is not supported — the cursor was computed against a different result set, so
    pass a consistent value for the lifetime of a given pagination sequence.
    """

    has_voice_or_mobile_messages: bool
    """
    When true, restricts the list to conversations that contain at least one voice
    message or had a message sent from the Datagrid mobile app. Defaults to false,
    returning conversations regardless of modality or client. Combined with
    `has_voice_messages=true`, both filters apply and only voice conversations are
    returned. Changing this value between requests that reuse the same
    `before`/`after` cursor is not supported — the cursor was computed against a
    different result set, so pass a consistent value for the lifetime of a given
    pagination sequence.
    """

    limit: int
    """The limit on the number of objects to return, ranging between 1 and 100."""

    sort: ConversationSortField
    """The field to sort the conversations by."""
