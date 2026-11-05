# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import ConverseResponse
from datagrid_ai._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConverse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_converse(self, client: Datagrid) -> None:
        converse = client.beta.converse.converse(
            prompt="string",
        )
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    def test_method_converse_with_all_params(self, client: Datagrid) -> None:
        converse = client.beta.converse.converse(
            prompt="string",
            agent_id="agent_id",
            agent_routing={"mode": "auto"},
            chat_mode="auto",
            config={
                "agent_model": "magpie-1.1",
                "agent_tools": ["string"],
                "corpus": [
                    {
                        "knowledge_id": "knowledge_id",
                        "type": "knowledge",
                    }
                ],
                "custom_prompt": "custom_prompt",
                "disabled_agent_tools": ["string"],
                "disabled_tools": ["string"],
                "knowledge_ids": ["string"],
                "llm_model": "gemini-2.0-flash",
                "mcp_servers": [
                    {
                        "server_id": "server_id",
                        "server_label": "server_label",
                        "server_url": "https://example.com",
                        "type": "inline_mcp",
                        "authorization": "authorization",
                        "credential_id": "credential_id",
                        "server_description": "server_description",
                    }
                ],
                "planning_prompt": "planning_prompt",
                "system_prompt": "system_prompt",
                "temperature": 0,
                "tools": ["string"],
            },
            conversation_id="conversation_id",
            current_view_content="current_view_content",
            generate_citations=True,
            generate_title=True,
            include_steps=True,
            reference_date=parse_date("2019-12-27"),
            secret_ids=["string"],
            skill_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skills=[
                {
                    "content": "content",
                    "type": "inline",
                }
            ],
            slash_keys=["string"],
            stream=True,
            text={"format": {}},
            user={
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
            },
        )
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    def test_raw_response_converse(self, client: Datagrid) -> None:
        response = client.beta.converse.with_raw_response.converse(
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        converse = response.parse()
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    def test_streaming_response_converse(self, client: Datagrid) -> None:
        with client.beta.converse.with_streaming_response.converse(
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            converse = response.parse()
            assert_matches_type(ConverseResponse, converse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConverse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_converse(self, async_client: AsyncDatagrid) -> None:
        converse = await async_client.beta.converse.converse(
            prompt="string",
        )
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    async def test_method_converse_with_all_params(self, async_client: AsyncDatagrid) -> None:
        converse = await async_client.beta.converse.converse(
            prompt="string",
            agent_id="agent_id",
            agent_routing={"mode": "auto"},
            chat_mode="auto",
            config={
                "agent_model": "magpie-1.1",
                "agent_tools": ["string"],
                "corpus": [
                    {
                        "knowledge_id": "knowledge_id",
                        "type": "knowledge",
                    }
                ],
                "custom_prompt": "custom_prompt",
                "disabled_agent_tools": ["string"],
                "disabled_tools": ["string"],
                "knowledge_ids": ["string"],
                "llm_model": "gemini-2.0-flash",
                "mcp_servers": [
                    {
                        "server_id": "server_id",
                        "server_label": "server_label",
                        "server_url": "https://example.com",
                        "type": "inline_mcp",
                        "authorization": "authorization",
                        "credential_id": "credential_id",
                        "server_description": "server_description",
                    }
                ],
                "planning_prompt": "planning_prompt",
                "system_prompt": "system_prompt",
                "temperature": 0,
                "tools": ["string"],
            },
            conversation_id="conversation_id",
            current_view_content="current_view_content",
            generate_citations=True,
            generate_title=True,
            include_steps=True,
            reference_date=parse_date("2019-12-27"),
            secret_ids=["string"],
            skill_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skills=[
                {
                    "content": "content",
                    "type": "inline",
                }
            ],
            slash_keys=["string"],
            stream=True,
            text={"format": {}},
            user={
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
            },
        )
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    async def test_raw_response_converse(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.beta.converse.with_raw_response.converse(
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        converse = await response.parse()
        assert_matches_type(ConverseResponse, converse, path=["response"])

    @parametrize
    async def test_streaming_response_converse(self, async_client: AsyncDatagrid) -> None:
        async with async_client.beta.converse.with_streaming_response.converse(
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            converse = await response.parse()
            assert_matches_type(ConverseResponse, converse, path=["response"])

        assert cast(Any, response.is_closed) is True
