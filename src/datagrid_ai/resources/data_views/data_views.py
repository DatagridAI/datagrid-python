# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import data_view_list_params, data_view_create_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .service_accounts import (
    ServiceAccountsResource,
    AsyncServiceAccountsResource,
    ServiceAccountsResourceWithRawResponse,
    AsyncServiceAccountsResourceWithRawResponse,
    ServiceAccountsResourceWithStreamingResponse,
    AsyncServiceAccountsResourceWithStreamingResponse,
)
from ...types.data_view import DataView
from ...types.data_view_list_response import DataViewListResponse

__all__ = ["DataViewsResource", "AsyncDataViewsResource"]


class DataViewsResource(SyncAPIResource):
    @cached_property
    def service_accounts(self) -> ServiceAccountsResource:
        return ServiceAccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return DataViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return DataViewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        knowledge_id: str,
        name: str,
        service_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataView:
        """
        Creates a new data view for a knowledge source, providing controlled access
        through a service account.

        Args:
          knowledge_id: The id of the knowledge to create a data view for.

          name: The name of the data view.

          service_account_id: The id of the service account that will access this data view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data-views",
            body=maybe_transform(
                {
                    "knowledge_id": knowledge_id,
                    "name": name,
                    "service_account_id": service_account_id,
                },
                data_view_create_params.DataViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataView,
        )

    def list(
        self,
        *,
        service_account_id: str,
        knowledge_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataViewListResponse:
        """
        Returns the list of data views for a service account.

        Args:
          service_account_id: The id of the service account to list data views for.

          knowledge_id: The id of the knowledge to list data views for.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          offset: A cursor to use in pagination. `offset` is an integer that defines your place in
              the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `offset=100` to fetch
              the next page of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "service_account_id": service_account_id,
                        "knowledge_id": knowledge_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    data_view_list_params.DataViewListParams,
                ),
            ),
            cast_to=DataViewListResponse,
        )

    def delete(
        self,
        data_view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a data view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_view_id:
            raise ValueError(f"Expected a non-empty value for `data_view_id` but received {data_view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/data-views/{data_view_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDataViewsResource(AsyncAPIResource):
    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResource:
        return AsyncServiceAccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncDataViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        knowledge_id: str,
        name: str,
        service_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataView:
        """
        Creates a new data view for a knowledge source, providing controlled access
        through a service account.

        Args:
          knowledge_id: The id of the knowledge to create a data view for.

          name: The name of the data view.

          service_account_id: The id of the service account that will access this data view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data-views",
            body=await async_maybe_transform(
                {
                    "knowledge_id": knowledge_id,
                    "name": name,
                    "service_account_id": service_account_id,
                },
                data_view_create_params.DataViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataView,
        )

    async def list(
        self,
        *,
        service_account_id: str,
        knowledge_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataViewListResponse:
        """
        Returns the list of data views for a service account.

        Args:
          service_account_id: The id of the service account to list data views for.

          knowledge_id: The id of the knowledge to list data views for.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          offset: A cursor to use in pagination. `offset` is an integer that defines your place in
              the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `offset=100` to fetch
              the next page of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "service_account_id": service_account_id,
                        "knowledge_id": knowledge_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    data_view_list_params.DataViewListParams,
                ),
            ),
            cast_to=DataViewListResponse,
        )

    async def delete(
        self,
        data_view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a data view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_view_id:
            raise ValueError(f"Expected a non-empty value for `data_view_id` but received {data_view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/data-views/{data_view_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DataViewsResourceWithRawResponse:
    def __init__(self, data_views: DataViewsResource) -> None:
        self._data_views = data_views

        self.create = to_raw_response_wrapper(
            data_views.create,
        )
        self.list = to_raw_response_wrapper(
            data_views.list,
        )
        self.delete = to_raw_response_wrapper(
            data_views.delete,
        )

    @cached_property
    def service_accounts(self) -> ServiceAccountsResourceWithRawResponse:
        return ServiceAccountsResourceWithRawResponse(self._data_views.service_accounts)


class AsyncDataViewsResourceWithRawResponse:
    def __init__(self, data_views: AsyncDataViewsResource) -> None:
        self._data_views = data_views

        self.create = async_to_raw_response_wrapper(
            data_views.create,
        )
        self.list = async_to_raw_response_wrapper(
            data_views.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_views.delete,
        )

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResourceWithRawResponse:
        return AsyncServiceAccountsResourceWithRawResponse(self._data_views.service_accounts)


class DataViewsResourceWithStreamingResponse:
    def __init__(self, data_views: DataViewsResource) -> None:
        self._data_views = data_views

        self.create = to_streamed_response_wrapper(
            data_views.create,
        )
        self.list = to_streamed_response_wrapper(
            data_views.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_views.delete,
        )

    @cached_property
    def service_accounts(self) -> ServiceAccountsResourceWithStreamingResponse:
        return ServiceAccountsResourceWithStreamingResponse(self._data_views.service_accounts)


class AsyncDataViewsResourceWithStreamingResponse:
    def __init__(self, data_views: AsyncDataViewsResource) -> None:
        self._data_views = data_views

        self.create = async_to_streamed_response_wrapper(
            data_views.create,
        )
        self.list = async_to_streamed_response_wrapper(
            data_views.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_views.delete,
        )

    @cached_property
    def service_accounts(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        return AsyncServiceAccountsResourceWithStreamingResponse(self._data_views.service_accounts)
