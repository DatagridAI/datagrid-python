# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.pagination import SyncCursorPage, AsyncCursorPage
from datagrid_ai.types.knowledge.tables import Record

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        record = client.knowledge.tables.records.list(
            table_id="table_id",
        )
        assert_matches_type(SyncCursorPage[Record], record, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        record = client.knowledge.tables.records.list(
            table_id="table_id",
            limit=1,
            next="next",
        )
        assert_matches_type(SyncCursorPage[Record], record, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.knowledge.tables.records.with_raw_response.list(
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(SyncCursorPage[Record], record, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.knowledge.tables.records.with_streaming_response.list(
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(SyncCursorPage[Record], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id` but received ''"):
            client.knowledge.tables.records.with_raw_response.list(
                table_id="",
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        record = await async_client.knowledge.tables.records.list(
            table_id="table_id",
        )
        assert_matches_type(AsyncCursorPage[Record], record, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        record = await async_client.knowledge.tables.records.list(
            table_id="table_id",
            limit=1,
            next="next",
        )
        assert_matches_type(AsyncCursorPage[Record], record, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.tables.records.with_raw_response.list(
            table_id="table_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(AsyncCursorPage[Record], record, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.tables.records.with_streaming_response.list(
            table_id="table_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(AsyncCursorPage[Record], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id` but received ''"):
            await async_client.knowledge.tables.records.with_raw_response.list(
                table_id="",
            )
