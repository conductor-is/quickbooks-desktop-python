# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import PayrollWageItem
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayrollWageItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        payroll_wage_item = client.qbd.payroll_wage_items.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        payroll_wage_item = client.qbd.payroll_wage_items.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
            is_active=True,
            overtime_multiplier="1.5",
            rate="15.00",
            rate_percent="10",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.payroll_wage_items.with_raw_response.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = response.parse()
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.payroll_wage_items.with_streaming_response.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = response.parse()
            assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        payroll_wage_item = client.qbd.payroll_wage_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.payroll_wage_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = response.parse()
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.payroll_wage_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = response.parse()
            assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.payroll_wage_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        payroll_wage_item = client.qbd.payroll_wage_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        payroll_wage_item = client.qbd.payroll_wage_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Regular Pay"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.payroll_wage_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = response.parse()
        assert_matches_type(SyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.payroll_wage_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = response.parse()
            assert_matches_type(SyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayrollWageItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        payroll_wage_item = await async_client.qbd.payroll_wage_items.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        payroll_wage_item = await async_client.qbd.payroll_wage_items.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
            is_active=True,
            overtime_multiplier="1.5",
            rate="15.00",
            rate_percent="10",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.payroll_wage_items.with_raw_response.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = await response.parse()
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.payroll_wage_items.with_streaming_response.create(
            expense_account_id="80000001-1234567890",
            name="Regular Pay",
            wage_type="hourly_regular",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = await response.parse()
            assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        payroll_wage_item = await async_client.qbd.payroll_wage_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.payroll_wage_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = await response.parse()
        assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.payroll_wage_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = await response.parse()
            assert_matches_type(PayrollWageItem, payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.payroll_wage_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        payroll_wage_item = await async_client.qbd.payroll_wage_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        payroll_wage_item = await async_client.qbd.payroll_wage_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["Regular Pay"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.payroll_wage_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payroll_wage_item = await response.parse()
        assert_matches_type(AsyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.payroll_wage_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payroll_wage_item = await response.parse()
            assert_matches_type(AsyncCursorPage[PayrollWageItem], payroll_wage_item, path=["response"])

        assert cast(Any, response.is_closed) is True
