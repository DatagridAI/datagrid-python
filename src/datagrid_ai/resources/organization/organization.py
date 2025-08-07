# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .teamspaces import (
    TeamspacesResource,
    AsyncTeamspacesResource,
    TeamspacesResourceWithRawResponse,
    AsyncTeamspacesResourceWithRawResponse,
    TeamspacesResourceWithStreamingResponse,
    AsyncTeamspacesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def teamspaces(self) -> TeamspacesResource:
        return TeamspacesResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return OrganizationResourceWithStreamingResponse(self)


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def teamspaces(self) -> AsyncTeamspacesResource:
        return AsyncTeamspacesResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncOrganizationResourceWithStreamingResponse(self)


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def teamspaces(self) -> TeamspacesResourceWithRawResponse:
        return TeamspacesResourceWithRawResponse(self._organization.teamspaces)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._organization.credits)


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def teamspaces(self) -> AsyncTeamspacesResourceWithRawResponse:
        return AsyncTeamspacesResourceWithRawResponse(self._organization.teamspaces)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._organization.credits)


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def teamspaces(self) -> TeamspacesResourceWithStreamingResponse:
        return TeamspacesResourceWithStreamingResponse(self._organization.teamspaces)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._organization.credits)


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def teamspaces(self) -> AsyncTeamspacesResourceWithStreamingResponse:
        return AsyncTeamspacesResourceWithStreamingResponse(self._organization.teamspaces)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._organization.credits)
