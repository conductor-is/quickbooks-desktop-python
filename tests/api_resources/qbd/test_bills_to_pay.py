# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import BillsToPayListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillsToPay:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        bills_to_pay = client.qbd.bills_to_pay.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        bills_to_pay = client.qbd.bills_to_pay.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            due_date=parse_date("2025-02-01"),
            payables_account_id="80000001-1234567890",
        )
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.bills_to_pay.with_raw_response.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bills_to_pay = response.parse()
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.bills_to_pay.with_streaming_response.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bills_to_pay = response.parse()
            assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillsToPay:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        bills_to_pay = await async_client.qbd.bills_to_pay.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        bills_to_pay = await async_client.qbd.bills_to_pay.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            currency_ids=["80000001-1234567890"],
            due_date=parse_date("2025-02-01"),
            payables_account_id="80000001-1234567890",
        )
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bills_to_pay.with_raw_response.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bills_to_pay = await response.parse()
        assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bills_to_pay.with_streaming_response.list(
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bills_to_pay = await response.parse()
            assert_matches_type(BillsToPayListResponse, bills_to_pay, path=["response"])

        assert cast(Any, response.is_closed) is True
