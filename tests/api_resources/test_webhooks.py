# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    Webhook,
    WebhookCreateResponse,
    WebhookListActiveForEventResponse,
)
from datagrid_ai.pagination import SyncWebhookCursorPage, AsyncWebhookCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        webhook = client.webhooks.create(
            events=["string"],
            url="url",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.create(
            events=["string"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.create(
            events=["string"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        webhook = client.webhooks.retrieve(
            "webhook_id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        webhook = client.webhooks.update(
            webhook_id="webhook_id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        webhook = client.webhooks.update(
            webhook_id="webhook_id",
            enabled=True,
            events=["string"],
            url="url",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.update(
            webhook_id="webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.update(
            webhook_id="webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(SyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        webhook = client.webhooks.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncWebhookCursorPage[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        webhook = client.webhooks.delete(
            "webhook_id",
        )
        assert webhook is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.delete(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.delete(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_list_active_for_event(self, client: Datagrid) -> None:
        webhook = client.webhooks.list_active_for_event(
            event_type="event_type",
        )
        assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_list_active_for_event(self, client: Datagrid) -> None:
        response = client.webhooks.with_raw_response.list_active_for_event(
            event_type="event_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_list_active_for_event(self, client: Datagrid) -> None:
        with client.webhooks.with_streaming_response.list_active_for_event(
            event_type="event_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.create(
            events=["string"],
            url="url",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            events=["string"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            events=["string"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.retrieve(
            "webhook_id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="webhook_id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="webhook_id",
            enabled=True,
            events=["string"],
            url="url",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            webhook_id="webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            webhook_id="webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(AsyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncWebhookCursorPage[Webhook], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncWebhookCursorPage[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.delete(
            "webhook_id",
        )
        assert webhook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_list_active_for_event(self, async_client: AsyncDatagrid) -> None:
        webhook = await async_client.webhooks.list_active_for_event(
            event_type="event_type",
        )
        assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_list_active_for_event(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.webhooks.with_raw_response.list_active_for_event(
            event_type="event_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list_active_for_event(self, async_client: AsyncDatagrid) -> None:
        async with async_client.webhooks.with_streaming_response.list_active_for_event(
            event_type="event_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListActiveForEventResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
