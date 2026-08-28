# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.organization import (
    McpServer,
    ListMcpServersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.create(
            base_url="https://example.com",
            name="name",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.create(
            base_url="https://example.com",
            name="name",
            authorization="authorization",
            authorization_secret_id="authorization_secret_id",
            icon_url="icon_url",
            protocol_version="protocol_version",
            transport="http",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.organization.mcp_servers.with_raw_response.create(
            base_url="https://example.com",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.organization.mcp_servers.with_streaming_response.create(
            base_url="https://example.com",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.retrieve(
            "server_id",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.organization.mcp_servers.with_raw_response.retrieve(
            "server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.organization.mcp_servers.with_streaming_response.retrieve(
            "server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.organization.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.update(
            server_id="server_id",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.update(
            server_id="server_id",
            authorization="authorization",
            authorization_secret_id="authorization_secret_id",
            base_url="https://example.com",
            icon_url="icon_url",
            name="name",
            protocol_version="protocol_version",
            transport="http",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.organization.mcp_servers.with_raw_response.update(
            server_id="server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.organization.mcp_servers.with_streaming_response.update(
            server_id="server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.organization.mcp_servers.with_raw_response.update(
                server_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.list()
        assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.organization.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.organization.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        mcp_server = client.organization.mcp_servers.delete(
            "server_id",
        )
        assert mcp_server is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.organization.mcp_servers.with_raw_response.delete(
            "server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert mcp_server is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.organization.mcp_servers.with_streaming_response.delete(
            "server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            client.organization.mcp_servers.with_raw_response.delete(
                "",
            )


class TestAsyncMcpServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.create(
            base_url="https://example.com",
            name="name",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.create(
            base_url="https://example.com",
            name="name",
            authorization="authorization",
            authorization_secret_id="authorization_secret_id",
            icon_url="icon_url",
            protocol_version="protocol_version",
            transport="http",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.mcp_servers.with_raw_response.create(
            base_url="https://example.com",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.mcp_servers.with_streaming_response.create(
            base_url="https://example.com",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.retrieve(
            "server_id",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.mcp_servers.with_raw_response.retrieve(
            "server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.mcp_servers.with_streaming_response.retrieve(
            "server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.organization.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.update(
            server_id="server_id",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.update(
            server_id="server_id",
            authorization="authorization",
            authorization_secret_id="authorization_secret_id",
            base_url="https://example.com",
            icon_url="icon_url",
            name="name",
            protocol_version="protocol_version",
            transport="http",
        )
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.mcp_servers.with_raw_response.update(
            server_id="server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServer, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.mcp_servers.with_streaming_response.update(
            server_id="server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServer, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.organization.mcp_servers.with_raw_response.update(
                server_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.list()
        assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(ListMcpServersResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        mcp_server = await async_client.organization.mcp_servers.delete(
            "server_id",
        )
        assert mcp_server is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.mcp_servers.with_raw_response.delete(
            "server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert mcp_server is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.mcp_servers.with_streaming_response.delete(
            "server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server_id` but received ''"):
            await async_client.organization.mcp_servers.with_raw_response.delete(
                "",
            )
