# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    connection_provider_list_params,
    connection_provider_create_params,
    connection_provider_update_params,
)
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
from .._base_client import AsyncPaginator, make_request_options
from ..types.connection_provider import ConnectionProvider

__all__ = ["ConnectionProvidersResource", "AsyncConnectionProvidersResource"]


class ConnectionProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ConnectionProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        connector_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Create a new connection provider that specifies custom OAuth credentials for a
        connector. Verify that your OAuth app meets the connector's OAuth app settings
        requirements.

        Args:
          client_id: The OAuth client ID to use for this connector.

          client_secret: The OAuth client secret to use for this connector.

          connector_id: The connector ID this provider is configured for.

          name: The name of the connection provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connection-providers",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "connector_id": connector_id,
                    "name": name,
                },
                connection_provider_create_params.ConnectionProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    def retrieve(
        self,
        connection_provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Retrieve a specific connection provider by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        return self._get(
            f"/connection-providers/{connection_provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    def update(
        self,
        connection_provider_id: str,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Update a connection provider.

        Args:
          client_id: The OAuth client ID to use for this connector.

          client_secret: The OAuth client secret to use for this connector.

          name: The name of the connection provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        return self._patch(
            f"/connection-providers/{connection_provider_id}",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "name": name,
                },
                connection_provider_update_params.ConnectionProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        connector_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[ConnectionProvider]:
        """
        Returns the list of connection providers.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          connector_id: Filter connection providers by connector ID.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/connection-providers",
            page=SyncCursorIDPage[ConnectionProvider],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "connector_id": connector_id,
                        "limit": limit,
                    },
                    connection_provider_list_params.ConnectionProviderListParams,
                ),
            ),
            model=ConnectionProvider,
        )

    def delete(
        self,
        connection_provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a connection provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/connection-providers/{connection_provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConnectionProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncConnectionProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        connector_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Create a new connection provider that specifies custom OAuth credentials for a
        connector. Verify that your OAuth app meets the connector's OAuth app settings
        requirements.

        Args:
          client_id: The OAuth client ID to use for this connector.

          client_secret: The OAuth client secret to use for this connector.

          connector_id: The connector ID this provider is configured for.

          name: The name of the connection provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connection-providers",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "connector_id": connector_id,
                    "name": name,
                },
                connection_provider_create_params.ConnectionProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    async def retrieve(
        self,
        connection_provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Retrieve a specific connection provider by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        return await self._get(
            f"/connection-providers/{connection_provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    async def update(
        self,
        connection_provider_id: str,
        *,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionProvider:
        """
        Update a connection provider.

        Args:
          client_id: The OAuth client ID to use for this connector.

          client_secret: The OAuth client secret to use for this connector.

          name: The name of the connection provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        return await self._patch(
            f"/connection-providers/{connection_provider_id}",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "name": name,
                },
                connection_provider_update_params.ConnectionProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionProvider,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        connector_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConnectionProvider, AsyncCursorIDPage[ConnectionProvider]]:
        """
        Returns the list of connection providers.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          connector_id: Filter connection providers by connector ID.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/connection-providers",
            page=AsyncCursorIDPage[ConnectionProvider],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "connector_id": connector_id,
                        "limit": limit,
                    },
                    connection_provider_list_params.ConnectionProviderListParams,
                ),
            ),
            model=ConnectionProvider,
        )

    async def delete(
        self,
        connection_provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a connection provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `connection_provider_id` but received {connection_provider_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/connection-providers/{connection_provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConnectionProvidersResourceWithRawResponse:
    def __init__(self, connection_providers: ConnectionProvidersResource) -> None:
        self._connection_providers = connection_providers

        self.create = to_raw_response_wrapper(
            connection_providers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connection_providers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connection_providers.update,
        )
        self.list = to_raw_response_wrapper(
            connection_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            connection_providers.delete,
        )


class AsyncConnectionProvidersResourceWithRawResponse:
    def __init__(self, connection_providers: AsyncConnectionProvidersResource) -> None:
        self._connection_providers = connection_providers

        self.create = async_to_raw_response_wrapper(
            connection_providers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connection_providers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connection_providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            connection_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connection_providers.delete,
        )


class ConnectionProvidersResourceWithStreamingResponse:
    def __init__(self, connection_providers: ConnectionProvidersResource) -> None:
        self._connection_providers = connection_providers

        self.create = to_streamed_response_wrapper(
            connection_providers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connection_providers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connection_providers.update,
        )
        self.list = to_streamed_response_wrapper(
            connection_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            connection_providers.delete,
        )


class AsyncConnectionProvidersResourceWithStreamingResponse:
    def __init__(self, connection_providers: AsyncConnectionProvidersResource) -> None:
        self._connection_providers = connection_providers

        self.create = async_to_streamed_response_wrapper(
            connection_providers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connection_providers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connection_providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connection_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connection_providers.delete,
        )
