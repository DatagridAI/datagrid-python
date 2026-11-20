# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import AgenticAutomation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgenticAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_scheduled(self, client: Datagrid) -> None:
        agentic_automation = client.agentic_automations.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        )
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    def test_method_create_scheduled_with_all_params(self, client: Datagrid) -> None:
        agentic_automation = client.agentic_automations.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            description="description",
            enabled=True,
            timezone="America/New_York",
        )
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    def test_raw_response_create_scheduled(self, client: Datagrid) -> None:
        response = client.agentic_automations.with_raw_response.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agentic_automation = response.parse()
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    def test_streaming_response_create_scheduled(self, client: Datagrid) -> None:
        with client.agentic_automations.with_streaming_response.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agentic_automation = response.parse()
            assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgenticAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_scheduled(self, async_client: AsyncDatagrid) -> None:
        agentic_automation = await async_client.agentic_automations.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        )
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    async def test_method_create_scheduled_with_all_params(self, async_client: AsyncDatagrid) -> None:
        agentic_automation = await async_client.agentic_automations.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            description="description",
            enabled=True,
            timezone="America/New_York",
        )
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    async def test_raw_response_create_scheduled(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agentic_automations.with_raw_response.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agentic_automation = await response.parse()
        assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

    @parametrize
    async def test_streaming_response_create_scheduled(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agentic_automations.with_streaming_response.create_scheduled(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agentic_automation = await response.parse()
            assert_matches_type(AgenticAutomation, agentic_automation, path=["response"])

        assert cast(Any, response.is_closed) is True
