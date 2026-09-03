# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .user_credits_consumption import (
    UserCreditsConsumptionResource,
    AsyncUserCreditsConsumptionResource,
    UserCreditsConsumptionResourceWithRawResponse,
    AsyncUserCreditsConsumptionResourceWithRawResponse,
    UserCreditsConsumptionResourceWithStreamingResponse,
    AsyncUserCreditsConsumptionResourceWithStreamingResponse,
)

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def user_credits_consumption(self) -> UserCreditsConsumptionResource:
        return UserCreditsConsumptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def user_credits_consumption(self) -> AsyncUserCreditsConsumptionResource:
        return AsyncUserCreditsConsumptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def user_credits_consumption(self) -> UserCreditsConsumptionResourceWithRawResponse:
        return UserCreditsConsumptionResourceWithRawResponse(self._reports.user_credits_consumption)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def user_credits_consumption(self) -> AsyncUserCreditsConsumptionResourceWithRawResponse:
        return AsyncUserCreditsConsumptionResourceWithRawResponse(self._reports.user_credits_consumption)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def user_credits_consumption(self) -> UserCreditsConsumptionResourceWithStreamingResponse:
        return UserCreditsConsumptionResourceWithStreamingResponse(self._reports.user_credits_consumption)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def user_credits_consumption(self) -> AsyncUserCreditsConsumptionResourceWithStreamingResponse:
        return AsyncUserCreditsConsumptionResourceWithStreamingResponse(self._reports.user_credits_consumption)
