# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.voice import orchestrator_task_list_params
from ..._base_client import make_request_options
from ...types.voice.voice_orchestrator_task import VoiceOrchestratorTask
from ...types.voice.voice_orchestrator_task_list import VoiceOrchestratorTaskList

__all__ = ["OrchestratorTasksResource", "AsyncOrchestratorTasksResource"]


class OrchestratorTasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrchestratorTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return OrchestratorTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrchestratorTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return OrchestratorTasksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTask:
        """
        Retrieve voice orchestrator task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/voice-orchestrator/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceOrchestratorTask,
        )

    def list(
        self,
        *,
        conversation_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTaskList:
        """List delegated voice tasks for the authenticated user.

        By default this returns
        active, non-expired queued or running tasks plus unacknowledged terminal tasks
        and omits task result content from list views. Pass an explicit status filter to
        request a specific task state. A `cancelled` status is reserved for terminal
        task records produced by future cancellation flows; the current voice task inbox
        does not add a user-facing cancel endpoint.

        Args:
          status: Status filter. Repeat the parameter for multiple statuses
              (`?status=queued&status=running`); comma-separated values are also accepted.
              Supported values: queued, running, completed, failed, cancelled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/voice-orchestrator/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "limit": limit,
                        "status": status,
                    },
                    orchestrator_task_list_params.OrchestratorTaskListParams,
                ),
            ),
            cast_to=VoiceOrchestratorTaskList,
        )

    def acknowledge(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTask:
        """
        Acknowledge voice orchestrator task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._patch(
            path_template("/voice-orchestrator/tasks/{task_id}/acknowledge", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceOrchestratorTask,
        )


class AsyncOrchestratorTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrchestratorTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrchestratorTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrchestratorTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncOrchestratorTasksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTask:
        """
        Retrieve voice orchestrator task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/voice-orchestrator/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceOrchestratorTask,
        )

    async def list(
        self,
        *,
        conversation_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTaskList:
        """List delegated voice tasks for the authenticated user.

        By default this returns
        active, non-expired queued or running tasks plus unacknowledged terminal tasks
        and omits task result content from list views. Pass an explicit status filter to
        request a specific task state. A `cancelled` status is reserved for terminal
        task records produced by future cancellation flows; the current voice task inbox
        does not add a user-facing cancel endpoint.

        Args:
          status: Status filter. Repeat the parameter for multiple statuses
              (`?status=queued&status=running`); comma-separated values are also accepted.
              Supported values: queued, running, completed, failed, cancelled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/voice-orchestrator/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversation_id": conversation_id,
                        "limit": limit,
                        "status": status,
                    },
                    orchestrator_task_list_params.OrchestratorTaskListParams,
                ),
            ),
            cast_to=VoiceOrchestratorTaskList,
        )

    async def acknowledge(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceOrchestratorTask:
        """
        Acknowledge voice orchestrator task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._patch(
            path_template("/voice-orchestrator/tasks/{task_id}/acknowledge", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceOrchestratorTask,
        )


class OrchestratorTasksResourceWithRawResponse:
    def __init__(self, orchestrator_tasks: OrchestratorTasksResource) -> None:
        self._orchestrator_tasks = orchestrator_tasks

        self.retrieve = to_raw_response_wrapper(
            orchestrator_tasks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            orchestrator_tasks.list,
        )
        self.acknowledge = to_raw_response_wrapper(
            orchestrator_tasks.acknowledge,
        )


class AsyncOrchestratorTasksResourceWithRawResponse:
    def __init__(self, orchestrator_tasks: AsyncOrchestratorTasksResource) -> None:
        self._orchestrator_tasks = orchestrator_tasks

        self.retrieve = async_to_raw_response_wrapper(
            orchestrator_tasks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            orchestrator_tasks.list,
        )
        self.acknowledge = async_to_raw_response_wrapper(
            orchestrator_tasks.acknowledge,
        )


class OrchestratorTasksResourceWithStreamingResponse:
    def __init__(self, orchestrator_tasks: OrchestratorTasksResource) -> None:
        self._orchestrator_tasks = orchestrator_tasks

        self.retrieve = to_streamed_response_wrapper(
            orchestrator_tasks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            orchestrator_tasks.list,
        )
        self.acknowledge = to_streamed_response_wrapper(
            orchestrator_tasks.acknowledge,
        )


class AsyncOrchestratorTasksResourceWithStreamingResponse:
    def __init__(self, orchestrator_tasks: AsyncOrchestratorTasksResource) -> None:
        self._orchestrator_tasks = orchestrator_tasks

        self.retrieve = async_to_streamed_response_wrapper(
            orchestrator_tasks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            orchestrator_tasks.list,
        )
        self.acknowledge = async_to_streamed_response_wrapper(
            orchestrator_tasks.acknowledge,
        )
