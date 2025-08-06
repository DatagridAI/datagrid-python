# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.memory import UserMemory, UserListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        user = client.memory.user.create(
            agent_id="agent_id",
            memory="memory",
        )
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        user = client.memory.user.create(
            agent_id="agent_id",
            memory="memory",
            context="context",
            user_prompt="user_prompt",
        )
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.memory.user.with_raw_response.create(
            agent_id="agent_id",
            memory="memory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.memory.user.with_streaming_response.create(
            agent_id="agent_id",
            memory="memory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserMemory, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        user = client.memory.user.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        user = client.memory.user.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.memory.user.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.memory.user.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        user = client.memory.user.delete(
            "user_memory_id",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.memory.user.with_raw_response.delete(
            "user_memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.memory.user.with_streaming_response.delete(
            "user_memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_memory_id` but received ''"):
            client.memory.user.with_raw_response.delete(
                "",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.memory.user.create(
            agent_id="agent_id",
            memory="memory",
        )
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.memory.user.create(
            agent_id="agent_id",
            memory="memory",
            context="context",
            user_prompt="user_prompt",
        )
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.memory.user.with_raw_response.create(
            agent_id="agent_id",
            memory="memory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserMemory, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.memory.user.with_streaming_response.create(
            agent_id="agent_id",
            memory="memory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserMemory, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.memory.user.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.memory.user.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.memory.user.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.memory.user.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.memory.user.delete(
            "user_memory_id",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.memory.user.with_raw_response.delete(
            "user_memory_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.memory.user.with_streaming_response.delete(
            "user_memory_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_memory_id` but received ''"):
            await async_client.memory.user.with_raw_response.delete(
                "",
            )
