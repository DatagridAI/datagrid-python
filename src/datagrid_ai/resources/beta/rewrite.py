# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import rewrite_rewrite_text_params
from ..._base_client import make_request_options
from ...types.beta.rewrite_response import RewriteResponse

__all__ = ["RewriteResource", "AsyncRewriteResource"]


class RewriteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RewriteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return RewriteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RewriteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return RewriteResourceWithStreamingResponse(self)

    def rewrite_text(
        self,
        *,
        full_text: str,
        prompt: str,
        text_to_rewrite: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewriteResponse:
        """
        Rewrite text using AI with context-aware rewriting capabilities.

        Args:
          full_text: The full text of the document for context.

          prompt: The prompt with instructions for rewriting the text.

          text_to_rewrite: The text to be rewritten.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/beta/rewrite",
            body=maybe_transform(
                {
                    "full_text": full_text,
                    "prompt": prompt,
                    "text_to_rewrite": text_to_rewrite,
                },
                rewrite_rewrite_text_params.RewriteRewriteTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewriteResponse,
        )


class AsyncRewriteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRewriteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRewriteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRewriteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncRewriteResourceWithStreamingResponse(self)

    async def rewrite_text(
        self,
        *,
        full_text: str,
        prompt: str,
        text_to_rewrite: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewriteResponse:
        """
        Rewrite text using AI with context-aware rewriting capabilities.

        Args:
          full_text: The full text of the document for context.

          prompt: The prompt with instructions for rewriting the text.

          text_to_rewrite: The text to be rewritten.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/beta/rewrite",
            body=await async_maybe_transform(
                {
                    "full_text": full_text,
                    "prompt": prompt,
                    "text_to_rewrite": text_to_rewrite,
                },
                rewrite_rewrite_text_params.RewriteRewriteTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewriteResponse,
        )


class RewriteResourceWithRawResponse:
    def __init__(self, rewrite: RewriteResource) -> None:
        self._rewrite = rewrite

        self.rewrite_text = to_raw_response_wrapper(
            rewrite.rewrite_text,
        )


class AsyncRewriteResourceWithRawResponse:
    def __init__(self, rewrite: AsyncRewriteResource) -> None:
        self._rewrite = rewrite

        self.rewrite_text = async_to_raw_response_wrapper(
            rewrite.rewrite_text,
        )


class RewriteResourceWithStreamingResponse:
    def __init__(self, rewrite: RewriteResource) -> None:
        self._rewrite = rewrite

        self.rewrite_text = to_streamed_response_wrapper(
            rewrite.rewrite_text,
        )


class AsyncRewriteResourceWithStreamingResponse:
    def __init__(self, rewrite: AsyncRewriteResource) -> None:
        self._rewrite = rewrite

        self.rewrite_text = async_to_streamed_response_wrapper(
            rewrite.rewrite_text,
        )
