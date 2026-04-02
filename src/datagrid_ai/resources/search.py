# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import search_search_params, search_search_ai_params, search_search_tree_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_ai_result import SearchAIResult
from ..types.search_tree_result import SearchTreeResult
from ..types.search_search_response import SearchSearchResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def search(
        self,
        *,
        query: str,
        knowledge_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_types: List[Literal["rows", "tables", "files", "pages", "cells"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchSearchResponse:
        """[DEPRECATED] Search across knowledge.

        Use /search/ai for AI-powered generative
        search or /search/tree for merged context tree results.

        Args:
          query: The search query to run against knowledge. Must contain at least one
              non-whitespace character after trimming.

          knowledge_ids: Optional list of knowledge IDs to scope the search to.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_types: Filter results by record type in the vector database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "knowledge_ids": knowledge_ids,
                        "limit": limit,
                        "next": next,
                        "record_types": record_types,
                    },
                    search_search_params.SearchSearchParams,
                ),
            ),
            cast_to=SearchSearchResponse,
        )

    def search_ai(
        self,
        *,
        query: str,
        limit: Optional[int] | Omit = omit,
        record_types: Optional[List[Literal["rows", "tables", "files", "pages", "cells"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchAIResult:
        """
        AI-powered search that retrieves relevant knowledge from your teamspace, builds
        a merged context, and generates a natural language answer with numbered source
        citations. The response includes the generated answer, the sources cited (with
        links and metadata), and the full search tree results for reference. Use this
        when you want an AI-generated summary answer grounded in your team's data.

        Args:
          query: The natural language search query. The AI will search your indexed knowledge and
              generate an answer.

          limit: Maximum number of search results to consider when generating the answer.

          record_types: Optional filter to restrict search to specific record types (rows, tables,
              files, pages, cells).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search/ai",
            body=maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "record_types": record_types,
                },
                search_search_ai_params.SearchSearchAIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchAIResult,
        )

    def search_tree(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_types: List[Literal["rows", "tables", "files", "pages", "cells"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchTreeResult:
        """
        Search across your teamspace's indexed knowledge and return results as a
        hierarchical context tree. Results are grouped by source (datasets, files,
        pages) with navigation items for quick access. Supports pagination via
        cursor-based `next` parameter. This endpoint is the foundation for the AI Search
        endpoint — use this when you need structured results without AI summarization.

        Args:
          query: The natural language search query.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_types: Filter results by record type in the vector database. When omitted, all record
              types are searched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/tree",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "next": next,
                        "record_types": record_types,
                    },
                    search_search_tree_params.SearchSearchTreeParams,
                ),
            ),
            cast_to=SearchTreeResult,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def search(
        self,
        *,
        query: str,
        knowledge_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_types: List[Literal["rows", "tables", "files", "pages", "cells"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchSearchResponse:
        """[DEPRECATED] Search across knowledge.

        Use /search/ai for AI-powered generative
        search or /search/tree for merged context tree results.

        Args:
          query: The search query to run against knowledge. Must contain at least one
              non-whitespace character after trimming.

          knowledge_ids: Optional list of knowledge IDs to scope the search to.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_types: Filter results by record type in the vector database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "knowledge_ids": knowledge_ids,
                        "limit": limit,
                        "next": next,
                        "record_types": record_types,
                    },
                    search_search_params.SearchSearchParams,
                ),
            ),
            cast_to=SearchSearchResponse,
        )

    async def search_ai(
        self,
        *,
        query: str,
        limit: Optional[int] | Omit = omit,
        record_types: Optional[List[Literal["rows", "tables", "files", "pages", "cells"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchAIResult:
        """
        AI-powered search that retrieves relevant knowledge from your teamspace, builds
        a merged context, and generates a natural language answer with numbered source
        citations. The response includes the generated answer, the sources cited (with
        links and metadata), and the full search tree results for reference. Use this
        when you want an AI-generated summary answer grounded in your team's data.

        Args:
          query: The natural language search query. The AI will search your indexed knowledge and
              generate an answer.

          limit: Maximum number of search results to consider when generating the answer.

          record_types: Optional filter to restrict search to specific record types (rows, tables,
              files, pages, cells).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search/ai",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "record_types": record_types,
                },
                search_search_ai_params.SearchSearchAIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchAIResult,
        )

    async def search_tree(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_types: List[Literal["rows", "tables", "files", "pages", "cells"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchTreeResult:
        """
        Search across your teamspace's indexed knowledge and return results as a
        hierarchical context tree. Results are grouped by source (datasets, files,
        pages) with navigation items for quick access. Supports pagination via
        cursor-based `next` parameter. This endpoint is the foundation for the AI Search
        endpoint — use this when you need structured results without AI summarization.

        Args:
          query: The natural language search query.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_types: Filter results by record type in the vector database. When omitted, all record
              types are searched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/tree",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "next": next,
                        "record_types": record_types,
                    },
                    search_search_tree_params.SearchSearchTreeParams,
                ),
            ),
            cast_to=SearchTreeResult,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                search.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_ai = to_raw_response_wrapper(
            search.search_ai,
        )
        self.search_tree = to_raw_response_wrapper(
            search.search_tree,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                search.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_ai = async_to_raw_response_wrapper(
            search.search_ai,
        )
        self.search_tree = async_to_raw_response_wrapper(
            search.search_tree,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                search.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_ai = to_streamed_response_wrapper(
            search.search_ai,
        )
        self.search_tree = to_streamed_response_wrapper(
            search.search_tree,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                search.search,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_ai = async_to_streamed_response_wrapper(
            search.search_ai,
        )
        self.search_tree = async_to_streamed_response_wrapper(
            search.search_tree,
        )
