# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.organization import user_list_params, user_update_params
from ...types.organization.organization_user import OrganizationUser

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUser:
        """
        Retrieve details of a specific user in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/organization/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUser,
        )

    def update(
        self,
        user_id: str,
        *,
        role: Literal["admin", "member"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUser:
        """
        Update user permissions in the organization.

        Args:
          role: The role to assign to the user in the organization. Available roles: admin,
              member

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/organization/users/{user_id}",
            body=maybe_transform({"role": role}, user_update_params.UserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUser,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[OrganizationUser]:
        """
        Retrieve a list of users in the specified organization.

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

          search: Search term to filter users by name or email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organization/users",
            page=SyncCursorIDPage[OrganizationUser],
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
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=OrganizationUser,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUser:
        """
        Retrieve details of a specific user in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/organization/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUser,
        )

    async def update(
        self,
        user_id: str,
        *,
        role: Literal["admin", "member"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUser:
        """
        Update user permissions in the organization.

        Args:
          role: The role to assign to the user in the organization. Available roles: admin,
              member

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/organization/users/{user_id}",
            body=await async_maybe_transform({"role": role}, user_update_params.UserUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUser,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OrganizationUser, AsyncCursorIDPage[OrganizationUser]]:
        """
        Retrieve a list of users in the specified organization.

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

          search: Search term to filter users by name or email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organization/users",
            page=AsyncCursorIDPage[OrganizationUser],
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
                        "search": search,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=OrganizationUser,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
