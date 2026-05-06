# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import batch_prediction_list_params, batch_prediction_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncAfterCursorPage, AsyncAfterCursorPage
from .._base_client import AsyncPaginator, make_request_options
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.batch_prediction import BatchPrediction
from ..types.batch_prediction_result_line import BatchPredictionResultLine

__all__ = ["BatchPredictionsResource", "AsyncBatchPredictionsResource"]


class BatchPredictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return BatchPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return BatchPredictionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        items: Iterable[batch_prediction_create_params.Item],
        model: Literal[
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "anthropic.claude-haiku-4-5-20251001-v1:0",
            "anthropic.claude-sonnet-4-5-20250929-v1:0",
            "amazon.nova-2-lite-v1:0",
        ],
        output_schema: Dict[str, object],
        prompt: str,
        completion_window: Optional[Literal["24h"]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """Create a new asynchronous batch prediction job.

        The response returns immediately
        with a `validating` batch while Datagrid validates files and starts background
        processing. Supply an `Idempotency-Key` header to safely retry the same create
        request.

        Args:
          items: Files to process. Each item uses the shared `prompt` and `output_schema`.

          model: LLM model to use for every item in the batch.

          output_schema: JSON Schema Draft 2020-12 describing each item output. The root schema must be
              `type: object`. The batch prediction API currently rejects `$defs`, `$ref`,
              `allOf`, `anyOf`, `not`, `oneOf`, and `patternProperties` anywhere in the
              schema.

          prompt: Shared instruction applied to each item in the batch.

          completion_window: Requested completion window. Defaults to `24h` when omitted; no other values are
              currently supported.

          metadata: Optional metadata map with up to 16 entries. Metadata keys must be 64 characters
              or fewer and values must be 512 characters or fewer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/batch-predictions",
            body=maybe_transform(
                {
                    "items": items,
                    "model": model,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "completion_window": completion_window,
                    "metadata": metadata,
                },
                batch_prediction_create_params.BatchPredictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    def retrieve(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """Retrieves a batch prediction by id.

        Terminal batches include a `results_url`
        until retained result lines are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        return self._get(
            path_template("/batch-predictions/{batch_prediction_id}", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal[
            "validating", "failed", "in_progress", "finalizing", "completed", "expired", "cancelling", "cancelled"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncAfterCursorPage[BatchPrediction]:
        """
        Returns batch predictions for the authenticated teamspace in reverse
        chronological order. Use `after` with `next_cursor` from the previous response
        to paginate.

        Args:
          after: Opaque cursor returned by a previous list call.

          limit: The maximum number of batch predictions to return, between 1 and 100.

          status: Optional filter by batch prediction status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/batch-predictions",
            page=SyncAfterCursorPage[BatchPrediction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "status": status,
                    },
                    batch_prediction_list_params.BatchPredictionListParams,
                ),
            ),
            model=BatchPrediction,
        )

    def cancel(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """
        Requests cancellation for a batch prediction that is still validating or in
        progress. A batch that is already `cancelling` or `cancelled` is returned
        unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        return self._post(
            path_template("/batch-predictions/{batch_prediction_id}/cancel", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    def retrieve_results(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[BatchPredictionResultLine]:
        """
        Streams newline-delimited JSON (NDJSON) result lines for a terminal batch
        prediction. Read the response body line-by-line and JSON parse each non-empty
        line. Results are retained for a limited window after batch creation; after
        cleanup, this endpoint returns `410 Gone`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return self._get(
            path_template("/batch-predictions/{batch_prediction_id}/results", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[BatchPredictionResultLine],
            stream=True,
        )


class AsyncBatchPredictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchPredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchPredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchPredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncBatchPredictionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        items: Iterable[batch_prediction_create_params.Item],
        model: Literal[
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "anthropic.claude-haiku-4-5-20251001-v1:0",
            "anthropic.claude-sonnet-4-5-20250929-v1:0",
            "amazon.nova-2-lite-v1:0",
        ],
        output_schema: Dict[str, object],
        prompt: str,
        completion_window: Optional[Literal["24h"]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """Create a new asynchronous batch prediction job.

        The response returns immediately
        with a `validating` batch while Datagrid validates files and starts background
        processing. Supply an `Idempotency-Key` header to safely retry the same create
        request.

        Args:
          items: Files to process. Each item uses the shared `prompt` and `output_schema`.

          model: LLM model to use for every item in the batch.

          output_schema: JSON Schema Draft 2020-12 describing each item output. The root schema must be
              `type: object`. The batch prediction API currently rejects `$defs`, `$ref`,
              `allOf`, `anyOf`, `not`, `oneOf`, and `patternProperties` anywhere in the
              schema.

          prompt: Shared instruction applied to each item in the batch.

          completion_window: Requested completion window. Defaults to `24h` when omitted; no other values are
              currently supported.

          metadata: Optional metadata map with up to 16 entries. Metadata keys must be 64 characters
              or fewer and values must be 512 characters or fewer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/batch-predictions",
            body=await async_maybe_transform(
                {
                    "items": items,
                    "model": model,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "completion_window": completion_window,
                    "metadata": metadata,
                },
                batch_prediction_create_params.BatchPredictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    async def retrieve(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """Retrieves a batch prediction by id.

        Terminal batches include a `results_url`
        until retained result lines are cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        return await self._get(
            path_template("/batch-predictions/{batch_prediction_id}", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal[
            "validating", "failed", "in_progress", "finalizing", "completed", "expired", "cancelling", "cancelled"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BatchPrediction, AsyncAfterCursorPage[BatchPrediction]]:
        """
        Returns batch predictions for the authenticated teamspace in reverse
        chronological order. Use `after` with `next_cursor` from the previous response
        to paginate.

        Args:
          after: Opaque cursor returned by a previous list call.

          limit: The maximum number of batch predictions to return, between 1 and 100.

          status: Optional filter by batch prediction status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/batch-predictions",
            page=AsyncAfterCursorPage[BatchPrediction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "status": status,
                    },
                    batch_prediction_list_params.BatchPredictionListParams,
                ),
            ),
            model=BatchPrediction,
        )

    async def cancel(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchPrediction:
        """
        Requests cancellation for a batch prediction that is still validating or in
        progress. A batch that is already `cancelling` or `cancelled` is returned
        unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        return await self._post(
            path_template("/batch-predictions/{batch_prediction_id}/cancel", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchPrediction,
        )

    async def retrieve_results(
        self,
        batch_prediction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[BatchPredictionResultLine]:
        """
        Streams newline-delimited JSON (NDJSON) result lines for a terminal batch
        prediction. Read the response body line-by-line and JSON parse each non-empty
        line. Results are retained for a limited window after batch creation; after
        cleanup, this endpoint returns `410 Gone`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_prediction_id:
            raise ValueError(
                f"Expected a non-empty value for `batch_prediction_id` but received {batch_prediction_id!r}"
            )
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return await self._get(
            path_template("/batch-predictions/{batch_prediction_id}/results", batch_prediction_id=batch_prediction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[BatchPredictionResultLine],
            stream=True,
        )


class BatchPredictionsResourceWithRawResponse:
    def __init__(self, batch_predictions: BatchPredictionsResource) -> None:
        self._batch_predictions = batch_predictions

        self.create = to_raw_response_wrapper(
            batch_predictions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            batch_predictions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            batch_predictions.list,
        )
        self.cancel = to_raw_response_wrapper(
            batch_predictions.cancel,
        )
        self.retrieve_results = to_raw_response_wrapper(
            batch_predictions.retrieve_results,
        )


class AsyncBatchPredictionsResourceWithRawResponse:
    def __init__(self, batch_predictions: AsyncBatchPredictionsResource) -> None:
        self._batch_predictions = batch_predictions

        self.create = async_to_raw_response_wrapper(
            batch_predictions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            batch_predictions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            batch_predictions.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            batch_predictions.cancel,
        )
        self.retrieve_results = async_to_raw_response_wrapper(
            batch_predictions.retrieve_results,
        )


class BatchPredictionsResourceWithStreamingResponse:
    def __init__(self, batch_predictions: BatchPredictionsResource) -> None:
        self._batch_predictions = batch_predictions

        self.create = to_streamed_response_wrapper(
            batch_predictions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            batch_predictions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            batch_predictions.list,
        )
        self.cancel = to_streamed_response_wrapper(
            batch_predictions.cancel,
        )
        self.retrieve_results = to_streamed_response_wrapper(
            batch_predictions.retrieve_results,
        )


class AsyncBatchPredictionsResourceWithStreamingResponse:
    def __init__(self, batch_predictions: AsyncBatchPredictionsResource) -> None:
        self._batch_predictions = batch_predictions

        self.create = async_to_streamed_response_wrapper(
            batch_predictions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            batch_predictions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            batch_predictions.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            batch_predictions.cancel,
        )
        self.retrieve_results = async_to_streamed_response_wrapper(
            batch_predictions.retrieve_results,
        )
