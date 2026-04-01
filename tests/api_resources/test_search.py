# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    SearchAIResult,
    SearchTreeResult,
    SearchSearchResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: Datagrid) -> None:
        with pytest.warns(DeprecationWarning):
            search = client.search.search(
                query="x",
            )

        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Datagrid) -> None:
        with pytest.warns(DeprecationWarning):
            search = client.search.search(
                query="x",
                knowledge_ids=["string"],
                limit=1,
                next="next",
                record_types=["rows"],
            )

        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Datagrid) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.search.with_raw_response.search(
                query="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Datagrid) -> None:
        with pytest.warns(DeprecationWarning):
            with client.search.with_streaming_response.search(
                query="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                search = response.parse()
                assert_matches_type(SearchSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_ai(self, client: Datagrid) -> None:
        search = client.search.search_ai(
            query="query",
        )
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    def test_method_search_ai_with_all_params(self, client: Datagrid) -> None:
        search = client.search.search_ai(
            query="query",
            limit=0,
            record_types=["rows"],
        )
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    def test_raw_response_search_ai(self, client: Datagrid) -> None:
        response = client.search.with_raw_response.search_ai(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    def test_streaming_response_search_ai(self, client: Datagrid) -> None:
        with client.search.with_streaming_response.search_ai(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchAIResult, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_tree(self, client: Datagrid) -> None:
        search = client.search.search_tree(
            query="query",
        )
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    def test_method_search_tree_with_all_params(self, client: Datagrid) -> None:
        search = client.search.search_tree(
            query="query",
            limit=1,
            next="next",
            record_types=["rows"],
        )
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    def test_raw_response_search_tree(self, client: Datagrid) -> None:
        response = client.search.with_raw_response.search_tree(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    def test_streaming_response_search_tree(self, client: Datagrid) -> None:
        with client.search.with_streaming_response.search_tree(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchTreeResult, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncDatagrid) -> None:
        with pytest.warns(DeprecationWarning):
            search = await async_client.search.search(
                query="x",
            )

        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncDatagrid) -> None:
        with pytest.warns(DeprecationWarning):
            search = await async_client.search.search(
                query="x",
                knowledge_ids=["string"],
                limit=1,
                next="next",
                record_types=["rows"],
            )

        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncDatagrid) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.search.with_raw_response.search(
                query="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchSearchResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncDatagrid) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.search.with_streaming_response.search(
                query="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                search = await response.parse()
                assert_matches_type(SearchSearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_ai(self, async_client: AsyncDatagrid) -> None:
        search = await async_client.search.search_ai(
            query="query",
        )
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    async def test_method_search_ai_with_all_params(self, async_client: AsyncDatagrid) -> None:
        search = await async_client.search.search_ai(
            query="query",
            limit=0,
            record_types=["rows"],
        )
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    async def test_raw_response_search_ai(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.search.with_raw_response.search_ai(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchAIResult, search, path=["response"])

    @parametrize
    async def test_streaming_response_search_ai(self, async_client: AsyncDatagrid) -> None:
        async with async_client.search.with_streaming_response.search_ai(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchAIResult, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_tree(self, async_client: AsyncDatagrid) -> None:
        search = await async_client.search.search_tree(
            query="query",
        )
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    async def test_method_search_tree_with_all_params(self, async_client: AsyncDatagrid) -> None:
        search = await async_client.search.search_tree(
            query="query",
            limit=1,
            next="next",
            record_types=["rows"],
        )
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    async def test_raw_response_search_tree(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.search.with_raw_response.search_tree(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchTreeResult, search, path=["response"])

    @parametrize
    async def test_streaming_response_search_tree(self, async_client: AsyncDatagrid) -> None:
        async with async_client.search.with_streaming_response.search_tree(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchTreeResult, search, path=["response"])

        assert cast(Any, response.is_closed) is True
