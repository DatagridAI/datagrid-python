# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..types import knowledge_list_params, knowledge_create_params, knowledge_update_params, knowledge_connect_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import is_given, extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._constants import DEFAULT_TIMEOUT
from ..pagination import SyncCursorIDPage, AsyncCursorIDPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.knowledge import Knowledge
from ..types.redirect_url_response import RedirectURLResponse

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Create knowledge which will be learned and leveraged by agents.

        Args:
          files: The files to be uploaded and learned. Supported media types are `pdf`, `json`,
              `csv`, `text`, `png`, `jpeg`, `excel`, `google sheets`, `docx`, `pptx`.

          name: The name of the knowledge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/knowledge",
            body=maybe_transform(body, knowledge_create_params.KnowledgeCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def retrieve(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Retrieves a knowledge by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return self._get(
            f"/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def update(
        self,
        knowledge_id: str,
        *,
        files: Optional[SequenceNotStr[FileTypes]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Update a knowledge's attributes.

        Args:
          files: The files to replace existing knowledge. When provided, all existing data will
              be removed from the knowledge and replaced with these files. Supported media
              types are `pdf`, `json`, `csv`, `text`, `png`, `jpeg`, `excel`, `google sheets`,
              `docx`, `pptx`.

          name: The new name for the `knowledge`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            f"/knowledge/{knowledge_id}",
            body=maybe_transform(body, knowledge_update_params.KnowledgeUpdateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def list(
        self,
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
    ) -> SyncCursorIDPage[Knowledge]:
        """Returns the list of knowledge.

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
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
        return self._get_api_list(
            "/knowledge",
            page=SyncCursorIDPage[Knowledge],
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
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            model=Knowledge,
        )

    def delete(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete knowledge.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def connect(
        self,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedirectURLResponse:
        """
        Create knowledge from connection which will be learned and leveraged by agents.

        Args:
          connection_id: The id of the connection to be used to create the knowledge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/knowledge/connect",
            body=maybe_transform({"connection_id": connection_id}, knowledge_connect_params.KnowledgeConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedirectURLResponse,
        )

    def reindex(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Manually trigger a full re-indexing of the knowledge.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/knowledge/{knowledge_id}/reindex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Create knowledge which will be learned and leveraged by agents.

        Args:
          files: The files to be uploaded and learned. Supported media types are `pdf`, `json`,
              `csv`, `text`, `png`, `jpeg`, `excel`, `google sheets`, `docx`, `pptx`.

          name: The name of the knowledge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/knowledge",
            body=await async_maybe_transform(body, knowledge_create_params.KnowledgeCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    async def retrieve(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Retrieves a knowledge by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        return await self._get(
            f"/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    async def update(
        self,
        knowledge_id: str,
        *,
        files: Optional[SequenceNotStr[FileTypes]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Knowledge:
        """
        Update a knowledge's attributes.

        Args:
          files: The files to replace existing knowledge. When provided, all existing data will
              be removed from the knowledge and replaced with these files. Supported media
              types are `pdf`, `json`, `csv`, `text`, `png`, `jpeg`, `excel`, `google sheets`,
              `docx`, `pptx`.

          name: The new name for the `knowledge`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        body = deepcopy_minimal(
            {
                "files": files,
                "name": name,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            f"/knowledge/{knowledge_id}",
            body=await async_maybe_transform(body, knowledge_update_params.KnowledgeUpdateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Knowledge,
        )

    def list(
        self,
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
    ) -> AsyncPaginator[Knowledge, AsyncCursorIDPage[Knowledge]]:
        """Returns the list of knowledge.

        Args:
          after: A cursor to use in pagination.

        `after` is an object ID that defines your place
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
        return self._get_api_list(
            "/knowledge",
            page=AsyncCursorIDPage[Knowledge],
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
                    knowledge_list_params.KnowledgeListParams,
                ),
            ),
            model=Knowledge,
        )

    async def delete(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete knowledge.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/knowledge/{knowledge_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def connect(
        self,
        *,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedirectURLResponse:
        """
        Create knowledge from connection which will be learned and leveraged by agents.

        Args:
          connection_id: The id of the connection to be used to create the knowledge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/knowledge/connect",
            body=await async_maybe_transform(
                {"connection_id": connection_id}, knowledge_connect_params.KnowledgeConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedirectURLResponse,
        )

    async def reindex(
        self,
        knowledge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Manually trigger a full re-indexing of the knowledge.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_id` but received {knowledge_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/knowledge/{knowledge_id}/reindex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge.delete,
        )
        self.connect = to_raw_response_wrapper(
            knowledge.connect,
        )
        self.reindex = to_raw_response_wrapper(
            knowledge.reindex,
        )


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_raw_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge.delete,
        )
        self.connect = async_to_raw_response_wrapper(
            knowledge.connect,
        )
        self.reindex = async_to_raw_response_wrapper(
            knowledge.reindex,
        )


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge.delete,
        )
        self.connect = to_streamed_response_wrapper(
            knowledge.connect,
        )
        self.reindex = to_streamed_response_wrapper(
            knowledge.reindex,
        )


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

        self.create = async_to_streamed_response_wrapper(
            knowledge.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            knowledge.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge.delete,
        )
        self.connect = async_to_streamed_response_wrapper(
            knowledge.connect,
        )
        self.reindex = async_to_streamed_response_wrapper(
            knowledge.reindex,
        )
