# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.voice import VoiceOrchestratorTask, VoiceOrchestratorTaskList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrchestratorTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        orchestrator_task = client.voice.orchestrator_tasks.retrieve(
            "task_id",
        )
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.voice.orchestrator_tasks.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = response.parse()
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.voice.orchestrator_tasks.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = response.parse()
            assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.voice.orchestrator_tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        orchestrator_task = client.voice.orchestrator_tasks.list()
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        orchestrator_task = client.voice.orchestrator_tasks.list(
            conversation_id="conversation_id",
            limit=1,
            status=["string"],
        )
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.voice.orchestrator_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = response.parse()
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.voice.orchestrator_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = response.parse()
            assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_acknowledge(self, client: Datagrid) -> None:
        orchestrator_task = client.voice.orchestrator_tasks.acknowledge(
            "task_id",
        )
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    def test_raw_response_acknowledge(self, client: Datagrid) -> None:
        response = client.voice.orchestrator_tasks.with_raw_response.acknowledge(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = response.parse()
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    def test_streaming_response_acknowledge(self, client: Datagrid) -> None:
        with client.voice.orchestrator_tasks.with_streaming_response.acknowledge(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = response.parse()
            assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_acknowledge(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.voice.orchestrator_tasks.with_raw_response.acknowledge(
                "",
            )


class TestAsyncOrchestratorTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        orchestrator_task = await async_client.voice.orchestrator_tasks.retrieve(
            "task_id",
        )
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.voice.orchestrator_tasks.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = await response.parse()
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.voice.orchestrator_tasks.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = await response.parse()
            assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.voice.orchestrator_tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        orchestrator_task = await async_client.voice.orchestrator_tasks.list()
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        orchestrator_task = await async_client.voice.orchestrator_tasks.list(
            conversation_id="conversation_id",
            limit=1,
            status=["string"],
        )
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.voice.orchestrator_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = await response.parse()
        assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.voice.orchestrator_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = await response.parse()
            assert_matches_type(VoiceOrchestratorTaskList, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_acknowledge(self, async_client: AsyncDatagrid) -> None:
        orchestrator_task = await async_client.voice.orchestrator_tasks.acknowledge(
            "task_id",
        )
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    async def test_raw_response_acknowledge(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.voice.orchestrator_tasks.with_raw_response.acknowledge(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orchestrator_task = await response.parse()
        assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

    @parametrize
    async def test_streaming_response_acknowledge(self, async_client: AsyncDatagrid) -> None:
        async with async_client.voice.orchestrator_tasks.with_streaming_response.acknowledge(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orchestrator_task = await response.parse()
            assert_matches_type(VoiceOrchestratorTask, orchestrator_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_acknowledge(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.voice.orchestrator_tasks.with_raw_response.acknowledge(
                "",
            )
