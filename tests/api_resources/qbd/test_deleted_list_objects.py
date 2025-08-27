# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import DeletedListObjectListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeletedListObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        deleted_list_object = client.qbd.deleted_list_objects.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        deleted_list_object = client.qbd.deleted_list_objects.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
            deleted_after="2025-01-01T12:34:56+00:00",
            deleted_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.deleted_list_objects.with_raw_response.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_list_object = response.parse()
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.deleted_list_objects.with_streaming_response.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_list_object = response.parse()
            assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeletedListObjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        deleted_list_object = await async_client.qbd.deleted_list_objects.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        deleted_list_object = await async_client.qbd.deleted_list_objects.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
            deleted_after="2025-01-01T12:34:56+00:00",
            deleted_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.deleted_list_objects.with_raw_response.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted_list_object = await response.parse()
        assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.deleted_list_objects.with_streaming_response.list(
            object_types=["customer"],
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted_list_object = await response.parse()
            assert_matches_type(DeletedListObjectListResponse, deleted_list_object, path=["response"])

        assert cast(Any, response.is_closed) is True
