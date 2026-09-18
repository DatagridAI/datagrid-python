# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import converse_converse_params
from ..._base_client import make_request_options
from ...types.converse_response import ConverseResponse

__all__ = ["ConverseResource", "AsyncConverseResource"]


class ConverseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConverseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ConverseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConverseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ConverseResourceWithStreamingResponse(self)

    def converse(
        self,
        *,
        prompt: Union[str, Iterable[converse_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | Omit = omit,
        agent_routing: Optional[converse_converse_params.AgentRouting] | Omit = omit,
        chat_mode: Optional[Literal["auto", "full_agent", "light_agent", "llm_router"]] | Omit = omit,
        config: Optional[converse_converse_params.Config] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        current_view_content: Optional[str] | Omit = omit,
        generate_citations: Optional[bool] | Omit = omit,
        generate_title: Optional[bool] | Omit = omit,
        include_steps: Optional[bool] | Omit = omit,
        reference_date: Union[str, date, None] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        skills: Iterable[converse_converse_params.Skill] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        text: Optional[converse_converse_params.Text] | Omit = omit,
        user: Optional[converse_converse_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse:
        """
        **BETA**: This endpoint is in beta and the schema may change.

        Converse with an AI Agent, optionally supplying request-scoped **inline skills**
        that apply to this turn only. Inline skills are parsed server-side and become
        the turn's skill catalogue; they are never persisted and never affect stored
        agent skills.

        Inline skills are made **available** to the agent, not force-applied. Supplying
        a skill does not guarantee the agent follows its procedure. Request-scoped
        skills require a skills-capable agent model set via `config.agent_model`: Magpie
        2.5, Magpie 2.5 Reporting, or Magpie 3.0. Any other model (including Magpie 2.5
        Flash) returns a `400`.

        The request body is the stable Converse body plus the optional top-level
        `skills` array; all other behavior matches `POST /converse`.

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse. When omitted and a
              `conversation_id` is provided, the conversation's existing agent assignments are
              preserved. When omitted without a `conversation_id`, a new conversation is
              created with the default agent.

          agent_routing: Determines how the API routes the converse request to an agent.

          chat_mode: Controls how the agent processes the request for this turn. Matches the chat
              mode selector in the Datagrid web app: **Execute** (`full_agent`), **Extended**
              (`light_agent`), **Ask** (`llm_router`). Ask uses the agent path with Magpie 2.5
              and Ask-specific prompt guidance. When omitted, the request inherits the
              conversation's persisted `chat_mode`; new conversations default to **Execute**
              (`full_agent`). When set to `auto`, the request also runs as **Execute**
              (`full_agent`); Auto is currently accepted for compatibility but does not
              predict Ask, Extended, or Execute per message. When set to a concrete mode, that
              concrete mode is used directly. The default `agent_model` for Execute is
              `magpie-2.5` unless `config.agent_model` explicitly sets another supported
              model.

          config: Override the agent config for this converse call. This is applied as a partial
              override.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          current_view_content: A datagrid file URI pointing to content the user is currently viewing on screen
              (e.g., a web page, document, or dashboard rendered as markdown). The agent uses
              this context to resolve ambiguous queries like 'what is this about?' or 'review
              this'. The content is automatically summarized and made available to the agent.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          generate_title: Determines whether generated_title metadata should be included. Defaults to
              false. generated_title is emitted only when this flag is explicitly true.

          include_steps: When set to false, tool call and reasoning step events are omitted from SSE
              streams. Non-streaming responses always include the tool_calls and reasoning
              fields (as null when empty).

          reference_date: Optional deterministic reference date override in YYYY-MM-DD format. Must be a
              real calendar date (for example, rejects impossible dates like 2026-02-31). When
              set, the agent treats this date as today for relative date resolution and date
              context rendering.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          skills: Request-scoped skills made available to the agent for this turn only. They form
              the turn's skill catalogue and are selected by the agent (Magpie 2.5 planner) or
              read from its workspace (Magpie 3.0) — they are not force-applied, so supplying
              a skill does not guarantee the agent follows its procedure. Each entry is a
              discriminated union on `type`. Only `inline` is supported today;
              `skill_reference` is reserved for a future release. Inline skills are never
              persisted.

              Omitting `skills` keeps the agent's account-scoped skill catalogue. An empty
              array (`[]`) isolates the turn — no skills. A non-empty array uses only the
              supplied inline skills.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema
              (`text.format`). Structured output is supported for all `agent_model` values and
              `chat_mode` settings when `text.format` is provided (same JSON Schema mechanism
              everywhere). **Ask** in the web app maps to `chat_mode: llm_router`; `auto`
              currently maps to **Execute** (`full_agent`).

          user: User information override for converse calls. All fields are optional - only
              provided fields will override the default user information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/beta/converse",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "agent_id": agent_id,
                    "agent_routing": agent_routing,
                    "chat_mode": chat_mode,
                    "config": config,
                    "conversation_id": conversation_id,
                    "current_view_content": current_view_content,
                    "generate_citations": generate_citations,
                    "generate_title": generate_title,
                    "include_steps": include_steps,
                    "reference_date": reference_date,
                    "secret_ids": secret_ids,
                    "skills": skills,
                    "stream": stream,
                    "text": text,
                    "user": user,
                },
                converse_converse_params.ConverseConverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConverseResponse,
        )


class AsyncConverseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConverseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConverseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConverseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncConverseResourceWithStreamingResponse(self)

    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[converse_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | Omit = omit,
        agent_routing: Optional[converse_converse_params.AgentRouting] | Omit = omit,
        chat_mode: Optional[Literal["auto", "full_agent", "light_agent", "llm_router"]] | Omit = omit,
        config: Optional[converse_converse_params.Config] | Omit = omit,
        conversation_id: Optional[str] | Omit = omit,
        current_view_content: Optional[str] | Omit = omit,
        generate_citations: Optional[bool] | Omit = omit,
        generate_title: Optional[bool] | Omit = omit,
        include_steps: Optional[bool] | Omit = omit,
        reference_date: Union[str, date, None] | Omit = omit,
        secret_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        skills: Iterable[converse_converse_params.Skill] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        text: Optional[converse_converse_params.Text] | Omit = omit,
        user: Optional[converse_converse_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse:
        """
        **BETA**: This endpoint is in beta and the schema may change.

        Converse with an AI Agent, optionally supplying request-scoped **inline skills**
        that apply to this turn only. Inline skills are parsed server-side and become
        the turn's skill catalogue; they are never persisted and never affect stored
        agent skills.

        Inline skills are made **available** to the agent, not force-applied. Supplying
        a skill does not guarantee the agent follows its procedure. Request-scoped
        skills require a skills-capable agent model set via `config.agent_model`: Magpie
        2.5, Magpie 2.5 Reporting, or Magpie 3.0. Any other model (including Magpie 2.5
        Flash) returns a `400`.

        The request body is the stable Converse body plus the optional top-level
        `skills` array; all other behavior matches `POST /converse`.

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse. When omitted and a
              `conversation_id` is provided, the conversation's existing agent assignments are
              preserved. When omitted without a `conversation_id`, a new conversation is
              created with the default agent.

          agent_routing: Determines how the API routes the converse request to an agent.

          chat_mode: Controls how the agent processes the request for this turn. Matches the chat
              mode selector in the Datagrid web app: **Execute** (`full_agent`), **Extended**
              (`light_agent`), **Ask** (`llm_router`). Ask uses the agent path with Magpie 2.5
              and Ask-specific prompt guidance. When omitted, the request inherits the
              conversation's persisted `chat_mode`; new conversations default to **Execute**
              (`full_agent`). When set to `auto`, the request also runs as **Execute**
              (`full_agent`); Auto is currently accepted for compatibility but does not
              predict Ask, Extended, or Execute per message. When set to a concrete mode, that
              concrete mode is used directly. The default `agent_model` for Execute is
              `magpie-2.5` unless `config.agent_model` explicitly sets another supported
              model.

          config: Override the agent config for this converse call. This is applied as a partial
              override.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          current_view_content: A datagrid file URI pointing to content the user is currently viewing on screen
              (e.g., a web page, document, or dashboard rendered as markdown). The agent uses
              this context to resolve ambiguous queries like 'what is this about?' or 'review
              this'. The content is automatically summarized and made available to the agent.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          generate_title: Determines whether generated_title metadata should be included. Defaults to
              false. generated_title is emitted only when this flag is explicitly true.

          include_steps: When set to false, tool call and reasoning step events are omitted from SSE
              streams. Non-streaming responses always include the tool_calls and reasoning
              fields (as null when empty).

          reference_date: Optional deterministic reference date override in YYYY-MM-DD format. Must be a
              real calendar date (for example, rejects impossible dates like 2026-02-31). When
              set, the agent treats this date as today for relative date resolution and date
              context rendering.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          skills: Request-scoped skills made available to the agent for this turn only. They form
              the turn's skill catalogue and are selected by the agent (Magpie 2.5 planner) or
              read from its workspace (Magpie 3.0) — they are not force-applied, so supplying
              a skill does not guarantee the agent follows its procedure. Each entry is a
              discriminated union on `type`. Only `inline` is supported today;
              `skill_reference` is reserved for a future release. Inline skills are never
              persisted.

              Omitting `skills` keeps the agent's account-scoped skill catalogue. An empty
              array (`[]`) isolates the turn — no skills. A non-empty array uses only the
              supplied inline skills.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema
              (`text.format`). Structured output is supported for all `agent_model` values and
              `chat_mode` settings when `text.format` is provided (same JSON Schema mechanism
              everywhere). **Ask** in the web app maps to `chat_mode: llm_router`; `auto`
              currently maps to **Execute** (`full_agent`).

          user: User information override for converse calls. All fields are optional - only
              provided fields will override the default user information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/beta/converse",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "agent_id": agent_id,
                    "agent_routing": agent_routing,
                    "chat_mode": chat_mode,
                    "config": config,
                    "conversation_id": conversation_id,
                    "current_view_content": current_view_content,
                    "generate_citations": generate_citations,
                    "generate_title": generate_title,
                    "include_steps": include_steps,
                    "reference_date": reference_date,
                    "secret_ids": secret_ids,
                    "skills": skills,
                    "stream": stream,
                    "text": text,
                    "user": user,
                },
                converse_converse_params.ConverseConverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConverseResponse,
        )


class ConverseResourceWithRawResponse:
    def __init__(self, converse: ConverseResource) -> None:
        self._converse = converse

        self.converse = to_raw_response_wrapper(
            converse.converse,
        )


class AsyncConverseResourceWithRawResponse:
    def __init__(self, converse: AsyncConverseResource) -> None:
        self._converse = converse

        self.converse = async_to_raw_response_wrapper(
            converse.converse,
        )


class ConverseResourceWithStreamingResponse:
    def __init__(self, converse: ConverseResource) -> None:
        self._converse = converse

        self.converse = to_streamed_response_wrapper(
            converse.converse,
        )


class AsyncConverseResourceWithStreamingResponse:
    def __init__(self, converse: AsyncConverseResource) -> None:
        self._converse = converse

        self.converse = async_to_streamed_response_wrapper(
            converse.converse,
        )
