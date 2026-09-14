# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai._utils import parse_datetime
from datagrid_ai.types.organization.reports import UserCreditConsumptionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserCreditsConsumption:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        user_credits_consumption = client.organization.reports.user_credits_consumption.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        user_credits_consumption = client.organization.reports.user_credits_consumption.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.organization.reports.user_credits_consumption.with_raw_response.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credits_consumption = response.parse()
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.organization.reports.user_credits_consumption.with_streaming_response.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credits_consumption = response.parse()
            assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserCreditsConsumption:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        user_credits_consumption = await async_client.organization.reports.user_credits_consumption.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        user_credits_consumption = await async_client.organization.reports.user_credits_consumption.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.organization.reports.user_credits_consumption.with_raw_response.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_credits_consumption = await response.parse()
        assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.organization.reports.user_credits_consumption.with_streaming_response.list(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_credits_consumption = await response.parse()
            assert_matches_type(UserCreditConsumptionList, user_credits_consumption, path=["response"])

        assert cast(Any, response.is_closed) is True
