# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import ConverseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_converse(self, client: Datagrid) -> None:
        client_ = client.converse(
            prompt="prompt",
        )
        assert_matches_type(ConverseResponse, client_, path=["response"])

    @parametrize
    def test_method_converse_with_all_params(self, client: Datagrid) -> None:
        client_ = client.converse(
            prompt="prompt",
            agent_id="agent_id",
            config={
                "agent_model": "magpie-1",
                "knowledge_ids": ["string"],
                "system_prompt": "system_prompt",
            },
            conversation_id="conversation_id",
            stream=False,
        )
        assert_matches_type(ConverseResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_converse(self, client: Datagrid) -> None:
        response = client.with_raw_response.converse(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ConverseResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_converse(self, client: Datagrid) -> None:
        with client.with_streaming_response.converse(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ConverseResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_converse(self, async_client: AsyncDatagrid) -> None:
        client = await async_client.converse(
            prompt="prompt",
        )
        assert_matches_type(ConverseResponse, client, path=["response"])

    @parametrize
    async def test_method_converse_with_all_params(self, async_client: AsyncDatagrid) -> None:
        client = await async_client.converse(
            prompt="prompt",
            agent_id="agent_id",
            config={
                "agent_model": "magpie-1",
                "knowledge_ids": ["string"],
                "system_prompt": "system_prompt",
            },
            conversation_id="conversation_id",
            stream=False,
        )
        assert_matches_type(ConverseResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_converse(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.with_raw_response.converse(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ConverseResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_converse(self, async_client: AsyncDatagrid) -> None:
        async with async_client.with_streaming_response.converse(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ConverseResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
