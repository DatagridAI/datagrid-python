# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping, Iterable, Optional, overload
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .lib import sse_converse
from .types import client_converse_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._constants import DEFAULT_TIMEOUT
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import DatagridError, APIStatusError
from ._base_client import (
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.converse_response import ConverseResponse

if TYPE_CHECKING:
    from .resources import (
        beta,
        files,
        tools,
        agents,
        memory,
        search,
        secrets,
        knowledge,
        connectors,
        data_views,
        connections,
        organization,
        conversations,
    )
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.secrets import SecretsResource, AsyncSecretsResource
    from .resources.beta.beta import BetaResource, AsyncBetaResource
    from .resources.knowledge import KnowledgeResource, AsyncKnowledgeResource
    from .resources.connectors import ConnectorsResource, AsyncConnectorsResource
    from .resources.connections import ConnectionsResource, AsyncConnectionsResource
    from .resources.memory.memory import MemoryResource, AsyncMemoryResource
    from .resources.data_views.data_views import DataViewsResource, AsyncDataViewsResource
    from .resources.organization.organization import OrganizationResource, AsyncOrganizationResource
    from .resources.conversations.conversations import ConversationsResource, AsyncConversationsResource

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
    # client options
    api_key: str
    teamspace: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        from .resources.knowledge import KnowledgeResource

        return KnowledgeResource(self)

    @cached_property
    def connections(self) -> ConnectionsResource:
        from .resources.connections import ConnectionsResource

        return ConnectionsResource(self)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        from .resources.connectors import ConnectorsResource

        return ConnectorsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def secrets(self) -> SecretsResource:
        from .resources.secrets import SecretsResource

        return SecretsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def memory(self) -> MemoryResource:
        from .resources.memory import MemoryResource

        return MemoryResource(self)

    @cached_property
    def organization(self) -> OrganizationResource:
        from .resources.organization import OrganizationResource

        return OrganizationResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def data_views(self) -> DataViewsResource:
        from .resources.data_views import DataViewsResource

        return DataViewsResource(self)

    @cached_property
    def beta(self) -> BetaResource:
        from .resources.beta import BetaResource

        return BetaResource(self)

    @cached_property
    def with_raw_response(self) -> DatagridWithRawResponse:
        return DatagridWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatagridWithStreamedResponse:
        return DatagridWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Optional[Literal[False]] | NotGiven = not_given,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse: ...

    @overload
    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Literal[True],
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[sse_converse.AgentStreamEvent]: ...

    @overload
    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: bool,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse | Stream[sse_converse.AgentStreamEvent]: ...

    def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = not_given,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse | Stream[sse_converse.AgentStreamEvent]:
        """
        Converse with an AI Agent

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse.

          config: Override the agent config for this converse call. This is applied as a partial
              override.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema.
              Structured output is not supported only supported by the default agent model,
              magpie-1.1 and magpie-2.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self.timeout == DEFAULT_TIMEOUT:
            timeout = 1800
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
    # client options
    api_key: str
    teamspace: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        teamspace: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        from .resources.knowledge import AsyncKnowledgeResource

        return AsyncKnowledgeResource(self)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        from .resources.connections import AsyncConnectionsResource

        return AsyncConnectionsResource(self)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        from .resources.connectors import AsyncConnectorsResource

        return AsyncConnectorsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        from .resources.secrets import AsyncSecretsResource

        return AsyncSecretsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def memory(self) -> AsyncMemoryResource:
        from .resources.memory import AsyncMemoryResource

        return AsyncMemoryResource(self)

    @cached_property
    def organization(self) -> AsyncOrganizationResource:
        from .resources.organization import AsyncOrganizationResource

        return AsyncOrganizationResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def data_views(self) -> AsyncDataViewsResource:
        from .resources.data_views import AsyncDataViewsResource

        return AsyncDataViewsResource(self)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        from .resources.beta import AsyncBetaResource

        return AsyncBetaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncDatagridWithRawResponse:
        return AsyncDatagridWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatagridWithStreamedResponse:
        return AsyncDatagridWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Literal[False] | NotGiven = not_given,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse: ...

    @overload
    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Literal[True],
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[sse_converse.AgentStreamEvent]: ...

    @overload
    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: bool,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse | AsyncStream[sse_converse.AgentStreamEvent]: ...

    async def converse(
        self,
        *,
        prompt: Union[str, Iterable[client_converse_params.PromptInputItemList]],
        agent_id: Optional[str] | NotGiven = not_given,
        config: Optional[client_converse_params.Config] | NotGiven = not_given,
        conversation_id: Optional[str] | NotGiven = not_given,
        generate_citations: Optional[bool] | NotGiven = not_given,
        secret_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = not_given,
        text: Optional[client_converse_params.Text] | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConverseResponse | AsyncStream[sse_converse.AgentStreamEvent]:
        """
        Converse with an AI Agent

        Args:
          prompt: A text prompt to send to the agent.

          agent_id: The ID of the agent that should be used for the converse.

          config: Override the agent config for this converse call. This is applied as a partial
              override.

          conversation_id: The ID of the present conversation to use. If it's not provided - a new
              conversation will be created.

          generate_citations: Determines whether the response should include citations. When enabled, the
              agent will generate citations for factual statements.

          secret_ids: Array of secret ID's to be included in the context. The secret value will be
              appended to the prompt but not stored in conversation history.

          stream: Determines the response type of the converse. Response is the Server-Sent Events
              if stream is set to true.

          text: Contains the format property used to specify the structured output schema.
              Structured output is not supported only supported by the default agent model,
              magpie-1.1 and magpie-2.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self.timeout == DEFAULT_TIMEOUT:
            timeout = 1800
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
    _client: Datagrid

    def __init__(self, client: Datagrid) -> None:
        self._client = client

        self.converse = to_raw_response_wrapper(
            client.converse,
        )

    @cached_property
    def knowledge(self) -> knowledge.KnowledgeResourceWithRawResponse:
        from .resources.knowledge import KnowledgeResourceWithRawResponse

        return KnowledgeResourceWithRawResponse(self._client.knowledge)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithRawResponse:
        from .resources.connections import ConnectionsResourceWithRawResponse

        return ConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithRawResponse:
        from .resources.connectors import ConnectorsResourceWithRawResponse

        return ConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithRawResponse:
        from .resources.secrets import SecretsResourceWithRawResponse

        return SecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def memory(self) -> memory.MemoryResourceWithRawResponse:
        from .resources.memory import MemoryResourceWithRawResponse

        return MemoryResourceWithRawResponse(self._client.memory)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithRawResponse:
        from .resources.organization import OrganizationResourceWithRawResponse

        return OrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def data_views(self) -> data_views.DataViewsResourceWithRawResponse:
        from .resources.data_views import DataViewsResourceWithRawResponse

        return DataViewsResourceWithRawResponse(self._client.data_views)

    @cached_property
    def beta(self) -> beta.BetaResourceWithRawResponse:
        from .resources.beta import BetaResourceWithRawResponse

        return BetaResourceWithRawResponse(self._client.beta)


class AsyncDatagridWithRawResponse:
    _client: AsyncDatagrid

    def __init__(self, client: AsyncDatagrid) -> None:
        self._client = client

        self.converse = async_to_raw_response_wrapper(
            client.converse,
        )

    @cached_property
    def knowledge(self) -> knowledge.AsyncKnowledgeResourceWithRawResponse:
        from .resources.knowledge import AsyncKnowledgeResourceWithRawResponse

        return AsyncKnowledgeResourceWithRawResponse(self._client.knowledge)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithRawResponse:
        from .resources.connections import AsyncConnectionsResourceWithRawResponse

        return AsyncConnectionsResourceWithRawResponse(self._client.connections)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithRawResponse:
        from .resources.connectors import AsyncConnectorsResourceWithRawResponse

        return AsyncConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithRawResponse:
        from .resources.secrets import AsyncSecretsResourceWithRawResponse

        return AsyncSecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def memory(self) -> memory.AsyncMemoryResourceWithRawResponse:
        from .resources.memory import AsyncMemoryResourceWithRawResponse

        return AsyncMemoryResourceWithRawResponse(self._client.memory)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithRawResponse:
        from .resources.organization import AsyncOrganizationResourceWithRawResponse

        return AsyncOrganizationResourceWithRawResponse(self._client.organization)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def data_views(self) -> data_views.AsyncDataViewsResourceWithRawResponse:
        from .resources.data_views import AsyncDataViewsResourceWithRawResponse

        return AsyncDataViewsResourceWithRawResponse(self._client.data_views)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithRawResponse:
        from .resources.beta import AsyncBetaResourceWithRawResponse

        return AsyncBetaResourceWithRawResponse(self._client.beta)


class DatagridWithStreamedResponse:
    _client: Datagrid

    def __init__(self, client: Datagrid) -> None:
        self._client = client

        self.converse = to_streamed_response_wrapper(
            client.converse,
        )

    @cached_property
    def knowledge(self) -> knowledge.KnowledgeResourceWithStreamingResponse:
        from .resources.knowledge import KnowledgeResourceWithStreamingResponse

        return KnowledgeResourceWithStreamingResponse(self._client.knowledge)

    @cached_property
    def connections(self) -> connections.ConnectionsResourceWithStreamingResponse:
        from .resources.connections import ConnectionsResourceWithStreamingResponse

        return ConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithStreamingResponse:
        from .resources.connectors import ConnectorsResourceWithStreamingResponse

        return ConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithStreamingResponse:
        from .resources.secrets import SecretsResourceWithStreamingResponse

        return SecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def memory(self) -> memory.MemoryResourceWithStreamingResponse:
        from .resources.memory import MemoryResourceWithStreamingResponse

        return MemoryResourceWithStreamingResponse(self._client.memory)

    @cached_property
    def organization(self) -> organization.OrganizationResourceWithStreamingResponse:
        from .resources.organization import OrganizationResourceWithStreamingResponse

        return OrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def data_views(self) -> data_views.DataViewsResourceWithStreamingResponse:
        from .resources.data_views import DataViewsResourceWithStreamingResponse

        return DataViewsResourceWithStreamingResponse(self._client.data_views)

    @cached_property
    def beta(self) -> beta.BetaResourceWithStreamingResponse:
        from .resources.beta import BetaResourceWithStreamingResponse

        return BetaResourceWithStreamingResponse(self._client.beta)


class AsyncDatagridWithStreamedResponse:
    _client: AsyncDatagrid

    def __init__(self, client: AsyncDatagrid) -> None:
        self._client = client

        self.converse = async_to_streamed_response_wrapper(
            client.converse,
        )

    @cached_property
    def knowledge(self) -> knowledge.AsyncKnowledgeResourceWithStreamingResponse:
        from .resources.knowledge import AsyncKnowledgeResourceWithStreamingResponse

        return AsyncKnowledgeResourceWithStreamingResponse(self._client.knowledge)

    @cached_property
    def connections(self) -> connections.AsyncConnectionsResourceWithStreamingResponse:
        from .resources.connections import AsyncConnectionsResourceWithStreamingResponse

        return AsyncConnectionsResourceWithStreamingResponse(self._client.connections)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithStreamingResponse:
        from .resources.connectors import AsyncConnectorsResourceWithStreamingResponse

        return AsyncConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithStreamingResponse:
        from .resources.secrets import AsyncSecretsResourceWithStreamingResponse

        return AsyncSecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def memory(self) -> memory.AsyncMemoryResourceWithStreamingResponse:
        from .resources.memory import AsyncMemoryResourceWithStreamingResponse

        return AsyncMemoryResourceWithStreamingResponse(self._client.memory)

    @cached_property
    def organization(self) -> organization.AsyncOrganizationResourceWithStreamingResponse:
        from .resources.organization import AsyncOrganizationResourceWithStreamingResponse

        return AsyncOrganizationResourceWithStreamingResponse(self._client.organization)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def data_views(self) -> data_views.AsyncDataViewsResourceWithStreamingResponse:
        from .resources.data_views import AsyncDataViewsResourceWithStreamingResponse

        return AsyncDataViewsResourceWithStreamingResponse(self._client.data_views)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithStreamingResponse:
        from .resources.beta import AsyncBetaResourceWithStreamingResponse

        return AsyncBetaResourceWithStreamingResponse(self._client.beta)


Client = Datagrid

AsyncClient = AsyncDatagrid
