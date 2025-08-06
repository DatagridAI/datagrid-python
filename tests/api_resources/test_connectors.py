# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import Connector
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        connector = client.connectors.list()
        assert_matches_type(SyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        connector = client.connectors.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.connectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(SyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.connectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(SyncCursorIDPage[Connector], connector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        connector = await async_client.connectors.list()
        assert_matches_type(AsyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        connector = await async_client.connectors.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Connector], connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Connector], connector, path=["response"])

        assert cast(Any, response.is_closed) is True
