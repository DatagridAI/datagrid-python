# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChannelAddReactionParams"]


class ChannelAddReactionParams(TypedDict, total=False):
    channel_id: Required[str]

    reaction: Required[str]
    """Emoji shortcode (for example `:+1:` or `:heart:`) or unicode emoji (`👍`).

    Must be an emoji offered by the Datagrid emoji picker; shortcodes are stored as
    their unicode character so API and in-app reactions group together. Always
    attributed to the authenticated API user; there is no field to react as another
    user.
    """
