# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import Company, Preferences

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompany:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_info(self, client: Conductor) -> None:
        company = client.qbd.company.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Conductor) -> None:
        response = client.qbd.company.with_raw_response.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Conductor) -> None:
        with client.qbd.company.with_streaming_response.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_preferences(self, client: Conductor) -> None:
        company = client.qbd.company.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Preferences, company, path=["response"])

    @parametrize
    def test_raw_response_preferences(self, client: Conductor) -> None:
        response = client.qbd.company.with_raw_response.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Preferences, company, path=["response"])

    @parametrize
    def test_streaming_response_preferences(self, client: Conductor) -> None:
        with client.qbd.company.with_streaming_response.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Preferences, company, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompany:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_info(self, async_client: AsyncConductor) -> None:
        company = await async_client.qbd.company.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.company.with_raw_response.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.company.with_streaming_response.info(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Company, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_preferences(self, async_client: AsyncConductor) -> None:
        company = await async_client.qbd.company.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Preferences, company, path=["response"])

    @parametrize
    async def test_raw_response_preferences(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.company.with_raw_response.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Preferences, company, path=["response"])

    @parametrize
    async def test_streaming_response_preferences(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.company.with_streaming_response.preferences(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Preferences, company, path=["response"])

        assert cast(Any, response.is_closed) is True
