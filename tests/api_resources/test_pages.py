# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import Page
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        page = client.pages.create(
            name="name",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        page = client.pages.create(
            name="name",
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.pages.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.pages.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        page = client.pages.retrieve(
            "page_id",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.pages.with_raw_response.retrieve(
            "page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.pages.with_streaming_response.retrieve(
            "page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        page = client.pages.update(
            page_id="page_id",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        page = client.pages.update(
            page_id="page_id",
            name="name",
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.pages.with_raw_response.update(
            page_id="page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.pages.with_streaming_response.update(
            page_id="page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.update(
                page_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        page = client.pages.list()
        assert_matches_type(SyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        page = client.pages.list(
            after="after",
            before="before",
            limit=1,
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(SyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(SyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(SyncCursorIDPage[Page], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        page = client.pages.delete(
            "page_id",
        )
        assert page is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.pages.with_raw_response.delete(
            "page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert page is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.pages.with_streaming_response.delete(
            "page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.pages.with_raw_response.delete(
                "",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.create(
            name="name",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.create(
            name="name",
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.pages.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.pages.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.retrieve(
            "page_id",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.pages.with_raw_response.retrieve(
            "page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.pages.with_streaming_response.retrieve(
            "page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.update(
            page_id="page_id",
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.update(
            page_id="page_id",
            name="name",
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.pages.with_raw_response.update(
            page_id="page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Page, page, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.pages.with_streaming_response.update(
            page_id="page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Page, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.update(
                page_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.list()
        assert_matches_type(AsyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.list(
            after="after",
            before="before",
            limit=1,
            parent={
                "page_id": "page_id",
                "type": "page",
            },
        )
        assert_matches_type(AsyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Page], page, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Page], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        page = await async_client.pages.delete(
            "page_id",
        )
        assert page is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.pages.with_raw_response.delete(
            "page_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert page is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.pages.with_streaming_response.delete(
            "page_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert page is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.pages.with_raw_response.delete(
                "",
            )
