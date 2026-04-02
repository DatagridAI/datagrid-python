# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    ConnectionProvider,
)
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectionProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.connection_providers.with_raw_response.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.connection_providers.with_streaming_response.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.retrieve(
            "connection_provider_id",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.connection_providers.with_raw_response.retrieve(
            "connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.connection_providers.with_streaming_response.retrieve(
            "connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            client.connection_providers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.update(
            connection_provider_id="connection_provider_id",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.update(
            connection_provider_id="connection_provider_id",
            client_id="client_id",
            client_secret="client_secret",
            name="name",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.connection_providers.with_raw_response.update(
            connection_provider_id="connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.connection_providers.with_streaming_response.update(
            connection_provider_id="connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            client.connection_providers.with_raw_response.update(
                connection_provider_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.list()
        assert_matches_type(SyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.list(
            after="after",
            before="before",
            connector_id="connector_id",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.connection_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = response.parse()
        assert_matches_type(SyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.connection_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = response.parse()
            assert_matches_type(SyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        connection_provider = client.connection_providers.delete(
            "connection_provider_id",
        )
        assert connection_provider is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.connection_providers.with_raw_response.delete(
            "connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = response.parse()
        assert connection_provider is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.connection_providers.with_streaming_response.delete(
            "connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = response.parse()
            assert connection_provider is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            client.connection_providers.with_raw_response.delete(
                "",
            )


class TestAsyncConnectionProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connection_providers.with_raw_response.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = await response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connection_providers.with_streaming_response.create(
            client_id="client_id",
            client_secret="client_secret",
            connector_id="connector_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = await response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.retrieve(
            "connection_provider_id",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connection_providers.with_raw_response.retrieve(
            "connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = await response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connection_providers.with_streaming_response.retrieve(
            "connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = await response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            await async_client.connection_providers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.update(
            connection_provider_id="connection_provider_id",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.update(
            connection_provider_id="connection_provider_id",
            client_id="client_id",
            client_secret="client_secret",
            name="name",
        )
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connection_providers.with_raw_response.update(
            connection_provider_id="connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = await response.parse()
        assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connection_providers.with_streaming_response.update(
            connection_provider_id="connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = await response.parse()
            assert_matches_type(ConnectionProvider, connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            await async_client.connection_providers.with_raw_response.update(
                connection_provider_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.list()
        assert_matches_type(AsyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.list(
            after="after",
            before="before",
            connector_id="connector_id",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connection_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = await response.parse()
        assert_matches_type(AsyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connection_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = await response.parse()
            assert_matches_type(AsyncCursorIDPage[ConnectionProvider], connection_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        connection_provider = await async_client.connection_providers.delete(
            "connection_provider_id",
        )
        assert connection_provider is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.connection_providers.with_raw_response.delete(
            "connection_provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_provider = await response.parse()
        assert connection_provider is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.connection_providers.with_streaming_response.delete(
            "connection_provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_provider = await response.parse()
            assert connection_provider is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `connection_provider_id` but received ''"
        ):
            await async_client.connection_providers.with_raw_response.delete(
                "",
            )
