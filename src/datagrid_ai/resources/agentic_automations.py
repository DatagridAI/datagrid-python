# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import agentic_automation_create_scheduled_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.agentic_automation import AgenticAutomation

__all__ = ["AgenticAutomationsResource", "AsyncAgenticAutomationsResource"]


class AgenticAutomationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgenticAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AgenticAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgenticAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AgenticAutomationsResourceWithStreamingResponse(self)

    def create_scheduled(
        self,
        *,
        agent_id: str,
        cron: str,
        name: str,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgenticAutomation:
        """Create a scheduled automation for an agent.

        The automation fires on the given
        cron schedule and runs the agent. `agent_id` is in the body. Schedules must fire
        at most once every 15 minutes.

        Args:
          agent_id: The ID of the agent this automation runs.

          cron: Five-field cron expression (minute hour day month day-of-week) controlling when
              the automation fires. Seconds are not supported. The schedule must fire at most
              once every 15 minutes.

          name: Human-readable name for the automation.

          description: Optional free-text description of what this automation does.

          enabled: Whether the automation should be active immediately after creation. Defaults to
              `true` when omitted or null.

          timezone: IANA timezone identifier in which `cron` is interpreted. Defaults to `"UTC"`
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agentic-automations/scheduled",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "cron": cron,
                    "name": name,
                    "description": description,
                    "enabled": enabled,
                    "timezone": timezone,
                },
                agentic_automation_create_scheduled_params.AgenticAutomationCreateScheduledParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgenticAutomation,
        )


class AsyncAgenticAutomationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgenticAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgenticAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgenticAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncAgenticAutomationsResourceWithStreamingResponse(self)

    async def create_scheduled(
        self,
        *,
        agent_id: str,
        cron: str,
        name: str,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgenticAutomation:
        """Create a scheduled automation for an agent.

        The automation fires on the given
        cron schedule and runs the agent. `agent_id` is in the body. Schedules must fire
        at most once every 15 minutes.

        Args:
          agent_id: The ID of the agent this automation runs.

          cron: Five-field cron expression (minute hour day month day-of-week) controlling when
              the automation fires. Seconds are not supported. The schedule must fire at most
              once every 15 minutes.

          name: Human-readable name for the automation.

          description: Optional free-text description of what this automation does.

          enabled: Whether the automation should be active immediately after creation. Defaults to
              `true` when omitted or null.

          timezone: IANA timezone identifier in which `cron` is interpreted. Defaults to `"UTC"`
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agentic-automations/scheduled",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "cron": cron,
                    "name": name,
                    "description": description,
                    "enabled": enabled,
                    "timezone": timezone,
                },
                agentic_automation_create_scheduled_params.AgenticAutomationCreateScheduledParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgenticAutomation,
        )


class AgenticAutomationsResourceWithRawResponse:
    def __init__(self, agentic_automations: AgenticAutomationsResource) -> None:
        self._agentic_automations = agentic_automations

        self.create_scheduled = to_raw_response_wrapper(
            agentic_automations.create_scheduled,
        )


class AsyncAgenticAutomationsResourceWithRawResponse:
    def __init__(self, agentic_automations: AsyncAgenticAutomationsResource) -> None:
        self._agentic_automations = agentic_automations

        self.create_scheduled = async_to_raw_response_wrapper(
            agentic_automations.create_scheduled,
        )


class AgenticAutomationsResourceWithStreamingResponse:
    def __init__(self, agentic_automations: AgenticAutomationsResource) -> None:
        self._agentic_automations = agentic_automations

        self.create_scheduled = to_streamed_response_wrapper(
            agentic_automations.create_scheduled,
        )


class AsyncAgenticAutomationsResourceWithStreamingResponse:
    def __init__(self, agentic_automations: AsyncAgenticAutomationsResource) -> None:
        self._agentic_automations = agentic_automations

        self.create_scheduled = async_to_streamed_response_wrapper(
            agentic_automations.create_scheduled,
        )
