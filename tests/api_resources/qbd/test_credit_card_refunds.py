# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    CreditCardRefund,
    CreditCardRefundDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditCardRefunds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
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
            credit_card_transaction={
                "request": {
                    "expiration_month": 12,
                    "expiration_year": 2024,
                    "name": "John Doe",
                    "number": "xxxxxxxxxxxx1234",
                    "address": "1234 Main St, Anytown, USA, 12345",
                    "commercial_card_code": "corporate",
                    "postal_code": "12345",
                    "transaction_mode": "card_not_present",
                    "transaction_type": "charge",
                },
                "response": {
                    "credit_card_transaction_id": "1234567890",
                    "merchant_account_number": "1234567890",
                    "payment_status": "completed",
                    "status_code": 0,
                    "status_message": "Success",
                    "transaction_authorized_at": "2024-01-01T12:34:56Z",
                    "authorization_code": "1234567890",
                    "avs_street_status": "pass",
                    "avs_zip_status": "pass",
                    "card_security_code_match": "pass",
                    "client_transaction_id": "1234567890",
                    "payment_grouping_code": 2,
                    "recon_batch_id": "1234567890",
                    "transaction_authorization_stamp": 2,
                },
            },
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            memo="Refund to customer for duplicate credit card charge",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="REFUND-1234",
            refund_from_account_id="80000001-1234567890",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.credit_card_refunds.with_raw_response.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = response.parse()
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.credit_card_refunds.with_streaming_response.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = response.parse()
            assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.credit_card_refunds.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = response.parse()
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.credit_card_refunds.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = response.parse()
            assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_refunds.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="REFUND-1234",
            ref_number_ends_with="1234",
            ref_number_from="REFUND-0001",
            ref_numbers=["CREDIT CARD REFUND-1234"],
            ref_number_starts_with="REFUND",
            ref_number_to="REFUND-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.credit_card_refunds.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = response.parse()
        assert_matches_type(SyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.credit_card_refunds.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = response.parse()
            assert_matches_type(SyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        credit_card_refund = client.qbd.credit_card_refunds.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.credit_card_refunds.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = response.parse()
        assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.credit_card_refunds.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = response.parse()
            assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_refunds.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncCreditCardRefunds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
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
            credit_card_transaction={
                "request": {
                    "expiration_month": 12,
                    "expiration_year": 2024,
                    "name": "John Doe",
                    "number": "xxxxxxxxxxxx1234",
                    "address": "1234 Main St, Anytown, USA, 12345",
                    "commercial_card_code": "corporate",
                    "postal_code": "12345",
                    "transaction_mode": "card_not_present",
                    "transaction_type": "charge",
                },
                "response": {
                    "credit_card_transaction_id": "1234567890",
                    "merchant_account_number": "1234567890",
                    "payment_status": "completed",
                    "status_code": 0,
                    "status_message": "Success",
                    "transaction_authorized_at": "2024-01-01T12:34:56Z",
                    "authorization_code": "1234567890",
                    "avs_street_status": "pass",
                    "avs_zip_status": "pass",
                    "card_security_code_match": "pass",
                    "client_transaction_id": "1234567890",
                    "payment_grouping_code": 2,
                    "recon_batch_id": "1234567890",
                    "transaction_authorization_stamp": 2,
                },
            },
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            memo="Refund to customer for duplicate credit card charge",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="REFUND-1234",
            refund_from_account_id="80000001-1234567890",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_refunds.with_raw_response.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = await response.parse()
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_refunds.with_streaming_response.create(
            customer_id="80000001-1234567890",
            refund_applied_to_transactions=[
                {
                    "refund_amount": "15.00",
                    "transaction_id": "123ABC-1234567890",
                }
            ],
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = await response.parse()
            assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_refunds.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = await response.parse()
        assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_refunds.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = await response.parse()
            assert_matches_type(CreditCardRefund, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_refunds.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="REFUND-1234",
            ref_number_ends_with="1234",
            ref_number_from="REFUND-0001",
            ref_numbers=["CREDIT CARD REFUND-1234"],
            ref_number_starts_with="REFUND",
            ref_number_to="REFUND-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_refunds.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = await response.parse()
        assert_matches_type(AsyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_refunds.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = await response.parse()
            assert_matches_type(AsyncCursorPage[CreditCardRefund], credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        credit_card_refund = await async_client.qbd.credit_card_refunds.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_refunds.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_refund = await response.parse()
        assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_refunds.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_refund = await response.parse()
            assert_matches_type(CreditCardRefundDeleteResponse, credit_card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_refunds.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
