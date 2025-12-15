# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.data_views import service_account_list_params, service_account_create_params
from ...types.data_views.service_account import ServiceAccount
from ...types.data_views.service_account_credentials import ServiceAccountCredentials
from ...types.data_views.service_account_list_response import ServiceAccountListResponse

__all__ = ["ServiceAccountsResource", "AsyncServiceAccountsResource"]


class ServiceAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ServiceAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["gcp"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """Creates a service account for accessing data views.

        Only one service account per
        teamspace is allowed.

        Args:
          name: The name of the service account. Your organization's domain will automatically
              be prepended to the service account name. The name must only include letters
              (a-z, A-Z), numbers (0-9), and hyphens (-), and must be between 6 and 30
              characters long.

          type: The type of service account, currently only `gcp` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data-views/service-accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccount,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountListResponse:
        """Returns the list of service accounts for your teamspace.

        Only one service
        account per teamspace is allowed at this time.

        Args:
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
            "/data-views/service-accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
            ),
            cast_to=ServiceAccountListResponse,
        )

    def delete(
        self,
        service_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a service account and all associated data views.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/data-views/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def credentials(
        self,
        service_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountCredentials:
        """
        Retrieves the credentials (private key) for a service account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        return self._get(
            f"/data-views/service-accounts/{service_account_id}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccountCredentials,
        )


class AsyncServiceAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncServiceAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["gcp"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccount:
        """Creates a service account for accessing data views.

        Only one service account per
        teamspace is allowed.

        Args:
          name: The name of the service account. Your organization's domain will automatically
              be prepended to the service account name. The name must only include letters
              (a-z, A-Z), numbers (0-9), and hyphens (-), and must be between 6 and 30
              characters long.

          type: The type of service account, currently only `gcp` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data-views/service-accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                service_account_create_params.ServiceAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccount,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountListResponse:
        """Returns the list of service accounts for your teamspace.

        Only one service
        account per teamspace is allowed at this time.

        Args:
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
            "/data-views/service-accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    service_account_list_params.ServiceAccountListParams,
                ),
            ),
            cast_to=ServiceAccountListResponse,
        )

    async def delete(
        self,
        service_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a service account and all associated data views.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/data-views/service-accounts/{service_account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def credentials(
        self,
        service_account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServiceAccountCredentials:
        """
        Retrieves the credentials (private key) for a service account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_account_id:
            raise ValueError(f"Expected a non-empty value for `service_account_id` but received {service_account_id!r}")
        return await self._get(
            f"/data-views/service-accounts/{service_account_id}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceAccountCredentials,
        )


class ServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_raw_response_wrapper(
            service_accounts.create,
        )
        self.list = to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            service_accounts.delete,
        )
        self.credentials = to_raw_response_wrapper(
            service_accounts.credentials,
        )


class AsyncServiceAccountsResourceWithRawResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_raw_response_wrapper(
            service_accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_accounts.delete,
        )
        self.credentials = async_to_raw_response_wrapper(
            service_accounts.credentials,
        )


class ServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: ServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_accounts.delete,
        )
        self.credentials = to_streamed_response_wrapper(
            service_accounts.credentials,
        )


class AsyncServiceAccountsResourceWithStreamingResponse:
    def __init__(self, service_accounts: AsyncServiceAccountsResource) -> None:
        self._service_accounts = service_accounts

        self.create = async_to_streamed_response_wrapper(
            service_accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            service_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_accounts.delete,
        )
        self.credentials = async_to_streamed_response_wrapper(
            service_accounts.credentials,
        )
