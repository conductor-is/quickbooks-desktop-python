# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types import QbdHealthCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQbd:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_health_check(self, client: Conductor) -> None:
        qbd = client.qbd.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

    @parametrize
    def test_raw_response_health_check(self, client: Conductor) -> None:
        response = client.qbd.with_raw_response.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qbd = response.parse()
        assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

    @parametrize
    def test_streaming_response_health_check(self, client: Conductor) -> None:
        with client.qbd.with_streaming_response.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qbd = response.parse()
            assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQbd:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_health_check(self, async_client: AsyncConductor) -> None:
        qbd = await async_client.qbd.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

    @parametrize
    async def test_raw_response_health_check(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.with_raw_response.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qbd = await response.parse()
        assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

    @parametrize
    async def test_streaming_response_health_check(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.with_streaming_response.health_check(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qbd = await response.parse()
            assert_matches_type(QbdHealthCheckResponse, qbd, path=["response"])

        assert cast(Any, response.is_closed) is True
