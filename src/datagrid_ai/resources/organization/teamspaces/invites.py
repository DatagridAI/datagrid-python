# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorIDPage, AsyncCursorIDPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.organization.teamspaces import invite_list_params, invite_create_params
from ....types.organization.teamspaces.teamspace_invite import TeamspaceInvite

__all__ = ["InvitesResource", "AsyncInvitesResource"]


class InvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return InvitesResourceWithStreamingResponse(self)

    def create(
        self,
        teamspace_id: str,
        *,
        email: str,
        permissions: Optional[invite_create_params.Permissions] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamspaceInvite:
        """Invite a user to join the teamspace.

        This will send an invitation email. If the
        user already exists, the invite will be automatically accepted.

        Args:
          email: The email address of the user to invite

          permissions: The permissions to assign to the user in the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return self._post(
            f"/organization/teamspaces/{teamspace_id}/invites",
            body=maybe_transform(
                {
                    "email": email,
                    "permissions": permissions,
                },
                invite_create_params.InviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamspaceInvite,
        )

    def retrieve(
        self,
        invite_id: str,
        *,
        teamspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamspaceInvite:
        """
        Get a pending invite for in a teamspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return self._get(
            f"/organization/teamspaces/{teamspace_id}/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamspaceInvite,
        )

    def list(
        self,
        teamspace_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorIDPage[TeamspaceInvite]:
        """
        List all pending invites for a teamspace.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return self._get_api_list(
            f"/organization/teamspaces/{teamspace_id}/invites",
            page=SyncCursorIDPage[TeamspaceInvite],
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
                    invite_list_params.InviteListParams,
                ),
            ),
            model=TeamspaceInvite,
        )

    def delete(
        self,
        invite_id: str,
        *,
        teamspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a pending invite for a user in a teamspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/organization/teamspaces/{teamspace_id}/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def create(
        self,
        teamspace_id: str,
        *,
        email: str,
        permissions: Optional[invite_create_params.Permissions] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamspaceInvite:
        """Invite a user to join the teamspace.

        This will send an invitation email. If the
        user already exists, the invite will be automatically accepted.

        Args:
          email: The email address of the user to invite

          permissions: The permissions to assign to the user in the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return await self._post(
            f"/organization/teamspaces/{teamspace_id}/invites",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "permissions": permissions,
                },
                invite_create_params.InviteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamspaceInvite,
        )

    async def retrieve(
        self,
        invite_id: str,
        *,
        teamspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamspaceInvite:
        """
        Get a pending invite for in a teamspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        return await self._get(
            f"/organization/teamspaces/{teamspace_id}/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamspaceInvite,
        )

    def list(
        self,
        teamspace_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TeamspaceInvite, AsyncCursorIDPage[TeamspaceInvite]]:
        """
        List all pending invites for a teamspace.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return self._get_api_list(
            f"/organization/teamspaces/{teamspace_id}/invites",
            page=AsyncCursorIDPage[TeamspaceInvite],
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
                    invite_list_params.InviteListParams,
                ),
            ),
            model=TeamspaceInvite,
        )

    async def delete(
        self,
        invite_id: str,
        *,
        teamspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a pending invite for a user in a teamspace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/organization/teamspaces/{teamspace_id}/invites/{invite_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invites.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invites.list,
        )
        self.delete = to_raw_response_wrapper(
            invites.delete,
        )


class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invites.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invites.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invites.delete,
        )


class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invites.list,
        )
        self.delete = to_streamed_response_wrapper(
            invites.delete,
        )


class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invites.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invites.delete,
        )
