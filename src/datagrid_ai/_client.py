# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Union, Mapping, Iterable, Optional, overload
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .lib import sse_converse
from .types import client_converse_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import files, search, secrets, knowledge, connectors, connections
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import DatagridError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.memory import memory
from .resources.organization import organization
from .types.converse_response import ConverseResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Datagrid",
    "AsyncDatagrid",
    "Client",
    "AsyncClient",
]


class Datagrid(SyncAPIClient):
    knowledge: knowledge.KnowledgeResource
    connections: connections.ConnectionsResource
    connectors: connectors.ConnectorsResource
    files: files.FilesResource
    secrets: secrets.SecretsResource
    search: search.SearchResource
    organization: organization.OrganizationResource
    memory: memory.MemoryResource
    with_raw_response: DatagridWithRawResponse
    with_streaming_response: DatagridWithStreamedResponse

    # client options
    api_key: str
    teamspace: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Datagrid client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DATAGRID_API_KEY`
        - `teamspace` from `DATAGRID_TEAMSPACE_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DATAGRID_API_KEY")
        if api_key is None:
            raise DatagridError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DATAGRID_API_KEY environment variable"
            )
        self.api_key = api_key

        if teamspace is None:
            teamspace = os.environ.get("DATAGRID_TEAMSPACE_ID")
        self.teamspace = teamspace

        if base_url is None:
            base_url = os.environ.get("DATAGRID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.datagrid.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.knowledge = knowledge.KnowledgeResource(self)
        self.connections = connections.ConnectionsResource(self)
        self.connectors = connectors.ConnectorsResource(self)
        self.files = files.FilesResource(self)
        self.secrets = secrets.SecretsResource(self)
        self.search = search.SearchResource(self)
        self.organization = organization.OrganizationResource(self)
        self.memory = memory.MemoryResource(self)
        self.with_raw_response = DatagridWithRawResponse(self)
        self.with_streaming_response = DatagridWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Datagrid-Teamspace": self.teamspace if self.teamspace is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            teamspace=teamspace or self.teamspace,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @overload
    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse: ...

    @overload
    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[True],
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[sse_converse.AgentStreamEvent]: ...

    @overload
    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: bool,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse | Stream[sse_converse.AgentStreamEvent]: ...

    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse | Stream[sse_converse.AgentStreamEvent]:
        """
        Converse with an AI Agent

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse. If both agent_id and
              conversation_id aren't provided - the new agent is created.

          config: The config that overrides the default config of the agent for that converse.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema.
              Structured output is currently only supported by the default agent model,
              magpie-1.1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/converse",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "agent_id": agent_id,
                    "config": config,
                    "conversation_id": conversation_id,
                    "generate_citations": generate_citations,
                    "secret_ids": secret_ids,
                    "stream": stream,
                    "text": text,
                },
                client_converse_params.ClientConverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConverseResponse,
            stream=stream or False,
            stream_cls=Stream[sse_converse.AgentStreamEvent],
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDatagrid(AsyncAPIClient):
    knowledge: knowledge.AsyncKnowledgeResource
    connections: connections.AsyncConnectionsResource
    connectors: connectors.AsyncConnectorsResource
    files: files.AsyncFilesResource
    secrets: secrets.AsyncSecretsResource
    search: search.AsyncSearchResource
    organization: organization.AsyncOrganizationResource
    memory: memory.AsyncMemoryResource
    with_raw_response: AsyncDatagridWithRawResponse
    with_streaming_response: AsyncDatagridWithStreamedResponse

    # client options
    api_key: str
    teamspace: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncDatagrid client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `DATAGRID_API_KEY`
        - `teamspace` from `DATAGRID_TEAMSPACE_ID`
        """
        if api_key is None:
            api_key = os.environ.get("DATAGRID_API_KEY")
        if api_key is None:
            raise DatagridError(
                "The api_key client option must be set either by passing api_key to the client or by setting the DATAGRID_API_KEY environment variable"
            )
        self.api_key = api_key

        if teamspace is None:
            teamspace = os.environ.get("DATAGRID_TEAMSPACE_ID")
        self.teamspace = teamspace

        if base_url is None:
            base_url = os.environ.get("DATAGRID_BASE_URL")
        if base_url is None:
            base_url = f"https://api.datagrid.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.knowledge = knowledge.AsyncKnowledgeResource(self)
        self.connections = connections.AsyncConnectionsResource(self)
        self.connectors = connectors.AsyncConnectorsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.secrets = secrets.AsyncSecretsResource(self)
        self.search = search.AsyncSearchResource(self)
        self.organization = organization.AsyncOrganizationResource(self)
        self.memory = memory.AsyncMemoryResource(self)
        self.with_raw_response = AsyncDatagridWithRawResponse(self)
        self.with_streaming_response = AsyncDatagridWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Datagrid-Teamspace": self.teamspace if self.teamspace is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            teamspace=teamspace or self.teamspace,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @overload
    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse: ...

    @overload
    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[True],
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[sse_converse.AgentStreamEvent]: ...

    @overload
    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: bool,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse | AsyncStream[sse_converse.AgentStreamEvent]: ...

    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        config: Optional[client_converse_params.Config] | NotGiven = NOT_GIVEN,
        conversation_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_citations: Optional[bool] | NotGiven = NOT_GIVEN,
        secret_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        text: Optional[client_converse_params.Text] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConverseResponse | AsyncStream[sse_converse.AgentStreamEvent]:
        """
        Converse with an AI Agent

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse. If both agent_id and
              conversation_id aren't provided - the new agent is created.

          config: The config that overrides the default config of the agent for that converse.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema.
              Structured output is currently only supported by the default agent model,
              magpie-1.1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/converse",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "agent_id": agent_id,
                    "config": config,
                    "conversation_id": conversation_id,
                    "generate_citations": generate_citations,
                    "secret_ids": secret_ids,
                    "stream": stream,
                    "text": text,
                },
                client_converse_params.ClientConverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConverseResponse,
            stream=stream or False,
            stream_cls=AsyncStream[sse_converse.AgentStreamEvent],
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DatagridWithRawResponse:
    def __init__(self, client: Datagrid) -> None:
        self.knowledge = knowledge.KnowledgeResourceWithRawResponse(client.knowledge)
        self.connections = connections.ConnectionsResourceWithRawResponse(client.connections)
        self.connectors = connectors.ConnectorsResourceWithRawResponse(client.connectors)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.secrets = secrets.SecretsResourceWithRawResponse(client.secrets)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.organization = organization.OrganizationResourceWithRawResponse(client.organization)
        self.memory = memory.MemoryResourceWithRawResponse(client.memory)

        self.converse = to_raw_response_wrapper(
            client.converse,
        )


class AsyncDatagridWithRawResponse:
    def __init__(self, client: AsyncDatagrid) -> None:
        self.knowledge = knowledge.AsyncKnowledgeResourceWithRawResponse(client.knowledge)
        self.connections = connections.AsyncConnectionsResourceWithRawResponse(client.connections)
        self.connectors = connectors.AsyncConnectorsResourceWithRawResponse(client.connectors)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.secrets = secrets.AsyncSecretsResourceWithRawResponse(client.secrets)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.organization = organization.AsyncOrganizationResourceWithRawResponse(client.organization)
        self.memory = memory.AsyncMemoryResourceWithRawResponse(client.memory)

        self.converse = async_to_raw_response_wrapper(
            client.converse,
        )


class DatagridWithStreamedResponse:
    def __init__(self, client: Datagrid) -> None:
        self.knowledge = knowledge.KnowledgeResourceWithStreamingResponse(client.knowledge)
        self.connections = connections.ConnectionsResourceWithStreamingResponse(client.connections)
        self.connectors = connectors.ConnectorsResourceWithStreamingResponse(client.connectors)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.secrets = secrets.SecretsResourceWithStreamingResponse(client.secrets)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.organization = organization.OrganizationResourceWithStreamingResponse(client.organization)
        self.memory = memory.MemoryResourceWithStreamingResponse(client.memory)

        self.converse = to_streamed_response_wrapper(
            client.converse,
        )


class AsyncDatagridWithStreamedResponse:
    def __init__(self, client: AsyncDatagrid) -> None:
        self.knowledge = knowledge.AsyncKnowledgeResourceWithStreamingResponse(client.knowledge)
        self.connections = connections.AsyncConnectionsResourceWithStreamingResponse(client.connections)
        self.connectors = connectors.AsyncConnectorsResourceWithStreamingResponse(client.connectors)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.secrets = secrets.AsyncSecretsResourceWithStreamingResponse(client.secrets)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.organization = organization.AsyncOrganizationResourceWithStreamingResponse(client.organization)
        self.memory = memory.AsyncMemoryResourceWithStreamingResponse(client.memory)

        self.converse = async_to_streamed_response_wrapper(
            client.converse,
        )


Client = Datagrid

AsyncClient = AsyncDatagrid
