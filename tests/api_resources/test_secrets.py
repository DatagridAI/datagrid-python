# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import Secret
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        secret = client.secrets.create(
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.secrets.with_raw_response.create(
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.secrets.with_streaming_response.create(
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        secret = client.secrets.retrieve(
            "secret_id",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.secrets.with_raw_response.retrieve(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.secrets.with_streaming_response.retrieve(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        secret = client.secrets.list()
        assert_matches_type(SyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        secret = client.secrets.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncCursorIDPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        secret = client.secrets.delete(
            "secret_id",
        )
        assert secret is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.secrets.with_raw_response.delete(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.secrets.with_streaming_response.delete(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets.with_raw_response.delete(
                "",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        secret = await async_client.secrets.create(
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.secrets.with_raw_response.create(
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.secrets.with_streaming_response.create(
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        secret = await async_client.secrets.retrieve(
            "secret_id",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.secrets.with_raw_response.retrieve(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.secrets.with_streaming_response.retrieve(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        secret = await async_client.secrets.list()
        assert_matches_type(AsyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        secret = await async_client.secrets.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Secret], secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Secret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        secret = await async_client.secrets.delete(
            "secret_id",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.secrets.with_raw_response.delete(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.secrets.with_streaming_response.delete(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets.with_raw_response.delete(
                "",
            )
