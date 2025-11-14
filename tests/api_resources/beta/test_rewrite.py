# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.beta import RewriteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRewrite:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rewrite_text(self, client: Datagrid) -> None:
        rewrite = client.beta.rewrite.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        )
        assert_matches_type(RewriteResponse, rewrite, path=["response"])

    @parametrize
    def test_raw_response_rewrite_text(self, client: Datagrid) -> None:
        response = client.beta.rewrite.with_raw_response.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rewrite = response.parse()
        assert_matches_type(RewriteResponse, rewrite, path=["response"])

    @parametrize
    def test_streaming_response_rewrite_text(self, client: Datagrid) -> None:
        with client.beta.rewrite.with_streaming_response.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rewrite = response.parse()
            assert_matches_type(RewriteResponse, rewrite, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRewrite:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rewrite_text(self, async_client: AsyncDatagrid) -> None:
        rewrite = await async_client.beta.rewrite.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        )
        assert_matches_type(RewriteResponse, rewrite, path=["response"])

    @parametrize
    async def test_raw_response_rewrite_text(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.beta.rewrite.with_raw_response.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rewrite = await response.parse()
        assert_matches_type(RewriteResponse, rewrite, path=["response"])

    @parametrize
    async def test_streaming_response_rewrite_text(self, async_client: AsyncDatagrid) -> None:
        async with async_client.beta.rewrite.with_streaming_response.rewrite_text(
            full_text="full_text",
            prompt="prompt",
            text_to_rewrite="text_to_rewrite",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rewrite = await response.parse()
            assert_matches_type(RewriteResponse, rewrite, path=["response"])

        assert cast(Any, response.is_closed) is True
