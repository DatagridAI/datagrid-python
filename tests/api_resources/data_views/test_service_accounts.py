# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types.data_views import (
    ServiceAccount,
    ServiceAccountCredentials,
    ServiceAccountListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        service_account = client.data_views.service_accounts.create(
            name="name",
            type="gcp",
        )
        assert_matches_type(ServiceAccount, service_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.data_views.service_accounts.with_raw_response.create(
            name="name",
            type="gcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = response.parse()
        assert_matches_type(ServiceAccount, service_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.data_views.service_accounts.with_streaming_response.create(
            name="name",
            type="gcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = response.parse()
            assert_matches_type(ServiceAccount, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        service_account = client.data_views.service_accounts.list()
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        service_account = client.data_views.service_accounts.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.data_views.service_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = response.parse()
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.data_views.service_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = response.parse()
            assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        service_account = client.data_views.service_accounts.delete(
            "service_account_id",
        )
        assert service_account is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.data_views.service_accounts.with_raw_response.delete(
            "service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = response.parse()
        assert service_account is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.data_views.service_accounts.with_streaming_response.delete(
            "service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = response.parse()
            assert service_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.data_views.service_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_credentials(self, client: Datagrid) -> None:
        service_account = client.data_views.service_accounts.credentials(
            "service_account_id",
        )
        assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

    @parametrize
    def test_raw_response_credentials(self, client: Datagrid) -> None:
        response = client.data_views.service_accounts.with_raw_response.credentials(
            "service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = response.parse()
        assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

    @parametrize
    def test_streaming_response_credentials(self, client: Datagrid) -> None:
        with client.data_views.service_accounts.with_streaming_response.credentials(
            "service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = response.parse()
            assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_credentials(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            client.data_views.service_accounts.with_raw_response.credentials(
                "",
            )


class TestAsyncServiceAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        service_account = await async_client.data_views.service_accounts.create(
            name="name",
            type="gcp",
        )
        assert_matches_type(ServiceAccount, service_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.service_accounts.with_raw_response.create(
            name="name",
            type="gcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = await response.parse()
        assert_matches_type(ServiceAccount, service_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.service_accounts.with_streaming_response.create(
            name="name",
            type="gcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = await response.parse()
            assert_matches_type(ServiceAccount, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        service_account = await async_client.data_views.service_accounts.list()
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        service_account = await async_client.data_views.service_accounts.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.service_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = await response.parse()
        assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.service_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = await response.parse()
            assert_matches_type(ServiceAccountListResponse, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        service_account = await async_client.data_views.service_accounts.delete(
            "service_account_id",
        )
        assert service_account is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.service_accounts.with_raw_response.delete(
            "service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = await response.parse()
        assert service_account is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.service_accounts.with_streaming_response.delete(
            "service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = await response.parse()
            assert service_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.data_views.service_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_credentials(self, async_client: AsyncDatagrid) -> None:
        service_account = await async_client.data_views.service_accounts.credentials(
            "service_account_id",
        )
        assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

    @parametrize
    async def test_raw_response_credentials(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.data_views.service_accounts.with_raw_response.credentials(
            "service_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_account = await response.parse()
        assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

    @parametrize
    async def test_streaming_response_credentials(self, async_client: AsyncDatagrid) -> None:
        async with async_client.data_views.service_accounts.with_streaming_response.credentials(
            "service_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_account = await response.parse()
            assert_matches_type(ServiceAccountCredentials, service_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_credentials(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_account_id` but received ''"):
            await async_client.data_views.service_accounts.with_raw_response.credentials(
                "",
            )
