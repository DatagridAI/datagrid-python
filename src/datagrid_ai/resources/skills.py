# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import skill_list_params, skill_create_params, skill_update_params, skill_generate_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import is_given, path_template, maybe_transform, async_maybe_transform
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
from ..types.skill import Skill
from .._base_client import AsyncPaginator, make_request_options
from ..types.skill_generate_response import SkillGenerateResponse
from ..types.skill_list_builtins_response import SkillListBuiltinsResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return SkillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: Literal[
            "document_analysis",
            "construction_project_management",
            "financial_analysis",
            "estimation",
            "quality_and_safety",
            "scheduling",
            "contracts_and_legal",
            "data_and_reporting",
            "research",
            "communication",
            "general_productivity",
        ],
        instructions: str,
        name: str,
        slash_key: str,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        preferred_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        required_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        scope: Optional[Literal["user", "account"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Create a skill.

        Defaults to Public (`account`) privacy with an initial
        invocation assignment to the API key's teamspace; creation and assignment are
        atomic, and the returned scope remains `account`. Pass `scope: user` to create a
        Private skill without an initial assignment. Public slash keys must not collide
        with a built-in.

        Args:
          category: Category bucket.

          instructions: The full instructions / system prompt for this skill.

          name: Display name of the skill.

          slash_key: The slash command key (e.g. `budget-check`, `3d-review`). Must use lowercase
              letters, digits, and single dashes, start and end with a letter or digit, and be
              unique within the scope.

          description: Short description. When omitted, an AI-generated description is produced from
              the instructions.

          enabled: Whether the skill is active. Defaults to `true`.

          preferred_tools: Tool identifiers preferred by this skill.

          required_tools: Tool identifiers required by this skill.

          scope: Ownership of the new skill. Defaults to `account` (company-owned). Pass `user`
              for a private skill that can later be promoted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/skills",
            body=maybe_transform(
                {
                    "category": category,
                    "instructions": instructions,
                    "name": name,
                    "slash_key": slash_key,
                    "description": description,
                    "enabled": enabled,
                    "preferred_tools": preferred_tools,
                    "required_tools": required_tools,
                    "scope": scope,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Get details of a specific skill.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def update(
        self,
        skill_id: str,
        *,
        category: Optional[
            Literal[
                "document_analysis",
                "construction_project_management",
                "financial_analysis",
                "estimation",
                "quality_and_safety",
                "scheduling",
                "contracts_and_legal",
                "data_and_reporting",
                "research",
                "communication",
                "general_productivity",
            ]
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preferred_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        required_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        slash_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Update a skill.

        Requires an API key with `ep:skills:write` whose user
        administers skills in the account. A shared (`account`-scope) skill may be
        updated by any skill administrator; a private (`user`-scope) skill only by its
        author. Built-in skills and company copies of them cannot have their content
        edited, but a skill administrator may set `enabled` on one to enable or disable
        it for the whole company. The global built-in row is never changed; the response
        carries your company's state.

        Args:
          category: Category bucket.

          description: Short description. Pass an empty string to clear it and re-enable AI generation.

          enabled: Whether the skill is active.

          instructions: The full instructions / system prompt.

          name: Display name of the skill.

          preferred_tools: Tool identifiers preferred by this skill.

          required_tools: Tool identifiers required by this skill.

          slash_key: The slash command key. Must use lowercase letters, digits, and single dashes,
              start and end with a letter or digit, and be unique within the scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._patch(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            body=maybe_transform(
                {
                    "category": category,
                    "description": description,
                    "enabled": enabled,
                    "instructions": instructions,
                    "name": name,
                    "preferred_tools": preferred_tools,
                    "required_tools": required_tools,
                    "slash_key": slash_key,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        scope: Literal["user", "account", "teamspace", "builtin"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorIDPage[Skill]:
        """List skills invocable in the authenticated teamspace.

        Returns built-ins, Public
        custom skills that are unrestricted or assigned here, and the API-key subject's
        own Private skills assigned here. Other users' Private skills and unassigned
        Private skills are excluded. Built-in skills your company removed are excluded,
        and a built-in your company disabled is returned with `enabled: false`.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          enabled: Filter by enabled status.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          scope: Return only skills of this scope. `user` returns the API-key subject's own
              Private skills assigned to the authenticated teamspace; `account` returns Public
              custom skills invocable here; `teamspace` is a deprecated legacy Public value
              that remains assignment-required until normalized by a privacy or assignment
              action; and `builtin` is the global catalogue. Omit to return everything the
              caller can invoke.

          search: Optional search string to filter skills by name or slash key. Case-insensitive
              partial match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/skills",
            page=SyncCursorIDPage[Skill],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "enabled": enabled,
                        "limit": limit,
                        "scope": scope,
                        "search": search,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            model=Skill,
        )

    def delete(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a skill.

        For a built-in skill (or a company copy of one) this removes it
        for your company only — it is excluded from listings and agents and can be
        restored with `POST /skills/builtin/{builtin_key}/override` — rather than
        deleting it. Requires an API key with `ep:skills:delete` whose user administers
        skills in the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clone(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Create a private copy of any reachable skill, owned by the key's subject.

        Clone
        is deliberately `user`-scope even when `POST /v1/skills` defaults to `account`:
        it is 'make my own copy', not another company skill. Requires `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._post(
            path_template("/skills/{skill_id}/clone", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def demote(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Convert a Public (`account`) skill or deprecated legacy `teamspace` skill to
        Private (`user`) scope. Existing teamspace assignments are preserved. The caller
        must be the skill's original author and administer skills in the account.
        Company copies of built-in skills cannot be demoted; use `/reset` instead.
        Requires `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._post(
            path_template("/skills/{skill_id}/demote", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def generate(
        self,
        *,
        file_ids: SequenceNotStr[str] | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillGenerateResponse:
        """
        Generate one or more skill drafts from a natural-language prompt and/or
        previously uploaded SOP files (`POST /v1/files`). Drafts are returned as a list
        and are **not** persisted — use `POST /v1/skills` to create each draft you want
        to keep. Requires `ep:skills:write`.

        Args:
          file_ids: IDs of previously uploaded files to use as source material (e.g. SOP documents).
              Obtain file IDs via `POST /v1/files`. At least one of `prompt` or `file_ids`
              must be non-empty.

          prompt: Natural-language description of the skill(s) to generate. At least one of
              `prompt` or `file_ids` must be non-empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 180
        return self._post(
            "/skills/generate",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "prompt": prompt,
                },
                skill_generate_params.SkillGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillGenerateResponse,
        )

    def list_builtins(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListBuiltinsResponse:
        """Return the full in-memory built-in catalogue shipped with Datagrid.

        The
        catalogue is small and not cursor-paginated (`has_more` is always `false`);
        adding pagination later would be a breaking SDK change. To disable or remove a
        built-in for your company, `PATCH` (`enabled`) or `DELETE` it by its skill id;
        restore a removed one with `POST /skills/builtin/{builtin_key}/override`.
        Requires `ep:skills:read`.
        """
        return self._get(
            "/skills/builtin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillListBuiltinsResponse,
        )

    def override_builtin(
        self,
        builtin_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Create (or restore) a company-owned copy of a built-in skill that shadows the
        global default for your organization. Idempotent: if an override already exists
        it is returned unchanged; if it was previously removed it is restored. Requires
        `ep:skills:write` (account admin).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not builtin_key:
            raise ValueError(f"Expected a non-empty value for `builtin_key` but received {builtin_key!r}")
        return self._post(
            path_template("/skills/builtin/{builtin_key}/override", builtin_key=builtin_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def promote(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Convert a Private (`user`) skill or deprecated legacy `teamspace` skill to
        Public (`account`) scope. Existing teamspace assignments are preserved. The
        caller must be the skill's author and an account admin. Requires
        `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._post(
            path_template("/skills/{skill_id}/promote", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def reset_builtin_override(
        self,
        builtin_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Reset a built-in skill to the global default for your company: clears your
        company's disabled/removed state for it and deletes any company copy of it (the
        copy's id then no longer resolves). Idempotent: no-op when there is nothing to
        reset. Requires `ep:skills:write` (account admin).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not builtin_key:
            raise ValueError(f"Expected a non-empty value for `builtin_key` but received {builtin_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/skills/builtin/{builtin_key}/reset", builtin_key=builtin_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DatagridAI/datagrid-python#with_streaming_response
        """
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: Literal[
            "document_analysis",
            "construction_project_management",
            "financial_analysis",
            "estimation",
            "quality_and_safety",
            "scheduling",
            "contracts_and_legal",
            "data_and_reporting",
            "research",
            "communication",
            "general_productivity",
        ],
        instructions: str,
        name: str,
        slash_key: str,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        preferred_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        required_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        scope: Optional[Literal["user", "account"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Create a skill.

        Defaults to Public (`account`) privacy with an initial
        invocation assignment to the API key's teamspace; creation and assignment are
        atomic, and the returned scope remains `account`. Pass `scope: user` to create a
        Private skill without an initial assignment. Public slash keys must not collide
        with a built-in.

        Args:
          category: Category bucket.

          instructions: The full instructions / system prompt for this skill.

          name: Display name of the skill.

          slash_key: The slash command key (e.g. `budget-check`, `3d-review`). Must use lowercase
              letters, digits, and single dashes, start and end with a letter or digit, and be
              unique within the scope.

          description: Short description. When omitted, an AI-generated description is produced from
              the instructions.

          enabled: Whether the skill is active. Defaults to `true`.

          preferred_tools: Tool identifiers preferred by this skill.

          required_tools: Tool identifiers required by this skill.

          scope: Ownership of the new skill. Defaults to `account` (company-owned). Pass `user`
              for a private skill that can later be promoted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/skills",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "instructions": instructions,
                    "name": name,
                    "slash_key": slash_key,
                    "description": description,
                    "enabled": enabled,
                    "preferred_tools": preferred_tools,
                    "required_tools": required_tools,
                    "scope": scope,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Get details of a specific skill.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def update(
        self,
        skill_id: str,
        *,
        category: Optional[
            Literal[
                "document_analysis",
                "construction_project_management",
                "financial_analysis",
                "estimation",
                "quality_and_safety",
                "scheduling",
                "contracts_and_legal",
                "data_and_reporting",
                "research",
                "communication",
                "general_productivity",
            ]
        ]
        | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preferred_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        required_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        slash_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Update a skill.

        Requires an API key with `ep:skills:write` whose user
        administers skills in the account. A shared (`account`-scope) skill may be
        updated by any skill administrator; a private (`user`-scope) skill only by its
        author. Built-in skills and company copies of them cannot have their content
        edited, but a skill administrator may set `enabled` on one to enable or disable
        it for the whole company. The global built-in row is never changed; the response
        carries your company's state.

        Args:
          category: Category bucket.

          description: Short description. Pass an empty string to clear it and re-enable AI generation.

          enabled: Whether the skill is active.

          instructions: The full instructions / system prompt.

          name: Display name of the skill.

          preferred_tools: Tool identifiers preferred by this skill.

          required_tools: Tool identifiers required by this skill.

          slash_key: The slash command key. Must use lowercase letters, digits, and single dashes,
              start and end with a letter or digit, and be unique within the scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._patch(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            body=await async_maybe_transform(
                {
                    "category": category,
                    "description": description,
                    "enabled": enabled,
                    "instructions": instructions,
                    "name": name,
                    "preferred_tools": preferred_tools,
                    "required_tools": required_tools,
                    "slash_key": slash_key,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        scope: Literal["user", "account", "teamspace", "builtin"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Skill, AsyncCursorIDPage[Skill]]:
        """List skills invocable in the authenticated teamspace.

        Returns built-ins, Public
        custom skills that are unrestricted or assigned here, and the API-key subject's
        own Private skills assigned here. Other users' Private skills and unassigned
        Private skills are excluded. Built-in skills your company removed are excluded,
        and a built-in your company disabled is returned with `enabled: false`.

        Args:
          after: A cursor to use in pagination. `after` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              ending with `obj_foo`, your subsequent call can include `after=obj_foo` to fetch
              the next page of the list.

          before: A cursor to use in pagination. `before` is an object ID that defines your place
              in the list. For example, if you make a list request and receive 100 objects,
              starting with `obj_bar`, your subsequent call can include `before=obj_bar` to
              fetch the previous page of the list.

          enabled: Filter by enabled status.

          limit: The limit on the number of objects to return, ranging between 1 and 100.

          scope: Return only skills of this scope. `user` returns the API-key subject's own
              Private skills assigned to the authenticated teamspace; `account` returns Public
              custom skills invocable here; `teamspace` is a deprecated legacy Public value
              that remains assignment-required until normalized by a privacy or assignment
              action; and `builtin` is the global catalogue. Omit to return everything the
              caller can invoke.

          search: Optional search string to filter skills by name or slash key. Case-insensitive
              partial match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/skills",
            page=AsyncCursorIDPage[Skill],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "enabled": enabled,
                        "limit": limit,
                        "scope": scope,
                        "search": search,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            model=Skill,
        )

    async def delete(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a skill.

        For a built-in skill (or a company copy of one) this removes it
        for your company only — it is excluded from listings and agents and can be
        restored with `POST /skills/builtin/{builtin_key}/override` — rather than
        deleting it. Requires an API key with `ep:skills:delete` whose user administers
        skills in the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clone(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """Create a private copy of any reachable skill, owned by the key's subject.

        Clone
        is deliberately `user`-scope even when `POST /v1/skills` defaults to `account`:
        it is 'make my own copy', not another company skill. Requires `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._post(
            path_template("/skills/{skill_id}/clone", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def demote(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Convert a Public (`account`) skill or deprecated legacy `teamspace` skill to
        Private (`user`) scope. Existing teamspace assignments are preserved. The caller
        must be the skill's original author and administer skills in the account.
        Company copies of built-in skills cannot be demoted; use `/reset` instead.
        Requires `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._post(
            path_template("/skills/{skill_id}/demote", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def generate(
        self,
        *,
        file_ids: SequenceNotStr[str] | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillGenerateResponse:
        """
        Generate one or more skill drafts from a natural-language prompt and/or
        previously uploaded SOP files (`POST /v1/files`). Drafts are returned as a list
        and are **not** persisted — use `POST /v1/skills` to create each draft you want
        to keep. Requires `ep:skills:write`.

        Args:
          file_ids: IDs of previously uploaded files to use as source material (e.g. SOP documents).
              Obtain file IDs via `POST /v1/files`. At least one of `prompt` or `file_ids`
              must be non-empty.

          prompt: Natural-language description of the skill(s) to generate. At least one of
              `prompt` or `file_ids` must be non-empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 180
        return await self._post(
            "/skills/generate",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "prompt": prompt,
                },
                skill_generate_params.SkillGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillGenerateResponse,
        )

    async def list_builtins(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListBuiltinsResponse:
        """Return the full in-memory built-in catalogue shipped with Datagrid.

        The
        catalogue is small and not cursor-paginated (`has_more` is always `false`);
        adding pagination later would be a breaking SDK change. To disable or remove a
        built-in for your company, `PATCH` (`enabled`) or `DELETE` it by its skill id;
        restore a removed one with `POST /skills/builtin/{builtin_key}/override`.
        Requires `ep:skills:read`.
        """
        return await self._get(
            "/skills/builtin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillListBuiltinsResponse,
        )

    async def override_builtin(
        self,
        builtin_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Create (or restore) a company-owned copy of a built-in skill that shadows the
        global default for your organization. Idempotent: if an override already exists
        it is returned unchanged; if it was previously removed it is restored. Requires
        `ep:skills:write` (account admin).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not builtin_key:
            raise ValueError(f"Expected a non-empty value for `builtin_key` but received {builtin_key!r}")
        return await self._post(
            path_template("/skills/builtin/{builtin_key}/override", builtin_key=builtin_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def promote(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Skill:
        """
        Convert a Private (`user`) skill or deprecated legacy `teamspace` skill to
        Public (`account`) scope. Existing teamspace assignments are preserved. The
        caller must be the skill's author and an account admin. Requires
        `ep:skills:write`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._post(
            path_template("/skills/{skill_id}/promote", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Skill,
        )

    async def reset_builtin_override(
        self,
        builtin_key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Reset a built-in skill to the global default for your company: clears your
        company's disabled/removed state for it and deletes any company copy of it (the
        copy's id then no longer resolves). Idempotent: no-op when there is nothing to
        reset. Requires `ep:skills:write` (account admin).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not builtin_key:
            raise ValueError(f"Expected a non-empty value for `builtin_key` but received {builtin_key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/skills/builtin/{builtin_key}/reset", builtin_key=builtin_key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skills.update,
        )
        self.list = to_raw_response_wrapper(
            skills.list,
        )
        self.delete = to_raw_response_wrapper(
            skills.delete,
        )
        self.clone = to_raw_response_wrapper(
            skills.clone,
        )
        self.demote = to_raw_response_wrapper(
            skills.demote,
        )
        self.generate = to_raw_response_wrapper(
            skills.generate,
        )
        self.list_builtins = to_raw_response_wrapper(
            skills.list_builtins,
        )
        self.override_builtin = to_raw_response_wrapper(
            skills.override_builtin,
        )
        self.promote = to_raw_response_wrapper(
            skills.promote,
        )
        self.reset_builtin_override = to_raw_response_wrapper(
            skills.reset_builtin_override,
        )


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skills.update,
        )
        self.list = async_to_raw_response_wrapper(
            skills.list,
        )
        self.delete = async_to_raw_response_wrapper(
            skills.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            skills.clone,
        )
        self.demote = async_to_raw_response_wrapper(
            skills.demote,
        )
        self.generate = async_to_raw_response_wrapper(
            skills.generate,
        )
        self.list_builtins = async_to_raw_response_wrapper(
            skills.list_builtins,
        )
        self.override_builtin = async_to_raw_response_wrapper(
            skills.override_builtin,
        )
        self.promote = async_to_raw_response_wrapper(
            skills.promote,
        )
        self.reset_builtin_override = async_to_raw_response_wrapper(
            skills.reset_builtin_override,
        )


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skills.update,
        )
        self.list = to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = to_streamed_response_wrapper(
            skills.delete,
        )
        self.clone = to_streamed_response_wrapper(
            skills.clone,
        )
        self.demote = to_streamed_response_wrapper(
            skills.demote,
        )
        self.generate = to_streamed_response_wrapper(
            skills.generate,
        )
        self.list_builtins = to_streamed_response_wrapper(
            skills.list_builtins,
        )
        self.override_builtin = to_streamed_response_wrapper(
            skills.override_builtin,
        )
        self.promote = to_streamed_response_wrapper(
            skills.promote,
        )
        self.reset_builtin_override = to_streamed_response_wrapper(
            skills.reset_builtin_override,
        )


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            skills.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            skills.clone,
        )
        self.demote = async_to_streamed_response_wrapper(
            skills.demote,
        )
        self.generate = async_to_streamed_response_wrapper(
            skills.generate,
        )
        self.list_builtins = async_to_streamed_response_wrapper(
            skills.list_builtins,
        )
        self.override_builtin = async_to_streamed_response_wrapper(
            skills.override_builtin,
        )
        self.promote = async_to_streamed_response_wrapper(
            skills.promote,
        )
        self.reset_builtin_override = async_to_streamed_response_wrapper(
            skills.reset_builtin_override,
        )
