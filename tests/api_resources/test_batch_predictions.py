# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from datagrid_ai import Datagrid, AsyncDatagrid
from tests.utils import assert_matches_type
from datagrid_ai.types import (
    BatchPrediction,
    BatchPredictionResultLine,
)
from datagrid_ai.pagination import SyncAfterCursorPage, AsyncAfterCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatchPredictions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                    "page": 1,
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                    "page": 1,
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
            completion_window="24h",
            metadata={"project": "alpha"},
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Datagrid) -> None:
        response = client.batch_predictions.with_raw_response.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Datagrid) -> None:
        with client.batch_predictions.with_streaming_response.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.retrieve(
            "batch_prediction_id",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Datagrid) -> None:
        response = client.batch_predictions.with_raw_response.retrieve(
            "batch_prediction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Datagrid) -> None:
        with client.batch_predictions.with_streaming_response.retrieve(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            client.batch_predictions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.list()
        assert_matches_type(SyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.list(
            after="after",
            limit=1,
            status="validating",
        )
        assert_matches_type(SyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Datagrid) -> None:
        response = client.batch_predictions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = response.parse()
        assert_matches_type(SyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Datagrid) -> None:
        with client.batch_predictions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = response.parse()
            assert_matches_type(SyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Datagrid) -> None:
        batch_prediction = client.batch_predictions.cancel(
            "batch_prediction_id",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Datagrid) -> None:
        response = client.batch_predictions.with_raw_response.cancel(
            "batch_prediction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Datagrid) -> None:
        with client.batch_predictions.with_streaming_response.cancel(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            client.batch_predictions.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_retrieve_results(self, client: Datagrid) -> None:
        batch_prediction_stream = client.batch_predictions.retrieve_results(
            "batch_prediction_id",
        )
        for item in batch_prediction_stream:
            assert_matches_type(BatchPredictionResultLine, item, path=["response"])

    @parametrize
    def test_raw_response_retrieve_results(self, client: Datagrid) -> None:
        response = client.batch_predictions.with_raw_response.retrieve_results(
            "batch_prediction_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        for item in stream:
            assert_matches_type(BatchPredictionResultLine, item, path=["line"])

    @parametrize
    def test_streaming_response_retrieve_results(self, client: Datagrid) -> None:
        with client.batch_predictions.with_streaming_response.retrieve_results(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            for item in stream:
                assert_matches_type(BatchPredictionResultLine, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_results(self, client: Datagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            client.batch_predictions.with_raw_response.retrieve_results(
                "",
            )


class TestAsyncBatchPredictions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                    "page": 1,
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                    "page": 1,
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
            completion_window="24h",
            metadata={"project": "alpha"},
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.batch_predictions.with_raw_response.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = await response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDatagrid) -> None:
        async with async_client.batch_predictions.with_streaming_response.create(
            items=[
                {
                    "custom_id": "drawing_001",
                    "file_id": "file_abc123",
                },
                {
                    "custom_id": "drawing_002",
                    "file_id": "file_def456",
                },
            ],
            model="gemini-2.5-flash",
            output_schema={
                "type": "bar",
                "additionalProperties": "bar",
                "properties": "bar",
                "required": "bar",
            },
            prompt="Extract the project name, sheet title, and revision from this drawing.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = await response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.retrieve(
            "batch_prediction_id",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.batch_predictions.with_raw_response.retrieve(
            "batch_prediction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = await response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDatagrid) -> None:
        async with async_client.batch_predictions.with_streaming_response.retrieve(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = await response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            await async_client.batch_predictions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.list()
        assert_matches_type(AsyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.list(
            after="after",
            limit=1,
            status="validating",
        )
        assert_matches_type(AsyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.batch_predictions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = await response.parse()
        assert_matches_type(AsyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDatagrid) -> None:
        async with async_client.batch_predictions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = await response.parse()
            assert_matches_type(AsyncAfterCursorPage[BatchPrediction], batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncDatagrid) -> None:
        batch_prediction = await async_client.batch_predictions.cancel(
            "batch_prediction_id",
        )
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.batch_predictions.with_raw_response.cancel(
            "batch_prediction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_prediction = await response.parse()
        assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDatagrid) -> None:
        async with async_client.batch_predictions.with_streaming_response.cancel(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_prediction = await response.parse()
            assert_matches_type(BatchPrediction, batch_prediction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            await async_client.batch_predictions.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_retrieve_results(self, async_client: AsyncDatagrid) -> None:
        batch_prediction_stream = await async_client.batch_predictions.retrieve_results(
            "batch_prediction_id",
        )
        async for item in batch_prediction_stream:
            assert_matches_type(BatchPredictionResultLine, item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_results(self, async_client: AsyncDatagrid) -> None:
        response = await async_client.batch_predictions.with_raw_response.retrieve_results(
            "batch_prediction_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        async for item in stream:
            assert_matches_type(BatchPredictionResultLine, item, path=["line"])

    @parametrize
    async def test_streaming_response_retrieve_results(self, async_client: AsyncDatagrid) -> None:
        async with async_client.batch_predictions.with_streaming_response.retrieve_results(
            "batch_prediction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            async for item in stream:
                assert_matches_type(BatchPredictionResultLine, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_results(self, async_client: AsyncDatagrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_prediction_id` but received ''"):
            await async_client.batch_predictions.with_raw_response.retrieve_results(
                "",
            )
