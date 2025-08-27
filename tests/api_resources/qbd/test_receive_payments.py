# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    ReceivePayment,
    ReceivePaymentDeleteResponse,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReceivePayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
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
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_auto_apply=False,
            memo="Payment received at store location - cash",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="PAYMENT-1234",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.receive_payments.with_raw_response.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.receive_payments.with_streaming_response.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.receive_payments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.receive_payments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.receive_payments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
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
            credit_card_transaction={
                "request": {
                    "address": "1234 Main St, Anytown, USA, 12345",
                    "commercial_card_code": "corporate",
                    "expiration_month": 12,
                    "expiration_year": 2024,
                    "name": "John Doe",
                    "number": "xxxxxxxxxxxx1234",
                    "postal_code": "12345",
                    "transaction_mode": "card_not_present",
                    "transaction_type": "charge",
                },
                "response": {
                    "authorization_code": "1234567890",
                    "avs_street_status": "pass",
                    "avs_zip_status": "pass",
                    "card_security_code_match": "pass",
                    "client_transaction_id": "1234567890",
                    "credit_card_transaction_id": "1234567890",
                    "merchant_account_number": "1234567890",
                    "payment_grouping_code": 2,
                    "payment_status": "completed",
                    "recon_batch_id": "1234567890",
                    "status_code": 0,
                    "status_message": "Success",
                    "transaction_authorization_stamp": 2,
                    "transaction_authorized_at": "2024-01-01T12:34:56Z",
                },
            },
            customer_id="80000001-1234567890",
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            memo="Payment received at store location - cash",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="PAYMENT-1234",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.receive_payments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.receive_payments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.receive_payments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="PAYMENT-1234",
            ref_number_ends_with="1234",
            ref_number_from="PAYMENT-0001",
            ref_numbers=["RECEIVE-PAYMENT-1234"],
            ref_number_starts_with="PAYMENT",
            ref_number_to="PAYMENT-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(SyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.receive_payments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = response.parse()
        assert_matches_type(SyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.receive_payments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = response.parse()
            assert_matches_type(SyncCursorPage[ReceivePayment], receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Conductor) -> None:
        receive_payment = client.qbd.receive_payments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Conductor) -> None:
        response = client.qbd.receive_payments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = response.parse()
        assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Conductor) -> None:
        with client.qbd.receive_payments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = response.parse()
            assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.receive_payments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )


class TestAsyncReceivePayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
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
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_auto_apply=False,
            memo="Payment received at store location - cash",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="PAYMENT-1234",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.receive_payments.with_raw_response.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = await response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.receive_payments.with_streaming_response.create(
            customer_id="80000001-1234567890",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = await response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.receive_payments.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = await response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.receive_payments.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = await response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.receive_payments.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
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
            credit_card_transaction={
                "request": {
                    "address": "1234 Main St, Anytown, USA, 12345",
                    "commercial_card_code": "corporate",
                    "expiration_month": 12,
                    "expiration_year": 2024,
                    "name": "John Doe",
                    "number": "xxxxxxxxxxxx1234",
                    "postal_code": "12345",
                    "transaction_mode": "card_not_present",
                    "transaction_type": "charge",
                },
                "response": {
                    "authorization_code": "1234567890",
                    "avs_street_status": "pass",
                    "avs_zip_status": "pass",
                    "card_security_code_match": "pass",
                    "client_transaction_id": "1234567890",
                    "credit_card_transaction_id": "1234567890",
                    "merchant_account_number": "1234567890",
                    "payment_grouping_code": 2,
                    "payment_status": "completed",
                    "recon_batch_id": "1234567890",
                    "status_code": 0,
                    "status_message": "Success",
                    "transaction_authorization_stamp": 2,
                    "transaction_authorized_at": "2024-01-01T12:34:56Z",
                },
            },
            customer_id="80000001-1234567890",
            deposit_to_account_id="80000001-1234567890",
            exchange_rate=1.2345,
            memo="Payment received at store location - cash",
            payment_method_id="80000001-1234567890",
            receivables_account_id="80000001-1234567890",
            ref_number="PAYMENT-1234",
            total_amount="1000.00",
            transaction_date=parse_date("2024-10-01"),
        )
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.receive_payments.with_raw_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = await response.parse()
        assert_matches_type(ReceivePayment, receive_payment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.receive_payments.with_streaming_response.update(
            id="123ABC-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = await response.parse()
            assert_matches_type(ReceivePayment, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.receive_payments.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids=["80000001-1234567890"],
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="PAYMENT-1234",
            ref_number_ends_with="1234",
            ref_number_from="PAYMENT-0001",
            ref_numbers=["RECEIVE-PAYMENT-1234"],
            ref_number_starts_with="PAYMENT",
            ref_number_to="PAYMENT-9999",
            transaction_date_from=parse_date("2025-01-01"),
            transaction_date_to=parse_date("2025-02-01"),
            updated_after="2025-01-01T12:34:56+00:00",
            updated_before="2025-02-01T12:34:56+00:00",
        )
        assert_matches_type(AsyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.receive_payments.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = await response.parse()
        assert_matches_type(AsyncCursorPage[ReceivePayment], receive_payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.receive_payments.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = await response.parse()
            assert_matches_type(AsyncCursorPage[ReceivePayment], receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncConductor) -> None:
        receive_payment = await async_client.qbd.receive_payments.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.receive_payments.with_raw_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receive_payment = await response.parse()
        assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.receive_payments.with_streaming_response.delete(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receive_payment = await response.parse()
            assert_matches_type(ReceivePaymentDeleteResponse, receive_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.receive_payments.with_raw_response.delete(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )
