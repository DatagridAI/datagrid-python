# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import VoiceSessionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_start_session(self, client: Datagrid) -> None:
        voice = client.voice.start_session()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_method_start_session_with_all_params(self, client: Datagrid) -> None:
        voice = client.voice.start_session(
            agent_id="agent_id",
            config={
                "custom_prompt": "custom_prompt",
                "system_prompt": "system_prompt",
            },
            conversation_id="conversation_id",
            ephemeral=True,
            file_ids=["string"],
            initial_context="initial_context",
            initial_message="initial_message",
            knowledge_ids=["string"],
            page_ids=["string"],
            secret_ids=["string"],
            user={
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
            },
            voice_config={
                "input_transcription": True,
                "output_transcription": True,
                "segment_max_duration_ms": 0,
                "silence_commit_ms": 0,
                "silence_discard_ratio": 0,
                "silence_timeout": True,
                "silent_start": True,
                "voice_preset": "voice_preset",
            },
            voice_mode="orchestrator",
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_start_session(self, client: Datagrid) -> None:
        response = client.voice.with_raw_response.start_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_start_session(self, client: Datagrid) -> None:
        with client.voice.with_streaming_response.start_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceSessionResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_start_session(self, async_client: AsyncDatagrid) -> None:
        voice = await async_client.voice.start_session()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_method_start_session_with_all_params(self, async_client: AsyncDatagrid) -> None:
        voice = await async_client.voice.start_session(
            agent_id="agent_id",
            config={
                "custom_prompt": "custom_prompt",
                "system_prompt": "system_prompt",
            },
            conversation_id="conversation_id",
            ephemeral=True,
            file_ids=["string"],
            initial_context="initial_context",
            initial_message="initial_message",
            knowledge_ids=["string"],
            page_ids=["string"],
            secret_ids=["string"],
            user={
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
            },
            voice_config={
                "input_transcription": True,
                "output_transcription": True,
                "segment_max_duration_ms": 0,
                "silence_commit_ms": 0,
                "silence_discard_ratio": 0,
                "silence_timeout": True,
                "silent_start": True,
                "voice_preset": "voice_preset",
            },
            voice_mode="orchestrator",
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_start_session(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.voice.with_raw_response.start_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_start_session(self, async_client: AsyncDatagrid) -> None:
        async with async_client.voice.with_streaming_response.start_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceSessionResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
