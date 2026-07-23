# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage
from datagrid_ai.types.agents import (
    Automation,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        automation = client.agents.automations.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        automation = client.agents.automations.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
            description="description",
            destination_id="destination_id",
            destination_type="agent_dm",
            enabled=True,
            notification_preference="always",
            output_channel_id="output_channel_id",
            output_channel_type="email",
            prompt_file_ids=["string"],
            thread_mode="new_thread",
            timezone="America/New_York",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.agents.automations.with_raw_response.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.agents.automations.with_streaming_response.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.automations.with_raw_response.create(
                agent_id="",
                cron="0 9 * * 1",
                name="name",
                prompt="prompt",
            )

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        automation = client.agents.automations.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.agents.automations.with_raw_response.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.agents.automations.with_streaming_response.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.automations.with_raw_response.retrieve(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.agents.automations.with_raw_response.retrieve(
                automation_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        automation = client.agents.automations.update(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        automation = client.agents.automations.update(
            automation_id="automation_id",
            agent_id="agent_id",
            cron="30 8 * * 1-5",
            description="description",
            destination_id="destination_id",
            destination_type="agent_dm",
            enabled=True,
            name="name",
            notification_preference="always",
            output_channel_id="output_channel_id",
            output_channel_type="email",
            prompt="prompt",
            prompt_file_ids=["string"],
            thread_mode="new_thread",
            timezone="Europe/London",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.agents.automations.with_raw_response.update(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.agents.automations.with_streaming_response.update(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.automations.with_raw_response.update(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.agents.automations.with_raw_response.update(
                automation_id="",
                agent_id="agent_id",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        automation = client.agents.automations.list(
            agent_id="agent_id",
        )
        assert_matches_type(SyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        automation = client.agents.automations.list(
            agent_id="agent_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.agents.automations.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(SyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.agents.automations.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(SyncCursorIDPage[Automation], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.automations.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        automation = client.agents.automations.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert automation is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.agents.automations.with_raw_response.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert automation is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.agents.automations.with_streaming_response.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert automation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.automations.with_raw_response.delete(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.agents.automations.with_raw_response.delete(
                automation_id="",
                agent_id="agent_id",
            )


class TestAsyncAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
            description="description",
            destination_id="destination_id",
            destination_type="agent_dm",
            enabled=True,
            notification_preference="always",
            output_channel_id="output_channel_id",
            output_channel_type="email",
            prompt_file_ids=["string"],
            thread_mode="new_thread",
            timezone="America/New_York",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.automations.with_raw_response.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.automations.with_streaming_response.create(
            agent_id="agent_id",
            cron="0 9 * * 1",
            name="name",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.automations.with_raw_response.create(
                agent_id="",
                cron="0 9 * * 1",
                name="name",
                prompt="prompt",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.automations.with_raw_response.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.automations.with_streaming_response.retrieve(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.automations.with_raw_response.retrieve(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.agents.automations.with_raw_response.retrieve(
                automation_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.update(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.update(
            automation_id="automation_id",
            agent_id="agent_id",
            cron="30 8 * * 1-5",
            description="description",
            destination_id="destination_id",
            destination_type="agent_dm",
            enabled=True,
            name="name",
            notification_preference="always",
            output_channel_id="output_channel_id",
            output_channel_type="email",
            prompt="prompt",
            prompt_file_ids=["string"],
            thread_mode="new_thread",
            timezone="Europe/London",
        )
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.automations.with_raw_response.update(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(Automation, automation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.automations.with_streaming_response.update(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(Automation, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.automations.with_raw_response.update(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.agents.automations.with_raw_response.update(
                automation_id="",
                agent_id="agent_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.list(
            agent_id="agent_id",
        )
        assert_matches_type(AsyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.list(
            agent_id="agent_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.automations.with_raw_response.list(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Automation], automation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.automations.with_streaming_response.list(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Automation], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.automations.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        automation = await async_client.agents.automations.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        )
        assert automation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.agents.automations.with_raw_response.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert automation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.agents.automations.with_streaming_response.delete(
            automation_id="automation_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert automation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.automations.with_raw_response.delete(
                automation_id="automation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.agents.automations.with_raw_response.delete(
                automation_id="",
                agent_id="agent_id",
            )
