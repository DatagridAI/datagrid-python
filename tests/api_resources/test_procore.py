# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    ProcoreCompanyList,
    ProcoreProjectList,
    ProcoreProjectConnection,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProcore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_companies(self, client: Datagrid) -> None:
        procore = client.procore.list_companies()
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    def test_method_list_companies_with_all_params(self, client: Datagrid) -> None:
        procore = client.procore.list_companies(
            page=1,
            per_page=1,
        )
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    def test_raw_response_list_companies(self, client: Datagrid) -> None:
        response = client.procore.with_raw_response.list_companies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = response.parse()
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    def test_streaming_response_list_companies(self, client: Datagrid) -> None:
        with client.procore.with_streaming_response.list_companies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = response.parse()
            assert_matches_type(ProcoreCompanyList, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_projects(self, client: Datagrid) -> None:
        procore = client.procore.list_projects(
            company_id="269125115713",
        )
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    def test_method_list_projects_with_all_params(self, client: Datagrid) -> None:
        procore = client.procore.list_projects(
            company_id="269125115713",
            page=1,
            per_page=1,
        )
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    def test_raw_response_list_projects(self, client: Datagrid) -> None:
        response = client.procore.with_raw_response.list_projects(
            company_id="269125115713",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = response.parse()
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    def test_streaming_response_list_projects(self, client: Datagrid) -> None:
        with client.procore.with_streaming_response.list_projects(
            company_id="269125115713",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = response.parse()
            assert_matches_type(ProcoreProjectList, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_projects(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.procore.with_raw_response.list_projects(
                company_id="",
            )

    @parametrize
    def test_method_retrieve_project_connection(self, client: Datagrid) -> None:
        procore = client.procore.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        )
        assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

    @parametrize
    def test_raw_response_retrieve_project_connection(self, client: Datagrid) -> None:
        response = client.procore.with_raw_response.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = response.parse()
        assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_project_connection(self, client: Datagrid) -> None:
        with client.procore.with_streaming_response.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = response.parse()
            assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_project_connection(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.procore.with_raw_response.retrieve_project_connection(
                project_id="269125115713",
                company_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.procore.with_raw_response.retrieve_project_connection(
                project_id="",
                company_id="269125115713",
            )


class TestAsyncProcore:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_companies(self, async_client: AsyncDatagrid) -> None:
        procore = await async_client.procore.list_companies()
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    async def test_method_list_companies_with_all_params(self, async_client: AsyncDatagrid) -> None:
        procore = await async_client.procore.list_companies(
            page=1,
            per_page=1,
        )
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    async def test_raw_response_list_companies(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.procore.with_raw_response.list_companies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = await response.parse()
        assert_matches_type(ProcoreCompanyList, procore, path=["response"])

    @parametrize
    async def test_streaming_response_list_companies(self, async_client: AsyncDatagrid) -> None:
        async with async_client.procore.with_streaming_response.list_companies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = await response.parse()
            assert_matches_type(ProcoreCompanyList, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_projects(self, async_client: AsyncDatagrid) -> None:
        procore = await async_client.procore.list_projects(
            company_id="269125115713",
        )
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    async def test_method_list_projects_with_all_params(self, async_client: AsyncDatagrid) -> None:
        procore = await async_client.procore.list_projects(
            company_id="269125115713",
            page=1,
            per_page=1,
        )
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    async def test_raw_response_list_projects(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.procore.with_raw_response.list_projects(
            company_id="269125115713",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = await response.parse()
        assert_matches_type(ProcoreProjectList, procore, path=["response"])

    @parametrize
    async def test_streaming_response_list_projects(self, async_client: AsyncDatagrid) -> None:
        async with async_client.procore.with_streaming_response.list_projects(
            company_id="269125115713",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = await response.parse()
            assert_matches_type(ProcoreProjectList, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_projects(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.procore.with_raw_response.list_projects(
                company_id="",
            )

    @parametrize
    async def test_method_retrieve_project_connection(self, async_client: AsyncDatagrid) -> None:
        procore = await async_client.procore.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        )
        assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_project_connection(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.procore.with_raw_response.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        procore = await response.parse()
        assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_project_connection(self, async_client: AsyncDatagrid) -> None:
        async with async_client.procore.with_streaming_response.retrieve_project_connection(
            project_id="269125115713",
            company_id="269125115713",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            procore = await response.parse()
            assert_matches_type(ProcoreProjectConnection, procore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_project_connection(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.procore.with_raw_response.retrieve_project_connection(
                project_id="269125115713",
                company_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.procore.with_raw_response.retrieve_project_connection(
                project_id="",
                company_id="269125115713",
            )
