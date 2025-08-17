# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import agent_list_params, agent_create_params, agent_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorIDPage, AsyncCursorIDPage
from ..types.agent import Agent
from .._base_client import AsyncPaginator, make_request_options
from ..types.agent_tools import AgentTools

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]] | NotGiven = NOT_GIVEN,
        agent_tools: Optional[Iterable[agent_create_params.AgentTool]] | NotGiven = NOT_GIVEN,
        custom_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        disabled_agent_tools: Optional[List[AgentTools]] | NotGiven = NOT_GIVEN,
        knowledge_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        llm_model: Optional[
            Literal[
                "gemini-1.5-flash-001",
                "gemini-1.5-flash-002",
                "gemini-2.0-flash-001",
                "gemini-2.0-flash",
                "gemini-2.5-flash-preview-04-17",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-1.5-pro-001",
                "gemini-1.5-pro-002",
                "gemini-2.5-pro-preview-05-06",
                "gemini-2.5-pro",
                "chatgpt-4o-latest",
                "gpt-4",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-5",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        planning_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Create a new agent

        Args:
          name: The name of the agent

          agent_model: The version of Datagrid's agent brain.

          agent_tools: Array of the agent tools to enable. If not provided - default tools of the agent
              are used. If empty list provided - none of the tools are used. If null
              provided - all tools are used. When connection_id is set for a tool, it will use
              that specific connection instead of the default one.

              Knowledge management tools:

              - data_analysis: Answer statistical or analytical questions like "Show my
                quarterly revenue growth"
              - semantic_search: Search knowledge through natural language queries.
              - agent_memory: Agents can remember experiences, conversations and user
                preferences.
              - schema_info: Helps the Agent understand column names and dataset purpose.
                Avoid disabling
              - table_info: Allow the AI Agent to get information about datasets and schemas
              - create_dataset: Agents respond with data tables

              Actions:

              - calendar: Allow the Agent to access and make changes to your Google Calendar
              - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
                of today's meetings at 5pm on workdays"

              Data processing tools:

              - data_classification: Agents handle queries like "Label these emails as high,
                medium, or low priority"
              - data_extraction: Helps the agent understand data from other tools. Avoid
                disabling
              - image_detection: Extract information from images using AI
              - pdf_extraction: Extraction of information from PDFs using AI

              Enhanced response tools:

              - connect_data: Agents provide buttons to import data in response to queries
                like "Connect Hubspot"
              - download_data: Agents handle queries like "download the table as CSV"

              Web tools:

              - web_search: Agents search the internet, and provide links to their sources
              - fetch_url: Fetch URL content
              - company_prospect_researcher: Agents provide information about companies
              - people_prospect_researcher: Agents provide information about people

          custom_prompt: Use custom prompt to instruct the style and formatting of the agent's response

          description: Description of the agent

          disabled_agent_tools: Array of the agent tools to disable. Disabling is performed after the
              'agent_tools' rules are applied. For example, agent_tools: null and
              disabled_agent_tools: [data_analysis] will enable everything but the
              data_analysis tool. If nothing or [] is provided, nothing is disabled and
              therefore only the agent_tools setting is relevant.

          knowledge_ids: Array of Knowledge IDs the agent should use during the converse. If not
              provided - default settings are used. If null provided - all available knowledge
              is used.

          llm_model: The LLM used to generate responses.

          planning_prompt: Define the planning strategy your AI Agent should use when breaking down tasks
              and solving problems

          system_prompt: Directs your AI Agent's operational behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents",
            body=maybe_transform(
                {
                    "name": name,
                    "agent_model": agent_model,
                    "agent_tools": agent_tools,
                    "custom_prompt": custom_prompt,
                    "description": description,
                    "disabled_agent_tools": disabled_agent_tools,
                    "knowledge_ids": knowledge_ids,
                    "llm_model": llm_model,
                    "planning_prompt": planning_prompt,
                    "system_prompt": system_prompt,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get details of a specific agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def update(
        self,
        agent_id: str,
        *,
        agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]] | NotGiven = NOT_GIVEN,
        agent_tools: Optional[Iterable[agent_update_params.AgentTool]] | NotGiven = NOT_GIVEN,
        custom_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        disabled_agent_tools: Optional[List[AgentTools]] | NotGiven = NOT_GIVEN,
        knowledge_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        llm_model: Optional[
            Literal[
                "gemini-1.5-flash-001",
                "gemini-1.5-flash-002",
                "gemini-2.0-flash-001",
                "gemini-2.0-flash",
                "gemini-2.5-flash-preview-04-17",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-1.5-pro-001",
                "gemini-1.5-pro-002",
                "gemini-2.5-pro-preview-05-06",
                "gemini-2.5-pro",
                "chatgpt-4o-latest",
                "gpt-4",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-5",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        planning_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Update an agent configuration

        Args:
          agent_model: The version of Datagrid's agent brain.

          agent_tools: Array of the agent tools to enable. If not provided - default tools of the agent
              are used. If empty list provided - none of the tools are used. If null
              provided - all tools are used. When connection_id is set for a tool, it will use
              that specific connection instead of the default one.

              Knowledge management tools:

              - data_analysis: Answer statistical or analytical questions like "Show my
                quarterly revenue growth"
              - semantic_search: Search knowledge through natural language queries.
              - agent_memory: Agents can remember experiences, conversations and user
                preferences.
              - schema_info: Helps the Agent understand column names and dataset purpose.
                Avoid disabling
              - table_info: Allow the AI Agent to get information about datasets and schemas
              - create_dataset: Agents respond with data tables

              Actions:

              - calendar: Allow the Agent to access and make changes to your Google Calendar
              - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
                of today's meetings at 5pm on workdays"

              Data processing tools:

              - data_classification: Agents handle queries like "Label these emails as high,
                medium, or low priority"
              - data_extraction: Helps the agent understand data from other tools. Avoid
                disabling
              - image_detection: Extract information from images using AI
              - pdf_extraction: Extraction of information from PDFs using AI

              Enhanced response tools:

              - connect_data: Agents provide buttons to import data in response to queries
                like "Connect Hubspot"
              - download_data: Agents handle queries like "download the table as CSV"

              Web tools:

              - web_search: Agents search the internet, and provide links to their sources
              - fetch_url: Fetch URL content
              - company_prospect_researcher: Agents provide information about companies
              - people_prospect_researcher: Agents provide information about people

          custom_prompt: Use custom prompt to instruct the style and formatting of the agent's response

          description: Description of the agent

          disabled_agent_tools: Array of the agent tools to disable. Disabling is performed after the
              'agent_tools' rules are applied. For example, agent_tools: null and
              disabled_agent_tools: [data_analysis] will enable everything but the
              data_analysis tool. If nothing or [] is provided, nothing is disabled and
              therefore only the agent_tools setting is relevant.

          knowledge_ids: Array of Knowledge IDs the agent should use during the converse. If not
              provided - default settings are used. If null provided - all available knowledge
              is used.

          llm_model: The LLM used to generate responses.

          name: The name of the agent

          planning_prompt: Define the planning strategy your AI Agent should use when breaking down tasks
              and solving problems

          system_prompt: Directs your AI Agent's operational behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/agents/{agent_id}",
            body=maybe_transform(
                {
                    "agent_model": agent_model,
                    "agent_tools": agent_tools,
                    "custom_prompt": custom_prompt,
                    "description": description,
                    "disabled_agent_tools": disabled_agent_tools,
                    "knowledge_ids": knowledge_ids,
                    "llm_model": llm_model,
                    "name": name,
                    "planning_prompt": planning_prompt,
                    "system_prompt": system_prompt,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorIDPage[Agent]:
        """
        List all agents for the authenticated organization

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents",
            page=SyncCursorIDPage[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]] | NotGiven = NOT_GIVEN,
        agent_tools: Optional[Iterable[agent_create_params.AgentTool]] | NotGiven = NOT_GIVEN,
        custom_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        disabled_agent_tools: Optional[List[AgentTools]] | NotGiven = NOT_GIVEN,
        knowledge_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        llm_model: Optional[
            Literal[
                "gemini-1.5-flash-001",
                "gemini-1.5-flash-002",
                "gemini-2.0-flash-001",
                "gemini-2.0-flash",
                "gemini-2.5-flash-preview-04-17",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-1.5-pro-001",
                "gemini-1.5-pro-002",
                "gemini-2.5-pro-preview-05-06",
                "gemini-2.5-pro",
                "chatgpt-4o-latest",
                "gpt-4",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-5",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        planning_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Create a new agent

        Args:
          name: The name of the agent

          agent_model: The version of Datagrid's agent brain.

          agent_tools: Array of the agent tools to enable. If not provided - default tools of the agent
              are used. If empty list provided - none of the tools are used. If null
              provided - all tools are used. When connection_id is set for a tool, it will use
              that specific connection instead of the default one.

              Knowledge management tools:

              - data_analysis: Answer statistical or analytical questions like "Show my
                quarterly revenue growth"
              - semantic_search: Search knowledge through natural language queries.
              - agent_memory: Agents can remember experiences, conversations and user
                preferences.
              - schema_info: Helps the Agent understand column names and dataset purpose.
                Avoid disabling
              - table_info: Allow the AI Agent to get information about datasets and schemas
              - create_dataset: Agents respond with data tables

              Actions:

              - calendar: Allow the Agent to access and make changes to your Google Calendar
              - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
                of today's meetings at 5pm on workdays"

              Data processing tools:

              - data_classification: Agents handle queries like "Label these emails as high,
                medium, or low priority"
              - data_extraction: Helps the agent understand data from other tools. Avoid
                disabling
              - image_detection: Extract information from images using AI
              - pdf_extraction: Extraction of information from PDFs using AI

              Enhanced response tools:

              - connect_data: Agents provide buttons to import data in response to queries
                like "Connect Hubspot"
              - download_data: Agents handle queries like "download the table as CSV"

              Web tools:

              - web_search: Agents search the internet, and provide links to their sources
              - fetch_url: Fetch URL content
              - company_prospect_researcher: Agents provide information about companies
              - people_prospect_researcher: Agents provide information about people

          custom_prompt: Use custom prompt to instruct the style and formatting of the agent's response

          description: Description of the agent

          disabled_agent_tools: Array of the agent tools to disable. Disabling is performed after the
              'agent_tools' rules are applied. For example, agent_tools: null and
              disabled_agent_tools: [data_analysis] will enable everything but the
              data_analysis tool. If nothing or [] is provided, nothing is disabled and
              therefore only the agent_tools setting is relevant.

          knowledge_ids: Array of Knowledge IDs the agent should use during the converse. If not
              provided - default settings are used. If null provided - all available knowledge
              is used.

          llm_model: The LLM used to generate responses.

          planning_prompt: Define the planning strategy your AI Agent should use when breaking down tasks
              and solving problems

          system_prompt: Directs your AI Agent's operational behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "agent_model": agent_model,
                    "agent_tools": agent_tools,
                    "custom_prompt": custom_prompt,
                    "description": description,
                    "disabled_agent_tools": disabled_agent_tools,
                    "knowledge_ids": knowledge_ids,
                    "llm_model": llm_model,
                    "planning_prompt": planning_prompt,
                    "system_prompt": system_prompt,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get details of a specific agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        agent_id: str,
        *,
        agent_model: Optional[Literal["magpie-1", "magpie-1.1", "magpie-1.1-flash"]] | NotGiven = NOT_GIVEN,
        agent_tools: Optional[Iterable[agent_update_params.AgentTool]] | NotGiven = NOT_GIVEN,
        custom_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        disabled_agent_tools: Optional[List[AgentTools]] | NotGiven = NOT_GIVEN,
        knowledge_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        llm_model: Optional[
            Literal[
                "gemini-1.5-flash-001",
                "gemini-1.5-flash-002",
                "gemini-2.0-flash-001",
                "gemini-2.0-flash",
                "gemini-2.5-flash-preview-04-17",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-1.5-pro-001",
                "gemini-1.5-pro-002",
                "gemini-2.5-pro-preview-05-06",
                "gemini-2.5-pro",
                "chatgpt-4o-latest",
                "gpt-4",
                "gpt-4-turbo",
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-5",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        planning_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Update an agent configuration

        Args:
          agent_model: The version of Datagrid's agent brain.

          agent_tools: Array of the agent tools to enable. If not provided - default tools of the agent
              are used. If empty list provided - none of the tools are used. If null
              provided - all tools are used. When connection_id is set for a tool, it will use
              that specific connection instead of the default one.

              Knowledge management tools:

              - data_analysis: Answer statistical or analytical questions like "Show my
                quarterly revenue growth"
              - semantic_search: Search knowledge through natural language queries.
              - agent_memory: Agents can remember experiences, conversations and user
                preferences.
              - schema_info: Helps the Agent understand column names and dataset purpose.
                Avoid disabling
              - table_info: Allow the AI Agent to get information about datasets and schemas
              - create_dataset: Agents respond with data tables

              Actions:

              - calendar: Allow the Agent to access and make changes to your Google Calendar
              - schedule_recurring_message_tool: Eliminate busywork such as: "Send a summary
                of today's meetings at 5pm on workdays"

              Data processing tools:

              - data_classification: Agents handle queries like "Label these emails as high,
                medium, or low priority"
              - data_extraction: Helps the agent understand data from other tools. Avoid
                disabling
              - image_detection: Extract information from images using AI
              - pdf_extraction: Extraction of information from PDFs using AI

              Enhanced response tools:

              - connect_data: Agents provide buttons to import data in response to queries
                like "Connect Hubspot"
              - download_data: Agents handle queries like "download the table as CSV"

              Web tools:

              - web_search: Agents search the internet, and provide links to their sources
              - fetch_url: Fetch URL content
              - company_prospect_researcher: Agents provide information about companies
              - people_prospect_researcher: Agents provide information about people

          custom_prompt: Use custom prompt to instruct the style and formatting of the agent's response

          description: Description of the agent

          disabled_agent_tools: Array of the agent tools to disable. Disabling is performed after the
              'agent_tools' rules are applied. For example, agent_tools: null and
              disabled_agent_tools: [data_analysis] will enable everything but the
              data_analysis tool. If nothing or [] is provided, nothing is disabled and
              therefore only the agent_tools setting is relevant.

          knowledge_ids: Array of Knowledge IDs the agent should use during the converse. If not
              provided - default settings are used. If null provided - all available knowledge
              is used.

          llm_model: The LLM used to generate responses.

          name: The name of the agent

          planning_prompt: Define the planning strategy your AI Agent should use when breaking down tasks
              and solving problems

          system_prompt: Directs your AI Agent's operational behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "agent_model": agent_model,
                    "agent_tools": agent_tools,
                    "custom_prompt": custom_prompt,
                    "description": description,
                    "disabled_agent_tools": disabled_agent_tools,
                    "knowledge_ids": knowledge_ids,
                    "llm_model": llm_model,
                    "name": name,
                    "planning_prompt": planning_prompt,
                    "system_prompt": system_prompt,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Agent, AsyncCursorIDPage[Agent]]:
        """
        List all agents for the authenticated organization

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents",
            page=AsyncCursorIDPage[Agent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
