# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage
from datagrid_ai.types.organization.teamspaces import TeamspaceUser

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.users.with_raw_response.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.organization.teamspaces.users.with_streaming_response.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(TeamspaceUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.retrieve(
                user_id="user_id",
                teamspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.retrieve(
                user_id="",
                teamspace_id="teamspace_id",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
            agent_ids=["string"],
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.users.with_raw_response.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.organization.teamspaces.users.with_streaming_response.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(TeamspaceUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.update(
                user_id="user_id",
                teamspace_id="",
                role="admin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.update(
                user_id="",
                teamspace_id="teamspace_id",
                role="admin",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.list(
            teamspace_id="teamspace_id",
        )
        assert_matches_type(SyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.list(
            teamspace_id="teamspace_id",
            after="after",
            before="before",
            limit=1,
            search="search",
        )
        assert_matches_type(SyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.users.with_raw_response.list(
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.organization.teamspaces.users.with_streaming_response.list(
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncCursorIDPage[TeamspaceUser], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.list(
                teamspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        user = client.organization.teamspaces.users.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.users.with_raw_response.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.organization.teamspaces.users.with_streaming_response.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.delete(
                user_id="user_id",
                teamspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.teamspaces.users.with_raw_response.delete(
                user_id="",
                teamspace_id="teamspace_id",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.users.with_raw_response.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.users.with_streaming_response.retrieve(
            user_id="user_id",
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(TeamspaceUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.retrieve(
                user_id="user_id",
                teamspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.retrieve(
                user_id="",
                teamspace_id="teamspace_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
            agent_ids=["string"],
        )
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.users.with_raw_response.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(TeamspaceUser, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.users.with_streaming_response.update(
            user_id="user_id",
            teamspace_id="teamspace_id",
            role="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(TeamspaceUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.update(
                user_id="user_id",
                teamspace_id="",
                role="admin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.update(
                user_id="",
                teamspace_id="teamspace_id",
                role="admin",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.list(
            teamspace_id="teamspace_id",
        )
        assert_matches_type(AsyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.list(
            teamspace_id="teamspace_id",
            after="after",
            before="before",
            limit=1,
            search="search",
        )
        assert_matches_type(AsyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.users.with_raw_response.list(
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncCursorIDPage[TeamspaceUser], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.users.with_streaming_response.list(
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncCursorIDPage[TeamspaceUser], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.list(
                teamspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        user = await async_client.organization.teamspaces.users.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.users.with_raw_response.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.users.with_streaming_response.delete(
            user_id="user_id",
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.delete(
                user_id="user_id",
                teamspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.teamspaces.users.with_raw_response.delete(
                user_id="",
                teamspace_id="teamspace_id",
            )
