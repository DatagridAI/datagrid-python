# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.organization.reports import consumption_breakdown_list_params
from ....types.organization.reports.consumption_breakdown_list import ConsumptionBreakdownList

__all__ = ["ConsumptionBreakdownResource", "AsyncConsumptionBreakdownResource"]


class ConsumptionBreakdownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsumptionBreakdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ConsumptionBreakdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumptionBreakdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ConsumptionBreakdownResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionBreakdownList:
        """
        Return Control Tower teamspace/organization credit consumption rows for the
        authenticated organization. The date window is measured in UTC calendar days and
        must not exceed 90 days. A date-only `start_date` begins at UTC midnight and a
        date-only `end_date` covers that whole UTC day. Pagination uses opaque `after` /
        `before` cursors from `first_id` / `last_id`. The cursors encode a position in
        the result set, not a record id, so rows written between two page requests can
        shift the window. Dollar `amount` is not included.

        Args:
          end_date: Inclusive end of the report window (ISO 8601 date or date-time). A date-only
              value covers that entire UTC day; a date-time is used exactly as given.

          start_date: Inclusive start of the report window (ISO 8601 date or date-time). Date-only
              values are UTC midnight.

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
        return self._get(
            "/organization/reports/consumption-breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    consumption_breakdown_list_params.ConsumptionBreakdownListParams,
                ),
            ),
            cast_to=ConsumptionBreakdownList,
        )


class AsyncConsumptionBreakdownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsumptionBreakdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsumptionBreakdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumptionBreakdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncConsumptionBreakdownResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsumptionBreakdownList:
        """
        Return Control Tower teamspace/organization credit consumption rows for the
        authenticated organization. The date window is measured in UTC calendar days and
        must not exceed 90 days. A date-only `start_date` begins at UTC midnight and a
        date-only `end_date` covers that whole UTC day. Pagination uses opaque `after` /
        `before` cursors from `first_id` / `last_id`. The cursors encode a position in
        the result set, not a record id, so rows written between two page requests can
        shift the window. Dollar `amount` is not included.

        Args:
          end_date: Inclusive end of the report window (ISO 8601 date or date-time). A date-only
              value covers that entire UTC day; a date-time is used exactly as given.

          start_date: Inclusive start of the report window (ISO 8601 date or date-time). Date-only
              values are UTC midnight.

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
        return await self._get(
            "/organization/reports/consumption-breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    consumption_breakdown_list_params.ConsumptionBreakdownListParams,
                ),
            ),
            cast_to=ConsumptionBreakdownList,
        )


class ConsumptionBreakdownResourceWithRawResponse:
    def __init__(self, consumption_breakdown: ConsumptionBreakdownResource) -> None:
        self._consumption_breakdown = consumption_breakdown

        self.list = to_raw_response_wrapper(
            consumption_breakdown.list,
        )


class AsyncConsumptionBreakdownResourceWithRawResponse:
    def __init__(self, consumption_breakdown: AsyncConsumptionBreakdownResource) -> None:
        self._consumption_breakdown = consumption_breakdown

        self.list = async_to_raw_response_wrapper(
            consumption_breakdown.list,
        )


class ConsumptionBreakdownResourceWithStreamingResponse:
    def __init__(self, consumption_breakdown: ConsumptionBreakdownResource) -> None:
        self._consumption_breakdown = consumption_breakdown

        self.list = to_streamed_response_wrapper(
            consumption_breakdown.list,
        )


class AsyncConsumptionBreakdownResourceWithStreamingResponse:
    def __init__(self, consumption_breakdown: AsyncConsumptionBreakdownResource) -> None:
        self._consumption_breakdown = consumption_breakdown

        self.list = async_to_streamed_response_wrapper(
            consumption_breakdown.list,
        )
