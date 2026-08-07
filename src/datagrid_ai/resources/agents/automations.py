# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorIDPage, AsyncCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import automation_list_params, automation_create_params, automation_update_params
from ...types.agents.automation import Automation

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AutomationsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        cron: str,
        name: str,
        prompt: str,
        description: Optional[str] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        notification_preference: Optional[Literal["always", "on_failure", "never"]] | Omit = omit,
        output_channel_id: Optional[str] | Omit = omit,
        output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]] | Omit = omit,
        prompt_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        thread_mode: Optional[Literal["new_thread", "same_conversation"]] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """Create a new `runAgent` automation for the specified agent.

        The automation will
        fire on the provided cron schedule (in the given IANA timezone) and run the
        agent with the supplied prompt. Schedules must fire at most once every 15
        minutes — finer-grained expressions are rejected with a 400 error.

        Args:
          cron: Five-field cron expression (minute hour day month day-of-week) controlling when
              the automation fires. Seconds are not supported. The schedule must fire at most
              once every 15 minutes — finer-grained expressions are rejected with a 400 error.

          name: Human-readable name for the automation.

          prompt: The instruction text sent to the agent each time the automation fires. Supports
              Markdown. This is the agent's task for the run. Must not be empty or
              whitespace-only.

          description: Optional free-text description of what this automation does.

          destination_id: The channel ID or user ID for the conversation destination. Required when
              `destination_type` is `channel` or `user_dm`; omit for `agent_dm`.

          destination_type: Where the automation's conversation runs and results are delivered.

              - `agent_dm` — (default) Results are posted in the agent's own DM space. No
                `destination_id` is required.
              - `channel` — Results are posted in a specific Datagrid channel. Provide the
                channel ID in `destination_id`.
              - `user_dm` — Results are sent as a direct message to a specific user. Provide
                the user ID in `destination_id`.

          enabled: Whether the automation should be active immediately after creation. Defaults to
              `true` when omitted or null. Set to `false` to create the automation in a paused
              state — it will not fire until explicitly enabled via the Update automation
              endpoint.

          notification_preference: Controls when users are notified about automation run outcomes.

              - `always` — Notify after every run regardless of success or failure. -
                `on_failure` — (default) Notify only when a run fails or produces an error.
              - `never` — Do not send notifications for this automation.

          output_channel_id: ID of an additional delivery channel (Slack, Teams, email, etc.) where the
              agent's output is also delivered after each run. Must be provided together with
              `output_channel_type` — supplying one without the other is rejected with a 400
              error. This is an external transport address, not a Datagrid-owned resource —
              it's validated against the caller's own connected integrations at delivery time.

          output_channel_type: Transport type of `output_channel_id`. One of `"email"`, `"slack"`, `"teams"`,
              `"sms"`. Must be provided together with `output_channel_id`.

          prompt_file_ids: IDs of files to attach as context for every run of this automation. Each file
              must exist and belong to the caller's teamspace, or the request is rejected with
              a 404 error. Limited to 20 IDs per request.

          thread_mode: Controls whether each scheduled run creates a fresh conversation thread or
              continues in the same persistent conversation.

              - `new_thread` — (default) Each run starts a new conversation. Results are
                isolated; the agent has no memory of prior runs unless it uses agent memory
                tools.
              - `same_conversation` — Every run appends to the same conversation thread. The
                agent sees the full history of prior runs, which is useful for incremental
                summaries or stateful workflows.

          timezone: IANA timezone identifier in which `cron` is interpreted. Defaults to `"UTC"`
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/agents/{agent_id}/automations", agent_id=agent_id),
            body=maybe_transform(
                {
                    "cron": cron,
                    "name": name,
                    "prompt": prompt,
                    "description": description,
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled": enabled,
                    "notification_preference": notification_preference,
                    "output_channel_id": output_channel_id,
                    "output_channel_type": output_channel_type,
                    "prompt_file_ids": prompt_file_ids,
                    "thread_mode": thread_mode,
                    "timezone": timezone,
                },
                automation_create_params.AutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    def retrieve(
        self,
        automation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """
        Get details of a specific automation belonging to an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._get(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    def update(
        self,
        automation_id: str,
        *,
        agent_id: str,
        cron: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        notification_preference: Optional[Literal["always", "on_failure", "never"]] | Omit = omit,
        output_channel_id: Optional[str] | Omit = omit,
        output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        prompt_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        thread_mode: Optional[Literal["new_thread", "same_conversation"]] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """Update an existing automation.

        All fields are optional — only supplied fields
        are changed. Updating `cron` or `timezone` triggers the same 15-minute
        minimum-interval validation as creation.

        Args:
          cron: Updated five-field cron expression. The same 15-minute minimum interval rule
              applies. Pass `null` to leave the schedule unchanged.

          description: Updated description.

          destination_id: Updated destination channel or user ID.

          destination_type: Where the automation's conversation runs and results are delivered.

              - `agent_dm` — (default) Results are posted in the agent's own DM space. No
                `destination_id` is required.
              - `channel` — Results are posted in a specific Datagrid channel. Provide the
                channel ID in `destination_id`.
              - `user_dm` — Results are sent as a direct message to a specific user. Provide
                the user ID in `destination_id`.

          enabled: Set to `true` to resume scheduling; `false` to pause. Pausing does not delete
              the automation or its history. Null is treated as unset (no change).

          name: Updated human-readable name for the automation.

          notification_preference: Controls when users are notified about automation run outcomes.

              - `always` — Notify after every run regardless of success or failure. -
                `on_failure` — (default) Notify only when a run fails or produces an error.
              - `never` — Do not send notifications for this automation.

          output_channel_id: Updated output delivery channel ID. Must be provided together with
              `output_channel_type` in the resulting configuration — supplying one without the
              other is rejected with a 400 error. This is an external transport address, not a
              Datagrid-owned resource — it's validated against the caller's own connected
              integrations at delivery time.

          output_channel_type: Updated transport type for the output channel. One of `"email"`, `"slack"`,
              `"teams"`, `"sms"`. Must be provided together with `output_channel_id` in the
              resulting configuration.

          prompt: Updated instruction text for the agent. Pass `null` to leave unchanged. Must not
              be empty or whitespace-only.

          prompt_file_ids: Updated list of file IDs to attach as context. Each file must exist and belong
              to the caller's teamspace, or the request is rejected with a 404 error. Limited
              to 20 IDs per request.

          thread_mode: Controls whether each scheduled run creates a fresh conversation thread or
              continues in the same persistent conversation.

              - `new_thread` — (default) Each run starts a new conversation. Results are
                isolated; the agent has no memory of prior runs unless it uses agent memory
                tools.
              - `same_conversation` — Every run appends to the same conversation thread. The
                agent sees the full history of prior runs, which is useful for incremental
                summaries or stateful workflows.

          timezone: Updated IANA timezone. Pass `null` to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._patch(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            body=maybe_transform(
                {
                    "cron": cron,
                    "description": description,
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled": enabled,
                    "name": name,
                    "notification_preference": notification_preference,
                    "output_channel_id": output_channel_id,
                    "output_channel_type": output_channel_type,
                    "prompt": prompt,
                    "prompt_file_ids": prompt_file_ids,
                    "thread_mode": thread_mode,
                    "timezone": timezone,
                },
                automation_update_params.AutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[Automation]:
        """List all `runAgent` automations that belong to the specified agent.

        Returns
        automations in reverse-chronological order (newest first). Use the cursor
        pagination parameters (`limit`, `after`, `before`) to page through large result
        sets.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template("/agents/{agent_id}/automations", agent_id=agent_id),
            page=SyncCursorIDPage[Automation],
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
                    automation_list_params.AutomationListParams,
                ),
            ),
            model=Automation,
        )

    def delete(
        self,
        automation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an automation.

        The automation is soft-deleted: it stops firing and no
        longer appears in list or retrieve responses, but its past run history is
        retained. The agent and its other automations are not affected. Scheduled runs
        that are already queued may still execute before the deletion propagates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAutomationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncAutomationsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        cron: str,
        name: str,
        prompt: str,
        description: Optional[str] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        notification_preference: Optional[Literal["always", "on_failure", "never"]] | Omit = omit,
        output_channel_id: Optional[str] | Omit = omit,
        output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]] | Omit = omit,
        prompt_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        thread_mode: Optional[Literal["new_thread", "same_conversation"]] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """Create a new `runAgent` automation for the specified agent.

        The automation will
        fire on the provided cron schedule (in the given IANA timezone) and run the
        agent with the supplied prompt. Schedules must fire at most once every 15
        minutes — finer-grained expressions are rejected with a 400 error.

        Args:
          cron: Five-field cron expression (minute hour day month day-of-week) controlling when
              the automation fires. Seconds are not supported. The schedule must fire at most
              once every 15 minutes — finer-grained expressions are rejected with a 400 error.

          name: Human-readable name for the automation.

          prompt: The instruction text sent to the agent each time the automation fires. Supports
              Markdown. This is the agent's task for the run. Must not be empty or
              whitespace-only.

          description: Optional free-text description of what this automation does.

          destination_id: The channel ID or user ID for the conversation destination. Required when
              `destination_type` is `channel` or `user_dm`; omit for `agent_dm`.

          destination_type: Where the automation's conversation runs and results are delivered.

              - `agent_dm` — (default) Results are posted in the agent's own DM space. No
                `destination_id` is required.
              - `channel` — Results are posted in a specific Datagrid channel. Provide the
                channel ID in `destination_id`.
              - `user_dm` — Results are sent as a direct message to a specific user. Provide
                the user ID in `destination_id`.

          enabled: Whether the automation should be active immediately after creation. Defaults to
              `true` when omitted or null. Set to `false` to create the automation in a paused
              state — it will not fire until explicitly enabled via the Update automation
              endpoint.

          notification_preference: Controls when users are notified about automation run outcomes.

              - `always` — Notify after every run regardless of success or failure. -
                `on_failure` — (default) Notify only when a run fails or produces an error.
              - `never` — Do not send notifications for this automation.

          output_channel_id: ID of an additional delivery channel (Slack, Teams, email, etc.) where the
              agent's output is also delivered after each run. Must be provided together with
              `output_channel_type` — supplying one without the other is rejected with a 400
              error. This is an external transport address, not a Datagrid-owned resource —
              it's validated against the caller's own connected integrations at delivery time.

          output_channel_type: Transport type of `output_channel_id`. One of `"email"`, `"slack"`, `"teams"`,
              `"sms"`. Must be provided together with `output_channel_id`.

          prompt_file_ids: IDs of files to attach as context for every run of this automation. Each file
              must exist and belong to the caller's teamspace, or the request is rejected with
              a 404 error. Limited to 20 IDs per request.

          thread_mode: Controls whether each scheduled run creates a fresh conversation thread or
              continues in the same persistent conversation.

              - `new_thread` — (default) Each run starts a new conversation. Results are
                isolated; the agent has no memory of prior runs unless it uses agent memory
                tools.
              - `same_conversation` — Every run appends to the same conversation thread. The
                agent sees the full history of prior runs, which is useful for incremental
                summaries or stateful workflows.

          timezone: IANA timezone identifier in which `cron` is interpreted. Defaults to `"UTC"`
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/agents/{agent_id}/automations", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "cron": cron,
                    "name": name,
                    "prompt": prompt,
                    "description": description,
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled": enabled,
                    "notification_preference": notification_preference,
                    "output_channel_id": output_channel_id,
                    "output_channel_type": output_channel_type,
                    "prompt_file_ids": prompt_file_ids,
                    "thread_mode": thread_mode,
                    "timezone": timezone,
                },
                automation_create_params.AutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    async def retrieve(
        self,
        automation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """
        Get details of a specific automation belonging to an agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._get(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    async def update(
        self,
        automation_id: str,
        *,
        agent_id: str,
        cron: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        destination_id: Optional[str] | Omit = omit,
        destination_type: Optional[Literal["agent_dm", "channel", "user_dm"]] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        notification_preference: Optional[Literal["always", "on_failure", "never"]] | Omit = omit,
        output_channel_id: Optional[str] | Omit = omit,
        output_channel_type: Optional[Literal["email", "slack", "teams", "sms"]] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        prompt_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        thread_mode: Optional[Literal["new_thread", "same_conversation"]] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Automation:
        """Update an existing automation.

        All fields are optional — only supplied fields
        are changed. Updating `cron` or `timezone` triggers the same 15-minute
        minimum-interval validation as creation.

        Args:
          cron: Updated five-field cron expression. The same 15-minute minimum interval rule
              applies. Pass `null` to leave the schedule unchanged.

          description: Updated description.

          destination_id: Updated destination channel or user ID.

          destination_type: Where the automation's conversation runs and results are delivered.

              - `agent_dm` — (default) Results are posted in the agent's own DM space. No
                `destination_id` is required.
              - `channel` — Results are posted in a specific Datagrid channel. Provide the
                channel ID in `destination_id`.
              - `user_dm` — Results are sent as a direct message to a specific user. Provide
                the user ID in `destination_id`.

          enabled: Set to `true` to resume scheduling; `false` to pause. Pausing does not delete
              the automation or its history. Null is treated as unset (no change).

          name: Updated human-readable name for the automation.

          notification_preference: Controls when users are notified about automation run outcomes.

              - `always` — Notify after every run regardless of success or failure. -
                `on_failure` — (default) Notify only when a run fails or produces an error.
              - `never` — Do not send notifications for this automation.

          output_channel_id: Updated output delivery channel ID. Must be provided together with
              `output_channel_type` in the resulting configuration — supplying one without the
              other is rejected with a 400 error. This is an external transport address, not a
              Datagrid-owned resource — it's validated against the caller's own connected
              integrations at delivery time.

          output_channel_type: Updated transport type for the output channel. One of `"email"`, `"slack"`,
              `"teams"`, `"sms"`. Must be provided together with `output_channel_id` in the
              resulting configuration.

          prompt: Updated instruction text for the agent. Pass `null` to leave unchanged. Must not
              be empty or whitespace-only.

          prompt_file_ids: Updated list of file IDs to attach as context. Each file must exist and belong
              to the caller's teamspace, or the request is rejected with a 404 error. Limited
              to 20 IDs per request.

          thread_mode: Controls whether each scheduled run creates a fresh conversation thread or
              continues in the same persistent conversation.

              - `new_thread` — (default) Each run starts a new conversation. Results are
                isolated; the agent has no memory of prior runs unless it uses agent memory
                tools.
              - `same_conversation` — Every run appends to the same conversation thread. The
                agent sees the full history of prior runs, which is useful for incremental
                summaries or stateful workflows.

          timezone: Updated IANA timezone. Pass `null` to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._patch(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            body=await async_maybe_transform(
                {
                    "cron": cron,
                    "description": description,
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled": enabled,
                    "name": name,
                    "notification_preference": notification_preference,
                    "output_channel_id": output_channel_id,
                    "output_channel_type": output_channel_type,
                    "prompt": prompt,
                    "prompt_file_ids": prompt_file_ids,
                    "thread_mode": thread_mode,
                    "timezone": timezone,
                },
                automation_update_params.AutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Automation,
        )

    def list(
        self,
        agent_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Automation, AsyncCursorIDPage[Automation]]:
        """List all `runAgent` automations that belong to the specified agent.

        Returns
        automations in reverse-chronological order (newest first). Use the cursor
        pagination parameters (`limit`, `after`, `before`) to page through large result
        sets.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template("/agents/{agent_id}/automations", agent_id=agent_id),
            page=AsyncCursorIDPage[Automation],
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
                    automation_list_params.AutomationListParams,
                ),
            ),
            model=Automation,
        )

    async def delete(
        self,
        automation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an automation.

        The automation is soft-deleted: it stops firing and no
        longer appears in list or retrieve responses, but its past run history is
        retained. The agent and its other automations are not affected. Scheduled runs
        that are already queued may still execute before the deletion propagates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/agents/{agent_id}/automations/{automation_id}", agent_id=agent_id, automation_id=automation_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.create = to_raw_response_wrapper(
            automations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            automations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            automations.update,
        )
        self.list = to_raw_response_wrapper(
            automations.list,
        )
        self.delete = to_raw_response_wrapper(
            automations.delete,
        )


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.create = async_to_raw_response_wrapper(
            automations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            automations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            automations.update,
        )
        self.list = async_to_raw_response_wrapper(
            automations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            automations.delete,
        )


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.create = to_streamed_response_wrapper(
            automations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            automations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            automations.update,
        )
        self.list = to_streamed_response_wrapper(
            automations.list,
        )
        self.delete = to_streamed_response_wrapper(
            automations.delete,
        )


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.create = async_to_streamed_response_wrapper(
            automations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            automations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            automations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            automations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            automations.delete,
        )
