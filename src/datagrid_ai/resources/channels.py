# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    channel_list_params,
    channel_create_params,
    channel_update_params,
    channel_add_members_params,
    channel_add_reaction_params,
    channel_list_members_params,
    channel_list_threads_params,
    channel_list_messages_params,
    channel_create_message_params,
    channel_list_thread_messages_params,
    channel_create_thread_message_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorIDPage, AsyncCursorIDPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.channel import Channel
from ..types.channel_member import ChannelMember
from ..types.channel_thread import ChannelThread
from ..types.channel_message import ChannelMessage
from ..types.channel_add_members_response import ChannelAddMembersResponse

__all__ = ["ChannelsResource", "AsyncChannelsResource"]


class ChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """
        Creates a shared public channel and adds the authenticated API user as a member.

        Args:
          name: Channel name. Names longer than 50 characters are truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/channels",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                channel_create_params.ChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    def retrieve(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """
        Retrieve channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            path_template("/channels/{channel_id}", channel_id=channel_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    def update(
        self,
        channel_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """Update channel

        Args:
          name: Channel name.

        Names longer than 50 characters are truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._patch(
            path_template("/channels/{channel_id}", channel_id=channel_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                channel_update_params.ChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        type: Literal["channel"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[Channel]:
        """Lists shared public named channels in the resolved teamspace.

        Private channels,
        direct messages, and personal chats are intentionally omitted. `q` filters
        channel names and does not search message content.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          q: Case-insensitive channel-name substring.

          type: Filter by channel type. Only shared named channels are available in v1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/channels",
            page=SyncCursorIDPage[Channel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "q": q,
                        "type": type,
                    },
                    channel_list_params.ChannelListParams,
                ),
            ),
            model=Channel,
        )

    def add_members(
        self,
        channel_id: str,
        *,
        actors: Iterable[channel_add_members_params.Actor],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAddMembersResponse:
        """
        Add channel members

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._post(
            path_template("/channels/{channel_id}/members", channel_id=channel_id),
            body=maybe_transform({"actors": actors}, channel_add_members_params.ChannelAddMembersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAddMembersResponse,
        )

    def add_reaction(
        self,
        message_id: str,
        *,
        channel_id: str,
        reaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Adds the authenticated API user's reaction to a channel or thread message.

        The
        reacting user cannot be overridden: callers can only add their own reaction.
        Repeating the same reaction is idempotent. The caller must be a channel member.
        Returns the updated message.

        The reaction must be an emoji available in the Datagrid emoji picker, supplied
        either as a shortcode (`:+1:`) or as the unicode character (`👍`). Shortcodes
        are resolved to the unicode character before storage, so a reaction added
        through the API groups together with the same emoji added in the app. Anything
        else is rejected with a 400.

        Args:
          reaction: Emoji shortcode (for example `:+1:` or `:heart:`) or unicode emoji (`👍`). Must
              be an emoji offered by the Datagrid emoji picker; shortcodes are stored as their
              unicode character so API and in-app reactions group together. Always attributed
              to the authenticated API user; there is no field to react as another user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/reactions", channel_id=channel_id, message_id=message_id
            ),
            body=maybe_transform({"reaction": reaction}, channel_add_reaction_params.ChannelAddReactionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def create_message(
        self,
        channel_id: str,
        *,
        content: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Posts as the authenticated API user, who must be a channel member.

        Eligible
        channel agents may respond and consume credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._post(
            path_template("/channels/{channel_id}/messages", channel_id=channel_id),
            body=maybe_transform(
                {
                    "content": content,
                    "file_ids": file_ids,
                },
                channel_create_message_params.ChannelCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def create_thread(
        self,
        message_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelThread:
        """
        Returns the existing thread when the message already has one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/threads", channel_id=channel_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelThread,
        )

    def create_thread_message(
        self,
        thread_id: str,
        *,
        channel_id: str,
        content: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Posts as the authenticated API user, who must be a channel member.

        Eligible
        channel agents may respond and consume credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._post(
            path_template(
                "/channels/{channel_id}/threads/{thread_id}/messages", channel_id=channel_id, thread_id=thread_id
            ),
            body=maybe_transform(
                {
                    "content": content,
                    "file_ids": file_ids,
                },
                channel_create_thread_message_params.ChannelCreateThreadMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def list_members(
        self,
        channel_id: str,
        *,
        actor_type: Literal["user", "agent"] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[ChannelMember]:
        """List channel members

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          q: Case-insensitive actor-name substring.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/members", channel_id=channel_id),
            page=SyncCursorIDPage[ChannelMember],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor_type": actor_type,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "q": q,
                    },
                    channel_list_members_params.ChannelListMembersParams,
                ),
            ),
            model=ChannelMember,
        )

    def list_messages(
        self,
        channel_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[ChannelMessage]:
        """List channel messages

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/messages", channel_id=channel_id),
            page=SyncCursorIDPage[ChannelMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_messages_params.ChannelListMessagesParams,
                ),
            ),
            model=ChannelMessage,
        )

    def list_thread_messages(
        self,
        thread_id: str,
        *,
        channel_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[ChannelMessage]:
        """List thread messages

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get_api_list(
            path_template(
                "/channels/{channel_id}/threads/{thread_id}/messages", channel_id=channel_id, thread_id=thread_id
            ),
            page=SyncCursorIDPage[ChannelMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_thread_messages_params.ChannelListThreadMessagesParams,
                ),
            ),
            model=ChannelMessage,
        )

    def list_threads(
        self,
        channel_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[ChannelThread]:
        """List channel threads

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/threads", channel_id=channel_id),
            page=SyncCursorIDPage[ChannelThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_threads_params.ChannelListThreadsParams,
                ),
            ),
            model=ChannelThread,
        )

    def remove_member(
        self,
        member_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove channel member

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/channels/{channel_id}/members/{member_id}", channel_id=channel_id, member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_reaction(
        self,
        reaction: str,
        *,
        channel_id: str,
        message_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """
        Removes the authenticated API user's reaction from a channel or thread message.
        Callers cannot remove another user's reaction; a delete only clears the caller's
        own entry for that emoji. Removing a reaction that is not present is idempotent.
        The caller must be a channel member. Returns the updated message.

        Accepts the same values as adding a reaction: a shortcode (`:+1:`) or the
        unicode character (`👍`), resolved to the same stored emoji.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not reaction:
            raise ValueError(f"Expected a non-empty value for `reaction` but received {reaction!r}")
        return self._delete(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/reactions/{reaction}",
                channel_id=channel_id,
                message_id=message_id,
                reaction=reaction,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def retrieve_thread(
        self,
        thread_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelThread:
        """
        Retrieve channel thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/channels/{channel_id}/threads/{thread_id}", channel_id=channel_id, thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelThread,
        )


class AsyncChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """
        Creates a shared public channel and adds the authenticated API user as a member.

        Args:
          name: Channel name. Names longer than 50 characters are truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/channels",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                channel_create_params.ChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    async def retrieve(
        self,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """
        Retrieve channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            path_template("/channels/{channel_id}", channel_id=channel_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    async def update(
        self,
        channel_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Channel:
        """Update channel

        Args:
          name: Channel name.

        Names longer than 50 characters are truncated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._patch(
            path_template("/channels/{channel_id}", channel_id=channel_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                channel_update_params.ChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Channel,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        type: Literal["channel"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Channel, AsyncCursorIDPage[Channel]]:
        """Lists shared public named channels in the resolved teamspace.

        Private channels,
        direct messages, and personal chats are intentionally omitted. `q` filters
        channel names and does not search message content.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          q: Case-insensitive channel-name substring.

          type: Filter by channel type. Only shared named channels are available in v1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/channels",
            page=AsyncCursorIDPage[Channel],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "q": q,
                        "type": type,
                    },
                    channel_list_params.ChannelListParams,
                ),
            ),
            model=Channel,
        )

    async def add_members(
        self,
        channel_id: str,
        *,
        actors: Iterable[channel_add_members_params.Actor],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelAddMembersResponse:
        """
        Add channel members

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._post(
            path_template("/channels/{channel_id}/members", channel_id=channel_id),
            body=await async_maybe_transform({"actors": actors}, channel_add_members_params.ChannelAddMembersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelAddMembersResponse,
        )

    async def add_reaction(
        self,
        message_id: str,
        *,
        channel_id: str,
        reaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Adds the authenticated API user's reaction to a channel or thread message.

        The
        reacting user cannot be overridden: callers can only add their own reaction.
        Repeating the same reaction is idempotent. The caller must be a channel member.
        Returns the updated message.

        The reaction must be an emoji available in the Datagrid emoji picker, supplied
        either as a shortcode (`:+1:`) or as the unicode character (`👍`). Shortcodes
        are resolved to the unicode character before storage, so a reaction added
        through the API groups together with the same emoji added in the app. Anything
        else is rejected with a 400.

        Args:
          reaction: Emoji shortcode (for example `:+1:` or `:heart:`) or unicode emoji (`👍`). Must
              be an emoji offered by the Datagrid emoji picker; shortcodes are stored as their
              unicode character so API and in-app reactions group together. Always attributed
              to the authenticated API user; there is no field to react as another user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/reactions", channel_id=channel_id, message_id=message_id
            ),
            body=await async_maybe_transform(
                {"reaction": reaction}, channel_add_reaction_params.ChannelAddReactionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def create_message(
        self,
        channel_id: str,
        *,
        content: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Posts as the authenticated API user, who must be a channel member.

        Eligible
        channel agents may respond and consume credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._post(
            path_template("/channels/{channel_id}/messages", channel_id=channel_id),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "file_ids": file_ids,
                },
                channel_create_message_params.ChannelCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def create_thread(
        self,
        message_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelThread:
        """
        Returns the existing thread when the message already has one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/threads", channel_id=channel_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelThread,
        )

    async def create_thread_message(
        self,
        thread_id: str,
        *,
        channel_id: str,
        content: str,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """Posts as the authenticated API user, who must be a channel member.

        Eligible
        channel agents may respond and consume credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._post(
            path_template(
                "/channels/{channel_id}/threads/{thread_id}/messages", channel_id=channel_id, thread_id=thread_id
            ),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "file_ids": file_ids,
                },
                channel_create_thread_message_params.ChannelCreateThreadMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def list_members(
        self,
        channel_id: str,
        *,
        actor_type: Literal["user", "agent"] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelMember, AsyncCursorIDPage[ChannelMember]]:
        """List channel members

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          q: Case-insensitive actor-name substring.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/members", channel_id=channel_id),
            page=AsyncCursorIDPage[ChannelMember],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor_type": actor_type,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "q": q,
                    },
                    channel_list_members_params.ChannelListMembersParams,
                ),
            ),
            model=ChannelMember,
        )

    def list_messages(
        self,
        channel_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelMessage, AsyncCursorIDPage[ChannelMessage]]:
        """List channel messages

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/messages", channel_id=channel_id),
            page=AsyncCursorIDPage[ChannelMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_messages_params.ChannelListMessagesParams,
                ),
            ),
            model=ChannelMessage,
        )

    def list_thread_messages(
        self,
        thread_id: str,
        *,
        channel_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelMessage, AsyncCursorIDPage[ChannelMessage]]:
        """List thread messages

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get_api_list(
            path_template(
                "/channels/{channel_id}/threads/{thread_id}/messages", channel_id=channel_id, thread_id=thread_id
            ),
            page=AsyncCursorIDPage[ChannelMessage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_thread_messages_params.ChannelListThreadMessagesParams,
                ),
            ),
            model=ChannelMessage,
        )

    def list_threads(
        self,
        channel_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChannelThread, AsyncCursorIDPage[ChannelThread]]:
        """List channel threads

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            path_template("/channels/{channel_id}/threads", channel_id=channel_id),
            page=AsyncCursorIDPage[ChannelThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    channel_list_threads_params.ChannelListThreadsParams,
                ),
            ),
            model=ChannelThread,
        )

    async def remove_member(
        self,
        member_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove channel member

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/channels/{channel_id}/members/{member_id}", channel_id=channel_id, member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_reaction(
        self,
        reaction: str,
        *,
        channel_id: str,
        message_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelMessage:
        """
        Removes the authenticated API user's reaction from a channel or thread message.
        Callers cannot remove another user's reaction; a delete only clears the caller's
        own entry for that emoji. Removing a reaction that is not present is idempotent.
        The caller must be a channel member. Returns the updated message.

        Accepts the same values as adding a reaction: a shortcode (`:+1:`) or the
        unicode character (`👍`), resolved to the same stored emoji.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not reaction:
            raise ValueError(f"Expected a non-empty value for `reaction` but received {reaction!r}")
        return await self._delete(
            path_template(
                "/channels/{channel_id}/messages/{message_id}/reactions/{reaction}",
                channel_id=channel_id,
                message_id=message_id,
                reaction=reaction,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def retrieve_thread(
        self,
        thread_id: str,
        *,
        channel_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelThread:
        """
        Retrieve channel thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/channels/{channel_id}/threads/{thread_id}", channel_id=channel_id, thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelThread,
        )


class ChannelsResourceWithRawResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.create = to_raw_response_wrapper(
            channels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            channels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            channels.update,
        )
        self.list = to_raw_response_wrapper(
            channels.list,
        )
        self.add_members = to_raw_response_wrapper(
            channels.add_members,
        )
        self.add_reaction = to_raw_response_wrapper(
            channels.add_reaction,
        )
        self.create_message = to_raw_response_wrapper(
            channels.create_message,
        )
        self.create_thread = to_raw_response_wrapper(
            channels.create_thread,
        )
        self.create_thread_message = to_raw_response_wrapper(
            channels.create_thread_message,
        )
        self.list_members = to_raw_response_wrapper(
            channels.list_members,
        )
        self.list_messages = to_raw_response_wrapper(
            channels.list_messages,
        )
        self.list_thread_messages = to_raw_response_wrapper(
            channels.list_thread_messages,
        )
        self.list_threads = to_raw_response_wrapper(
            channels.list_threads,
        )
        self.remove_member = to_raw_response_wrapper(
            channels.remove_member,
        )
        self.remove_reaction = to_raw_response_wrapper(
            channels.remove_reaction,
        )
        self.retrieve_thread = to_raw_response_wrapper(
            channels.retrieve_thread,
        )


class AsyncChannelsResourceWithRawResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.create = async_to_raw_response_wrapper(
            channels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            channels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            channels.list,
        )
        self.add_members = async_to_raw_response_wrapper(
            channels.add_members,
        )
        self.add_reaction = async_to_raw_response_wrapper(
            channels.add_reaction,
        )
        self.create_message = async_to_raw_response_wrapper(
            channels.create_message,
        )
        self.create_thread = async_to_raw_response_wrapper(
            channels.create_thread,
        )
        self.create_thread_message = async_to_raw_response_wrapper(
            channels.create_thread_message,
        )
        self.list_members = async_to_raw_response_wrapper(
            channels.list_members,
        )
        self.list_messages = async_to_raw_response_wrapper(
            channels.list_messages,
        )
        self.list_thread_messages = async_to_raw_response_wrapper(
            channels.list_thread_messages,
        )
        self.list_threads = async_to_raw_response_wrapper(
            channels.list_threads,
        )
        self.remove_member = async_to_raw_response_wrapper(
            channels.remove_member,
        )
        self.remove_reaction = async_to_raw_response_wrapper(
            channels.remove_reaction,
        )
        self.retrieve_thread = async_to_raw_response_wrapper(
            channels.retrieve_thread,
        )


class ChannelsResourceWithStreamingResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.create = to_streamed_response_wrapper(
            channels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            channels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            channels.update,
        )
        self.list = to_streamed_response_wrapper(
            channels.list,
        )
        self.add_members = to_streamed_response_wrapper(
            channels.add_members,
        )
        self.add_reaction = to_streamed_response_wrapper(
            channels.add_reaction,
        )
        self.create_message = to_streamed_response_wrapper(
            channels.create_message,
        )
        self.create_thread = to_streamed_response_wrapper(
            channels.create_thread,
        )
        self.create_thread_message = to_streamed_response_wrapper(
            channels.create_thread_message,
        )
        self.list_members = to_streamed_response_wrapper(
            channels.list_members,
        )
        self.list_messages = to_streamed_response_wrapper(
            channels.list_messages,
        )
        self.list_thread_messages = to_streamed_response_wrapper(
            channels.list_thread_messages,
        )
        self.list_threads = to_streamed_response_wrapper(
            channels.list_threads,
        )
        self.remove_member = to_streamed_response_wrapper(
            channels.remove_member,
        )
        self.remove_reaction = to_streamed_response_wrapper(
            channels.remove_reaction,
        )
        self.retrieve_thread = to_streamed_response_wrapper(
            channels.retrieve_thread,
        )


class AsyncChannelsResourceWithStreamingResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.create = async_to_streamed_response_wrapper(
            channels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            channels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            channels.list,
        )
        self.add_members = async_to_streamed_response_wrapper(
            channels.add_members,
        )
        self.add_reaction = async_to_streamed_response_wrapper(
            channels.add_reaction,
        )
        self.create_message = async_to_streamed_response_wrapper(
            channels.create_message,
        )
        self.create_thread = async_to_streamed_response_wrapper(
            channels.create_thread,
        )
        self.create_thread_message = async_to_streamed_response_wrapper(
            channels.create_thread_message,
        )
        self.list_members = async_to_streamed_response_wrapper(
            channels.list_members,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            channels.list_messages,
        )
        self.list_thread_messages = async_to_streamed_response_wrapper(
            channels.list_thread_messages,
        )
        self.list_threads = async_to_streamed_response_wrapper(
            channels.list_threads,
        )
        self.remove_member = async_to_streamed_response_wrapper(
            channels.remove_member,
        )
        self.remove_reaction = async_to_streamed_response_wrapper(
            channels.remove_reaction,
        )
        self.retrieve_thread = async_to_streamed_response_wrapper(
            channels.retrieve_thread,
        )
