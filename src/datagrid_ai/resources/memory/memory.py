# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._memory.user)


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._memory.user)


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._memory.user)


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._memory.user)
