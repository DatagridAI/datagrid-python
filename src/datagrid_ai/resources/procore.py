# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import procore_list_projects_params, procore_list_companies_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.procore_company_list import ProcoreCompanyList
from ..types.procore_project_list import ProcoreProjectList

__all__ = ["ProcoreResource", "AsyncProcoreResource"]


class ProcoreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProcoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return ProcoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProcoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return ProcoreResourceWithStreamingResponse(self)

    def list_companies(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcoreCompanyList:
        """
        Lists the Procore companies the authenticated user's own Procore session can
        access. Procore authorizes the call with the user's token, so the result matches
        what the user can see in Procore. Pages with `page` / `per_page`, mirroring
        Procore's own paging.

        Args:
          page: 1-based page number. Values below 1 are treated as 1.

          per_page: Items per page. Values above 100 are clamped to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/procore/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    procore_list_companies_params.ProcoreListCompaniesParams,
                ),
            ),
            cast_to=ProcoreCompanyList,
        )

    def list_projects(
        self,
        company_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcoreProjectList:
        """
        Lists the Procore projects the authenticated user's own Procore session can
        access in one company, including inactive projects. Pages with `page` /
        `per_page`, passed through to Procore.

        Args:
          page: 1-based page number. Values below 1 are treated as 1.

          per_page: Items per page. Values above 100 are clamped to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            path_template("/procore/companies/{company_id}/projects", company_id=company_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    procore_list_projects_params.ProcoreListProjectsParams,
                ),
            ),
            cast_to=ProcoreProjectList,
        )


class AsyncProcoreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProcoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProcoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProcoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncProcoreResourceWithStreamingResponse(self)

    async def list_companies(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcoreCompanyList:
        """
        Lists the Procore companies the authenticated user's own Procore session can
        access. Procore authorizes the call with the user's token, so the result matches
        what the user can see in Procore. Pages with `page` / `per_page`, mirroring
        Procore's own paging.

        Args:
          page: 1-based page number. Values below 1 are treated as 1.

          per_page: Items per page. Values above 100 are clamped to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/procore/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    procore_list_companies_params.ProcoreListCompaniesParams,
                ),
            ),
            cast_to=ProcoreCompanyList,
        )

    async def list_projects(
        self,
        company_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProcoreProjectList:
        """
        Lists the Procore projects the authenticated user's own Procore session can
        access in one company, including inactive projects. Pages with `page` /
        `per_page`, passed through to Procore.

        Args:
          page: 1-based page number. Values below 1 are treated as 1.

          per_page: Items per page. Values above 100 are clamped to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            path_template("/procore/companies/{company_id}/projects", company_id=company_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    procore_list_projects_params.ProcoreListProjectsParams,
                ),
            ),
            cast_to=ProcoreProjectList,
        )


class ProcoreResourceWithRawResponse:
    def __init__(self, procore: ProcoreResource) -> None:
        self._procore = procore

        self.list_companies = to_raw_response_wrapper(
            procore.list_companies,
        )
        self.list_projects = to_raw_response_wrapper(
            procore.list_projects,
        )


class AsyncProcoreResourceWithRawResponse:
    def __init__(self, procore: AsyncProcoreResource) -> None:
        self._procore = procore

        self.list_companies = async_to_raw_response_wrapper(
            procore.list_companies,
        )
        self.list_projects = async_to_raw_response_wrapper(
            procore.list_projects,
        )


class ProcoreResourceWithStreamingResponse:
    def __init__(self, procore: ProcoreResource) -> None:
        self._procore = procore

        self.list_companies = to_streamed_response_wrapper(
            procore.list_companies,
        )
        self.list_projects = to_streamed_response_wrapper(
            procore.list_projects,
        )


class AsyncProcoreResourceWithStreamingResponse:
    def __init__(self, procore: AsyncProcoreResource) -> None:
        self._procore = procore

        self.list_companies = async_to_streamed_response_wrapper(
            procore.list_companies,
        )
        self.list_projects = async_to_streamed_response_wrapper(
            procore.list_projects,
        )
