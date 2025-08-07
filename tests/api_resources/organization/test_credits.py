# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.organization import CreditsReport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Datagrid) -> None:
        credit = client.organization.credits.get()
        assert_matches_type(CreditsReport, credit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Datagrid) -> None:
        response = client.organization.credits.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditsReport, credit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Datagrid) -> None:
        with client.organization.credits.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditsReport, credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncDatagrid) -> None:
        credit = await async_client.organization.credits.get()
        assert_matches_type(CreditsReport, credit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.credits.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditsReport, credit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.credits.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditsReport, credit, path=["response"])

        assert cast(Any, response.is_closed) is True
