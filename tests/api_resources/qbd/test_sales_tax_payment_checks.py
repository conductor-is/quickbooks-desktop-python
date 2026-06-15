# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    SalesTaxPaymentCheck,
    SalesTaxPaymentCheckVoidResponse,
    SalesTaxPaymentCheckDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSalesTaxPaymentChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.create(
            bank_account_id="80000001-1234567890",
            lines=[
                {
                    "amount": "1000.00",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_queued_for_print=True,
            memo="Sales tax payment for Q3 2024",
            ref_number="TAXPMT-1234",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_tax_payment_checks.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            bank_account_id="80000001-1234567890",
            is_queued_for_print=True,
            memo="Sales tax payment for Q3 2024",
            ref_number="TAXPMT-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_tax_payment_checks.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=150,
            ref_number_contains="TAXPMT-1234",
            ref_number_ends_with="1234",
            ref_number_from="TAXPMT-0001",
            ref_numbers=["SALES-TAX PAYMENT CHECK-1234"],
            ref_number_starts_with="TAXPMT",
            ref_number_to="TAXPMT-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(SyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_tax_payment_checks.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_void(self, client: Conductor) -> None:
        sales_tax_payment_check = client.qbd.sales_tax_payment_checks.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_payment_checks.with_raw_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = response.parse()
        assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Conductor) -> None:
        with client.qbd.sales_tax_payment_checks.with_streaming_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = response.parse()
            assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_void(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_tax_payment_checks.with_raw_response.void(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncSalesTaxPaymentChecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.create(
            bank_account_id="80000001-1234567890",
            lines=[
                {
                    "amount": "1000.00",
                    "sales_tax_item_id": "80000001-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_queued_for_print=True,
            memo="Sales tax payment for Q3 2024",
            ref_number="TAXPMT-1234",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.create(
            bank_account_id="80000001-1234567890",
            lines=[{"amount": "1000.00"}],
            transaction_date=parse_date("2024-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_tax_payment_checks.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            bank_account_id="80000001-1234567890",
            is_queued_for_print=True,
            memo="Sales tax payment for Q3 2024",
            ref_number="TAXPMT-1234",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(SalesTaxPaymentCheck, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_tax_payment_checks.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            item_ids=["80000001-1234567890"],
            limit=150,
            ref_number_contains="TAXPMT-1234",
            ref_number_ends_with="1234",
            ref_number_from="TAXPMT-0001",
            ref_numbers=["SALES-TAX PAYMENT CHECK-1234"],
            ref_number_starts_with="TAXPMT",
            ref_number_to="TAXPMT-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(AsyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(AsyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(AsyncCursorPage[SalesTaxPaymentCheck], sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(SalesTaxPaymentCheckDeleteResponse, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_tax_payment_checks.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncConductor) -> None:
        sales_tax_payment_check = await async_client.qbd.sales_tax_payment_checks.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_payment_checks.with_raw_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_payment_check = await response.parse()
        assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_payment_checks.with_streaming_response.void(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_payment_check = await response.parse()
            assert_matches_type(SalesTaxPaymentCheckVoidResponse, sales_tax_payment_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_void(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_tax_payment_checks.with_raw_response.void(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
