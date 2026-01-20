# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import page_list_params, page_create_params, page_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorIDPage, AsyncCursorIDPage
from ..types.page import Page
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent: Optional[page_create_params.Parent] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Create a new page

        Args:
          name: The name of the page

          parent: The parent page to nest this page under. If not provided, the page will be
              created at the root level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pages",
            body=maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                },
                page_create_params.PageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def retrieve(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Get details of a specific page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._get(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def update(
        self,
        page_id: str,
        *,
        name: Optional[str] | Omit = omit,
        parent: Optional[page_update_params.Parent] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Update a page's attributes

        Args:
          name: The new name for the page

          parent: Move the page to a different parent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._patch(
            f"/pages/{page_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        parent: page_list_params.Parent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[Page]:
        """
        List all pages for the authenticated organization

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

          parent: Filter pages by parent. Pass `{"type":"root"}` to get root-level pages, or
              `{"type":"page","page_id":"page_123"}` to get pages nested under a specific
              page. If not specified, returns all pages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pages",
            page=SyncCursorIDPage[Page],
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
                        "parent": parent,
                    },
                    page_list_params.PageListParams,
                ),
            ),
            model=Page,
        )

    def delete(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a page.

        The page must have no children or all its children must have been
        deleted before invoking this API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent: Optional[page_create_params.Parent] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Create a new page

        Args:
          name: The name of the page

          parent: The parent page to nest this page under. If not provided, the page will be
              created at the root level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pages",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                },
                page_create_params.PageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def retrieve(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Get details of a specific page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._get(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def update(
        self,
        page_id: str,
        *,
        name: Optional[str] | Omit = omit,
        parent: Optional[page_update_params.Parent] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Update a page's attributes

        Args:
          name: The new name for the page

          parent: Move the page to a different parent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._patch(
            f"/pages/{page_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        parent: page_list_params.Parent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Page, AsyncCursorIDPage[Page]]:
        """
        List all pages for the authenticated organization

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

          parent: Filter pages by parent. Pass `{"type":"root"}` to get root-level pages, or
              `{"type":"page","page_id":"page_123"}` to get pages nested under a specific
              page. If not specified, returns all pages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pages",
            page=AsyncCursorIDPage[Page],
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
                        "parent": parent,
                    },
                    page_list_params.PageListParams,
                ),
            ),
            model=Page,
        )

    async def delete(
        self,
        page_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a page.

        The page must have no children or all its children must have been
        deleted before invoking this API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/pages/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.create = to_raw_response_wrapper(
            pages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pages.update,
        )
        self.list = to_raw_response_wrapper(
            pages.list,
        )
        self.delete = to_raw_response_wrapper(
            pages.delete,
        )


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.create = async_to_raw_response_wrapper(
            pages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pages.update,
        )
        self.list = async_to_raw_response_wrapper(
            pages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pages.delete,
        )


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.create = to_streamed_response_wrapper(
            pages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pages.update,
        )
        self.list = to_streamed_response_wrapper(
            pages.list,
        )
        self.delete = to_streamed_response_wrapper(
            pages.delete,
        )


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.create = async_to_streamed_response_wrapper(
            pages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pages.delete,
        )
