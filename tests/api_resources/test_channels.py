# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    Channel,
    ChannelMember,
    ChannelThread,
    ChannelMessage,
    ChannelAddMembersResponse,
)
from datagrid_ai.pagination import SyncCursorIDPage, AsyncCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        channel = client.channels.create(
            name="x",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.create(
            name="x",
            description="description",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        channel = client.channels.retrieve(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.retrieve(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.retrieve(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Datagrid) -> None:
        channel = client.channels.update(
            channel_id="channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.update(
            channel_id="channel_id",
            description="description",
            name="x",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.update(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.update(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.update(
                channel_id="",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        channel = client.channels.list()
        assert_matches_type(SyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.list(
            after="after",
            before="before",
            limit=1,
            q="q",
            type="channel",
        )
        assert_matches_type(SyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncCursorIDPage[Channel], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_members(self, client: Datagrid) -> None:
        channel = client.channels.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        )
        assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

    @parametrize
    def test_raw_response_add_members(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

    @parametrize
    def test_streaming_response_add_members(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_members(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.add_members(
                channel_id="",
                actors=[
                    {
                        "id": "id",
                        "type": "user",
                    }
                ],
            )

    @parametrize
    def test_method_add_reaction(self, client: Datagrid) -> None:
        channel = client.channels.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_raw_response_add_reaction(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_streaming_response_add_reaction(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_reaction(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.add_reaction(
                message_id="message_id",
                channel_id="",
                reaction="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channels.with_raw_response.add_reaction(
                message_id="",
                channel_id="channel_id",
                reaction="x",
            )

    @parametrize
    def test_method_create_message(self, client: Datagrid) -> None:
        channel = client.channels.create_message(
            channel_id="channel_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_method_create_message_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.create_message(
            channel_id="channel_id",
            content="content",
            file_ids=["string"],
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_raw_response_create_message(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.create_message(
            channel_id="channel_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_streaming_response_create_message(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.create_message(
            channel_id="channel_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_message(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.create_message(
                channel_id="",
                content="content",
            )

    @parametrize
    def test_method_create_thread(self, client: Datagrid) -> None:
        channel = client.channels.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        )
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    def test_raw_response_create_thread(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    def test_streaming_response_create_thread(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelThread, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_thread(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.create_thread(
                message_id="message_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channels.with_raw_response.create_thread(
                message_id="",
                channel_id="channel_id",
            )

    @parametrize
    def test_method_create_thread_message(self, client: Datagrid) -> None:
        channel = client.channels.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_method_create_thread_message_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
            file_ids=["string"],
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_raw_response_create_thread_message(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_streaming_response_create_thread_message(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_thread_message(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.create_thread_message(
                thread_id="thread_id",
                channel_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.channels.with_raw_response.create_thread_message(
                thread_id="",
                channel_id="channel_id",
                content="content",
            )

    @parametrize
    def test_method_list_members(self, client: Datagrid) -> None:
        channel = client.channels.list_members(
            channel_id="channel_id",
        )
        assert_matches_type(SyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    def test_method_list_members_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.list_members(
            channel_id="channel_id",
            actor_type="user",
            after="after",
            before="before",
            limit=1,
            q="q",
        )
        assert_matches_type(SyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    def test_raw_response_list_members(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.list_members(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    def test_streaming_response_list_members(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.list_members(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncCursorIDPage[ChannelMember], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_members(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.list_members(
                channel_id="",
            )

    @parametrize
    def test_method_list_messages(self, client: Datagrid) -> None:
        channel = client.channels.list_messages(
            channel_id="channel_id",
        )
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_method_list_messages_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.list_messages(
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_raw_response_list_messages(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.list_messages(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_streaming_response_list_messages(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.list_messages(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_messages(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.list_messages(
                channel_id="",
            )

    @parametrize
    def test_method_list_thread_messages(self, client: Datagrid) -> None:
        channel = client.channels.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        )
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_method_list_thread_messages_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_raw_response_list_thread_messages(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    def test_streaming_response_list_thread_messages(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncCursorIDPage[ChannelMessage], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_thread_messages(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.list_thread_messages(
                thread_id="thread_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.channels.with_raw_response.list_thread_messages(
                thread_id="",
                channel_id="channel_id",
            )

    @parametrize
    def test_method_list_threads(self, client: Datagrid) -> None:
        channel = client.channels.list_threads(
            channel_id="channel_id",
        )
        assert_matches_type(SyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    def test_method_list_threads_with_all_params(self, client: Datagrid) -> None:
        channel = client.channels.list_threads(
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    def test_raw_response_list_threads(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.list_threads(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(SyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    def test_streaming_response_list_threads(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.list_threads(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(SyncCursorIDPage[ChannelThread], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_threads(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.list_threads(
                channel_id="",
            )

    @parametrize
    def test_method_remove_member(self, client: Datagrid) -> None:
        channel = client.channels.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        )
        assert channel is None

    @parametrize
    def test_raw_response_remove_member(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert channel is None

    @parametrize
    def test_streaming_response_remove_member(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_member(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.remove_member(
                member_id="member_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.channels.with_raw_response.remove_member(
                member_id="",
                channel_id="channel_id",
            )

    @parametrize
    def test_method_remove_reaction(self, client: Datagrid) -> None:
        channel = client.channels.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_raw_response_remove_reaction(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    def test_streaming_response_remove_reaction(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_reaction(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.remove_reaction(
                reaction="x",
                channel_id="",
                message_id="message_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channels.with_raw_response.remove_reaction(
                reaction="x",
                channel_id="channel_id",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reaction` but received ''"):
            client.channels.with_raw_response.remove_reaction(
                reaction="",
                channel_id="channel_id",
                message_id="message_id",
            )

    @parametrize
    def test_method_retrieve_thread(self, client: Datagrid) -> None:
        channel = client.channels.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        )
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    def test_raw_response_retrieve_thread(self, client: Datagrid) -> None:
        response = client.channels.with_raw_response.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_thread(self, client: Datagrid) -> None:
        with client.channels.with_streaming_response.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelThread, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_thread(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.retrieve_thread(
                thread_id="thread_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.channels.with_raw_response.retrieve_thread(
                thread_id="",
                channel_id="channel_id",
            )


class TestAsyncChannels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create(
            name="x",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create(
            name="x",
            description="description",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.retrieve(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.retrieve(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.retrieve(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.update(
            channel_id="channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.update(
            channel_id="channel_id",
            description="description",
            name="x",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.update(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.update(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.update(
                channel_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list()
        assert_matches_type(AsyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list(
            after="after",
            before="before",
            limit=1,
            q="q",
            type="channel",
        )
        assert_matches_type(AsyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncCursorIDPage[Channel], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncCursorIDPage[Channel], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_members(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        )
        assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

    @parametrize
    async def test_raw_response_add_members(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

    @parametrize
    async def test_streaming_response_add_members(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.add_members(
            channel_id="channel_id",
            actors=[
                {
                    "id": "id",
                    "type": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelAddMembersResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_members(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.add_members(
                channel_id="",
                actors=[
                    {
                        "id": "id",
                        "type": "user",
                    }
                ],
            )

    @parametrize
    async def test_method_add_reaction(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_raw_response_add_reaction(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_streaming_response_add_reaction(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.add_reaction(
            message_id="message_id",
            channel_id="channel_id",
            reaction="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_reaction(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.add_reaction(
                message_id="message_id",
                channel_id="",
                reaction="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channels.with_raw_response.add_reaction(
                message_id="",
                channel_id="channel_id",
                reaction="x",
            )

    @parametrize
    async def test_method_create_message(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create_message(
            channel_id="channel_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_method_create_message_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create_message(
            channel_id="channel_id",
            content="content",
            file_ids=["string"],
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_raw_response_create_message(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.create_message(
            channel_id="channel_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_streaming_response_create_message(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.create_message(
            channel_id="channel_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_message(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.create_message(
                channel_id="",
                content="content",
            )

    @parametrize
    async def test_method_create_thread(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        )
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    async def test_raw_response_create_thread(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    async def test_streaming_response_create_thread(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.create_thread(
            message_id="message_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelThread, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_thread(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.create_thread(
                message_id="message_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channels.with_raw_response.create_thread(
                message_id="",
                channel_id="channel_id",
            )

    @parametrize
    async def test_method_create_thread_message(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_method_create_thread_message_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
            file_ids=["string"],
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_raw_response_create_thread_message(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_streaming_response_create_thread_message(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.create_thread_message(
            thread_id="thread_id",
            channel_id="channel_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_thread_message(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.create_thread_message(
                thread_id="thread_id",
                channel_id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.channels.with_raw_response.create_thread_message(
                thread_id="",
                channel_id="channel_id",
                content="content",
            )

    @parametrize
    async def test_method_list_members(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_members(
            channel_id="channel_id",
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_members(
            channel_id="channel_id",
            actor_type="user",
            after="after",
            before="before",
            limit=1,
            q="q",
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.list_members(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncCursorIDPage[ChannelMember], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.list_members(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncCursorIDPage[ChannelMember], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.list_members(
                channel_id="",
            )

    @parametrize
    async def test_method_list_messages(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_messages(
            channel_id="channel_id",
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_messages(
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.list_messages(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.list_messages(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.list_messages(
                channel_id="",
            )

    @parametrize
    async def test_method_list_thread_messages(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_method_list_thread_messages_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_raw_response_list_thread_messages(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list_thread_messages(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.list_thread_messages(
            thread_id="thread_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncCursorIDPage[ChannelMessage], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_thread_messages(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.list_thread_messages(
                thread_id="thread_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.channels.with_raw_response.list_thread_messages(
                thread_id="",
                channel_id="channel_id",
            )

    @parametrize
    async def test_method_list_threads(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_threads(
            channel_id="channel_id",
        )
        assert_matches_type(AsyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    async def test_method_list_threads_with_all_params(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.list_threads(
            channel_id="channel_id",
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    async def test_raw_response_list_threads(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.list_threads(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(AsyncCursorIDPage[ChannelThread], channel, path=["response"])

    @parametrize
    async def test_streaming_response_list_threads(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.list_threads(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(AsyncCursorIDPage[ChannelThread], channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_threads(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.list_threads(
                channel_id="",
            )

    @parametrize
    async def test_method_remove_member(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        )
        assert channel is None

    @parametrize
    async def test_raw_response_remove_member(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert channel is None

    @parametrize
    async def test_streaming_response_remove_member(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.remove_member(
            member_id="member_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert channel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_member(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.remove_member(
                member_id="member_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.channels.with_raw_response.remove_member(
                member_id="",
                channel_id="channel_id",
            )

    @parametrize
    async def test_method_remove_reaction(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        )
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_raw_response_remove_reaction(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMessage, channel, path=["response"])

    @parametrize
    async def test_streaming_response_remove_reaction(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.remove_reaction(
            reaction="x",
            channel_id="channel_id",
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMessage, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_reaction(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.remove_reaction(
                reaction="x",
                channel_id="",
                message_id="message_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channels.with_raw_response.remove_reaction(
                reaction="x",
                channel_id="channel_id",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reaction` but received ''"):
            await async_client.channels.with_raw_response.remove_reaction(
                reaction="",
                channel_id="channel_id",
                message_id="message_id",
            )

    @parametrize
    async def test_method_retrieve_thread(self, async_client: AsyncDatagrid) -> None:
        channel = await async_client.channels.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        )
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_thread(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.channels.with_raw_response.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelThread, channel, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_thread(self, async_client: AsyncDatagrid) -> None:
        async with async_client.channels.with_streaming_response.retrieve_thread(
            thread_id="thread_id",
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelThread, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_thread(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.retrieve_thread(
                thread_id="thread_id",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.channels.with_raw_response.retrieve_thread(
                thread_id="",
                channel_id="channel_id",
            )
