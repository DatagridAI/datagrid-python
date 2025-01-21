# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check_api_health(self, client: Datagrid) -> None:
        health = client.health.check_api_health()
        assert health is None

    @parametrize
    def test_raw_response_check_api_health(self, client: Datagrid) -> None:
        response = client.health.with_raw_response.check_api_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert health is None

    @parametrize
    def test_streaming_response_check_api_health(self, client: Datagrid) -> None:
        with client.health.with_streaming_response.check_api_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert health is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_check_api_health(self, async_client: AsyncDatagrid) -> None:
        health = await async_client.health.check_api_health()
        assert health is None

    @parametrize
    async def test_raw_response_check_api_health(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.health.with_raw_response.check_api_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert health is None

    @parametrize
    async def test_streaming_response_check_api_health(self, async_client: AsyncDatagrid) -> None:
        async with async_client.health.with_streaming_response.check_api_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert health is None

        assert cast(Any, response.is_closed) is True
