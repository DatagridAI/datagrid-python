# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import connector_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
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
from ..types.connector import Connector

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

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
    ) -> SyncCursorIDPage[Connector]:
        """
        Returns the list of available connectors that can be used to connect to
        third-party services.

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
            "/connectors",
            page=SyncCursorIDPage[Connector],
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
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=Connector,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Connector, AsyncCursorIDPage[Connector]]:
        """
        Returns the list of available connectors that can be used to connect to
        third-party services.

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
            "/connectors",
            page=AsyncCursorIDPage[Connector],
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
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=Connector,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.list = to_raw_response_wrapper(
            connectors.list,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.list = to_streamed_response_wrapper(
            connectors.list,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
