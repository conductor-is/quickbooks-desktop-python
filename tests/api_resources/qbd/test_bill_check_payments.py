# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    BillCheckPayment,
    BillCheckPaymentDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillCheckPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.create(
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_transaction_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000001-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000001-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_queued_for_print=True,
            memo="Payment for office supplies - Invoice INV-1234",
            payables_account_id="80000001-1234567890",
            ref_number="CHECK-1234",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.bill_check_payments.with_raw_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.bill_check_payments.with_streaming_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.bill_check_payments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.bill_check_payments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.bill_check_payments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            amount="1000.00",
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_transaction_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000001-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000001-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            bank_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            is_queued_for_print=True,
            memo="Payment for office supplies - Invoice INV-1234",
            ref_number="CHECK-1234",
            transaction_date=parse_date("2021-10-01"),
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.bill_check_payments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.bill_check_payments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.bill_check_payments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="CHECK-1234",
            ref_number_ends_with="1234",
            ref_number_from="CHECK-0001",
            ref_numbers=["BILL CHECK PAYMENT-1234"],
            ref_number_starts_with="CHECK",
            ref_number_to="CHECK-9999",
            transaction_date_from=parse_date("2021-01-01"),
            transaction_date_to=parse_date("2021-02-01"),
            updated_after="2021-01-01T12:34:56",
            updated_before="2021-02-01T12:34:56",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(SyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.bill_check_payments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = response.parse()
        assert_matches_type(SyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.bill_check_payments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = response.parse()
            assert_matches_type(SyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        bill_check_payment = client.qbd.bill_check_payments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.bill_check_payments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = response.parse()
        assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.bill_check_payments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = response.parse()
            assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.bill_check_payments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncBillCheckPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.create(
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_transaction_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000001-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000001-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_queued_for_print=True,
            memo="Payment for office supplies - Invoice INV-1234",
            payables_account_id="80000001-1234567890",
            ref_number="CHECK-1234",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_check_payments.with_raw_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = await response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_check_payments.with_streaming_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            bank_account_id="80000001-1234567890",
            transaction_date=parse_date("2021-10-01"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = await response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_check_payments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = await response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_check_payments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = await response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.bill_check_payments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            amount="1000.00",
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_transaction_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000001-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000001-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            bank_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            is_queued_for_print=True,
            memo="Payment for office supplies - Invoice INV-1234",
            ref_number="CHECK-1234",
            transaction_date=parse_date("2021-10-01"),
        )
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_check_payments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = await response.parse()
        assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_check_payments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = await response.parse()
            assert_matches_type(BillCheckPayment, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.bill_check_payments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="CHECK-1234",
            ref_number_ends_with="1234",
            ref_number_from="CHECK-0001",
            ref_numbers=["BILL CHECK PAYMENT-1234"],
            ref_number_starts_with="CHECK",
            ref_number_to="CHECK-9999",
            transaction_date_from=parse_date("2021-01-01"),
            transaction_date_to=parse_date("2021-02-01"),
            updated_after="2021-01-01T12:34:56",
            updated_before="2021-02-01T12:34:56",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(AsyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_check_payments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = await response.parse()
        assert_matches_type(AsyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_check_payments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = await response.parse()
            assert_matches_type(AsyncCursorPage[BillCheckPayment], bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        bill_check_payment = await async_client.qbd.bill_check_payments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_check_payments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_check_payment = await response.parse()
        assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_check_payments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_check_payment = await response.parse()
            assert_matches_type(BillCheckPaymentDeleteResponse, bill_check_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.bill_check_payments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
