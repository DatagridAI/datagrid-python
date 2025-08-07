# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    Knowledge,
    RedirectURLResponse,
    KnowledgeUpdateResponse,
)
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])
    skip = pytest.mark.skip("Problematic tests - issue with Prism and array of files (multipart/form-data)")

    @parametrize
    @skip
    def test_method_create(self, client: Datagrid) -> None:
        knowledge = client.knowledge.create()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        knowledge = client.knowledge.create(
            files=[b"raw file contents"],
            name="name",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        knowledge = client.knowledge.retrieve(
            "knowledge_id",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.retrieve(
            "knowledge_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.retrieve(
            "knowledge_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            client.knowledge.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        knowledge = client.knowledge.update(
            knowledge_id="knowledge_id",
            name="name",
        )
        assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.update(
            knowledge_id="knowledge_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.update(
            knowledge_id="knowledge_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            client.knowledge.with_raw_response.update(
                knowledge_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        knowledge = client.knowledge.list()
        assert_matches_type(SyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        knowledge = client.knowledge.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(SyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(SyncCursorIDPage[Knowledge], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        knowledge = client.knowledge.delete(
            "knowledge_id",
        )
        assert knowledge is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.delete(
            "knowledge_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert knowledge is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.delete(
            "knowledge_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert knowledge is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            client.knowledge.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_connect(self, client: Datagrid) -> None:
        knowledge = client.knowledge.connect(
            connection_id="connection_id",
        )
        assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Datagrid) -> None:
        response = client.knowledge.with_raw_response.connect(
            connection_id="connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Datagrid) -> None:
        with client.knowledge.with_streaming_response.connect(
            connection_id="connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )
    skip = pytest.mark.skip("Problematic tests - issue with Prism and array of files (multipart/form-data)")

    @parametrize
    @skip
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.create()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.create(
            files=[b"raw file contents"],
            name="name",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    @skip
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.retrieve(
            "knowledge_id",
        )
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.retrieve(
            "knowledge_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Knowledge, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.retrieve(
            "knowledge_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Knowledge, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            await async_client.knowledge.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.update(
            knowledge_id="knowledge_id",
            name="name",
        )
        assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.update(
            knowledge_id="knowledge_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.update(
            knowledge_id="knowledge_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeUpdateResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            await async_client.knowledge.with_raw_response.update(
                knowledge_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.list()
        assert_matches_type(AsyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Knowledge], knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Knowledge], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.delete(
            "knowledge_id",
        )
        assert knowledge is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.delete(
            "knowledge_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert knowledge is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.delete(
            "knowledge_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert knowledge is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_id` but received ''"):
            await async_client.knowledge.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncDatagrid) -> None:
        knowledge = await async_client.knowledge.connect(
            connection_id="connection_id",
        )
        assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.knowledge.with_raw_response.connect(
            connection_id="connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncDatagrid) -> None:
        async with async_client.knowledge.with_streaming_response.connect(
            connection_id="connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(RedirectURLResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True
