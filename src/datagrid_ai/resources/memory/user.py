# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import is_given, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._constants import DEFAULT_TIMEOUT
from ..._base_client import make_request_options
from ...types.memory import user_list_params, user_create_params
from ...types.memory.user_memory import UserMemory
from ...types.memory.user_list_response import UserListResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        memory: str,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        user_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserMemory:
        """
        Create a user memory

        Args:
          agent_id: The agent ID of the user memory.

          memory: The memory of the user memory.

          context: The context of the user memory.

          user_prompt: The user prompt of the user memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 120
        return self._post(
            "/user-memories",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "memory": memory,
                    "context": context,
                    "user_prompt": user_prompt,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMemory,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        List the memories for a given user and agent that the user has access to

        Args:
          limit: The limit on the number of objects to return, ranging between 1 and 100.

          offset: A cursor to use in pagination. `offset` is an integer that defines your place in
              the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `offset=100` to fetch
              the next page of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user-memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a user memory

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_memory_id:
            raise ValueError(f"Expected a non-empty value for `user_memory_id` but received {user_memory_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user-memories/{user_memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        memory: str,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        user_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserMemory:
        """
        Create a user memory

        Args:
          agent_id: The agent ID of the user memory.

          memory: The memory of the user memory.

          context: The context of the user memory.

          user_prompt: The user prompt of the user memory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 120
        return await self._post(
            "/user-memories",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "memory": memory,
                    "context": context,
                    "user_prompt": user_prompt,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMemory,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        List the memories for a given user and agent that the user has access to

        Args:
          limit: The limit on the number of objects to return, ranging between 1 and 100.

          offset: A cursor to use in pagination. `offset` is an integer that defines your place in
              the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `offset=100` to fetch
              the next page of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user-memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_memory_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a user memory

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_memory_id:
            raise ValueError(f"Expected a non-empty value for `user_memory_id` but received {user_memory_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user-memories/{user_memory_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_raw_response_wrapper(
            user.create,
        )
        self.list = to_raw_response_wrapper(
            user.list,
        )
        self.delete = to_raw_response_wrapper(
            user.delete,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_raw_response_wrapper(
            user.create,
        )
        self.list = async_to_raw_response_wrapper(
            user.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user.delete,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_streamed_response_wrapper(
            user.create,
        )
        self.list = to_streamed_response_wrapper(
            user.list,
        )
        self.delete = to_streamed_response_wrapper(
            user.delete,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_streamed_response_wrapper(
            user.create,
        )
        self.list = async_to_streamed_response_wrapper(
            user.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user.delete,
        )
