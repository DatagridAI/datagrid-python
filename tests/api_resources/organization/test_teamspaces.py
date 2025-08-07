# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage
from datagrid_ai.types.organization import (
    Teamspace,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeamspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.create(
            access="open",
            name="name",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.with_raw_response.create(
            access="open",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.organization.teamspaces.with_streaming_response.create(
            access="open",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.retrieve(
            "teamspace_id",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.with_raw_response.retrieve(
            "teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.organization.teamspaces.with_streaming_response.retrieve(
            "teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.list()
        assert_matches_type(SyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = response.parse()
        assert_matches_type(SyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.organization.teamspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = response.parse()
            assert_matches_type(SyncCursorIDPage[Teamspace], teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_patch(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.patch(
            teamspace_id="teamspace_id",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_method_patch_with_all_params(self, client: Datagrid) -> None:
        teamspace = client.organization.teamspaces.patch(
            teamspace_id="teamspace_id",
            access="open",
            name="name",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_raw_response_patch(self, client: Datagrid) -> None:
        response = client.organization.teamspaces.with_raw_response.patch(
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    def test_streaming_response_patch(self, client: Datagrid) -> None:
        with client.organization.teamspaces.with_streaming_response.patch(
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_patch(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            client.organization.teamspaces.with_raw_response.patch(
                teamspace_id="",
            )


class TestAsyncTeamspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.create(
            access="open",
            name="name",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.with_raw_response.create(
            access="open",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = await response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.with_streaming_response.create(
            access="open",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = await response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.retrieve(
            "teamspace_id",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.with_raw_response.retrieve(
            "teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = await response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.with_streaming_response.retrieve(
            "teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = await response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.list()
        assert_matches_type(AsyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Teamspace], teamspace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Teamspace], teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_patch(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.patch(
            teamspace_id="teamspace_id",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncDatagrid) -> None:
        teamspace = await async_client.organization.teamspaces.patch(
            teamspace_id="teamspace_id",
            access="open",
            name="name",
        )
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.teamspaces.with_raw_response.patch(
            teamspace_id="teamspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        teamspace = await response.parse()
        assert_matches_type(Teamspace, teamspace, path=["response"])

    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.teamspaces.with_streaming_response.patch(
            teamspace_id="teamspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            teamspace = await response.parse()
            assert_matches_type(Teamspace, teamspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_patch(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `teamspace_id` but received ''"):
            await async_client.organization.teamspaces.with_raw_response.patch(
                teamspace_id="",
            )
