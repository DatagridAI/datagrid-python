# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    Skill,
    SkillGenerateResponse,
    SkillListBuiltinsResponse,
)
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        skill = client.skills.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        skill = client.skills.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
            description="description",
            enabled=True,
            preferred_tools=["string"],
            required_tools=["string"],
            scope="user",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        skill = client.skills.retrieve(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.retrieve(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.retrieve(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        skill = client.skills.update(
            skill_id="skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        skill = client.skills.update(
            skill_id="skill_id",
            category="document_analysis",
            description="description",
            enabled=True,
            instructions="instructions",
            name="name",
            preferred_tools=["string"],
            required_tools=["string"],
            slash_key="xx",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.update(
            skill_id="skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.update(
            skill_id="skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.update(
                skill_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        skill = client.skills.list()
        assert_matches_type(SyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        skill = client.skills.list(
            after="after",
            before="before",
            enabled=True,
            limit=1,
            scope="user",
            search="search",
        )
        assert_matches_type(SyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SyncCursorIDPage[Skill], skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Datagrid) -> None:
        skill = client.skills.delete(
            "skill_id",
        )
        assert skill is None

    @parametrize
    def test_raw_response_delete(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.delete(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert skill is None

    @parametrize
    def test_streaming_response_delete(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.delete(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert skill is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_clone(self, client: Datagrid) -> None:
        skill = client.skills.clone(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.clone(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.clone(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clone(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.clone(
                "",
            )

    @parametrize
    def test_method_demote(self, client: Datagrid) -> None:
        skill = client.skills.demote(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_demote(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.demote(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_demote(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.demote(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_demote(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.demote(
                "",
            )

    @parametrize
    def test_method_generate(self, client: Datagrid) -> None:
        skill = client.skills.generate()
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Datagrid) -> None:
        skill = client.skills.generate(
            file_ids=["string"],
            prompt="prompt",
        )
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillGenerateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_builtins(self, client: Datagrid) -> None:
        skill = client.skills.list_builtins()
        assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_list_builtins(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.list_builtins()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_list_builtins(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.list_builtins() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_override_builtin(self, client: Datagrid) -> None:
        skill = client.skills.override_builtin(
            "builtin_key",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_override_builtin(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.override_builtin(
            "builtin_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_override_builtin(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.override_builtin(
            "builtin_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_override_builtin(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `builtin_key` but received ''"):
            client.skills.with_raw_response.override_builtin(
                "",
            )

    @parametrize
    def test_method_promote(self, client: Datagrid) -> None:
        skill = client.skills.promote(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_raw_response_promote(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.promote(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    def test_streaming_response_promote(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.promote(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.skills.with_raw_response.promote(
                "",
            )

    @parametrize
    def test_method_reset_builtin_override(self, client: Datagrid) -> None:
        skill = client.skills.reset_builtin_override(
            "builtin_key",
        )
        assert skill is None

    @parametrize
    def test_raw_response_reset_builtin_override(self, client: Datagrid) -> None:
        response = client.skills.with_raw_response.reset_builtin_override(
            "builtin_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert skill is None

    @parametrize
    def test_streaming_response_reset_builtin_override(self, client: Datagrid) -> None:
        with client.skills.with_streaming_response.reset_builtin_override(
            "builtin_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert skill is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_builtin_override(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `builtin_key` but received ''"):
            client.skills.with_raw_response.reset_builtin_override(
                "",
            )


class TestAsyncSkills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
            description="description",
            enabled=True,
            preferred_tools=["string"],
            required_tools=["string"],
            scope="user",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.create(
            category="document_analysis",
            instructions="instructions",
            name="name",
            slash_key="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.retrieve(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.retrieve(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.retrieve(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.update(
            skill_id="skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.update(
            skill_id="skill_id",
            category="document_analysis",
            description="description",
            enabled=True,
            instructions="instructions",
            name="name",
            preferred_tools=["string"],
            required_tools=["string"],
            slash_key="xx",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.update(
            skill_id="skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.update(
            skill_id="skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.update(
                skill_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.list()
        assert_matches_type(AsyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.list(
            after="after",
            before="before",
            enabled=True,
            limit=1,
            scope="user",
            search="search",
        )
        assert_matches_type(AsyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Skill], skill, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Skill], skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.delete(
            "skill_id",
        )
        assert skill is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.delete(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert skill is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.delete(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert skill is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_clone(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.clone(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.clone(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.clone(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clone(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.clone(
                "",
            )

    @parametrize
    async def test_method_demote(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.demote(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_demote(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.demote(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_demote(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.demote(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_demote(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.demote(
                "",
            )

    @parametrize
    async def test_method_generate(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.generate()
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.generate(
            file_ids=["string"],
            prompt="prompt",
        )
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillGenerateResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillGenerateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_builtins(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.list_builtins()
        assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_list_builtins(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.list_builtins()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_list_builtins(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.list_builtins() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillListBuiltinsResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_override_builtin(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.override_builtin(
            "builtin_key",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_override_builtin(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.override_builtin(
            "builtin_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_override_builtin(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.override_builtin(
            "builtin_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_override_builtin(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `builtin_key` but received ''"):
            await async_client.skills.with_raw_response.override_builtin(
                "",
            )

    @parametrize
    async def test_method_promote(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.promote(
            "skill_id",
        )
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.promote(
            "skill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(Skill, skill, path=["response"])

    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.promote(
            "skill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(Skill, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.skills.with_raw_response.promote(
                "",
            )

    @parametrize
    async def test_method_reset_builtin_override(self, async_client: AsyncDatagrid) -> None:
        skill = await async_client.skills.reset_builtin_override(
            "builtin_key",
        )
        assert skill is None

    @parametrize
    async def test_raw_response_reset_builtin_override(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.skills.with_raw_response.reset_builtin_override(
            "builtin_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert skill is None

    @parametrize
    async def test_streaming_response_reset_builtin_override(self, async_client: AsyncDatagrid) -> None:
        async with async_client.skills.with_streaming_response.reset_builtin_override(
            "builtin_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert skill is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_builtin_override(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `builtin_key` but received ''"):
            await async_client.skills.with_raw_response.reset_builtin_override(
                "",
            )
