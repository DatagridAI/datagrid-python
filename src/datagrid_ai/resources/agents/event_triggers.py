# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import event_trigger_create_params, event_trigger_update_params
from ...types.agents.event_trigger_list_response import EventTriggerListResponse
from ...types.agents.event_trigger_create_response import EventTriggerCreateResponse
from ...types.agents.event_trigger_update_response import EventTriggerUpdateResponse

__all__ = ["EventTriggersResource", "AsyncEventTriggersResource"]


class EventTriggersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventTriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return EventTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventTriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return EventTriggersResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        enabled: bool,
        trigger_event: str,
        trigger_source: Literal["procore", "sharepoint"],
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_thread: Optional[Literal["create_new_thread_each_time"]] | Omit = omit,
        run_conditions: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerCreateResponse:
        """
        Create an event trigger for the specified agent so it runs automatically when
        the configured provider event fires. Prerequisite gaps that do not prevent the
        trigger from being saved (e.g. a missing Procore company/project mapping or
        credentials) are returned in the `warnings` array on the response rather than
        failing the request. An agent may only have one event trigger — attempting to
        create a second is rejected with a 409 error.

        Args:
          enabled: Whether the trigger should be active immediately. Set to `false` to create it in
              a paused state.

          trigger_event: The event that fires the agent, in `"ResourceName:eventType"` format (e.g.
              `"Tasks:create"`). Required even when `enabled` is `false`.

          trigger_source: The external provider that emits the event.

          description: Optional description of what the App Event automation does.

          name: Optional name for the App Event automation.

          response_thread: Controls how the agent's response conversation is threaded when the trigger
              fires. `create_new_thread_each_time` starts a fresh thread for every event; when
              omitted, responses reuse a single thread.

          run_conditions: Optional natural-language conditions that must hold for the agent to run when
              the event fires.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/agents/{agent_id}/event-triggers", agent_id=agent_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "trigger_event": trigger_event,
                    "trigger_source": trigger_source,
                    "description": description,
                    "name": name,
                    "response_thread": response_thread,
                    "run_conditions": run_conditions,
                },
                event_trigger_create_params.EventTriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerCreateResponse,
        )

    def update(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_thread: Optional[Literal["create_new_thread_each_time"]] | Omit = omit,
        run_conditions: Optional[str] | Omit = omit,
        trigger_event: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerUpdateResponse:
        """Update an existing event trigger on the specified agent.

        Only the fields
        supplied in the request body are changed; omitted fields keep their current
        value. Use `enabled` to pause (`false`) or resume (`true`) the trigger. As with
        creation, non-fatal prerequisite gaps are returned in the `warnings` array
        rather than failing the request.

        Args:
          description: Updated description. Pass `null` to clear.

          enabled: Set to `true` to resume the trigger; `false` to pause it.

          name: Updated name. Pass `null` to clear.

          response_thread: Controls how the agent's response conversation is threaded when the trigger
              fires. `create_new_thread_each_time` starts a fresh thread for every event; when
              omitted, responses reuse a single thread.

          run_conditions: Updated run conditions. Pass `null` to clear.

          trigger_event: Updated event in `"ResourceName:eventType"` format. Omit to leave the current
              event unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._patch(
            path_template("/agents/{agent_id}/event-triggers/{trigger_id}", agent_id=agent_id, trigger_id=trigger_id),
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "response_thread": response_thread,
                    "run_conditions": run_conditions,
                    "trigger_event": trigger_event,
                },
                event_trigger_update_params.EventTriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerUpdateResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerListResponse:
        """
        List the App Event automations (event triggers) configured for the specified
        agent. An event trigger fires the agent in response to an external provider
        event (e.g. a Procore webhook such as `Tasks:create`). An agent has at most one
        event trigger, so the returned list contains zero or one item and `has_more` is
        always `false`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/agents/{agent_id}/event-triggers", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerListResponse,
        )

    def delete(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an event trigger from the specified agent.

        This unregisters the
        underlying provider webhook subscription and stops the agent from running in
        response to the event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/agents/{agent_id}/event-triggers/{trigger_id}", agent_id=agent_id, trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEventTriggersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventTriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventTriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncEventTriggersResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        enabled: bool,
        trigger_event: str,
        trigger_source: Literal["procore", "sharepoint"],
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_thread: Optional[Literal["create_new_thread_each_time"]] | Omit = omit,
        run_conditions: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerCreateResponse:
        """
        Create an event trigger for the specified agent so it runs automatically when
        the configured provider event fires. Prerequisite gaps that do not prevent the
        trigger from being saved (e.g. a missing Procore company/project mapping or
        credentials) are returned in the `warnings` array on the response rather than
        failing the request. An agent may only have one event trigger — attempting to
        create a second is rejected with a 409 error.

        Args:
          enabled: Whether the trigger should be active immediately. Set to `false` to create it in
              a paused state.

          trigger_event: The event that fires the agent, in `"ResourceName:eventType"` format (e.g.
              `"Tasks:create"`). Required even when `enabled` is `false`.

          trigger_source: The external provider that emits the event.

          description: Optional description of what the App Event automation does.

          name: Optional name for the App Event automation.

          response_thread: Controls how the agent's response conversation is threaded when the trigger
              fires. `create_new_thread_each_time` starts a fresh thread for every event; when
              omitted, responses reuse a single thread.

          run_conditions: Optional natural-language conditions that must hold for the agent to run when
              the event fires.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/agents/{agent_id}/event-triggers", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "trigger_event": trigger_event,
                    "trigger_source": trigger_source,
                    "description": description,
                    "name": name,
                    "response_thread": response_thread,
                    "run_conditions": run_conditions,
                },
                event_trigger_create_params.EventTriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerCreateResponse,
        )

    async def update(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        response_thread: Optional[Literal["create_new_thread_each_time"]] | Omit = omit,
        run_conditions: Optional[str] | Omit = omit,
        trigger_event: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerUpdateResponse:
        """Update an existing event trigger on the specified agent.

        Only the fields
        supplied in the request body are changed; omitted fields keep their current
        value. Use `enabled` to pause (`false`) or resume (`true`) the trigger. As with
        creation, non-fatal prerequisite gaps are returned in the `warnings` array
        rather than failing the request.

        Args:
          description: Updated description. Pass `null` to clear.

          enabled: Set to `true` to resume the trigger; `false` to pause it.

          name: Updated name. Pass `null` to clear.

          response_thread: Controls how the agent's response conversation is threaded when the trigger
              fires. `create_new_thread_each_time` starts a fresh thread for every event; when
              omitted, responses reuse a single thread.

          run_conditions: Updated run conditions. Pass `null` to clear.

          trigger_event: Updated event in `"ResourceName:eventType"` format. Omit to leave the current
              event unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._patch(
            path_template("/agents/{agent_id}/event-triggers/{trigger_id}", agent_id=agent_id, trigger_id=trigger_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "response_thread": response_thread,
                    "run_conditions": run_conditions,
                    "trigger_event": trigger_event,
                },
                event_trigger_update_params.EventTriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerUpdateResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventTriggerListResponse:
        """
        List the App Event automations (event triggers) configured for the specified
        agent. An event trigger fires the agent in response to an external provider
        event (e.g. a Procore webhook such as `Tasks:create`). An agent has at most one
        event trigger, so the returned list contains zero or one item and `has_more` is
        always `false`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/agents/{agent_id}/event-triggers", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventTriggerListResponse,
        )

    async def delete(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an event trigger from the specified agent.

        This unregisters the
        underlying provider webhook subscription and stops the agent from running in
        response to the event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/agents/{agent_id}/event-triggers/{trigger_id}", agent_id=agent_id, trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EventTriggersResourceWithRawResponse:
    def __init__(self, event_triggers: EventTriggersResource) -> None:
        self._event_triggers = event_triggers

        self.create = to_raw_response_wrapper(
            event_triggers.create,
        )
        self.update = to_raw_response_wrapper(
            event_triggers.update,
        )
        self.list = to_raw_response_wrapper(
            event_triggers.list,
        )
        self.delete = to_raw_response_wrapper(
            event_triggers.delete,
        )


class AsyncEventTriggersResourceWithRawResponse:
    def __init__(self, event_triggers: AsyncEventTriggersResource) -> None:
        self._event_triggers = event_triggers

        self.create = async_to_raw_response_wrapper(
            event_triggers.create,
        )
        self.update = async_to_raw_response_wrapper(
            event_triggers.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_triggers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            event_triggers.delete,
        )


class EventTriggersResourceWithStreamingResponse:
    def __init__(self, event_triggers: EventTriggersResource) -> None:
        self._event_triggers = event_triggers

        self.create = to_streamed_response_wrapper(
            event_triggers.create,
        )
        self.update = to_streamed_response_wrapper(
            event_triggers.update,
        )
        self.list = to_streamed_response_wrapper(
            event_triggers.list,
        )
        self.delete = to_streamed_response_wrapper(
            event_triggers.delete,
        )


class AsyncEventTriggersResourceWithStreamingResponse:
    def __init__(self, event_triggers: AsyncEventTriggersResource) -> None:
        self._event_triggers = event_triggers

        self.create = async_to_streamed_response_wrapper(
            event_triggers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            event_triggers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_triggers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            event_triggers.delete,
        )
