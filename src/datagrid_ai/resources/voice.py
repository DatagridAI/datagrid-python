# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import voice_start_session_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.voice_session_response import VoiceSessionResponse

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

    def start_session(
        self,
        *,
        agent_id: Optional[str] | Omit = omit,
        config: Optional[voice_start_session_params.Config] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        ephemeral: Optional[bool] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        initial_context: Optional[str] | Omit = omit,
        initial_message: Optional[str] | Omit = omit,
        knowledge_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        page_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user: Optional[voice_start_session_params.User] | Omit = omit,
        voice_config: Optional[voice_start_session_params.VoiceConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSessionResponse:
        """
        Prepare a real-time voice conversation with an AI Agent.

        Returns a WebSocket URL and a ready-made `start` message. Open a WebSocket
        connection to the returned `url`, send `start_message` as the first frame, then
        stream audio back and forth.

        You can also skip this endpoint and connect directly:
        `wss://api.datagrid.com/ws/voice?token=YOUR_API_KEY`

        **WebSocket Protocol:**

        Once connected, send a JSON message with `type: "start"` and the session
        parameters as the payload. The server responds with `type: "started"` containing
        the session and conversation IDs, followed by `type: "ready"` when the agent is
        ready to receive audio.

        **Audio Format:**

        - Client → Server: 16-bit mono PCM at 16kHz, base64-encoded
        - Server → Client: 16-bit mono PCM at 24kHz, base64-encoded

        **Message Types:**

        - Client: `start`, `audio`, `stop`, `interrupt`, `text`
        - Server: `started`, `ready`, `audio`, `tool_call`, `interrupted`, `error`,
          `transcript`, `citation`, `ended`

        Args:
          agent_id: The ID of the agent to use for the voice conversation. If not provided, the
              default agent is used.

          config: Override the agent config for this voice session. Only prompt overrides are
              supported — voice sessions always use Gemini Live, so LLM model, agent model,
              planning prompt, and tool settings are not applicable.

          conversation_id: The ID of an existing conversation to continue. If not provided, a new
              conversation will be created.

          ephemeral: When true, the session is ephemeral and will not save messages to conversation
              history.

          file_ids: Array of file IDs to attach to the voice conversation.

          initial_context: Optional context text for the voice session. When provided, the AI will start by
              briefly explaining this content before listening for user input.

          initial_message: Optional initial user message. When provided, the system greeting is skipped and
              the AI responds directly to this text (e.g. a suggested prompt). Takes
              precedence over initial_context.

          knowledge_ids: Array of knowledge IDs to make accessible to the agent.

          page_ids: Array of page IDs to make accessible to the agent. The page and all knowledge
              under it will be accessible.

          secret_ids: Array of secret IDs to include in the context.

          user: User information override for converse calls. All fields are optional - only
              provided fields will override the default user information.

          voice_config: Voice session configuration options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "config": config,
                    "conversation_id": conversation_id,
                    "ephemeral": ephemeral,
                    "file_ids": file_ids,
                    "initial_context": initial_context,
                    "initial_message": initial_message,
                    "knowledge_ids": knowledge_ids,
                    "page_ids": page_ids,
                    "secret_ids": secret_ids,
                    "user": user,
                    "voice_config": voice_config,
                },
                voice_start_session_params.VoiceStartSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSessionResponse,
        )


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

    async def start_session(
        self,
        *,
        agent_id: Optional[str] | Omit = omit,
        config: Optional[voice_start_session_params.Config] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        ephemeral: Optional[bool] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        initial_context: Optional[str] | Omit = omit,
        initial_message: Optional[str] | Omit = omit,
        knowledge_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        page_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        user: Optional[voice_start_session_params.User] | Omit = omit,
        voice_config: Optional[voice_start_session_params.VoiceConfig] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSessionResponse:
        """
        Prepare a real-time voice conversation with an AI Agent.

        Returns a WebSocket URL and a ready-made `start` message. Open a WebSocket
        connection to the returned `url`, send `start_message` as the first frame, then
        stream audio back and forth.

        You can also skip this endpoint and connect directly:
        `wss://api.datagrid.com/ws/voice?token=YOUR_API_KEY`

        **WebSocket Protocol:**

        Once connected, send a JSON message with `type: "start"` and the session
        parameters as the payload. The server responds with `type: "started"` containing
        the session and conversation IDs, followed by `type: "ready"` when the agent is
        ready to receive audio.

        **Audio Format:**

        - Client → Server: 16-bit mono PCM at 16kHz, base64-encoded
        - Server → Client: 16-bit mono PCM at 24kHz, base64-encoded

        **Message Types:**

        - Client: `start`, `audio`, `stop`, `interrupt`, `text`
        - Server: `started`, `ready`, `audio`, `tool_call`, `interrupted`, `error`,
          `transcript`, `citation`, `ended`

        Args:
          agent_id: The ID of the agent to use for the voice conversation. If not provided, the
              default agent is used.

          config: Override the agent config for this voice session. Only prompt overrides are
              supported — voice sessions always use Gemini Live, so LLM model, agent model,
              planning prompt, and tool settings are not applicable.

          conversation_id: The ID of an existing conversation to continue. If not provided, a new
              conversation will be created.

          ephemeral: When true, the session is ephemeral and will not save messages to conversation
              history.

          file_ids: Array of file IDs to attach to the voice conversation.

          initial_context: Optional context text for the voice session. When provided, the AI will start by
              briefly explaining this content before listening for user input.

          initial_message: Optional initial user message. When provided, the system greeting is skipped and
              the AI responds directly to this text (e.g. a suggested prompt). Takes
              precedence over initial_context.

          knowledge_ids: Array of knowledge IDs to make accessible to the agent.

          page_ids: Array of page IDs to make accessible to the agent. The page and all knowledge
              under it will be accessible.

          secret_ids: Array of secret IDs to include in the context.

          user: User information override for converse calls. All fields are optional - only
              provided fields will override the default user information.

          voice_config: Voice session configuration options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "config": config,
                    "conversation_id": conversation_id,
                    "ephemeral": ephemeral,
                    "file_ids": file_ids,
                    "initial_context": initial_context,
                    "initial_message": initial_message,
                    "knowledge_ids": knowledge_ids,
                    "page_ids": page_ids,
                    "secret_ids": secret_ids,
                    "user": user,
                    "voice_config": voice_config,
                },
                voice_start_session_params.VoiceStartSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSessionResponse,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.start_session = to_raw_response_wrapper(
            voice.start_session,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.start_session = async_to_raw_response_wrapper(
            voice.start_session,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.start_session = to_streamed_response_wrapper(
            voice.start_session,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.start_session = async_to_streamed_response_wrapper(
            voice.start_session,
        )
