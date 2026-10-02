# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.knowledge.tables import summary_list_params
from ....types.knowledge.tables.summary import Summary

__all__ = ["SummariesResource", "AsyncSummariesResource"]


class SummariesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return SummariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return SummariesResourceWithStreamingResponse(self)

    def list(
        self,
        table_id: str,
        *,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_type: Literal["row", "table", "file", "page"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Summary]:
        """Returns indexed summary content for a knowledge table.

        Use `record_type=row`
        (the default) for per-row summaries, `record_type=table` for the table-level
        summary, `record_type=file` for file-level overviews, or `record_type=page` for
        page extraction bodies. This endpoint reflects the current index state and does
        not consume AI credits.

        Args:
          limit: The limit on the number of objects to return, ranging between 1 and 1000.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_type: Which summary variant to return. `row` (default) returns one summary per source
              row. `table` returns the table-level summary. `file` returns file-level
              overviews. `page` returns page extraction bodies. Matches `record_type` on each
              Summary in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return self._get_api_list(
            path_template("/tables/{table_id}/summaries", table_id=table_id),
            page=SyncCursorPage[Summary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next": next,
                        "record_type": record_type,
                    },
                    summary_list_params.SummaryListParams,
                ),
            ),
            model=Summary,
        )


class AsyncSummariesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncSummariesResourceWithStreamingResponse(self)

    def list(
        self,
        table_id: str,
        *,
        limit: int | Omit = omit,
        next: str | Omit = omit,
        record_type: Literal["row", "table", "file", "page"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Summary, AsyncCursorPage[Summary]]:
        """Returns indexed summary content for a knowledge table.

        Use `record_type=row`
        (the default) for per-row summaries, `record_type=table` for the table-level
        summary, `record_type=file` for file-level overviews, or `record_type=page` for
        page extraction bodies. This endpoint reflects the current index state and does
        not consume AI credits.

        Args:
          limit: The limit on the number of objects to return, ranging between 1 and 1000.

          next: A cursor to use in pagination to continue a query from the previous request.
              This is automatically added when the request has more results to fetch.

          record_type: Which summary variant to return. `row` (default) returns one summary per source
              row. `table` returns the table-level summary. `file` returns file-level
              overviews. `page` returns page extraction bodies. Matches `record_type` on each
              Summary in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return self._get_api_list(
            path_template("/tables/{table_id}/summaries", table_id=table_id),
            page=AsyncCursorPage[Summary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next": next,
                        "record_type": record_type,
                    },
                    summary_list_params.SummaryListParams,
                ),
            ),
            model=Summary,
        )


class SummariesResourceWithRawResponse:
    def __init__(self, summaries: SummariesResource) -> None:
        self._summaries = summaries

        self.list = to_raw_response_wrapper(
            summaries.list,
        )


class AsyncSummariesResourceWithRawResponse:
    def __init__(self, summaries: AsyncSummariesResource) -> None:
        self._summaries = summaries

        self.list = async_to_raw_response_wrapper(
            summaries.list,
        )


class SummariesResourceWithStreamingResponse:
    def __init__(self, summaries: SummariesResource) -> None:
        self._summaries = summaries

        self.list = to_streamed_response_wrapper(
            summaries.list,
        )


class AsyncSummariesResourceWithStreamingResponse:
    def __init__(self, summaries: AsyncSummariesResource) -> None:
        self._summaries = summaries

        self.list = async_to_streamed_response_wrapper(
            summaries.list,
        )
