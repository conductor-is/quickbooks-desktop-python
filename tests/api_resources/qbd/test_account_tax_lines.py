# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import AccountTaxLineListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountTaxLines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        account_tax_line = client.qbd.account_tax_lines.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.account_tax_lines.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tax_line = response.parse()
        assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.account_tax_lines.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tax_line = response.parse()
            assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountTaxLines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        account_tax_line = await async_client.qbd.account_tax_lines.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.account_tax_lines.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_tax_line = await response.parse()
        assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.account_tax_lines.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_tax_line = await response.parse()
            assert_matches_type(AccountTaxLineListResponse, account_tax_line, path=["response"])

        assert cast(Any, response.is_closed) is True
