# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import DataView, DataViewListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        data_view = client.data_views.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        )
        assert_matches_type(DataView, data_view, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.data_views.with_raw_response.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = response.parse()
        assert_matches_type(DataView, data_view, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.data_views.with_streaming_response.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = response.parse()
            assert_matches_type(DataView, data_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        data_view = client.data_views.list(
            service_account_id="service_account_id",
        )
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        data_view = client.data_views.list(
            service_account_id="service_account_id",
            knowledge_id="knowledge_id",
            limit=1,
            offset=0,
        )
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.data_views.with_raw_response.list(
            service_account_id="service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = response.parse()
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.data_views.with_streaming_response.list(
            service_account_id="service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = response.parse()
            assert_matches_type(DataViewListResponse, data_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        data_view = client.data_views.delete(
            "data_view_id",
        )
        assert data_view is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.data_views.with_raw_response.delete(
            "data_view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = response.parse()
        assert data_view is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.data_views.with_streaming_response.delete(
            "data_view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = response.parse()
            assert data_view is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_view_id` but received ''"):
            client.data_views.with_raw_response.delete(
                "",
            )


class TestAsyncDataViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        data_view = await async_client.data_views.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        )
        assert_matches_type(DataView, data_view, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.with_raw_response.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = await response.parse()
        assert_matches_type(DataView, data_view, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.with_streaming_response.create(
            bigquery_dataset_name="bigquery_dataset_name",
            knowledge_id="knowledge_id",
            service_account_id="service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = await response.parse()
            assert_matches_type(DataView, data_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        data_view = await async_client.data_views.list(
            service_account_id="service_account_id",
        )
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        data_view = await async_client.data_views.list(
            service_account_id="service_account_id",
            knowledge_id="knowledge_id",
            limit=1,
            offset=0,
        )
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.with_raw_response.list(
            service_account_id="service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = await response.parse()
        assert_matches_type(DataViewListResponse, data_view, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.with_streaming_response.list(
            service_account_id="service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = await response.parse()
            assert_matches_type(DataViewListResponse, data_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        data_view = await async_client.data_views.delete(
            "data_view_id",
        )
        assert data_view is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.with_raw_response.delete(
            "data_view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_view = await response.parse()
        assert data_view is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.with_streaming_response.delete(
            "data_view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_view = await response.parse()
            assert data_view is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_view_id` but received ''"):
            await async_client.data_views.with_raw_response.delete(
                "",
            )
