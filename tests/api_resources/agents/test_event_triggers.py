# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.agents import (
    EventTriggerListResponse,
    EventTriggerCreateResponse,
    EventTriggerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventTriggers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        )
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
            description="description",
            name="name",
            response_thread="create_new_thread_each_time",
            run_conditions="run_conditions",
        )
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.agents.event_triggers.with_raw_response.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = response.parse()
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.agents.event_triggers.with_streaming_response.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = response.parse()
            assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.event_triggers.with_raw_response.create(
                agent_id="",
                enabled=True,
                trigger_event="trigger_event",
                trigger_source="procore",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
            description="description",
            enabled=True,
            name="name",
            response_thread="create_new_thread_each_time",
            run_conditions="run_conditions",
            trigger_event="trigger_event",
        )
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.agents.event_triggers.with_raw_response.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = response.parse()
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.agents.event_triggers.with_streaming_response.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = response.parse()
            assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.event_triggers.with_raw_response.update(
                trigger_id="trigger_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.agents.event_triggers.with_raw_response.update(
                trigger_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.list(
            "agent_id",
        )
        assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.agents.event_triggers.with_raw_response.list(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = response.parse()
        assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.agents.event_triggers.with_streaming_response.list(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = response.parse()
            assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.event_triggers.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        event_trigger = client.agents.event_triggers.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )
        assert event_trigger is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.agents.event_triggers.with_raw_response.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = response.parse()
        assert event_trigger is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.agents.event_triggers.with_streaming_response.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = response.parse()
            assert event_trigger is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.event_triggers.with_raw_response.delete(
                trigger_id="trigger_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.agents.event_triggers.with_raw_response.delete(
                trigger_id="",
                agent_id="agent_id",
            )


class TestAsyncEventTriggers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        )
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
            description="description",
            name="name",
            response_thread="create_new_thread_each_time",
            run_conditions="run_conditions",
        )
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.event_triggers.with_raw_response.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = await response.parse()
        assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.event_triggers.with_streaming_response.create(
            agent_id="agent_id",
            enabled=True,
            trigger_event="trigger_event",
            trigger_source="procore",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = await response.parse()
            assert_matches_type(EventTriggerCreateResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.create(
                agent_id="",
                enabled=True,
                trigger_event="trigger_event",
                trigger_source="procore",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
            description="description",
            enabled=True,
            name="name",
            response_thread="create_new_thread_each_time",
            run_conditions="run_conditions",
            trigger_event="trigger_event",
        )
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.event_triggers.with_raw_response.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = await response.parse()
        assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.event_triggers.with_streaming_response.update(
            trigger_id="trigger_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = await response.parse()
            assert_matches_type(EventTriggerUpdateResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.update(
                trigger_id="trigger_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.update(
                trigger_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.list(
            "agent_id",
        )
        assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.event_triggers.with_raw_response.list(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = await response.parse()
        assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.event_triggers.with_streaming_response.list(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = await response.parse()
            assert_matches_type(EventTriggerListResponse, event_trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        event_trigger = await async_client.agents.event_triggers.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )
        assert event_trigger is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.event_triggers.with_raw_response.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_trigger = await response.parse()
        assert event_trigger is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.event_triggers.with_streaming_response.delete(
            trigger_id="trigger_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_trigger = await response.parse()
            assert event_trigger is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.delete(
                trigger_id="trigger_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.agents.event_triggers.with_raw_response.delete(
                trigger_id="",
                agent_id="agent_id",
            )
