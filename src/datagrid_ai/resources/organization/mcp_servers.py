# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organization import mcp_server_create_params, mcp_server_update_params
from ...types.organization.mcp_server import McpServer
from ...types.organization.list_mcp_servers_response import ListMcpServersResponse

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return McpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return McpServersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        base_url: str,
        name: str,
        authorization: Optional[str] | Omit = omit,
        authorization_secret_id: Optional[str] | Omit = omit,
        icon_url: Optional[str] | Omit = omit,
        protocol_version: Optional[str] | Omit = omit,
        transport: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Register a new MCP server in the current teamspace.

        Args:
          base_url: The HTTPS URL of the MCP server.

          authorization: Raw Authorization header value (for example, 'Bearer <token>'). Datagrid stores
              it as a secret and links it to this server. If both authorization and
              authorization_secret_id are provided, authorization takes precedence.

          authorization_secret_id: Secret ID containing the full Authorization header value to use when calling
              this MCP server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organization/mcp-servers",
            body=maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "authorization": authorization,
                    "authorization_secret_id": authorization_secret_id,
                    "icon_url": icon_url,
                    "protocol_version": protocol_version,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    def retrieve(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Retrieve a registered MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._get(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    def update(
        self,
        server_id: str,
        *,
        authorization: Optional[str] | Omit = omit,
        authorization_secret_id: Optional[str] | Omit = omit,
        base_url: str | Omit = omit,
        icon_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        protocol_version: Optional[str] | Omit = omit,
        transport: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Update a registered MCP server.

        Args:
          authorization: Raw Authorization header value (for example, 'Bearer <token>'). Datagrid stores
              it as a secret and links it to this server. Set to null to clear. If both
              authorization and authorization_secret_id are provided, authorization takes
              precedence.

          authorization_secret_id: Secret ID containing the full Authorization header value to use when calling
              this MCP server. Set to null to clear.

          base_url: The HTTPS URL of the MCP server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._patch(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            body=maybe_transform(
                {
                    "authorization": authorization,
                    "authorization_secret_id": authorization_secret_id,
                    "base_url": base_url,
                    "icon_url": icon_url,
                    "name": name,
                    "protocol_version": protocol_version,
                    "transport": transport,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListMcpServersResponse:
        """List registered MCP servers for the current teamspace."""
        return self._get(
            "/organization/mcp-servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListMcpServersResponse,
        )

    def delete(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a registered MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMcpServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncMcpServersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        base_url: str,
        name: str,
        authorization: Optional[str] | Omit = omit,
        authorization_secret_id: Optional[str] | Omit = omit,
        icon_url: Optional[str] | Omit = omit,
        protocol_version: Optional[str] | Omit = omit,
        transport: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Register a new MCP server in the current teamspace.

        Args:
          base_url: The HTTPS URL of the MCP server.

          authorization: Raw Authorization header value (for example, 'Bearer <token>'). Datagrid stores
              it as a secret and links it to this server. If both authorization and
              authorization_secret_id are provided, authorization takes precedence.

          authorization_secret_id: Secret ID containing the full Authorization header value to use when calling
              this MCP server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organization/mcp-servers",
            body=await async_maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "authorization": authorization,
                    "authorization_secret_id": authorization_secret_id,
                    "icon_url": icon_url,
                    "protocol_version": protocol_version,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    async def retrieve(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Retrieve a registered MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._get(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    async def update(
        self,
        server_id: str,
        *,
        authorization: Optional[str] | Omit = omit,
        authorization_secret_id: Optional[str] | Omit = omit,
        base_url: str | Omit = omit,
        icon_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        protocol_version: Optional[str] | Omit = omit,
        transport: Optional[Literal["http"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Update a registered MCP server.

        Args:
          authorization: Raw Authorization header value (for example, 'Bearer <token>'). Datagrid stores
              it as a secret and links it to this server. Set to null to clear. If both
              authorization and authorization_secret_id are provided, authorization takes
              precedence.

          authorization_secret_id: Secret ID containing the full Authorization header value to use when calling
              this MCP server. Set to null to clear.

          base_url: The HTTPS URL of the MCP server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._patch(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            body=await async_maybe_transform(
                {
                    "authorization": authorization,
                    "authorization_secret_id": authorization_secret_id,
                    "base_url": base_url,
                    "icon_url": icon_url,
                    "name": name,
                    "protocol_version": protocol_version,
                    "transport": transport,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListMcpServersResponse:
        """List registered MCP servers for the current teamspace."""
        return await self._get(
            "/organization/mcp-servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListMcpServersResponse,
        )

    async def delete(
        self,
        server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a registered MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/organization/mcp-servers/{server_id}", server_id=server_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_raw_response_wrapper(
            mcp_servers.delete,
        )


class AsyncMcpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp_servers.delete,
        )


class McpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            mcp_servers.delete,
        )


class AsyncMcpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_servers.delete,
        )
