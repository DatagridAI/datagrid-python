# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorIDPage, AsyncCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.organization import teamspace_list_params, teamspace_patch_params, teamspace_create_params
from ...types.organization.teamspace import Teamspace

__all__ = ["TeamspacesResource", "AsyncTeamspacesResource"]


class TeamspacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return TeamspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return TeamspacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access: Literal["open", "closed"],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Create a new teamspace within your organization.

        Args:
          access: Open teamspaces allow all organization members to join without admin approval.
              Access for users who join this way is limited to conversations with agents in
              this teamspace.

              Closed teamspaces require admin approval to join.

          name: The name of the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organization/teamspaces",
            body=maybe_transform(
                {
                    "access": access,
                    "name": name,
                },
                teamspace_create_params.TeamspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )

    def retrieve(
        self,
        teamspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Retrieve a specific teamspace by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return self._get(
            f"/organization/teamspaces/{teamspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )

    def list(
        self,
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
    ) -> SyncCursorIDPage[Teamspace]:
        """
        Returns the list of teamspaces within your organization.

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
        return self._get_api_list(
            "/organization/teamspaces",
            page=SyncCursorIDPage[Teamspace],
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
                    teamspace_list_params.TeamspaceListParams,
                ),
            ),
            model=Teamspace,
        )

    def patch(
        self,
        teamspace_id: str,
        *,
        access: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Update the name and/or access settings of a teamspace.

        Args:
          access: Open teamspaces allow all organization members to join without admin approval.
              Access for users who join this way is limited to conversations with agents in
              this teamspace.

              Closed teamspaces require admin approval to join.

          name: The new name of the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return self._patch(
            f"/organization/teamspaces/{teamspace_id}",
            body=maybe_transform(
                {
                    "access": access,
                    "name": name,
                },
                teamspace_patch_params.TeamspacePatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )


class AsyncTeamspacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncTeamspacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access: Literal["open", "closed"],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Create a new teamspace within your organization.

        Args:
          access: Open teamspaces allow all organization members to join without admin approval.
              Access for users who join this way is limited to conversations with agents in
              this teamspace.

              Closed teamspaces require admin approval to join.

          name: The name of the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organization/teamspaces",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "name": name,
                },
                teamspace_create_params.TeamspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )

    async def retrieve(
        self,
        teamspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Retrieve a specific teamspace by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return await self._get(
            f"/organization/teamspaces/{teamspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )

    def list(
        self,
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
    ) -> AsyncPaginator[Teamspace, AsyncCursorIDPage[Teamspace]]:
        """
        Returns the list of teamspaces within your organization.

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
        return self._get_api_list(
            "/organization/teamspaces",
            page=AsyncCursorIDPage[Teamspace],
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
                    teamspace_list_params.TeamspaceListParams,
                ),
            ),
            model=Teamspace,
        )

    async def patch(
        self,
        teamspace_id: str,
        *,
        access: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamspace:
        """
        Update the name and/or access settings of a teamspace.

        Args:
          access: Open teamspaces allow all organization members to join without admin approval.
              Access for users who join this way is limited to conversations with agents in
              this teamspace.

              Closed teamspaces require admin approval to join.

          name: The new name of the teamspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not teamspace_id:
            raise ValueError(f"Expected a non-empty value for `teamspace_id` but received {teamspace_id!r}")
        return await self._patch(
            f"/organization/teamspaces/{teamspace_id}",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "name": name,
                },
                teamspace_patch_params.TeamspacePatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Teamspace,
        )


class TeamspacesResourceWithRawResponse:
    def __init__(self, teamspaces: TeamspacesResource) -> None:
        self._teamspaces = teamspaces

        self.create = to_raw_response_wrapper(
            teamspaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            teamspaces.retrieve,
        )
        self.list = to_raw_response_wrapper(
            teamspaces.list,
        )
        self.patch = to_raw_response_wrapper(
            teamspaces.patch,
        )


class AsyncTeamspacesResourceWithRawResponse:
    def __init__(self, teamspaces: AsyncTeamspacesResource) -> None:
        self._teamspaces = teamspaces

        self.create = async_to_raw_response_wrapper(
            teamspaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            teamspaces.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            teamspaces.list,
        )
        self.patch = async_to_raw_response_wrapper(
            teamspaces.patch,
        )


class TeamspacesResourceWithStreamingResponse:
    def __init__(self, teamspaces: TeamspacesResource) -> None:
        self._teamspaces = teamspaces

        self.create = to_streamed_response_wrapper(
            teamspaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            teamspaces.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            teamspaces.list,
        )
        self.patch = to_streamed_response_wrapper(
            teamspaces.patch,
        )


class AsyncTeamspacesResourceWithStreamingResponse:
    def __init__(self, teamspaces: AsyncTeamspacesResource) -> None:
        self._teamspaces = teamspaces

        self.create = async_to_streamed_response_wrapper(
            teamspaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            teamspaces.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            teamspaces.list,
        )
        self.patch = async_to_streamed_response_wrapper(
            teamspaces.patch,
        )
