# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    Connection,
    RedirectURLResponse,
)
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        connection = client.connections.create(
            connector_id="connector_id",
        )
        assert_matches_type(RedirectURLResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.connections.with_raw_response.create(
            connector_id="connector_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(RedirectURLResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.connections.with_streaming_response.create(
            connector_id="connector_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(RedirectURLResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        connection = client.connections.retrieve(
            "connection_id",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.connections.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.connections.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        connection = client.connections.update(
            connection_id="connection_id",
            name="name",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.connections.with_raw_response.update(
            connection_id="connection_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.connections.with_streaming_response.update(
            connection_id="connection_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.update(
                connection_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        connection = client.connections.list()
        assert_matches_type(SyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        connection = client.connections.list(
            after="after",
            before="before",
            connector_id="connector_id",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(SyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(SyncCursorIDPage[Connection], connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        connection = client.connections.delete(
            "connection_id",
        )
        assert connection is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.connections.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.connections.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.delete(
                "",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.create(
            connector_id="connector_id",
        )
        assert_matches_type(RedirectURLResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connections.with_raw_response.create(
            connector_id="connector_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(RedirectURLResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connections.with_streaming_response.create(
            connector_id="connector_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(RedirectURLResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.retrieve(
            "connection_id",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connections.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connections.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.update(
            connection_id="connection_id",
            name="name",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connections.with_raw_response.update(
            connection_id="connection_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connections.with_streaming_response.update(
            connection_id="connection_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.update(
                connection_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.list()
        assert_matches_type(AsyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.list(
            after="after",
            before="before",
            connector_id="connector_id",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Connection], connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Connection], connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        connection = await async_client.connections.delete(
            "connection_id",
        )
        assert connection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connections.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connections.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.delete(
                "",
            )
