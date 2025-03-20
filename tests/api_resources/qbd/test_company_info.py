# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import CompanyInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanyInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        company_info = client.qbd.company_info.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CompanyInfo, company_info, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.company_info.with_raw_response.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_info = response.parse()
        assert_matches_type(CompanyInfo, company_info, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.company_info.with_streaming_response.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_info = response.parse()
            assert_matches_type(CompanyInfo, company_info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanyInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        company_info = await async_client.qbd.company_info.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CompanyInfo, company_info, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.company_info.with_raw_response.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_info = await response.parse()
        assert_matches_type(CompanyInfo, company_info, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.company_info.with_streaming_response.retrieve(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_info = await response.parse()
            assert_matches_type(CompanyInfo, company_info, path=["response"])

        assert cast(Any, response.is_closed) is True
